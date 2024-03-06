#
# Example file for working with date information
# LinkedIn Learning Python course by Joe Marini
#

from datetime import time
from datetime import datetime
from datetime import date
import pytz

def main():
    ## DATE OBJECTS
    # TODO: Get today's date from the simple today() method from the date class
    today=date.today()

    # TODO: print out the date's individual components

    
    # TODO: retrieve today's weekday (0=Monday, 6=Sunday)

    
    ## DATETIME OBJECTS
    # TODO: Get today's date from the datetime class

    
    # TODO: Get the current time
    #print("todays weekday number is ",today.weekday())
    #days=["mon","tue","wed","thu","fri","sat","sun"]
    #print("which correspond to ", days[today.weekday()])
    #print("mas o numero da semana eh: ", today.isocalendar()[1])
    
    today=datetime.now(pytz.timezone("America/Sao_Paulo"))
    t=datetime.time(today)
    print("current time is: ", t)

  
if __name__ == "__main__":
    main()
  