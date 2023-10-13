child_price = float(input("What is the price of a child meal?" ))
adult_price = float(input("What is the price of a adult meal?" ))
num_of_kids = int(input("How many children are there?" ))
num_of_adults = int(input("How many adults are there?" ))
tax = float(input("What is the sales tax?" ))

child_total = child_price * num_of_kids
adult_total = adult_price * num_of_adults
sub_total = round(child_total + adult_total, 2)

tax_rate = round(tax / 100 * sub_total, 2)
total = round(sub_total + tax_rate, 2)


print(f"Subtotal is: ${sub_total}")
print(f"Sales Tax: ${tax_rate}")
print(F"Total: ${total}")

payment = float(input("Enter payment amount? "))
change = round(payment - total, 2)
if payment < total:
     print("Payment is not enough, please try again")
     payment = float(input("Enter payment amount? "))

if change <= 0:
      print("No Change")
elif change > 0:
     print(f"Change: ${change} ")
                # if change >= 0:
                #      final_total > payment
# print(f"Change: ${change} ")

tip = input("Would you like to tip? Type 'Y' for yes and 'N' for no ").upper()



if tip == "Y":
    tip_amount = float(input("How much would you like to tip? Suggestions: 10% , 15% , 20%. "))
    total_after_tip = tip_amount / 100 * total
    final_total = round(total + total_after_tip, 2)
    new_change = round(payment - final_total, 2)
    print(f"Your new total: ${final_total}")
# elif tip == "N":
#     print(f"Change: ${change} ")
#     print("Thank you for using Meal Calculator, Have a nice day!")
    if final_total > payment:
        balance = round(final_total - payment, 2)
        print(f"You owe: ${balance} Please pay the balance ")
        new_payment = float(input("Enter dollar amount here $"))
        if new_payment < balance:
             print("Payment is not enough, please try again")
             new_payment = float(input("Enter payment amount? "))
        final_payment = payment + new_payment
        new_change = round(final_payment - final_total, 2)
        # print(f"Change: ${new_change} ")
        if new_change <= 0:
                print("No Change")
        elif new_change > 0:
                print(f"Change: ${new_change} ")
                print("Thank you for using Meal Calculator, Have a nice day!")
                # if change >= 0:
                #      final_total > payment
else:
    print(f"Change: ${change} ")
    print("Thank you for using Meal Calculator, Have a nice day!")






