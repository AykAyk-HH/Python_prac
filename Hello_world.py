a = "Ayaan"
print(a)

varOne = "43"
varTwo = 76
varThree = "10"
varFour = 1.5
varFive = "python"
varSix = "4.5"
 
#What happens here?
print(varOne + varThree)
 
#The output here?
print(varTwo + varFour)
 
#What happens here?
print(int(varOne) + varTwo)
 
#print(int(varOne) + varTwo)
print((varOne) + str(varTwo))
 
#can you do this?
print(varFive + str(varTwo))
 
#will this work?
print(int(float(varSix)))

print("-------------------------------")
print(round(2.3))
print("-------------------------------")

#Literals
 
a = 0b1010 #Binary Literals
b = 100 #Decimal Literal
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal
 
#Float Literal
float_1 = 10.5
float_2 = 1.5e2
 
#Complex Literal
x = 3.14j
 
print(a, b, c, d)
print("{0:b}".format(10),bin(10))
print(float_1, float_2)
print(x, x.imag, x.real)
print("-------------------------------")

strr = 'Hello World'
print (strr)            # prints complete string
print (strr[0])         # prints first character of string
print (strr[2:7])       # prints characters starting from 3rd to 6th. Exclude last element. 'W' is excluded.
print (strr[:7])        # prints string starting from 1st character till 7th character
print (strr*2)          # prints string two times
print (strr[-1])        # prints the last character
print (strr[-4:])       # prints the last four characters
print (strr[-4:-2])     # prints the 2 - 4 chars from the last

print("-------------------------------")
print(str.index(strr,'W')) #Gets the location of 'W'
 
#Can you guess the output?
print (strr[::-1])
print(id(strr))
 
newstrin = strr.replace('o','a')
print(id(newstrin))
print (strr.lower())
print (strr.upper())
print (len(strr))
print("-------------------------------")

#More string operations
school = 'ISB'
print('s' in school)
print('S' in school)
 
#Consider two strings x and y
firstName = 'Sriram'
lastName = 'Ragavendran'
 
#What does this give you?
print (firstName[:3].lower() + lastName[:3].lower())

print("-------------------------------")
from datetime import datetime, date, time
#help(datetime.strptime)                                       # Help for a function
 
date1 = datetime(2014, 7, 16, 14, 45, 5)
print(date1)
print(str(date1.day) + ' ' + str(date1.month) + ' ' + str(date1.year))
 
print(datetime.strptime('20140516134328','%Y%m%d%H%M%S'))      # Parses a string representing a time according to a format
print (date1.strftime('I am time-travelling. We are in %d, %B %y' ))  #strftime() converts a time input into a string output. .
 
date1 = datetime(2014, 5, 16)
date2 = datetime(2015, 5, 15)
datediff = date2 - date1
print(datediff)
print("-------------------------------")

from datetime import datetime, timedelta
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
'Friday', 'Saturday', 'Sunday']
 
def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date
 
print(get_previous_byday('Sunday'))
print(get_previous_byday('Saturday'))