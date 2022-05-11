class CustomContextManager:

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('시작')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f'{exc_type,exc_val,exc_tb}')
        print('끝')

    def happy(self):
        print(f'{self.name}는 행복합니다')


cm = CustomContextManager('정호')

with cm:
    cm.happy()
    make_error = 2/0

