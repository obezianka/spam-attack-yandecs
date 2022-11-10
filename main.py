import smtplib
import json
with open("lololo.json", "r") as my_file:
    file_contents = my_file.read()
pochta1 = json.loads(file_contents)
pochta = input("Твоя яндекс почта :")
password=input("Напиши пароль,без смс и регистрации онлайн без номера телефона P.s это не взлом :")
neletter =f"""\
From:{pochta}
To: {pochta1}
Subject: Реклама
Content-Type: text/plain; charset="UTF-8";

"""
print(neletter)

with open("txt.txt", "r" , encoding="UTF-8") as my_file:
  text = my_file.read()

#________________________________________________________________________________________________________=
x1 = "Броуууууууууу"
text = text.replace("%friend_name%" , x1 )
x2 ="Чичня"
text = text.replace("%my_name%", x2)
x3 = "polus101.ru"
text = text.replace("%website%", x3)
x1 = input ("Каму:")
x2 = input ("Ат каго:")
print(text)
#_________________________________________________________________________________________________=
letter= neletter + text
letter = letter.encode("UTF-8")
print(letter)
server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(pochta, password)
server.sendmail(pochta, pochta1, letter)
server.quit()
