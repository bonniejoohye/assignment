'''
Q2. 인자에 따라 홀수 구구단(1,3,5,7,9단) 또는 짝수 구구단(2,4,6,8단)을 출력하는 함수 작성 및 실행
• 인자로 숫자 하나를 받는다.
• 해당숫자가홀수면홀수구구단출력
• 해당숫자가짝수면짝수구구단출력
• 두개 숫자 포맷팅 => print(“%d * %d” %(1,2))
'''

def gugu_even():   
    for i in range(2,10,2):
            for j in range(1,10):
                print("%d X %d = %d" %(i,j,i*j))

def gugu_odd():
    for i in range(1,10,2):
            for j in range(1,10):
                print("%d X %d = %d" %(i,j,i*j))

def gugu(num):
    if (num%2==1):
        gugu_odd()
    else:
        gugu_even()

 gugu(30)