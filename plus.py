num1 = float(input("1つ目の数字を入力してください: "))
num2 = float(input("2つ目の数字を入力してください: "))

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")

s = 'abc'
#インデント？
print(f'right : {s:*>8}')
print(f'center: {s:*^8}')
print(f'left  : {s:*<8}')

i = 255
# ゼロ埋め
print(f'zero padding: {i:08}')
# zero padding: 00001234

# 2 8 16進数
print(f'bin       : {i:08b}')
print(f'oct       : {i:08o}')
print(f'hex(lower): {i:08x}')
print(f'hex(upper): {i:08X}')
# bin       : 11111111
# oct       : 00000377
# hex(lower): 000000ff
# hex(upper): 000000FF