is_leap_year = False
   
input_year = int(input())

def is_leap(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
        
    return False
    
if is_leap(input_year):
    print('2016 - leap year')
else:
    print('1954 - not a leap year')
    
