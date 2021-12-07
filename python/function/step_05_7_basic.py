# /c/Users/GREEN/Desktop/python_fun/venv/Scripts/python
# -*- coding: utf-8 -*-

import contextlib
import step_05_6_basic # <---- utils
import time

@contextlib.contextmanager
def openReadOnly(fileName):
    """

    :param fileName:
    :return:
    """

    read_file = open(fileName, mode = "r", encoding="utf-8")
    yield read_file
    read_file.close()

def main(fileName):
    with openReadOnly(fileName) as file:
        text = file.read() # 파일 전체 읽어오기 (한줄씩 읽어오기 아님...)

    n=0
    for word in text.split():
        if word in ["오미크론", "코로나"]:
            n += 1
    print("오미크론 및 코로나 단어의 갯수는 {} 이다.".format(n))

if __name__ == "__main__":
    fileName = "data/news_article.txt"
    with step_05_6_basic.timer():
        main(fileName)
        time.sleep(0.25)
