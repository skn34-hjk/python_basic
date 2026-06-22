print('--- 1번 ---')

import team_module 

print('안녕하세요, ', team_module.company, '입니다')
print(team_module.introduce_manager())
print(team_module.introduce_developers())



print('--- 2번 ---')

import attandance_module

print(attandance_module.record_attendance('카피바라', '9:00'))
print(attandance_module.record_leave('카피바라', '18:00'))



print('--- 3번 ---')

import task_module as tm

print(tm.start_task('코드 리뷰'))
print(tm.complete_task('코드 리뷰'))



print('--- 4번 ---')

import math 

task = [10, 12, 8, 15, 9]
more = 0

avg = sum(task)/len(task)

for i in task:
    if i > avg:
        more = more+1

print('평균 업무량: ', avg)
print('평균 업무량보다 많이 처리한 날의 수: ', more)



print('--- 5번 ---')

import datetime

def report(name, taskname):
    return f"[{datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')}] {name}님이 작업'{taskname}'을(를) 완료했습니다."

print(report('카피바라', '코드 리뷰'))


# from datetime import datetime as dt

# dt.now().strftime('%Y/%m/%d %H:%M:%S')