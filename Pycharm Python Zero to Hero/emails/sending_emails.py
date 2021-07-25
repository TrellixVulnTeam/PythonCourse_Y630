import smtplib
import getpass

smtp_object = smtplib.SMTP("smtp.gmail.com", 587)
ehlo = smtp_object.ehlo()
print(ehlo)
tls = smtp_object.starttls()
print(tls)

password = getpass.getpass("Password please: ")
email = getpass.getpass("Email: ")
password = getpass.getpass("Password: ")
smtp_object.login(email.password)
