from datetime import timedelta, datetime


hoje = datetime.today()
amanha =datetime.today() + timedelta( hours=12, minutes=55)

print(amanha - hoje)