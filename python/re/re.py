import re

p= re.compile('[a-z]+') #모든 소문자 알파벳이 한 번 이상 반복될 수 있음을 의미

m = p.match('yoonjungho')
print(m)

m = p.match('yoon7jungho')
print(m)

m = p.match('7 yoonjungho')
print(m)

m = p.match('yoon7jungho')

print(m.group())
print(m.start())
print(m.end())
print(m.span())

m = p.match('yoon7jungho')
if m:
    print('Match found: ', m.group())
else:
    print('No match')


m = p.search('7 yoon7jungho')

print(m)

m = p.findall('jungho is awesome')

print(m)

m = p.finditer('jungho is awesome')

for x in m :
    print(x)