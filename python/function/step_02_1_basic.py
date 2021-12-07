# /c/Users/GREEN/Desktop/python_fun/venv/Scripts/python
# -*- coding: utf-8 -*-

# 정규화
# Normalization (빅데이터 분석 기사, 단골!!) ~ Standardization (표준화) = Z-Score
# 데이터의 범위를 0과 1로 변환해서 데이터의 분포를 조정하는 방법
# Min_Max Normalization
#
# Y = (개별 값 - 최소값) / (최대값 - 최소값)
# pandas 데이터 프레임

import seaborn as sns

def min_max_normalize(column):
   """데이터를 정규화를 만드는 과정이다.
    Args:
        column (pandas Series): 정규화를 하기 위한 것

    Return: Series
        pandas series: min_max 정규화 공식의 답을 가져온다.
   """

   min_max_score = (column - column.min()) / (column.max() - column.min())
   return min_max_score

if __name__ == "__main__":
    iris = sns.load_dataset("iris")
    print(iris.head())

    iris['sepal_length'] = min_max_normalize(iris['sepal_length'])
    iris['sepal_width'] = min_max_normalize(iris['sepal_width'])
    iris['petal_length'] = min_max_normalize(iris['petal_length'])
    iris['petal_width'] = min_max_normalize(iris['petal_width'])

    print(iris.head())



