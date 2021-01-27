try:
	nums = []
	nums.append(int(input("첫 인풋 입력:")))
	nums.append(int(input("두 번째 인풋 입력:")))
	print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError: # 타입에 맞지 않는 value
	print("잘못된 값 입력")
except ZeroDivisionError as err:
	print(err) # 0으로 나눈 에러
except Exception as err:
	print("알 수 없는 에러")
	print(err)
	# 나머지 모든 에러 처리, err => 구체적 오류 내용

