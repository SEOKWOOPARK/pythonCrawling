from random import *

class Unit:
	def __init__(self, name, hp, speed):
		self.name = name
		self.hp = hp
		self.speed = speed
		print("{0} 유닛이 생성되었다.".format(name))

	def move(self, location):
		print("[지상 유닛 이동중]")
		print("{0} -> {1} 방향으로 이동한다. 속도는 {2}"\
			.format(self.name, location, self.speed))
	
	def damaged(self, damage): 
		print("{0}가 {1} 데미지를 입다." .format(self.name, damage))
		self.hp -= damage
		print("{0}의 현재 체력은 {1}이다." .format(self.name, self.hp))
		if self.hp <= 0:
			print("{0}은 소멸." .format(self.name))

class AttackUnit(Unit): # () 안에 상속받을 클래스명
	def __init__(self, name, hp, speed, damage):
		Unit.__init__(self, name, hp, speed) 
		self.damage = damage

	def attack(self, location): # self 값은 호출 때 생략
		print("{0} -> {1} 방향으로 공격 중. [공격력 {2}]"\
		.format(self.name, location, self.damage))

class Marine(AttackUnit): # 마린 전용 클래스
	def __init__(self):
		AttackUnit.__init__(self, "마린", 40, 1, 5)

	def stimpack(self):
		if self.hp > 10:
			self.hp -= 10
			print("{0} : 스팀팩 사용(hp 10 감소).".format(self.name))
		else:
			print("{0} : 체력 부족으로 스팀팩 사용 불가".format(self.name))

class Tank(AttackUnit): # 탱크 전용 클래스
	seize_developed = False
	def __init__(self):
		AttackUnit.__init__(self, "탱크", 150, 1, 35)
		self.seize_mode = False

	def set_seize_mode(self):
		if Tank.seize_developed == False:
			return 

		if self.seize_mode == False:
			print("{0} : 시즈모드 전환".format(self.name))
			self.damage *= 2
			self.seize_mode = True
		else:
			print("{0} : 시즈모드 해제".format(self.name))
			self.damage /= 2
			self.seize_mode = False

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
		self.fly(self.name, location)

class Wraith(FlyableAttackUnit):
	def __init__(self):
		FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
		self.clocked = False # 클로킹 모드 상태

	def clocking(self):
		if self.clocked == True:
			print("{0} : 클로킹 모드 해제".format(self.name))
			self.clocked = False
		else:
			print("{0} : 클로킹 모드 전환".format(self.name))
			self.clocked = True
 
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
		

def game_start():
	print("[알림] 새로운 게임을 시작합니다")

def game_over():
	print("Player : gg")
	print("[Player]님이 게임에서 퇴장했습니다.")

game_start()
m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank() 

w1 = Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

for unit in attack_units:
	unit.move("1시")

Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발 완료")

for unit in attack_units:
	if isinstance(unit, Marine):
		unit.stimpack()
	elif isinstance(unit, Tank):
		unit.set_seize_mode()
	elif isinstance(unit, Wraith):
		unit.clocking()
	# isinstance(a, b) b가 a의 인스턴스인지 체크

for uni in attack_units:
	unit.attack("1시")

for unit in attack_units:
	unit.damaged(randint(5, 21)) # 랜덤값으로 공격받기, import random

game_over()








