class Employee(object): 
	#public members
	name = ""
	id = ""
	rate_hourly = 0
	worked_hours = 0
	
	#constructor
	def __init__(self, name, id, rate_hourly, worked_hours): 
		self.name = name
		self.id = id
		self.rate_hourly = rate_hourly
		self.worked_hours = worked_hours
		
	#public methods
	def get_salary(self): 
		return self.rate_hourly * self.worked_hours
		
	def get_name(self): 
		return self.name