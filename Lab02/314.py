import sys

def solve():
    
    try:
        line1 = sys.stdin.readline()
        if not line1: return
        n = int(line1.strip())
        
        
        line2 = sys.stdin.readline()
        if not line2: return
        array = list(map(int, line2.split()))
        
        
        line3 = sys.stdin.readline()
        if not line3: return
        q = int(line3.strip())
        
       
        ops_map = {
            "add": lambda x: (lambda a: a + x),
            "multiply": lambda x: (lambda a: a * x),
            "power": lambda x: (lambda a: a ** x),
            "abs": lambda: (lambda a: abs(a))
        }
        
        for _ in range(q):
            op_data = sys.stdin.readline().split()
            op_name = op_data[0]
            
            
            if op_name == "abs":
                func = ops_map["abs"]()
            else:
                val = int(op_data[1])
                func = ops_map[op_name](val)
            
           
            array = list(map(func, array))
        
        
        print(*(array))

    except (ValueError, EOFError):
        pass

if __name__ == "__main__":
    solve()