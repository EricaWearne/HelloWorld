#Assign values to variables
name = "Erica"
country = "Australia"
age = 42
hourly_wage = 25
satisfied = True

#Calculate the daily wage
daily_wage = hourly_wage * 8

#Print statement including variables
print("Hi, my name is " + name + ", I live in " + country + ", I'm " + str(age) + " years old and I earn $" + str(hourly_wage) + " per hour.")

#Print statement including calculation
print("My daily wage is $%s per day and the answer to the question of if I am satisfied is %s." % (daily_wage, satisfied))
