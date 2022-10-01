# hw1-1
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


def bmi(N):
    profiles = []
    for i in range(N):
        userInfo = input().split()
        userInfo = [userInfo[0], int(userInfo[1]), int(userInfo[2])]
        profiles.append(userInfo)
        profiles[i].append(calc_bmi(profiles[i][1], profiles[i][2]))
        profiles[i].append(Judge(profiles[i][3]))
    return profiles


# hw1-2
def bmi_list_min(profiles):
    min_bmi = profiles[0][3]
    min_idx = 0
    for i in range(len(profiles)):
        if min_bmi > profiles[i][3]:
            min_bmi = profiles[i][3]
            min_idx = i
    return profiles[min_idx]


# hw1-3
def bmi_dict(profiles):
    pf_dict = {}
    for i in range(len(profiles)):
        pf_dict[profiles[i][0]] = profiles[i][1:]
    return pf_dict


# hw1-4
def bmi_dictdict(pf_dict):
    # bmi_dict()를 실행한 결과가 pf_dict에 전달 된다.
    return {
        'ewcha': {'height': 183, 'weight': 75, 'bmi': 22.4, 'judge': '정상'},
        'bypark': {'height': 158, 'weight': 41, 'bmi': 16.42, 'judge': '저체중'},
        'jmhan': {'height': 160, 'weight': 43, 'bmi': 16.8, 'judge': '저체중'}
    }


# hw1-5


def bmi_dictdict_fix(pf_dd, attr, update_func):
    pass

# hw1-6


def bmi_dictdict_filter(pf_dd, jfilter):
    # bmi_dictdict()를 실행한 결과가 pf_dd에 전달 된다.
    # jfilter='저체중'이 전달될 경우
    return {'bypark', 'jmhan'}


# hw1-7
def bmi_dictdict_group(pf_dd):
    # bmi_dictdict()를 실행한 결과가 pf_dd에 전달 된다.
    return {
        '저체중': {'bypark', 'jmhan'},
        '정상': {'ewcha'},
        '과체중': set(),
        '비만': set()
    }
