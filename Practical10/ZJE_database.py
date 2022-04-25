class staff (object):
 def __init__(self, first_name, last_name, location, role):
 	self.first_name=first_name
 	self.last_name=last_name
 	self.location=location
 	self.role=role
 def ZJE_human_resources(self):
 	full_name=self.first_name+' '+self.last_name
 	return(f'{full_name},{self.location},{self.role}')
example=staff('Robert','Young', 'Edinburgh','professor')
print(example.ZJE_human_resources())
