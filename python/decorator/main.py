import time, math

def timer_decorator(func):
    def decorator():
        print('속도 측정 시작')
        start = time.time()
        func()
        end = time.time()
        print(f"속도 측정 결과 {end-start}")
    return decorator

@timer_decorator
def test():
    print("함수 실행")
    math.factorial(100000)

test()