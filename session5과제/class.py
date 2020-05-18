'''
실습
멋쟁이사자처럼 폴더 안에 session5 디렉토리 생성 class.py 파일 생성
FourCal 클래스 만들기
• 이름, 나이, 학교 속성을 지정하는 __init__ 메서드 작성
• 사칙연산(더하기, 빼기, 나누기, 곱하기) 메서드 작성
FourCal 클래스를 통해 계산기(객체) 만들기 속성, 메서드 결과 출력해보기
'''

class FourCal:
    def __init__(self, name, age, school):
        self.name =name
        self.age =age
        self.school=school
        self.add_num=0
        self.subtract_num=0
        self.multiply_num=0
        self.divide_num=0


    def add(self, n1, n2):
        self.add_num+= 1
        result = n1+n2
        return result
    def subtract(self,n1,n2):
        self.subtract_num+= 1
        result= n1-n2
        return result
    def multiply(self,n1,n2):
        self.multiply_num+= 1
        result=n1*n2
        return result
    def divide(self,n1,n2):
        if num2==0:
            print("0으로 못나눈다")
            return none
        self.divide_num+= 1
        result=n1/n2
        return result
    def showcount(self):
        print("덧셈: %d" % self.add_num)
        print("뺄셈: %d" % self.subtract_num)
        print("곱셉: %d" % self.multiply_num)
        print("나눗셈: %d" % self.divide_num)


person = FourCal("joohye",24,"korea_univ")
print(person.name, person.age, person.school)
print(person.add(3,2))
person.showcount()


