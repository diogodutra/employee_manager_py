from Employee import Employee 

class Manager(Employee):
	#public members
	rate_hourly_extra = 0.0
	
	#constructor
	def __init__(self, name, id, rate_hourly, worked_hours, rate_hourly_extra): 
		Employee.__init__(self, name, id, rate_hourly, worked_hours)
		self.rate_hourly_extra = rate_hourly_extra
		
	#public methods
	def get_salary(self): 
		return Employee.get_salary(self)*(1 + self.rate_hourly_extra)
		
	def get_rate_hourly_extra(self): 
		return self.rate_hourly_extra