import datetime
date=datetime.date.today()
currentYear=int(date.strftime("%Y"))
print("enter the last year")
endYear=int(input())
print("list of leap year")
for Year in range(currentYear,endYear):
    if((Year %4==0)and(Year%100!=0)or(Year%400==0)):
       print(Year)
