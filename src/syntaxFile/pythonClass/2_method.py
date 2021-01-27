class Unit:
	def __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp
		self.damage = damage
		print("{0} 유닛 생성." .format(self.name))
		print("체력 {0}, 공격력 {1}" .format(self.hp, self.damage))

class AttackUnit:
	def __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp 
		self.damage = damage

	def attack(self, location): # self 값은 호출 때 생략
		print("{0} -> {1} 방향으로 공격 중. [공격력 {2}]"\
			.format(self.name, location, self.damage))

	def damaged(self, damage): 
		print("{0}가 {1} 데미지를 입다." .format(self.name, damage))
		self.hp -= damage
		print("{0}의 현재 체력은 {1}이다." .format(self.name, self.hp))
		if self.hp <= 0:
			print("{0}은 소멸." .format(self.name))


firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)
