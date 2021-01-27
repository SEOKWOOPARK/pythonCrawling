import pickle

profile_file = open("profile.pickle", "wb")
# pick은 바이너리리딩 타입(wb) 사용, encoding 설정 필요 없다
profile = { "name" : "kane", "age" : 30, "hobby" : ["football", "fitness", "coding"]}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 profile_file에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # 파일 데이터 로딩
print(profile)
profile_file.close()