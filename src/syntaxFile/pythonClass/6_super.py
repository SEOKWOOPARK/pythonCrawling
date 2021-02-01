class Unit:
	def __init__(self, name, hp, speed):
		self.name = name
		self.hp = hp
		self.speed = speed

	def move(self, location):
		print("[지상 유닛 이동중]")
		print("{0} -> {1} 방향으로 이동한다. 속도는 {2}"\
			.format(self.name, location, self.speed))

class BuildingUnit(Unit):
	def __init__(self, name, hp, location):
		super().__init__(name, hp, 0) # super는 self 생략
		# Unit.__init__(self, name, hp, 0) 동일
		self.location = location

class Unit:
	def __init__(self):
		print("Unit 생성자")

class Flyable:
	def __init__(self):
		print("Flyable 생성자")

class Profile:
	def __init__(self):
		print("hello world")

class FlyableUnit(Flyable, Unit, Profile):
	def __init__(self):
		# super().__init__()  super는 첫 번쨰 첫 번쨰 파라미터만 상속 받는다. 
		Unit.__init__(self)
		Flyable.__init__(self)
		Profile.__init__(self)

dropship = FlyableUnit()