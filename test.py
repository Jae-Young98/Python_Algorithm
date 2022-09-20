dict = {'ewcha': [183, 75, 22.4, '정상'],
        'bypark': [158, 41, 16.42, '저체중'],
        'jmhan': [160, 43, 16.8, '저체중']}

newKey = ['height', 'weight', 'bmi', 'jedge']
for k in dict.keys():
    dict[k][newKey[0]] = dict[k][0]
print(dict)
