# ex 1
profiles = []

def bmi(N):
    list = []
    for i in range(N):
        userInfo = input().split()
        userInfo = [userInfo[0], int(userInfo[1]), int(userInfo[2])]
        list.append(userInfo)
        list[i].append(calc_bmi(list[i][1], list[i][2]))
        list[i].append(Judge(list[i][3]))
        profiles.append(list[i])
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


# ex 2
def bmi_list_min(profiles):
    min_bmi = profiles[0][3]
    min_idx = 0
    for i in range(len(profiles)):
        if min_bmi > profiles[i][3]:
            min_bmi = profiles[i][3]
            min_idx = i
    return profiles[min_idx]


# ex 3
def bmi_dict(profiles):
    userDict = {}
    for i in range(len(profiles)):
        userDict[profiles[i][0]] = profiles[i][1:]
    return userDict

print(bmi(3))
print(profiles)
print(bmi_list_min(profiles))
print(bmi_dict(profiles))