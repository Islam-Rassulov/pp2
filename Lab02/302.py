def is_usual(num: int) -> bool:
    
    if num <= 0:
        return False
    
    
    for factor in [2, 3, 5]:
      
        while num % factor == 0:
            num //= factor  
            
    
    return num == 1

def main():
    try:
        
        line = input().strip()
        if not line:
            return
            
        n = int(line)
        
        
        if is_usual(n):
            print("Yes")
        else:
            print("No")
    except ValueError:
       
        pass

if __name__ == "__main__":
    main()