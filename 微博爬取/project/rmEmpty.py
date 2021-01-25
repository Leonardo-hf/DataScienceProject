import os

# 删除空文件夹

path = 'core'

for dirpath, dirnames, filenames in os.walk(path):

    for i in dirnames:

        if not os.listdir(os.path.join(dirpath, i)):
            os.rmdir(os.path.join(dirpath, i))
