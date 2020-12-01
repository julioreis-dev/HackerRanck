import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import time


def enviarmail(*args):
    try:
        atual = time.localtime()
        fromaddr = "jrfirmino01@gmail.com"
        # toaddr = 'julreifir@yahoo.com.br'
        msg = MIMEMultipart()

        msg['From'] = fromaddr
        msg['To'] = args[0]
        msg['Subject'] = f'Amigo Secreto {atual[0]} (Família Firmino)'

        body = f"Como vai {args[1]}, tudo bem com você?.\nHoje é o grande dia, você conhecerá o seu " \
               f"amigo oculto {atual[0]} - (Grupo da Família Firmino).\nSegue descrito abaixo " \
               f"o nome do seu amigo oculto:\nPrepare-se pois, para a sua surpresa o nome do seu grande " \
               f"amigo secreto é {args[2].upper()}.\nNão conta para ninguem e espero que tenha gostado!!!.\nParabens!!!"

        msg.attach(MIMEText(body, 'plain'))

        filename = 'Resume.pdf'

        attachment = open(filename, 'rb')

        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        msg.attach(part)

        attachment.close()

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, 'Manuela01*')
        text = msg.as_string()
        server.sendmail(fromaddr, args[0], text)
        server.quit()
        print(f'Email enviado para {args[1]} com sucesso!\n')
    except:
        print("\nErro ao enviar email")
