import theaterModule

theaterModule.price(3)
theaterModule.price_morning(5)
theaterModule.price_soldier(9)

print('----------------------------------------')

import theaterModule as mv

mv.price(4)
mv.price_soldier(3)

print('----------------------------------------')

from theaterModule import *
# 모듈 내 모든 함수 바로 사용가능

price(3)
price_morning(2)

print('----------------------------------------')

from theaterModule import price, price_morning
# 모듈 내 필요한 함수 선별

price(5)
price_morning(6)

print('----------------------------------------')

from theaterModule import price_soldier as price
# 원하는 모듈 함수 as로 호출

price(2)