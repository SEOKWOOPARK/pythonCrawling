# 오버라이딩

class Unit:
	def __init__(self, name, hp, speed):
		self.name = name
		self.hp = hp
		self.speed = speed

	def move(self, location):
		print("[지상 유닛 이동중]")
		print("{0} -> {1} 방향으로 이동한다. 속도는 {2}"\
			.format(self.name, location, self.speed))

class AttackUnit(Unit): # () 안에 상속받을 클래스명
	def __init__(self, name, hp, speed, damage):
		Unit.__init__(self, name, hp, speed) 
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
 
class Flyable:
	def __init__(self, flying_speed):
		self.flying_speed = flying_speed

	def fly(self, name, location):
		print("{0} -> {1} 방향으로 비행 중. 속도는 {2}"\
			.format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable): # 다중상속
	def __init__(self, name, hp, damage, flying_speed):
		AttackUnit.__init__(self, name, hp, 0, damage) # 공중 유닛 -> 지상속도 = 0
		Flyable.__init__(self, flying_speed)

	def move(self, location): # 같은 함수 다시 정의 => 함수 상속 안받고 자체 함수를 쓴다
		print("[공중 유닛 이동]")
		self.fly(self.name, location)
		

vulture = AttackUnit("벌쳐", 80, 10, 20)
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")

battlecruiser.move("9시") # self.name은 저절로 할당 => 생략.




