# /c/Users/GREEN/Desktop/python_fun/venv/Scripts/python
# -*- coding: utf-8 -*-

# Context Manager                         카테터 (파티준비원)
# context 세팅                             - 테이블 세팅
# 코드 실행                                 - 하객이, 스테이크 주문, 식사
# context 없앰                             - 테이블 치움

def main():

    # context manager
    with open("data/my_file.txt") as file:
        text = file.read()
        text_length = len(text)

    print("파일 글자의 총 길이는 {} 이다.".format(text_length))

if __name__ == "__main__":
    main()