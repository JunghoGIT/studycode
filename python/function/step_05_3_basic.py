# /c/Users/GREEN/Desktop/python_fun/venv/Scripts/python
# -*- coding: utf-8 -*-

# context manager 파일을 생성

import contextlib

@contextlib.contextmanager
def my_context():
    print("안녕하세요 처음 인사드림.")
    yield 10
    print("안녕히 계세요.")
    
def main():
    with my_context() as temp:
        print("temp 인사말 {}".format(temp))

if __name__ == "__main__":
    main()