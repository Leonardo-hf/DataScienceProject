import math
import os


# 计算文件数目以及对月度数据进行分析

def fileNumber(filepath):
    number = 0
    for root, dirs, files in os.walk(filepath):
        for file in files:
            number += 1
    print(number)


# 全部微博 赞：6.9096616672479945 分享：4.621860830136031 评论：5.097706662016044
def radix():
    DEC = []
    JAN = []
    FEB = []
    MAR = []
    APR = []
    MAY = []
    JUN = []
    for root, dirs, files in os.walk('weibo'):
        for file in files:
            file = open(os.path.join(root, file), 'r', encoding='utf-8')
            lines = file.read().split('\n')
            for line in lines:
                line = line.split('_')
                if len(line) == 6:
                    time = line[1].split(' ')[1]
                    if time == 'Dec':
                        DEC.append(round(math.log(int(line[4]) + 1)) / 6.9096616672479945 + round(
                            math.log(int(line[3]) + 1)) / 5.097706662016044 + round(
                            math.log(int(line[5]) + 1)) / 4.621860830136031)
                    elif time == 'Jan':
                        JAN.append(round(math.log(int(line[4]) + 1)) / 6.9096616672479945 + round(
                            math.log(int(line[3]) + 1)) / 5.097706662016044 + round(
                            math.log(int(line[5]) + 1)) / 4.621860830136031)
                    elif time == 'Feb':
                        FEB.append(round(math.log(int(line[4]) + 1)) / 6.9096616672479945 + round(
                            math.log(int(line[3]) + 1)) / 5.097706662016044 + round(
                            math.log(int(line[5]) + 1)) / 4.621860830136031)
                    elif time == 'Mar':
                        MAR.append(round(math.log(int(line[4]) + 1)) / 6.9096616672479945 + round(
                            math.log(int(line[3]) + 1)) / 5.097706662016044 + round(
                            math.log(int(line[5]) + 1)) / 4.621860830136031)
                    elif time == 'Apr':
                        APR.append(round(math.log(int(line[4]) + 1)) / 6.9096616672479945 + round(
                            math.log(int(line[3]) + 1)) / 5.097706662016044 + round(
                            math.log(int(line[5]) + 1)) / 4.621860830136031)
                    elif time == 'May':
                        MAY.append(round(math.log(int(line[4]) + 1)) / 6.9096616672479945 + round(
                            math.log(int(line[3]) + 1)) / 5.097706662016044 + round(
                            math.log(int(line[5]) + 1)) / 4.621860830136031)
                    elif time == 'Jun':
                        JUN.append(round(math.log(int(line[4]) + 1)) / 6.9096616672479945 + round(
                            math.log(int(line[3]) + 1)) / 5.097706662016044 + round(
                            math.log(int(line[5]) + 1)) / 4.621860830136031)
            file.close()
    ExpectSUMAndList(DEC)
    ExpectSUMAndList(JAN)
    ExpectSUMAndList(FEB)
    ExpectSUMAndList(MAR)
    ExpectSUMAndList(APR)
    ExpectSUMAndList(MAY)
    ExpectSUMAndList(JUN)


def ExpectSUMAndList(lists):
    print(str(sum(lists)) + ' ' + str(len(lists)) + ' ' + str(sum(lists) / len(lists)), end=' ')
    print(lists)


radix()
# fileNumber('comment')
