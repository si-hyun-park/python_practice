'''
Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

ex) http://naver.com
Rule_01 : http:// 부분은 제외 = > naver.com
Rule_02 : 처음 만나는 점(.) 이후 부분은 제외 => naver
Rule_03 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수+"!" 로 구성

생성된 비밀번호 : nav51!
'''

# print("http://naver.com")

# pw = "http://naver.com"

# print(pw[7:10])
# print(pw[7:])
# print(pw[7:])

# print(pw[0:])

url = "http://naver.com"
my_str = url.replace("http://", "")
# print(my_str)
my_str = my_str[:my_str.index(".")]

# print(my_str)
password = my_str[:3]+str(len(my_str))+str(my_str.count("e"))+"!"
# print(my_str)
print(my_str[:3]+str(len(my_str))+str(my_str.count("e"))+"!")

print("{0} 의 비밀번호는 {1} 입니다".format(url, password))
