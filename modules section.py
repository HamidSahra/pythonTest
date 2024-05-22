
import modulesHamidSahranavardSiyahmazgi as hss
from modulesHamidSahranavardSiyahmazgi import hello, sms, user
from modulesHamidSahranavardSiyahmazgi import *

import platform
print(platform.processor)
print(platform.machine)

import random
print(random.randint(15, 27))

hss.greeting("hamid")
u2 = hss.User()

import mymodule


mymodule.hello("hamid")
mymodule.sms("09381834121")

u1 = mymodule.User()


print(user["name"])

print(user["age"])

x = dir(hss)
print(x)

print(random.choice(mylist))