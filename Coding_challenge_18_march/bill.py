current_bill=int(input("Enter the amount of your bill : "))  #bill before discount
discount=int(input("Enter discount in percentage : "))  #discount in %

# logic 
def findBill(current_bill,discount):   #function definition
   disc_amount=(discount/100)*current_bill    #amount has to be discounted
   paid_bill=current_bill-disc_amount   
   return paid_bill  #amount to be paid

print(findBill(current_bill,discount))