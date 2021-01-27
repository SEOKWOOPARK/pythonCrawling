try:
	num1 = int(input("첫 인풋 입력:"))
	num2 = int(input("두 번째 인풋 입력:"))
	if num1 >= 10 or num2 >= 10:
		raise ValueError # 조건문으로 에러 발생시키기
	print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError: # 타입에 맞지 않는 value
	print("잘못된 값 입력. 10 이하만 입력하시오")
