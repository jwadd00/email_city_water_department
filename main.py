#libraries 
import os
import datetime
import smtplib
import ssl
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# number of days from start of issue
start_date = datetime.datetime.strptime("07-01-2022", '%m-%d-%Y')
today = datetime.datetime.today()
n_days = (today-start_date).days

# number of emails sent
email_start_date = datetime.datetime.strptime("12-28-2022", '%m-%d-%Y')
n_emails = (today-email_start_date).days

# address
address = os.environ['HOME_ADDRESS'] #shhhh its a secret

# to / from
email_sender = os.environ['GMAIL_ADDRESS'] #shhhh its a secret
email_password = os.environ['GOOGLE_APP_PWD'] #shhhh its a secret
email_receiver = 'jwadd00@gmail.com' # send to

# email content
subject = 'Meter Issue: Ongoing for ' + str(n_days) + ' days'
body = """
Hello,

We have had standing water near our driveway for several months now. I have emailed and called repeatedly to no avail. It would be greatly appreciated if someone could come out and take a gander. Thanks.
\n
Our address is:
""" + address + "\n\nThis is email number " + str(n_emails) + ". \n---sent automatically with python and Github Actions"

# initiate email object
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

# secure
context = ssl.create_default_context()

# execute
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())