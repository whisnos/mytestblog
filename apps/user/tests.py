from django.test import TestCase

# Create your tests here.
import json
tup=(1,2,3)
a=json.dumps(tup)   #json中不存在元组。序列化元组之后元组变列表
print(a)
print(json.loads(a))


import json
mset={1,2,3}      #不能是集合，序列化集合报错。
print(json.dumps(mset))