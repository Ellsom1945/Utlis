def tos(t):
    if t < 10:
        return "0"+str(t)
    else:
        return str(t)
def trans(s, t1, t2, t3, t4):
    s1 = s.split(':')
    time1, time2 = int(s1[0]), int(s1[1])
    time3, time4 = map(int, s1[2].split('.'))

    time1 += t1
    time2 += t2
    time3 += t3
    time4 += t4

    while time4 >= 100:
        time4 -= 100
        time3 += 1
    while time4 < 0:
        time4 += 100
        time3 -= 1

    while time3 >= 60:
        time3 -= 60
        time2 += 1
    while time3 < 0:
        time3 += 60
        time2 -= 1

    while time2 >= 60:
        time2 -= 60
        time1 += 1
    while time2 < 0:
        time2 += 60
        time1 -= 1

    return tos(time1) + ':' + tos(time2) + ':' + tos(time3) + '.' + tos(time4)


# 修改字幕文件名称
f = open('Justice League.txt', 'r', encoding='UTF-8')
fo = open('Justice1 League.txt', 'w', encoding='UTF-8')
lines = f.readlines()
for line in lines:
    if line[:8] == 'Dialogue':
        lis = line.split(',')
        st = lis[1]
        ed = lis[2]
        # 修改时间差
        new_st = trans(st, 0, 0, 36, 0)
        new_ed = trans(ed, 0, 0, 36, 0)
        lis[1] = new_st
        lis[2] = new_ed
        new_line = ','.join(lis)
        fo.write(new_line)
    else:
        fo.write(line)
f.close()
fo.close()
