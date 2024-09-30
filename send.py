import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication 
import time

def send(toaddrs, professor_name, fromaddr, password):
    content = ""
    with open('content.html', 'r', encoding='utf-8') as f:
        content = f.read()

    cvFile = 'CV_Zhonghan.pdf'
    pdfApart1 = MIMEApplication(open(cvFile, 'rb').read())
    pdfApart1.add_header('Content-Disposition', 'attachment', filename=cvFile)

    TranscriptFile1 = 'Transcript_Master.pdf'
    pdfApart2 = MIMEApplication(open(TranscriptFile1, 'rb').read())
    pdfApart2.add_header('Content-Disposition', 'attachment', filename=TranscriptFile1)

    TranscriptFile2 = 'Transcript_Undergraduate.pdf'
    pdfApart3 = MIMEApplication(open(TranscriptFile2, 'rb').read())
    pdfApart3.add_header('Content-Disposition', 'attachment', filename=TranscriptFile2)

    paperFile = 'LS_NRA_VMCAI2024.pdf'
    pdfApart4 = MIMEApplication(open(paperFile, 'rb').read())
    pdfApart4.add_header('Content-Disposition', 'attachment', filename=paperFile)

    paperFile2 = 'clauseSMT.pdf'
    pdfApart5 = MIMEApplication(open(paperFile2, 'rb').read())
    pdfApart5.add_header('Content-Disposition', 'attachment', filename=paperFile2)

    RSFile = 'Research_Statement_0827.pdf'
    pdfApart6 = MIMEApplication(open(RSFile, 'rb').read())
    pdfApart6.add_header('Content-Disposition', 'attachment', filename=RSFile)

    m = MIMEMultipart()
    m.attach(MIMEText(content.replace("[Name]", professor_name), 'html', 'utf-8'))
    m.attach(pdfApart1)
    m.attach(pdfApart2)
    m.attach(pdfApart3)
    m.attach(pdfApart4)
    m.attach(pdfApart5)
    m.attach(pdfApart6)
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
    myemail = "your_email@email.com"
    password = "your_password"
    assert len(send2url) == len(names)
    for i in range(len(send2url)):
        send([send2url[i]], names[i], myemail, password)
        print("Email sent to", names[i])
        time.sleep(3)
    print("All emails sent successfully!")