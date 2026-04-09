#sunday 200 
#monday 150
#tuesday 99
#wednesday 179
#thursday 179
#friday 145
#saturday 145

day=input("Enter a day: ").lower()
if(day=="sunday"):
    print("Ticket price is 200(in rs)")
    
elif(day=="monday"):
    print("Ticket price is 150(in rs)")

elif(day=="tuesday"):
    print("Ticket price is 99(in rs)")

elif(day=="wednesday" or day=="thursday"):
    print("Ticket price is 179(in rs)")

elif(day=="friday" or day=="saturday"):
    print("Ticket price is 200(in rs)")

else:
    print("Enter valid day")