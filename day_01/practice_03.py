# 리스트 []

subway = [10, 20, 30]
print(subway)

subway = ["you", "jo", "pak"]
print(subway)

# 조는 몇번째 인가
print(subway.index("jo"))

# 하 탑승

subway.append("haha")
print(subway)
# append 는 뒤에 추가 된다 <--> pop

# 정 을 유 / 조 사이에 추가
subway.insert(1, "jeong")
print(subway)

# pop 은 뒤에서 하나씩 제거

print(subway.pop())
print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명있는지 확인
subway.append("you")
print(subway)
print(subway.count("you"))

# 리스트 정렬 방법
num_list = [5, 45, 7, 34, 5, 1, 2, 6, 9]
num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

# 모두 지우기
# num_list.clear()

# print(num_list)


# 다양한 자료형과 함께 사용

mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 합치기
num_list.extend(mix_list)
print(num_list)
