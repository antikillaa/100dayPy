import smtplib
import datetime as dt

# my_email = "zlymvSeRhc9@yahoo.com"
# password = "sbcxeorcmrvciuti"
#
# connection = smtplib.SMTP("smtp.mail.yahoo.com", port=465)
#
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs="7zlymvSeRhc9@gmail.com", msg="Hello")
# connection.close()


date = dt.datetime.now()
year = date.year

date_of_birth = dt.datetime(year=1995, month=12, day=25)
print(date_of_birth)
