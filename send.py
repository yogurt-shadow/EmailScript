import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication 
import time

def send(toaddrs, professor_name, fromaddr, password, files):
    content = ""
    with open('content.html', 'r', encoding='utf-8') as f:
        content = f.read()
    pdfs = []
    for file in files:
        pdfApart = MIMEApplication(open(file, 'rb').read())
        pdfApart.add_header('Content-Disposition', 'attachment', filename=file)
        pdfs.append(pdfApart)
    m = MIMEMultipart()
    m.attach(MIMEText(content.replace("[Name]", professor_name), 'html', 'utf-8'))
    for pdf in pdfs:
        m.attach(pdf)
    m['Subject'] = 'Application for 25Fall PhD - Zhonghan Wang'

    try:
        server = smtplib.SMTP('mail.ios.ac.cn')
        server.login(fromaddr,password)
        server.sendmail(fromaddr, toaddrs, m.as_string())
        print('success')
        server.quit()
    except smtplib.SMTPException as e:
        print('error:',e)

if __name__ == '__main__':
    send2url = [
        "prof1@email.com",
        "prof2@email.com"
    ]
    names = [
        "prof1", "prof2"
    ]
    attaches = [
        "CV_Zhonghan.pdf",
        "Transcript_Master.pdf",
        "Transcript_Undergraduate.pdf",
        "LS_NRA_VMCAI2024.pdf",
        "clauseSMT.pdf",
        "Research_Statement_0827.pdf"
    ]
    sender_email = "your_email@email.com"
    sender_password = "your_password"
    assert len(send2url) == len(names)
    for i in range(len(send2url)):
        send([send2url[i]], names[i], sender_email, sender_password, attaches)
        print("Email sent to", names[i])
        time.sleep(3)
    print("All emails sent successfully!")