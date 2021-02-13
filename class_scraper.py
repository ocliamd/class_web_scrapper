import urllib.request
import string
import time
import smtplib
from email.mime.text import MIMEText

def scrap():
    lines = []
    CRN = '>25302<' #target CRN of class
    full = '>0<'    #class has 0 spots available
    with urllib.request.urlopen( 'http://classes.uoregon.edu/pls/prod/hwskdhnt.P_ListCrse?term_in=201902&sel_subj=dummy&sel_day=dummy&sel_schd=dummy&sel_insm=dummy&sel_camp=dummy&sel_levl=dummy&sel_sess=dummy&sel_instr=dummy&sel_ptrm=dummy&sel_attr=dummy&sel_cred=dummy&sel_tuition=dummy&sel_open=dummy&sel_weekend=dummy&sel_title=&sel_to_cred=&sel_from_cred=&sel_subj=PSY&sel_crse=304&sel_crn=&sel_camp=%25&sel_levl=%25&sel_attr=%25&begin_hh=0&begin_mi=0&begin_ap=a&end_hh=0&end_mi=0&end_ap=a&submit_btn=Show+Classes') as classf:
        find_class = classf.readlines() # read all lines of web page
        target = find_class[168:170]    # reduce to two lines of web page source
        for i in range(len(target)):
            lines.append(str(target[i]))    #change web page lines to list of strings
        if CRN in lines[0]:                 # if CRN found 
            print('Class CRN:', CRN, end=' ')   # found and print CRN 
        if full in lines[1]:
            print('is still full :-(')      # CRN is still full
        else:
            print('is available!')          # CRN is available
            sendmail()                      #notify via email
            exit()                          #exit program
    return None

def sendmail():
    SMTP_SERVER = "mail.uoregon.edu"
    SMTP_PORT = 587
    SMTP_USERNAME = "ldauphin@uoregon.edu"
    SMTP_PASSWORD = "your_password"

    EMAIL_TO = ["ocliam@me.com"]
    EMAIL_FROM = "ldauphin@uoregon.edu"
    EMAIL_SUBJECT = "Pysch 304"

    DATE_FORMAT = "%d/%m/%Y"
    EMAIL_SPACE = ", "

    DATA = 'Pysch 304 has an open spot.'        #email message

    msg = MIMEText(DATA)
    msg['Subject'] = EMAIL_SUBJECT #+ " %s" % (date.today().strftime(DATE_FORMAT))
    msg['To'] = EMAIL_SPACE.join(EMAIL_TO)
    msg['From'] = EMAIL_FROM
    mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    mail.starttls()
    mail.login(SMTP_USERNAME, SMTP_PASSWORD)
    mail.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    mail.quit()
    return None

    
def main():
    while True:
        scrap()
        time.sleep(300)
    return None

main()
