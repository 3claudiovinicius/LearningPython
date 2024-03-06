#
# Example file for formatting time and date output
# LinkedIn Learning Python course by Joe Marini
#


from datetime import datetime

def main():
    # Times and dates can be formatted using a set of predefined string
    # control codes 

    
    #### Date Formatting ####
    
    # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month


    # %c - locale's date and time, %x - locale's date, %X - locale's time
    now=datetime.now()
    print(now.strftime("Locale date and time: %c"))


    #### Time Formatting ####
    
    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
    print(now.strftime("Current time: %H:%M:%S of day %d of the %Y year in the %B month"))

if __name__ == "__main__":
    main()
