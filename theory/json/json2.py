# dict -> Object

import json
blog = {'URL': 'datacamp.com', 'name': 'Datacamp'} # Cловарь 
to_json= json.dumps(blog) # Метод
print(to_json)

'''
Python	JSON
dict	Object
list	Array
tuple	Array
str	String
int	Number
float	Number
True	true
False	false
None	null
'''
