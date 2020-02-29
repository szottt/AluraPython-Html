# import smtplib

# #email recipiente
# email_from = "emailenviopython@gmail.com"
# #senha
# email_senha = 'testeemail'
# #email destinatario
# email_to = "emailenviopython@gmail.com"
# #servidor SMTP
# smtp = "smtp.gmail.com"

# server = smtplib.SMTP(smtp, 578)

# msg = "Teste email"


# server.starttls()

# server.login(email_from, email_senha)


# server.sendmail(email_from,email_to,msg)

# server.quit()


import smtplib
s = smtplib.SMTP("localhost")
print(s.help())