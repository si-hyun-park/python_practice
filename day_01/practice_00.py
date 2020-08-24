# 줄바꿈 기능

# sentence = "나는 소년 입니다"
# print(sentence)
# sentence2 = "파이썬은 쉬워요 "
# print(sentence2)
# sentence3 = """
# 나는 소년이고 파이썬은 쉬워요
# """
# print(sentence3)

# 슬라이싱
# personal_num = "990123-1234567"

# print("성별 : ", personal_num[7])
# print("연 : ", personal_num[0:2])  # 0~2 전까지


# print("월 : ", personal_num[2:4])
# print("일 : ", personal_num[4:6])

# print("생년월일 : ", personal_num[:6])
# print("뒤 7자리", personal_num[7:])  # 7 부터 끝까지

# print("뒤 7자리 (뒤부터)", personal_num[-7:]) #e 뒤로 -7 이동하고 끝까지


# 문자열 처리
python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python", "java"))

index = python.index("n")
print(index)

index = python.index("n", index+1)
print(index)
print(python.find("n"))
