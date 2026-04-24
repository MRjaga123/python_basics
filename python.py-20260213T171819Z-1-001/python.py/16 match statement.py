####match statement
#for using many if else statement, you can use #match statement.

day=16                  
match day:
    case 1:
        print("mon")
    case 2:
        print("tues")
    case 3:
        print("wed")
    case 4:
        print("thurs")
    case 5:
        print("fri")
    case 6:
        print("satur")
    case 7:
        print("sun")
    case 8|9|10|11|12|13|14|15:    #combine a data
        print("next")
    case _:         #default case
        print("end")

#if statement in match statement
day=4
month=5
match day|month:
    case 1|2|3|4|5|6|7 if month==4:
        print("4,4")
    case 1|2|3|4|5|6|7 if month==5:
        print("4,5")
    case _:
        print("no match")
    



