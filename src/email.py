import smtplib

def send_email():
    receivers_list = ["abcd@gmail.com", "efgh@gmail.com", "hijk@gmail.com"]

    for user in receivers_list:
        s = smtplib.SMTP('smtp.gmail.com', 587)

        s.starttls()

        s.login("YourEmailId@gmail.com", "YourEmailpassword")

        message = "I am spamming you with gmails"

        s.sendmail("sender_email_id", user, message)

        s.quit()