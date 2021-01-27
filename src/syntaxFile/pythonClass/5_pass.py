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
		pass # init이 작성된 것처럼 인식하고 패싱

supply_depot = BuildingUnit("서플라이 디팟", 500, "7시")

def game_start():
	print("새로운 게임 시작")

def game_over():
	pass

game_start()
game_over()