import datetime
weekday = datetime.date.today().weekday()
# 0=Mon, 1=Tue, 2=Wed, 3=Thu, 4=Fri, 5=Sat, 6=Sun

subtotal = float(input("What is the subtotal?: "))
salesTaxPercent = 0.06
discountAmount = 0

if weekday == 1 or weekday == 2:
    if subtotal >= 50:
        discountAmount = round((subtotal * 0.10), 2)
postDiscountSubtotal = round((subtotal - discountAmount), 2)
salesTaxAmount = round((salesTaxPercent*postDiscountSubtotal), 2)
final = postDiscountSubtotal + salesTaxAmount
print(salesTaxAmount)
print(final)
print(f"Discount amount: ",discountAmount)
print(f"Sales tax amount: ",salesTaxAmount)
print(f"Total: ",final)
