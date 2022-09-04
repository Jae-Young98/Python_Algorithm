# hw1-1

# 2차원 리스트 1, 2번 인덱스 정수로 변환 해줘야함
def bmi(N):
    list = []
    for i in range(N):
        info = input().split()
        list.append(info)
        list[i].append(bmi_calc(list[i][1], list[i][2]))
        list[i].append(Judge(list[i][3]))
    return list

def bmi_calc(h, w):
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



print(bmi(1))