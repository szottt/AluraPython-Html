import smtplib
from smtplib import SMTP

#email recipiente
email_from = "emailenviopython@gmail.com"
#senha
email_senha = 'testeemail'
#email destinatario
email_to = "emailenviopython@gmail.com"
#servidor SMTP
smtp = "smtp.gmail.com"

#inicia instancia
server = smtplib.SMPT(smtp, 587)

#conexao
server.starttls()

#realiza login
server.login(email_from, email_senha)

#corpo do email
msg = "TEste"

#envia email

server.sendmail(email_from,email_to,msg)

#fecha conexao

server.quit
