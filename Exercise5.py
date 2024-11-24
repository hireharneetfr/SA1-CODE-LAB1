#Write a program that tells a user how many days there are in a specific month. Use a dictionary to map the month numbers (1-12) to the number of days in each month.
dictionary = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

def get_days(month, year=None):
    if month < 1 or month > 12:
        return "The number added is wrong. Please enter a number between 1 and 12." #If the month number added is wrong, it is outputed the same
    
    if month == 2:  
        if year is not None: 
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): 
                return 29 
            else:
                return 28  
    return dictionary[month]  

month_input = input("Enter the month number (1-12): ") #The user is asked to enter a number

try:
    month_number = int(month_input)  
    
    if month_number == 2:
        year_input = input("Please enter year: ") #If febuary/2 is inputed, the user is asked for year to make sure of the leap year
        year_number = int(year_input)  
        days = get_days(month_number, year_number)  
    else:
        days = get_days(month_number)  
    

    print(f"There are {days} days in month {month_number}")

except ValueError:
    print("Invalid")

#In the code above, the user is asked for a month number (eg: 1 being january, 2 being febuary and so on). If the month requested is not month number 2 it proceeds by saying what has been typed in the dictionary. But, if it is the month of febuary it asks the user for year to make sure if its a leap year, to which it replies with 29 or 28 days.
