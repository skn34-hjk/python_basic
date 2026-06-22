def hello():
    print("Hello from module!")

if __name__== '__main__': # 현재 실행중인 모듈의 이름을 가져와주는 매직메서드 __name__
    print('직접 실행하다')
    hello()