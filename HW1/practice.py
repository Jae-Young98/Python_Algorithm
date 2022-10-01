# ex 1
def bmi(N):
    profiles = []
    for i in range(N):
        userInfo = input().split()
        userInfo = [userInfo[0], int(userInfo[1]), int(userInfo[2])]
        profiles.append(userInfo)
        profiles[i].append(calc_bmi(profiles[i][1], profiles[i][2]))
        profiles[i].append(Judge(profiles[i][3]))
    return profiles


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
    pf_dict = {}
    for i in range(len(profiles)):
        pf_dict[profiles[i][0]] = profiles[i][1:]
    return pf_dict

# ex 4


def bmi_dictdict(pf_dict):
    pf_dd = {}
    for key, value in pf_dict.items():
        pf_dd[key] = key = {'height': value[0],
                            'weight': value[1],
                            'bmi': value[2],
                            'judge': value[3]}
    return pf_dd


# bmis = bmi(3)
# print(bmis)
# light = bmi_list_min(bmis)
# print(light)
# bmis = bmi_dict(bmis)
# print(bmis)
# bmis = bmi_dictdict(bmis)
# print(bmis)
