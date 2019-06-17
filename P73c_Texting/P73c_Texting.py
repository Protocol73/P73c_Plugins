#Texting Plugin for Programs writen by Protocol73
#P73c-Texting.py {Subject to Change Without Notice}
# --- V 0.0.2 --- June 2019 
#Requires P73c-Texting.cfg  from [https://github.com/Protocol73/P73c_Plugins]

#[START P73c-Texting]

import smtplib #For conecting to smtp Server
from email import encoders

try: #for py v2 vs v3 input
    input = raw_input
except NameError:
    pass
try:
    import ConfigParser# Python 2
except ImportError:
    from configparser import ConfigParser
    import configparser as ConfigParser
try: #for Python smtp usage
    from email.MIMEText import MIMEText
    from email.MIMEMultipart import MIMEMultipart
except ImportError:
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

#import Settings from P73c-Texting.cfg

cfg_settings = ConfigParser.RawConfigParser()
configFilePath = r'P73c-Texting.cfg'
cfg_settings.read(configFilePath)

password = cfg_settings.get('Setting', 'password')
fromaddr = cfg_settings.get('Setting', 'fromaddr')

#=====================================================
def SMTP_Send(Message,Phone_email):#Don't Call this.
	msg = MIMEMultipart()
	msg.attach(MIMEText(Message, 'plain'))
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, password)
	try:
		server.sendmail(fromaddr,Phone_email,Message)
		return 0
	except SMTPException:
		return 1
	server.quit()
#=====================================================
def SendText(Ph_num,set_Carrier,Message):
	Carrier = cfg_settings.get('Gateway',set_Carrier)
	Phone_email = Ph_num + Carrier
	SMTP_Send(Message,Phone_email)
#=====================================================
def main():
	print('='* 37)
	print(' -- Plugin writen by Protocol73 --')
	print(' == Not for stand-alone usage == \n')
	print('   Only run to test your cfg...') 
	print('  Enter TO: # without ANY spacing.')
	print('='* 37)
	#-------------------------------------------------
	Phone_number = input("Phone Number#:")
	Message = input("Message:")
	Carrier = input("[See CFG]Send via:")
	Texting(Phone_number,Carrier,Message)
	print('If you recive "',Message,'" at:',Phone_number)
	print('This Plugin is working')
#=====================================================

if __name__ == '__main__':
    main()
#[END P73c-Texting]