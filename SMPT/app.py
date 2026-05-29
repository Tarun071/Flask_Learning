import smtplib
from email.message import EmailMessage
import random
import os
from itsdangerous import URLSafeTimedSerializer

serializer = URLSafeTimedSerializer("bd97315bcb7a13d286eaa8f78e2cafee1f433d03ca3127c656b3e81a8b98fbb0")
otp=str(random.randint(1000, 9999))


sender = "talaganatarun123@gmail.com"
password = "qapo dpdq guco rrwf"
msg = EmailMessage()
msg['Subject'] = "Registration"
msg['From'] = sender
msg['To'] = "dimplechittimuju2005@gmail.com"
msg.set_content(otp)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender, password)
server.send_message(msg)

server.quit()

ans=input()
if otp==ans:
    token = serializer.dumps(
    "verification succesfull"
    )
    email = serializer.loads(
    token)
else:

    print("Inavalid OTP")

# secret_key = os.urandom(32).hex()

# print(secret_key)