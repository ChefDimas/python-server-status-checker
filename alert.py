import smtplib
from config import PASSWORD, LOGIN, RECEIVER


class Alert:
    def __int__(self):
        self.password = PASSWORD
        self.login = LOGIN
        self.receiver = RECEIVER

    @staticmethod
    def send_alert(message):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        try:
            s.login(LOGIN, PASSWORD)
        except Exception as e:
            print("Incorrect login or password")
        message = message
        try:
            s.sendmail(LOGIN, RECEIVER, message)
        except Exception as e:
            print("Incorrect receiver email address")
        s.quit()
