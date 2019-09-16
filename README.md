# P73c_Plugins
Independent Python Plugins


Simple easy to import functions for Python



 Plugin| Version | Link | Files | Usage |								
   --- |---------| ----	| ----	|  ---- |
 Texting | June 2019 | [June 2019](https://github.com/Protocol73/P73c_Plugins/tree/master/P73c_Texting "Ver 0.0.2") | 2 | [Texting](https://github.com/Protocol73/P73c_Plugins/blob/master/README.md#using-p73c_textingpy "Usage Wiki")|	
 N.Y.B   |   N.Y.B   | 	N.Y.B |	N.Y.B |									

# Using These Functions

## Using P73c_Texting.py 
`[Set login for Gmail in Texting.cfg]`


```python
import P73c_Texting as P73c_Text

phone_number = '8005009999' #no spacing in the number
message = 'Sent from python'
carrier = 'AT&T' #SMS Gateway's are pulled from the config file.

P73c_Text.SendText(Phone_number,carrier,message)
```	

