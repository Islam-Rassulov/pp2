class Circle:
    def __init__(self, radius):
       
        self.radius = radius
      
        self.pi = 3.14159

    def area(self):
        
        return self.pi * (self.radius ** 2)

def main():
    try:
       
        r_input = input().strip()
        if r_input:
            r = int(r_input)
            
            
            my_circle = Circle(r)
            
            
            result = my_circle.area()
            print(f"{result:.2f}")
    except (EOFError, ValueError):
        pass

if __name__ == "__main__":
    main()