dict = {'ewcha': [183, 75, 22.4, '정상'],
        'bypark': [158, 41, 16.42, '저체중'],
        'jmhan': [160, 43, 16.8, '저체중']}


def test(pf_dict):
    pf_dd = {}
    for key, value in pf_dict.items():
        # pf_dd = key
        pf_dd[key] = key = {'height': value[0],
                            'weight': value[1],
                            'bmi': value[2],
                            'judge': value[3]}
    return pf_dd

# def test2(pf_dd, attr, update_func):
#     for key, value in pf_dd.items():
#         pf_dd[key][attr] 

# sample2 = test2(dict, 'height', lambda x: x + 1)
sample = test(dict)
print(sample['ewcha']['height'])
