#
# Example file for working with timedelta objects
# LinkedIn Learning Python course by Joe Marini
#


from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


# TODO: construct a basic timedelta and print it
now=datetime.now()
today=date.today()
#print(now)
#print(today)

# TODO: print today's date
#test_date=now - timedelta(weeks=4, days=2)
#print("Dia de hoje há 4 semanas e 2 dia", str(test_date))

# TODO: print today's date one year from now
#s=test_date.strftime("%A %B %d, %Y")

# TODO: create a timedelta that uses more than one argument


# TODO: calculate the date 1 week ago, formatted as a string


### How many days until April Fools' Day?
iBR=date(today.year,9,7)
time_next_iBR=iBR-today

if iBR < today:
    print("Já se passaram ", (today-iBR).days, " dias do Dia da Independência")
    iBR1=iBR.replace(year=today.year+1)
    time_next_iBR=iBR1-today
    print("E faltam ", time_next_iBR.days, " dias até o próximo Dia da Independência")
elif iBR > today:
    print("Faltam ", time_next_iBR.days, " dias até o feriado da Independência")
else:
    print("Hoje é o dia do Feriado da Independência")


# TODO: use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year


# TODO: Now calculate the amount of time until April Fool's Day  

