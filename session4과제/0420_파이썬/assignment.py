# 과제 1. 별찍기 (4월 20일까지)
# - 아래와 같이 * 을 출력 하는 프로그램을 만들어보세요
# **********
# *********
# ********
# *******
# *****
# ****
# ***
# **
# *

i=10
while i>0:
    print('*'* i)
    i=i-1

# # 과제 2. 구구단 (4월 20일까지)
# - 구구단 2단을 출력해보세요!

j=1
while j <10:
    print(j*2)
    j=j+1

for i in range(1,10):
    print("2 X %d = %d" %(i,2*i))

# 과제 3. while 문을 활용하여 1부터 1000까지의 자연수 중 3의 배수의 합을 구해보세요. (4월 20일까지)

i=1
j=0
while 3*i <1000:
    j+=3*(i)
    i=i+1
print(j)
    

# 과제 4. for 문을 활용하여 멋사 학생들의 평균 점수를 구해보세요. (4월 20일까지)
mutsa_scores = [90, 77, 40, 55, 90, 100, 88]

total_score=0
for score in mutsa_scores:
    total_score+= score
 
print(total_score/len(mutsa_scores))

# 과제 5. input.py 문제 2개 풀기 (4월 20일까지)

# 과제 6. HTML / CSS 페이스북 모바일 클론코딩 (4월 27일까지)
# - 이미지 자율
# - 까먹기전에 해주세요~
