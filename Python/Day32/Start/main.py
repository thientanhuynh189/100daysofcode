# import smtplib
#
# # my_email = "appbrewery.student2021@gmail.com"
# # password = "abcd123()"
# my_email = "appbrewery.student@yahoo.com"
# password = "tlyzlxmcnflevhns"
#
# with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="appbrewery.student2021@gmail.com",
#         msg="Subject:Hello\n\nThis is the body of email."
#     )

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1995, month=12, day=15)
# print(date_of_birth)


import datetime
import smtplib
import random

MY_EMAIL = "appbrewery.student2021@gmail.com"
MY_PASSWORD = "abcd123()"

now = datetime.datetime.now()
current_weekday = now.weekday()

if current_weekday == 1:
    with open("quotes.txt") as quote_file:
        quote_list = quote_file.readlines()
        random_quote = random.choice(quote_list)
        quote = random_quote.encode('utf-8').strip()
        print(random_quote)
        # with smtplib.SMTP("smtp.gmail.com") as connection:
        #     connection.starttls()
        #     connection.login(MY_EMAIL, MY_PASSWORD)
        #     connection.sendmail(from_addr=MY_EMAIL,
        #                         to_addrs=MY_EMAIL,
        #                         msg=f"Subject:Monday Motivation\n\n{quote}"
        #                         )
        print(quote)
