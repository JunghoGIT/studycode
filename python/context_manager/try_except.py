f = open('test.txt', 'r', encoding='UTF8')
try:
    text = f.read()
    print(text)
finally:
    f.close()