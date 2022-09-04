# hw1-1
def calc_bmi(h, w):
    return 0.0


def judge(bmi):
    return '정상'


def bmi(N):
    # N명의 (이름, 키, 몸무게) 입력 받아서 리스트 만들기
    return [
        ['ewcha', 183, 75, 22.4, '정상'],
        ['bypark', 158, 41, 16.42, '저체중'],
        ['jmhan', 160, 43, 16.8, '저체중']
    ]


# hw1-2
def bmi_list_min(profiles):
    # bmi()의 결과가 profiles 에 전달 된다.
    return ['bypark', 158, 41, 16.42, '저체중']


# hw1-3
def bmi_dict(profiles):
    # bmi()의 결과가 profiles에 전달 된다.
    return {
        'ewcha': [183, 75, 22.4, '정상'],
        'bypark': [158, 41, 16.42, '저체중'],
        'jmhan': [160, 43, 16.8, '저체중']
    }


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
    # bmi_dictdict()의 결과가 pf_dd에 전달 된다.
    # attr='height', update_func=lambda x: x + 1 을 전달받을 경우
    # 즉, 모든 사람의 키를 1cm씩 증가시킴
    return {
        'ewcha': {'height':184, 'weight':75, 'bmi':22.15, 'judge':'정상'},
        'bypark': {'height':159, 'weight':41, 'bmi':16.22, 'judge':'저체중'},
        'jmhan': {'height':161, 'weight':43, 'bmi':16.59, 'judge':'저체중'}
    }


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