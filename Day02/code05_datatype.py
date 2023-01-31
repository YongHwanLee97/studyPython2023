# 자료형
# None 값이 없는 값
None # 컴퓨터왈 난몰라

print(None)
print(0 == None)
print('' == None)

# 숫자형
val = 3
print(type(val))

val = 3.14
print(type(val))

val = 'Hello'
print(type(val))

val = 0b1010
print(type(val))

val = 12.09789678464
print(type(val))

val = 4_520_000
print(val)

val = 3_099.99
print(val)

# 문자열
val = 'Life is short, You need python.'
print(val)
print(type(val))

val = 'Hell\nWorld!' # 탈출문자
print(val)
val = 'Hell\tWorld!'
print(val)
val = 'Hell\t\bWorld!'
print(val)

val = '''Life is short,
You need Python'''
print(val)

val = "Hi, I'm 'Lee'"
print(val)
val = 'Hi, I\'m \'Lee\''
print(val)

# 불린형 or 불형
참 = True
거짓 = False
print(type(거짓))

print(1 + 1 ==1)
# 거짓이라는 False 값 변수가 참이냐
print(거짓 == True)
print(거짓 == False)
print(거짓 is False)

print(bool(1)) # 1 == True
print(bool(0)) # 0 == False
print(bool(3)) # 1이외의 값은 True라고 사용 X





