import time
from contextlib import contextmanager

class cm_timer_1:
    """
    Класс-контекстный менеджер для измерения времени выполнения
    """
    def __enter__(self):
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed_time = time.time() - self.start_time
        print(f"Время выполнения: {elapsed_time:.4f} секунд")

@contextmanager
def cm_timer_2():
    """
    Функция-контекстный менеджер для измерения времени выполнения
    """
    start_time = time.time()
    yield
    elapsed_time = time.time() - start_time
    print(f"Время выполнения: {elapsed_time:.4f} секунд")