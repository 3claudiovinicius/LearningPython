
import calendar

def count_days(year, month, whichday):
	count=0
	cal=calendar.Calendar(firstweekday=0)
	week_day=cal.itermonthdays2(year,month)
	#print(f"Os dias {calendar.day_name[whichday]} são: ") #para testes
	for x,y in week_day:
		if y==whichday:
			count+=1
			#print(f"Dia do mês: {x}") #para testes
	return count

#<=============>Comum<=============>
def main():
    print(count_days(2024,11,4))

if __name__ == "__main__":
    main()