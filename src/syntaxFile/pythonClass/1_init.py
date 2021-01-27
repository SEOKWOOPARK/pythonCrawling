class Unit:
	def __init__(self, name, hp, damage): # __init__ 꼭 필요한 함수
		self.name = name
		self.hp = hp
		self.damage = damage
		print("{0} 유닛 생성." .format(self.name))
		print("체력 {0}, 공격력 {1}" .format(self.hp, self.damage))
		# 객체 생성자

# 클래스에 의해 만들어진 객체 => 인스턴스
marine1 = Unit("마린", 40, 5) 
marine2 = Unit("마린", 40, 3)
tank = Unit("탱크", 150, 35)

wraith1 = Unit("레이스", 80, 5)
print("유닛 이름: {0}, 공격력: {1}" .format(wraith1.name, wraith1.name))

wraith2 = Unit("회유한 레이스", 80, 5)
wraith2.clocking = True # 객체 변수 확장

if wraith2.clocking == True:
	print("{0}는 현재 클로킹 상태." .format(wraith2.name))
	