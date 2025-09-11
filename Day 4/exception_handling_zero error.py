def divide(num,den):
    try:
        return num/den
    except :  # noqa: E722
        print("Error: Division bt zero is not allowed.")
        return



num=int(input("enter numerator:"))
den=int(input("enter denominator:"))
divide(num,den)