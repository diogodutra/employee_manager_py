class Employee(object): 
	#public members
	name = ""
	id = ""
	rate_hourly = 0
	hours_monthly = 0
	
	#constructor
	def __init__(self, name, id, rate_hourly, hours_monthly): 
		self.name = name
		self.id = id
		self.rate_hourly = rate_hourly
		self.hours_monthly = hours_monthly
		
	#destructor
	def __del__(self):
		#body of destructor
		pass
		
	def __str__(self):
		return str(self.id) + ", " + str(self.name) + ", " + str(self.hours_monthly) + "h, $" + str(self.rate_hourly) + "/h"
		
	#public methods
	def get_salary(self): 
		return self.rate_hourly * self.hours_monthly
		
	def get_name(self): 
		return self.name