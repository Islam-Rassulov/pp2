class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self, other):
        
        sum_a = self.a + other.a
        sum_b = self.b + other.b
        return sum_a, sum_b

def main():
    try:
        
        data = list(map(int, input().split()))
        
        if len(data) == 4:
           
            pair1 = Pair(data[0], data[1])
            pair2 = Pair(data[2], data[3])
            
           
            res_a, res_b = pair1.add(pair2)
            
            
            print(f"Result: {res_a} {res_b}")
            
    except (EOFError, ValueError):
        pass

if __name__ == "__main__":
    main()