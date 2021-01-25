# 月度微博关键词数据提供

file = open('origin\\5044281310.txt', 'r', encoding='utf=8')
things = file.read().split('\n')
oldDate = 'Dec31'
newFile = open('test\\Dec31.text', 'a+', encoding='utf-8')
for each in things:
    each = each.split('_')
    date = each[1].split(' ')
    date = date[1] + date[2]
    if not date == oldDate:
        oldDate = date
        newFile.close()
        newFile = open('test\\' + date + '.text', 'a+', encoding='utf-8')
    elif date.startswith('Jan'):
        newFile.write(each[2])
