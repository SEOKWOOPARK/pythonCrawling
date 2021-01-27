import sys

print("ManU", "Liverpool", file = sys.stdout) # 표준출력
print("ManU", "Liverpool", file = sys.stderr)

# print("ManU", "Liverpool", sep = ",", end = "?")
# sep = "" => 사이마다 끼워넣을 값

scores = {"Math" : 0, "English": 50, "Coding" : 100}

for subject, score in scores.items(): # dic의 (key, value) 튜플로 리턴
	print(subject.ljust(8), str(score).rjust(4), sep=":") 
	# .ljust(x) x칸 공백 만들고 왼쪽 정렬
	# .rjust(y) y칸 공백 만들고 오른쪽 정렬

for num in range(1, 21):
	print("대기번호 : " + str(num).zfill(3))
	# zfill(n) n자리수에서 값 없는 것은 0으로 채우기

answer = input("Enter anykey:")
print("입력 값은 " + answer + "이다.")
# 사용자 입력 값은 항상 문자열이다.






