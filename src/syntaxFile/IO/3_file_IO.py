score_file = open("score.txt", "w", encoding = "utf8")
# utf8 => 한글 파싱, w => 쓰기
print("Math : 0", file = score_file)
print("English : 50", file = score_file)
score_file.close() # open - close 반드시 셋트


score_file = open("score.txt", "a", encoding = "utf8")
# a (append)=> 이어쓰기
score_file.write("Science: 80")
score_file.write("\nCoding: 20") # 줄바꿈 기능 넣어주기
score_file.close()


score_file = open("score.txt", "r", encoding = "utf8")
print(score_file.read()) # 읽기 버전
score_file.close()


score_file = open("score.txt", "r", encoding = "utf8")
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
# 한 줄씩 읽고 다음 줄로 이동
score_file.close()


score_file = open("score.txt", "r", encoding = "utf8")
while True: # 읽어온 텍스트를 반복문을 통해 출력
	line = score_file.readline()
	if not line:
		break
	print(line)
score_file.close()


score_file = open("score.txt", "r", encoding = "utf8")
lines = score_file.readlines() # 읽어온 내용 배열에 저장
for line in lines:
	print(line, end = "")
score_file.close()




