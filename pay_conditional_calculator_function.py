def computepay(hours, rate): 
    try:

        ext_hours = hours - 40

        if ext_hours > 0:
            pay = (hours - ext_hours) * rate
            pay = pay + ext_hours * rate * 1.5
            return pay
        else:
            pay = hours * rate
            return pay
            
    except:
        print("Server error...")

hours = float( input("Enter Hours:") )
rate = float( input("Enter Rate:") )

pay = computepay(hours, rate)

print("Pay", pay)

