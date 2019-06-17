# P73c_Plugins
Independent Python Plugins


Simple easy to import functions for Python


| Plugin  	| Version         | Link 										|
| ------------- |:---------------:| [Readme.md](https://github.com/Protocol73/P73c_Plugins "Ver 0.0.2") 		|
| Texting       | June 2019 0.0.2 | [June 2019](https://github.com/Protocol73/P73c_Plugins#p73c_textingpy "Ver 0.0.2")	|
| N.Y.W         |   N.Y.W         | 											|

	

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

