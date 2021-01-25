import math
import os
import shutil

import numpy
import matplotlib.pyplot as plt
from scipy.stats import norm


# 高斯拟合，筛选核心数据

def getGS(data):
    x = numpy.array(data)
    mu = numpy.mean(x)
    sigma = numpy.std(x)
    num_bins = 30
    n, bins, patches = plt.hist(x, num_bins, density=1, alpha=0.75)
    y = norm.pdf(bins, mu, sigma)

    plt.grid(True)
    plt.plot(bins, y, 'r--')
    plt.xlabel('values')
    plt.ylabel('Probability')
    plt.title('Histogram : $\mu$=' + str(round(mu, 2)) + ' $\sigma=$' + str(round(sigma, 2)))
    # print(len(bins))
    # print(len(y))
    plt.show()
    return 'Histogram : $\mu$=' + str(round(mu, 2)) + ' $\sigma=$' + str(round(sigma, 2))


def NH():
    good = []

    share = []

    comment = []

    for root, dirs, files in os.walk('weibo'):
        for file in files:
            print(os.path.join(root, file), end=' ')
            file = open(os.path.join(root, file), 'r', encoding='utf-8')
            lines = file.read().split('\n')
            for line in lines:
                line = line.split('_')
                if len(line) == 6 and not int(line[4]) == 0 and not int(line[5]) == 0 and not int(line[3]) == 0:
                    good.append(round(math.log(int(line[4]))))
                    comment.append(round(math.log(int(line[3]))))
                    share.append(round(math.log(int(line[5]))))
            file.close()
    data = []
    index = 0
    good_sum = sum(good)
    comment_sum = sum(comment)
    share_sum = sum(share)
    print('赞：' + str(good_sum / len(good)) + " 分享：" + str(share_sum / len(share)) + " 评论：" + str(
        comment_sum / len(comment)))
    while index < len(good):
        data.append(good[index] / good_sum * len(good) + comment[index] / comment_sum * len(comment) + share[
            index] / share_sum * len(share))
        index += 1
    getGS(good)
    getGS(share)
    getGS(comment)
    print(getGS(data))

    '''good = []
    share = []
    comment = []'''


media = {
    '1644114654.txt': {'good': 6.4042861280046335, 'share': 4.14277439907327, 'comment': 4.811178685201274, 'mu': 3.0,
                       'sigma': 0.83},
    '2615417307.txt': {'good': 6.947234042553191, 'share': 4.473191489361702, 'comment': 5.220425531914894, 'mu': 3.0,
                       'sigma': 0.76},
    '2803301701.txt': {'good': 9.539365713018407, 'share': 6.813262364160567, 'comment': 7.289421157684631, 'mu': 3.0,
                       'sigma': 0.44},
    '3937348351.txt': {'good': 7.86027713625866, 'share': 5.719399538106235, 'comment': 5.804849884526559, 'mu': 3.0,
                       'sigma': 0.4},
    '5044281310.txt': {'good': 6.4042861280046335, 'share': 4.14277439907327, 'comment': 4.811178685201274, 'mu': 3.0,
                       'sigma': 0.81},
    '5467852665.txt': {'good': 7.264900662251655, 'share': 5.007726269315674, 'comment': 5.433774834437086, 'mu': 3.0,
                       'sigma': 0.43},
    '1887344341.txt': {'good': 7.456666666666667, 'share': 5.0633333333333335, 'comment': 5.41, 'mu': 3.0,
                       'sigma': 0.49},
    '2656274875.txt': {'good': 8.954929577464789, 'share': 6.346478873239437, 'comment': 6.830985915492958, 'mu': 3.0,
                       'sigma': 0.5},
}

NH()

'''
筛选出核心数据
pathList = []
dateList = []
fileList = []
coreWeibo = open('weibo//coreWeibo.txt', 'w', encoding='utf-8')
for root, dirs, files in os.walk('origin'):
    for file in files:
        ob = open(os.path.join(root, file), 'r', encoding='utf-8')
        lines = ob.read().split('\n')
        for line in lines:
            keepLine = line
            line = line.split('_')
            if len(line) == 6 and not int(line[4]) == 0 and not int(line[5]) == 0 and not int(line[3]) == 0 and (
                    round(math.log(int(line[4]))) / media[file]['good'] + round(
                math.log(int(line[3]))) / media[file]['comment'] + round(math.log(int(line[5]))) / media[file][
                        'share'] - media[file]['mu']) / media[file]['sigma'] > 1.28:#此处取0.1的上分位点
                pathList.append(line[0])
                date = line[1].split(' ')
                date = date[1] + date[2]
                dateList.append(date)
                fileList.append(file[0:file.index('.')])
                coreWeibo.write(keepLine + "\n")
        ob.close()

index = 0

while index < len(pathList):
    path = 'comment\\' + dateList[index] + '\\' + fileList[index] + '\\' + pathList[index]
    print(path)
    if os.path.exists(path):
        if not os.path.exists('core\\' + dateList[index]):
            os.mkdir('core\\' + dateList[index])
        for root, dirs, files in os.walk(path):
            for file in files:
                shutil.copy(os.path.join(root, file), 'core\\' + dateList[index])
    index += 1
'''
