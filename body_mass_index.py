#체중과 신장 물어보는 코드
weight = int(input('키가 몇인가요? 입력해주세요:'))
height = int(input('체중이 몇인가요? 입력해주세요:'))
#체질량 계산 코드
height = height/100
BMI = weight / (height * height)
#대답 코드
print('당신의 BMI 지수는', BMI ,'입니다.')