
try:
    hrs = float( input("Enter Hours:") )
    rate = float( input("Enter Rate:") )

    ext_hours = hrs - 40

    if ext_hours > 0:
        pay = (hrs - ext_hours) * rate
        pay = pay + ext_hours * rate * 1.5
    else:
        pay = hrs * rate
        
        
    h = float(pay)
    print(h)
except:
    print("Server error...")