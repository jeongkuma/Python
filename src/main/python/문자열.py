a = 'I love Python'
print(a)

a = "I love Python"
print(a)

a = 'I \"love\" Python'
print(a)

text = """실패하는 것보다
무서운건 시도하지않는 것이다.
"""

print(text)
print(len(text))

text = text * 3
print(text)

name = input("이름을 입력하세요 : ")

message = name + '님, 반갑습니다!'

print(message)

message = f'{name}님~ 반갑습니다!!'

print(message)

print(f'{message} 이건 탈출 케이스로 감싼거')
