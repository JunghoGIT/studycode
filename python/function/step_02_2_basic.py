# /c/Users/GREEN/Desktop/python_fun/venv/Scripts/python
# -*- coding: utf-8 -*-

# 수치형 데이터 활용해서, 정규화
# 표준화 (공식) z-score
# 공식 찾으시고, 함수 작성 하시고,
# iris 데이터에서 적용
import seaborn as sns

def standardize(column):
    """데이터의 정규화를 만드는 과정이다.
    Args:
        column (pandas Series): 정규화를 하기 위한 것

    Returns: series
        pandas series: 표준화 공식을 적용한다.
    """

    # z-score 반환함
    z_score = (column - column.mean()) / column.std()
    return z_score


if __name__ == "__main__":
    iris = sns.load_dataset("iris")
    print(iris.head())

    iris['sepal_length'] = standardize(iris['sepal_length'])
    iris['sepal_width'] = standardize(iris['sepal_width'])
    iris['petal_length'] = standardize(iris['petal_length'])
    iris['petal_width'] = standardize(iris['petal_width'])

    print(iris.head())