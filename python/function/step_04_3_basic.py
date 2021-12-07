# /c/Users/GREEN/Desktop/python_fun/venv/Scripts/python
# -*- coding: utf-8 -*-

# mutable (변경이 가능한): list, dict, set, bytearray, objects, functions
# immutable (변경이 어려운): tuple, int, float, bool, string, bytes

import pandas
import pandas as pd

def add_new_column(new_vals, data = None):
    """새로운 컬럼을 data에 추가. 컬럼명은 columns_<n> 형태로 저장. 이 때, 모두 numeric로 저장

    Args:
        new_vals (iterable): 함수 실행 시마다, 새로운 컬럼의 값 의미
        data (Dataframe, optional): 함수가 실행시 업데이트.
             만약에 데이터프레임으로 입력받지 못하면, 임의의 데이터프레임이 디폴트로 생성
    Returns:
        DataFrame
    """
    if data is None:
        data = pd.DataFrame()
    data['col_{}'.format(len(data.columns))] = new_vals
    return data

if __name__ == "__main__":
    print(add_new_column(new_vals=range(10)))
    print(add_new_column(new_vals=None))
    print(add_new_column(new_vals=range(10)))
    print(add_new_column(new_vals=None))
