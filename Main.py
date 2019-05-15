from Employee import Employee 
from Manager import Manager

f1 = Employee("Jose", "1259-8", 12.5, 44) 
print (f1.get_name(), " : ", f1.get_salary())

g1 = Manager("Andre", "6759-7", 12.5, 44, 10) 
print (g1.get_name(), " : ", g1.get_salary()) 

team = [] 
team.append(f1); 
team.append(g1);
 
for f in team: 
	print ("Name:", f.get_name(), "Salary $ ", f.get_salary()) 
	if isinstance(f, Manager): 
		print (" (added extra of $ ", f.get_rate_hourly_extra(), ")")