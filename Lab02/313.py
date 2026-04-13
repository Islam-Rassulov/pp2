def is_prime(n):
   
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    try:
        
        data = input().split()
        if not data:
            return
            
        numbers = list(map(int, data))
        
        
        primes = list(filter(lambda x: is_prime(x), numbers))
        
       
        if primes:
          
            print(*(primes))
        else:
            print("No primes")
            
    except EOFError:
        pass

if __name__ == "__main__":
    main()