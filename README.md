# P73c_Plugins
Independent Python Plugins


Simple easy to import functions for Python


## P73c_Texting.py


Files:  

	P73c_Texting.py
	P73c_Texting.cfg

Reminder: [Set login for Gmail in .cfg]

To import
```python
import P73c_Texting as P73c_Text
```
Function use:

```python
phone_number = '8005009999'
message = 'Sent from python'
carrier = 'AT&T'
```
	
	P73c_Text.SendText(Phone_number,carrier,message)
SMS Gateway's are pulled from the config file.
