# /c/Users/GREEN/Desktop/python_fun/venv/Scripts/python
# -*- coding: utf-8 -*-
# 함수의 규칙(Rule)

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# 1. 가독성이 안 좋음
# 2. 확장성이 안 좋음
# 3. 한 함수는 무조건 하나의 기능만 하게끔 설계.

def load_and_plot(datasetname):
    """데이터를 불러오고 그래프를 작성한다.

    :param datasetname:
    :return:
    """
    # 데이터를 불러오는 코드를 작성함.
    # 작업 1. DB 연결 하는 코드 작성
    data = sns.load_dataset(datasetname)

    # 데이터 전처리 하는 코드 등등
    y = data.iloc[:, 1].values
    X = data.columns
    num_list = data.select_dtypes(include=[np.number]).columns
    print("컬럼명: ", num_list)

    # 작업 2. 시각화 코드 작성
    sns.scatterplot(x = num_list[0], y = num_list[1], data = data)
    plt.show()

    # 작업 3.
    # X, y 값 반환하기
    return X, y

if __name__ == "__main__":
    X, y = load_and_plot("tips")
    print("X is:", X)
    print("y is:", y)