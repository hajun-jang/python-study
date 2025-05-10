# 코드블럭에 삽입하다보니 인덴트가 어긋날수 있습니다. 참고해주세요!
import smtplib
from email.mime.text import MIMEText

print('네이버 또는 구글 메일만 사용 가능합니다.')
sender_id = input('메일을 보낼 계정을 입력해 주세요: ')
print('='*50)
sender_pw = input('계정 비밀번호를 입력해 주세요: ')
print('='*50)
if 'naver' in sender_id:
    smtp_server = "smtp.naver.com"
elif 'gmail' in sender_id:
    smtp_server = "smtp.google.com"
else:
    print('네이버 또는 구글 메일만 사용 가능합니다.\n메일 주소를 확인해 주세요')
    raise Exception('네이버 또는 구글 메일만 사용 가능합니다.')

smtp_info = {
    "smtp_server": smtp_server,  # SMTP 서버 주소
    "smtp_user_id": sender_id,
    "smtp_user_pw": sender_pw,
    "smtp_port": 587 # SMTP 서버 포트
    }

to = input('받는 분 메일 주소를 입력해 주세요\n여러명일경우 ,로 구분됩니다.\nex)test@test.com, test2@test.com\n')
print('='*50)
title = input('메일 제목을 입력해 주세요\n')
print('='*50)
        
# 메일 내용이 몇줄이 들어갈지 모르기 때문에 무한반복으로 데이터를 인풋받아 리스트에 넣어줌
content = []
print('메일 내용을 작성해 주세요\n 작성 완료시 숫자 0을 입력해주세요.')
i = 0
while(True):
    i += 1
    data = input(f'{i}번째 라인: ')
    if data == '0':
        break
    else:
        content.append(data)
print('='*50)
# 리스트로 받은 content를 \n로 조인하여 줄바꿈
msg = MIMEText('\n'.join(content),_charset="utf8")

msg['Subject'] = title  # 메일 제목
msg['From'] = smtp_info['smtp_user_id']  # 송신자
msg['To'] = to
        
smtp = smtplib.SMTP(smtp_info['smtp_server'], smtp_info['smtp_port'])
smtp.starttls()  # TLS 보안 처리
smtp.login(sender_id , sender_pw)  # 로그인
        
smtp.sendmail(msg['From'], msg['To'].split(','), msg.as_string())

smtp.quit()
print('메일을 성공적으로 보냈습니다.')