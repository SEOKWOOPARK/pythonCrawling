import travel.thailand # 마지막 단위는 모듈이나 패키지만 가능. 함수와 클래스 불가

trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

print('---------------------------------')

from travel.thailand import ThailandPackage

trip_to = ThailandPackage()
trip_to.detail()

print('---------------------------------')

from travel import vietnam

trip_to = vietnam.VietnamPackage()
trip_to.detail()

print('---------------------------------')

from travel import * # __init.py__ => __all__ 설정 범위

# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

trip_to = thailand.ThailandPackage()
trip_to.detail()

print('---------------------------------')

import inspect 
import random

print(inspect.getfile(random)) # 불러올 모듈 위치 검사
print(inspect.getfile(thailand))