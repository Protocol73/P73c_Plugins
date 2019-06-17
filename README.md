# P73c_Plugins
Independent Python Plugins


Simple easy to import functions for Python

# P73c_Tesxting.py


Files:  

	P73c_Texting.py
	P73c_Texting.cfg

[Reminder: Set login for Gmail in .cfg]

To import:

	import P73c_Texting as P73c_Text
Funtion use:

	phone_number = '8005009999'
	message = 'Sent from python'
	carrier = 'AT&T' 
	
	P73c_Text.SendText(Phone_number,carrier,message)
