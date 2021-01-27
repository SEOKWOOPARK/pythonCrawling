class Unit:
	def __init__(self, name, hp):
		self.name = name
		self.hp = hp
		

class AttackUnit(Unit): # () 안에 상속받을 클래스명
	def __init__(self, name, hp, damage):
		Unit.__init__(self, name, hp) 
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
 

class Flyable:
	def __init__(self, flying_speed):
		self.flying_speed = flying_speed

	def fly(self, name, location):
		print("{0} -> {1} 방향으로 비행 중. 속도는 {2}"\
			.format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable): # 다중상속
	def __init__(self, name, hp, damage, flying_speed):
		AttackUnit.__init__(self, name, hp, damage)
		Flyable.__init__(self, flying_speed)

# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

a = FlyableAttackUnit("marine", 200, 6, 5)
a.fly(a.name, "3시")


