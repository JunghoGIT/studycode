from contextlib import contextmanager


@contextmanager
def custom_context_manager():
    print('시작')
    try:
        yield '메롱메롱'
    except Exception as e:
        print(f'error : {e}')
    finally:
        print('끝')


with custom_context_manager() as c:
    print(c)
    2/0


