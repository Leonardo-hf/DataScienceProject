import os
from time import sleep

# 初步筛选删除垃圾评论

cal = 0
pathList = []
for root, dirs, files in os.walk('core'):
    for file in files:
        path = os.path.join(root, file)
        ob = open(path, 'r', encoding='utf-8')
        text = ob.read()
        if text == '转发微博' or text == ' ':
            pathList.append(path)
            ob.close()
            continue
        while text.startswith(' ') or text.startswith('@'):
            if text.startswith(' '):
                print(text, end='_')
                text = text[1:]
                ob.close()
                ob = open(path, 'w', encoding='utf-8')
                ob.write(text)
                print(text)
            if text.startswith('@'):
                print(text, end='_')
                if not text.find(' ') == -1:
                    text = text[text.index(' ') + 1:]
                    ob.close()
                    ob = open(path, 'w', encoding='utf-8')
                    ob.write(text)
                else:
                    pathList.append(path)
                    break
                print(text)
        if len(text) == 0:
            print('empty' + str(cal))
            cal += 1
            pathList.append(path)
            ob.close()
            continue
        ob.close()
for each in pathList:
    os.remove(each)
