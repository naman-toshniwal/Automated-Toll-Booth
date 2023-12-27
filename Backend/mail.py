import smtplib

try:
    smtp=smtplib.SMTP('smtp.gmail.com',587)
    smtp.starttls()
    smtp.login("devinx34@gmail.com","ndmqnzqhsjenhpii")
    smtp.sendmail("devinx34@gmail.com","","YOUR TOLL TAX HAS SUCCESSFULLY BEEN DEBBITED FROM YOUR ACCOUNT")
    smtp.quit()
    print("Email sent successfully")
    
except Exception as err:
    print("Something went wrong...",err)

