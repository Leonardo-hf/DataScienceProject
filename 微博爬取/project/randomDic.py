import os
import random
from time import sleep

# 词典人工标签的随机化抽取

number = 0
flag = False
keepPath = ''
allList = []
tempList = []
for root, dirs, files in os.walk('test'):
    for file in files:
        if not root == keepPath:
            keepPath = root
            allList.append(tempList)
            tempList = []
        tempList.append(os.path.join(root, file))

allList.append(tempList)
allList.pop(0)

for each in allList:
    while len(each) > 300:
        index = random.randint(0, len(each) - 1)
        path = each[index]
        os.remove(path)
        each.pop(index)
