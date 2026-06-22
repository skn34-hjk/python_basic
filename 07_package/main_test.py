print('--- 1번 ---')

#from 절에는, 패키지/모듈급까지만 올 수 있음.
from team_management import developers as dev, managers as man

# from team_management.developers import developers_info
# from team_management.managers import managers_info

# import team_management.managers as mana
# import team_management.developers as devel

print(man.managers_info())
print(dev.developers_info()) 



print('\n--- 2번 ---')

import work_management.task_tracking as tt
import work_management.reporting as rp


print(tt.start_task('코드 리뷰'))
print(tt.end_task('코드 리뷰'))
print(rp.gengerate_report('코드 리뷰'))


print('\n--- 2-1번 ---')


from work_management.task_tracking import end_task, start_task as et, st
from work_management.reporting import gengerate_report as gr

for i, work in enumerate([st, et, gr]):
    print(i, '번째 작업: ', work('코드리뷰'))



print('\n--- 3번 ---')

import schedule_management.calender as cal

print(cal.add_event('2024-01-15', '회의'))
print(cal.remove_event('회의'))



print('\n--- 4번 ---')

import numpy as np

a = [1, 2, 3, 4, 5]

print(int(np.mean(a)))