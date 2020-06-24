
import csv

def read_file(filename):
    with open(filename,'r') as file:
        reader = csv.reader(file)
       
        for row in reader:
            months.append(row[0])
            pro_loss.append(row[1])
            
        months.pop(0)
        pro_loss.pop(0)

def total_pro_loss():
    total = 0 
    for var in pro_loss:
        #print(var)
        total = total + int(var)
    return  total

# def inc_pro():
#     prev = 0
#     max_diff = 0 
#     for val in pro_loss:
#         diff = int(val) - prev
#         prev = int(val)
#         if (max_diff<diff):
#             max_diff=diff
#     return max_diff

def inc_pro():
    max_diff=0
    count = 0
    for x in range(1,len(pro_loss)):
        diff=int(pro_loss[x]) - int(pro_loss[x-1])
        if(max_diff<diff):
            count=x
            max_diff=diff 
    return months[count],max_diff


months = []
pro_loss= []

filename= 'budget_data.csv'
read_file(filename)

lentgh = len(months)
print("total no of months in the dataset ", lentgh)

#total_amount = total_pro_loss()
#print (total_amount)

great_increase = inc_pro()
print ('The greatest increase in profits (date and amount) over the entire period',great_increase[0],great_increase[1])






