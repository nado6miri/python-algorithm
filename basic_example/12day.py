import theather_module
theather_module.price(3)
theather_module.price_morning(4)
theather_module.price_soldier(5)

import theather_module as mv
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

from theather_module import *
#from random import *
price(3)
price_morning(4)
price_soldier(5)

from theather_module import price, price_morning
price(5)
price_morning(6)
price_soldier(7)

from theather_module import price_soldier as price
price(5)


import travel.thailand
#import travel.thailand.ThailandPackage
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel.vietnam import VietnamPackage
trip_to = travel.vietnam.VietnamPackage()
trip_to.detail()

from travel import *
trip_to = vietnam.VietnamPackage()
trip_to.detail()

trip_to = thailand.ThailandPackage()
trip_to.detail()


# 내가 만든 모듈/패키지를 python의 기본 라이브러리로 이동하는 방법
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))
