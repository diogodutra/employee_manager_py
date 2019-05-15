from Employee import Employee 
from Manager import Manager

f1 = Employee("Joseph", "1259-8", 12.5, 44)
g1 = Manager ("Andrew", "6759-7", 12.5, 44, 10) 

team = [] 
team.append(f1); 
team.append(g1);
 
for f in team:
	print (f)