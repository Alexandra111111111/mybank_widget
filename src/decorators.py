import functools
import logging
from typing import Any
from typing import Callable
from typing import Optional

# Настройка логирования
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s]: %(message)s", datefmt="%Y-%m-%d %H:%M:%S")


def log(filename: Optional[str] = None) -> Callable[[Callable], Callable]:
    """
    Логирует выполнение функций, сохраняя информацию о входе, выходе и возможных ошибках.

    :param filename: Файл, в который будет вестись запись логов. По умолчанию логи выводятся в консоль.
    :return: Обёрнутую функцию с логированием
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
                if filename is not None:
                    with open(filename, "a") as file:
                        print(message, file=file)
                else:
                    logging.info(message)
                return result
            except Exception as e:
                err_message = f"{func.__name__} error: {type(e).__name__}. " f"Inputs: {args}, {kwargs}"
                if filename is not None:
                    with open(filename, "a") as file:
                        print(err_message, file=file)
                else:
                    logging.error(err_message)
                raise

        return wrapper

    return decorator
