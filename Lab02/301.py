def check_valid_number():
    
    n_str = input().strip()
    

    is_valid = all(int(digit) % 2 == 0 for digit in n_str)
    
    if is_valid:
        print("Valid")
    else:
        print("Not valid")


check_valid_number()    