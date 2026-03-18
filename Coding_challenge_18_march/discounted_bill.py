current_bill=int(input("Enter the amount of your bill : "))  #bill before discount
discount=int(input("Enter discount in percentage : "))  #discount in %

# logic 

disc_amount=(discount/100)*current_bill  

paid_bill=current_bill-disc_amount
#amount to be paid
print("You have the discount of",disc_amount,"in your bill..so u have to pay",paid_bill)  