# Ben Woolsey
#Lab Section: 11
#Submission Date: 11/5/2024
# Worked with: Cole Jordan

def leap_year(input):
    """Checks if the year is a leap year"""
    if input % 400 == 0:
        return True
    elif input % 4 == 0 and input % 100 != 0:
        return True
    else:
        return False

def first_day_jan(input):
    """Finds the day of the week January 1st falls on"""
    y = input - 1
    day = str((36 + y +(y/4) - (y/100) + (y/400))%7)
    day.split(".")
    day = int(day[0])
    return day

full_year = {"1":{},"2":{},"3":{},"4":{},"5":{},"6":{},"7":{},"8":{},"9":{},"10":{},"11":{},"12":{}}
month_length = {1:31,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
day_cycle = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

while True:
    entry = str(input("Declare a day in this format MM/DD/YYYY, type 'exit' to quit"))
    if entry.lower() == "exit":
        break

    entry = entry.split("/")
    month = entry[0]
    day = entry[1]
    year = entry[2]
    start_day = first_day_jan(int(year))
    current_day = start_day
    
    if leap_year(int(year)):
        month_length[2] = 29
    else:
        month_length[2] = 28

    if month.isdigit() != True or int(month) > 12 or int(month) < 1:
        print("Not a valid month")
        continue

    for i in range(1,13):
        for w in range(1,month_length.get(i)+1):
            full_year[str(i)][w] = day_cycle[int(current_day)]

            if current_day == 6:
                current_day = 0
            else: 
                current_day += 1       
    
    month = int(month)
    if int(day) > len(full_year[str(month)]):
        print("Not a valid day")
        continue     
    

    print(f"Your Input: {month}/{day}/{year}. Day of the week: {full_year[str(month)][int(day)]}")