import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def enviarmail(toadrr, name, namedest):
    try:
        fromaddr = "jrfirmino01@gmail.com"
        # toaddr = 'julreifir@yahoo.com.br'
        msg = MIMEMultipart()

        msg['From'] = fromaddr
        msg['To'] = toadrr
        msg['Subject'] = 'Amigo Secreto 2020 (Família Firmino)'

        body = "\nChegou o grande dia!!!.\nHoje você saberá o seu amigo oculto 2020 " \
               f"(Grupo da Família Firmino),\nSegue descrito abaixo o nome do seu amigo oculto:" \
               f"\n{name}, segue o nome do seu amigo secreto --> {namedest.upper()}.\nEspero que tenha gostado!!!!"

        msg.attach(MIMEText(body, 'plain'))

        filename = 'Resume.pdf'

        attachment = open(filename,'rb')


        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        msg.attach(part)

        attachment.close()

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, '*******')
        text = msg.as_string()
        server.sendmail(fromaddr, toadrr, text)
        server.quit()
        print('\nEmail enviado ao destinatário com sucesso!')
    except:
        print("\nErro ao enviar email")
