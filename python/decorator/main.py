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


class TimerDeco:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print('속도 측정 시작')
        start = time.time()
        self.func()
        end = time.time()
        print(f"속도 측정 결과 {end - start}")

class Test:

    @TimerDeco
    def test():
        print("함수 실행")
        math.factorial(100000)

    @TimerDeco
    def test_2():
        print("함수 실행")
        math.factorial(200000)


test()

t = Test
t.test()
t.test_2()
