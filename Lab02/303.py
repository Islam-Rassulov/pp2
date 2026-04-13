def solve():
    
    to_digit = {
        "ZER": "0", "ONE": "1", "TWO": "2", "THR": "3", "FOU": "4",
        "FIV": "5", "SIX": "6", "SEV": "7", "EIG": "8", "NIN": "9"
    }
  
    to_triplet = {v: k for k, v in to_digit.items()}

    s = input().strip()

    operator = ""
    for char in s:
        if char in "+-*":
            operator = char
            break
    
    parts = s.split(operator)
    
   
    def convert_to_int(triplet_str):
        res = ""
      
        for i in range(0, len(triplet_str), 3):
            res += to_digit[triplet_str[i:i+3]]
        return int(res)

    num1 = convert_to_int(parts[0])
    num2 = convert_to_int(parts[1])

    
    if operator == '+': result = num1 + num2
    elif operator == '-': result = num1 - num2
    else: result = num1 * num2

    
    res_str = str(result)
    output = ""
    for digit in res_str:
        if digit == "-": 
            output += "-" 
        else:
            output += to_triplet[digit]
    
    print(output)

solve()