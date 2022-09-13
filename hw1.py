# ex 1

def bmi(N):
    list = []
    for i in range(N):
        userInfo = input().split()
        userInfo = [userInfo[0], int(userInfo[1]), int(userInfo[2])]
        list.append(userInfo)
        list[i].append(calc_bmi(list[i][1], list[i][2]))
        list[i].append(Judge(list[i][3]))
    return list


def calc_bmi(h, w):
    H = 0.01 * int(h)
    W = int(w)
    bmi = W / (H * H)
    return round(bmi, 2)


def Judge(bmi):
    if bmi < 18.5:
        return '저체중'
    elif 18.5 <= bmi < 23:
        return '정상'
    elif 23 <= bmi < 25:
        return '과체중'
    else:
        return '비만'


print(bmi(3))
