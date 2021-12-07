# /c/Users/GREEN/Desktop/python_fun/venv/Scripts/python
# -*- coding: utf-8 -*-
#

def cnt_letter(content, letter):
    """content 안에 있는 문자를 세는 함수입니다.
    # Google Style
    Args:
        content(str): 탐색 문자열
        letter(str): 찾을 문자열

    Returns:
        int
    """
    # code 작업
    print("함수 테스트")
    return (len([char for char in content if char == letter])) # 리스트 컴프리헨션

if __name__ == "__main__":

    docstring = cnt_letter.__doc__
    border = "*" * 20
    print('{}\n{}\n{}'.format(border, docstring, border))
