# /c/Users/GREEN/Desktop/python_fun/venv/Scripts/python
# -*- coding: utf-8 -*-

import contextlib
import time

@contextlib.contextmanager
def timer():
    """시간 측정하는 context manager 관리 함수

    Yields:
        None
    """

    start = time.time()
    yield
    end = time.time()

    print("시간측정(Elapsed): {:.2f} 초".format(end - start))

def main():
    with timer():
        print("얼마 걸릴까요?")
        time.sleep(0.25) # 크롤링 할 때, 종종 사용

if __name__ == "__main__":
    main()