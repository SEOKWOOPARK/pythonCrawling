import re
p = re.compile("ca.e") 
# 점은 문자 하나, '^'은 문자열 시작 ^de라면 ade, bde, cde 등등
# '$'은 문자열 끝 se$ case, base

def print_match(m):
	if m:
		print(m.group())
		print(m.string) # 입력받은 문자열
		print(m.start()) # 일치하는 문자열의 시작 index
		print(m.end()) # 일치하는 문자열의 끝 index
		print(m.span()) # 일치하는 문자열의 시작, 끝 index
	else:
		print("매칭 안됨")

array = ["case", "cafe", "caffe", "careless"]
# m = p.match("caffe")

for i in range(len(array)):
	print_match(p.match(array[i]))
	# match("careless") => 주어진 문자열의 처음부터 "ca.e"만 포함하면 된다.

print('----------------')
m = p.search("good care")
print_match(m)
print('확인')
# search => 주어진 문자열 내에만 일치하면 출력해준다

print('----------------')
n = p.findall("good care cafe cave") # 해당 일치하는 값들을 배열로 받기
print(n)





