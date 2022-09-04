# ewcha	183  75
# bypark 158  41
# jmhan	160  43

from hw1_skeleton import *
from pprint import pprint

#hw1-1
bmis = bmi(3)
print('list of lists:')
pprint(bmis)

#hw1-2
lightest = bmi_list_min(bmis)
print('\nlightest:')
pprint(lightest)

#hw1-3
bmis = bmi_dict(bmis)
print('\ndict of lists:')
pprint(bmis)

#hw1-4
bmis = bmi_dictdict(bmis)
print('\ndict of dicts:')
pprint(bmis)

#hw1-5
bmis = bmi_dictdict_fix(bmis, 'height', lambda x: x + 1)
print('\ndictdit_fixed:')
pprint(bmis)

#hw1-6
light = bmi_dictdict_filter(bmis, '저체중')
print('\nlight people:', light)
# normal = bmi_dictdict_filter(bmis, '정상')
# print('normal people:', normal)
# heavy = bmi_dictdict_filter(bmis, '과체중')
# print('heavy people:', heavy)
# too_heavy = bmi_dictdict_filter(bmis, '비만')
# print('too heavy people:', too_heavy)

#hw1-7
groups = bmi_dictdict_group(bmis)
print('\ngroup by judgements:')
print(groups)