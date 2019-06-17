# P73c_Plugins
Independent Python Plugins


Simple easy to import functions for Python

Plugins

| Plugin  	| Version         |
| ------------- |:---------------:|
| Texting       | June 2019 0.0.2 | 
| N.Y.W         |   N.Y.W         |

	

## P73c_Texting.py

Files:  

	P73c_Texting.py
	P73c_Texting.cfg

Reminder: [Set login for Gmail in .cfg]


```python
import P73c_Texting as P73c_Text

phone_number = '8005009999' #no spacing in the number
message = 'Sent from python'
carrier = 'AT&T' #SMS Gateway's are pulled from the config file.

P73c_Text.SendText(Phone_number,carrier,message)
```	

