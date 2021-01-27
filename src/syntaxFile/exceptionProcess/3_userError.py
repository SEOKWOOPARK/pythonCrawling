class BigNumberError(Exception):
	def __init__(self, message):
		self.message = message

	def __str__(self):
		return self.message

try:
	num1 = int(input("첫 인풋 입력:"))
	num2 = int(input("두 번째 인풋 입력:"))
	if num1 >= 10 or num2 >= 10:
		raise BigNumberError("입력 값 : {0}, {1}".format(num1, num2))
		# 사용자 정의 에러
	print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError: # 타입에 맞지 않는 value
	print("잘못된 값 입력")
except BigNumberError as err:
	print("에러 발생. 한 자리 숫자만 입력")
	print(err)
finally:
	print("연산 종료")