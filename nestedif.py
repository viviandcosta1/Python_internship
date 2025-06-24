def check_float_value(number):
    if number > 0.0:
        if number < 1.0:
            print("the number is between 0 and 1.")
        elif number == 1:
            print("the number is exactly 1.")    

        else:
            print("the number is greater then 1.")
    elif number < 0.0:
        print("the number is negative.")
    else:

        print("the number is zero.")


                      
