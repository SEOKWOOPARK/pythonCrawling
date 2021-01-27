import pickle

# with open("profile.pickle", "rb") as profile_file:
# 	print(pickle.load(profile_file))
	# 파일 읽어서 profile_file에 저장 => pickle.load()

# with open("study.txt", "w", encoding = "utf8") as study_file:
# 	study_file.write("learning python") # 쓰기 버전

with open("study.txt", "r", encoding = "utf8") as study_file:
	print(study_file.read())

