
try:
    hours = float(input("Enter your hours:"))
    rate = float(input("Enter your rate:"))

    pay = hours * rate

    print("Pay: " + str(pay))

except:
    print("Server error...")
