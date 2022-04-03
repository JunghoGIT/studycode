# a = [1,2,3]
# b = a
#
# print(f'a = {a}')
# print(f'b = {b}')
#
# a[2] = 0
#
# print('값 변경')
# print(f'a = {a}')
# print(f'b = {b}')

# a = [1,2,3]
# b = a[:]
#
# print(f'a = {a}')
# print(f'b = {b}')
#
# a[2] = 0
#
# print('값 변경')
# print(f'a = {a}')
# print(f'b = {b}')

# a = [1,2,3]
# b = a.copy()
#
# print(f'a = {a}')
# print(f'b = {b}')
#
# a[2] = 0
#
# print('값 변경')
# print(f'a = {a}')
# print(f'b = {b}')

# a = [[1,2,3],[4,5,6],[7,8,9]]
# b = a.copy()
#
# print(f'a = {a}')
# print(f'b = {b}')
#
# a[2][2] = 0
# a[1] = 0
# b[0][0] = 100
# print('값 변경')
# print(f'a = {a}')
# print(f'b = {b}')
import copy

a = [[1,2,3],[4,5,6],[7,8,9]]
b = copy.deepcopy(a)

print(f'a = {a}')
print(f'b = {b}')

a[2][2] = 0
a[1] = 0
b[0][0] = 100
print('값 변경')
print(f'a = {a}')
print(f'b = {b}')