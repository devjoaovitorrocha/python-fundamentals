try:
    score = float(input("Enter Score: "))

    if (score > 1.0) & (score < 0):
        print("Sorry, out of range")
    elif score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else:
        print("F")
except ValueError:
    print("Server error:", ValueError)