# 1. 변수와 자료형
name = "Alice"
age = 30
height = 175.5
is_student = True

print(f"이름: {name}, 나이: {age}, 키: {height}, 학생 여부: {is_student}")
print(f"name의 타입: {type(name)}")
print(f"age의 타입: {type(age)}")

# 2. 연산자
a = 10
b = 3

print(f"a = {a}")
print(f"b = {b}")
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b} (나눗셈)")
print(f"a // b = {a // b} (정수 나눗셈)")
print(f"a % b = {a % b} (나머지)")
print(f"a ** b = {a ** b} (거듭제곱)")

# 3. 조건문 (if, elif, else)
score = 85

if score >= 90:
    print("학점: A")
elif score >= 80:
    print("학점: B")
else:
    print("학점: C 이하")

# 4. 반복문 (for, while)
# for 루프
fruits = ["apple", "banana", "cherry"]
print("과일 목록:")
for fruit in fruits:
    print(fruit)

# while 루프
count = 0
while count < 5:
    print(f"카운트: {count}")
    count += 1

# 5. 함수
def greet(name):
    return f"안녕하세요, {name}님!"

message = greet("Bob")
print(message)

def add(x, y):
    return x + y

result = add(5, 3)
print(f"5 + 3 = {result}")

# 6. 리스트 (List)
my_list = [1, 2, 3, "hello", True]
print(f"리스트: {my_list}")
print(f"리스트의 첫 번째 요소: {my_list[0]}")
my_list.append(4)
print(f"요소 추가 후 리스트: {my_list}")
my_list.remove("hello")
print(f"요소 제거 후 리스트: {my_list}")

# 7. 튜플 (Tuple)
my_tuple = (1, 2, "three")
print(f"튜플: {my_tuple}")
# my_tuple.append(4) # 튜플은 변경 불가능 (immutable)

# 8. 딕셔너리 (Dictionary)
person = {"name": "Charlie", "age": 25, "city": "Seoul"}
print(f"딕셔너리: {person}")
print(f"이름: {person['name']}")
person["age"] = 26
print(f"나이 변경 후: {person['age']}")
person["job"] = "Engineer"
print(f"직업 추가 후: {person}")

# 9. 세트 (Set)
my_set = {1, 2, 3, 2, 1} # 중복 제거
print(f"세트: {my_set}")
my_set.add(4)
print(f"요소 추가 후 세트: {my_set}")
my_set.remove(1)
print(f"요소 제거 후 세트: {my_set}")

# 10. 주석
# 한 줄 주석은 #으로 시작합니다.
"""
여러 줄 주석은 큰따옴표 세 개로 시작하고 끝납니다.
보통 함수나 클래스 설명에 사용됩니다.
"""
