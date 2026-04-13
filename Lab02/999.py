"""
a=int(input())

for i in range(0,a+1,2):
    if a<2:
        print(0)
    else:
        if i<a-1:
            print(i,end=",")
        else:
            print(i)


a,b=map(int,input().split())

for i in range(a,b+1):
    print(i**2)


a=int(input())

for i in range(0,a+1):
    print(a-i)


s=input()
print(s[::-1])



def limited_cycle(elements, k):
  
    for _ in range(k):
        for item in elements:
            yield item


items = input().split()


try:
    k_value = int(input())
    
    
    gen = limited_cycle(items, k_value)
    
 
    print(*(gen))
except EOFError:
    pass

def fibonacci_generator(n):

    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


try:
    
    line = input()
    if line:
        n = int(line)
      
        gen = fibonacci_generator(n)
        

        print(",".join(map(str, gen)))
except EOFError:
    pass


def is_prime(num):
   
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_generator(n):

    for i in range(1, n + 1):
        if is_prime(i):
            yield i


n_limit = int(input())


primes = prime_generator(n_limit)
print(*(primes))



import json
import sys

def apply_patch(source, patch):
   
    if not isinstance(patch, dict):
        return patch
    
    if not isinstance(source, dict):
        source = {}

    for key, value in patch.items():
        if value is None:
           
            if key in source:
                del source[key]
        elif isinstance(value, dict) and isinstance(source.get(key), dict):
           
            source[key] = apply_patch(source[key], value)
        else:
            
            source[key] = value
            
    return source

def solve():
   
    try:
        input_data = sys.stdin.read().splitlines()
        if not input_data:
            return
        
        source = json.loads(input_data[0])
        patch = json.loads(input_data[1])
        
        result = apply_patch(source, patch)
        
        
        print(json.dumps(result, sort_keys=True, separators=(',', ':')))
    except EOFError:
        pass

if __name__ == "__main__":
    solve()




import json
import sys

def to_compact_json(val):
    if val == "<missing>":
        return val
    return json.dumps(val, separators=(',', ':'), sort_keys=True)

def find_diffs(obj_a, obj_b, path="", diffs=None):
    if diffs is None:
        diffs = []
    
    
    keys_a = set(obj_a.keys()) if isinstance(obj_a, dict) else set()
    keys_b = set(obj_b.keys()) if isinstance(obj_b, dict) else set()
    all_keys = sorted(keys_a | keys_b)

    for key in all_keys:
        current_path = f"{path}.{key}" if path else key
        val_a = obj_a.get(key, "<missing>") if isinstance(obj_a, dict) else "<missing>"
        val_b = obj_b.get(key, "<missing>") if isinstance(obj_b, dict) else "<missing>"

        if val_a == val_b:
            continue
        
       
        if isinstance(val_a, dict) and isinstance(val_b, dict):
            find_diffs(val_a, val_b, current_path, diffs)
        else:
           
            diffs.append(f"{current_path} : {to_compact_json(val_a)} -> {to_compact_json(val_b)}")
            
    return diffs

def solve():
    input_data = sys.stdin.read().splitlines()
    if len(input_data) < 2:
        return
    
    obj_a = json.loads(input_data[0])
    obj_b = json.loads(input_data[1])
    
    differences = find_diffs(obj_a, obj_b)
    
    if not differences:
        print("No differences")
    else:
        
        for d in sorted(differences):
            print(d)

if __name__ == "__main__":
    solve()



import json, sys

def get_diffs(a, b, path="", diffs=None):
    if diffs is None: diffs = []
    
    
    keys_a = set(a.keys()) if isinstance(a, dict) else set()
    keys_b = set(b.keys()) if isinstance(b, dict) else set()
    all_keys = sorted(keys_a | keys_b)

    for key in all_keys:
        curr_path = f"{path}.{key}" if path else key
        val_a = a.get(key, "<missing>") if isinstance(a, dict) else "<missing>"
        val_b = b.get(key, "<missing>") if isinstance(b, dict) else "<missing>"

        if val_a == val_b:
            continue
        
        if isinstance(val_a, dict) and isinstance(val_b, dict):
            get_diffs(val_a, val_b, curr_path, diffs)
        else:
           
            str_a = "<missing>" if val_a == "<missing>" else json.dumps(val_a, separators=(',', ':'), sort_keys=True)
            str_b = "<missing>" if val_b == "<missing>" else json.dumps(val_b, separators=(',', ':'), sort_keys=True)
            diffs.append(f"{curr_path} : {str_a} -> {str_b}")
    return diffs


from datetime import datetime, timezone, timedelta

def solve():
    moments = []
    for _ in range(2):
        line = input().split()
        date_str = line[0] 
        offset_str = line[1].replace("UTC", "") 
        
    
        sign = 1 if offset_str[0] == '+' else -1
        h, m = map(int, offset_str[1:].split(':'))
        offset_delta = timedelta(hours=sign*h, minutes=sign*m)
        
        
        tz = timezone(offset_delta)
        dt = datetime.strptime(date_str, "%Y-%m-%d").replace(tzinfo=tz)
        moments.append(dt.timestamp())

   
    delta_seconds = abs(moments[0] - moments[1])
    
   
    print(int(delta_seconds // 86400))

solve()



import math
from datetime import datetime, timezone, timedelta

def get_tz(offset_str):
    offset_str = offset_str.replace("UTC", "")
    sign = 1 if offset_str[0] == '+' else -1
    h, m = map(int, offset_str[1:].split(':'))
    return timezone(timedelta(hours=sign*h, minutes=sign*m))

def solve():
   
    line1 = input().split()
    b_date = datetime.strptime(line1[0], "%Y-%m-%d")
    b_tz = get_tz(line1[1])
    
   
    line2 = input().split()
    curr_date = datetime.strptime(line2[0], "%Y-%m-%d")
    curr_tz = get_tz(line2[1])
    curr_moment = curr_date.replace(tzinfo=curr_tz)

   
    possible_years = [curr_date.year, curr_date.year + 1]
    
    for year in possible_years:
        month, day = b_date.month, b_date.day
        
       
        if month == 2 and day == 29:
            is_leap = (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
            if not is_leap:
                day = 28
        
        birthday_moment = datetime(year, month, day, tzinfo=b_tz)
        
        
        delta = (birthday_moment - curr_moment).total_seconds()
        
        if delta >= 0:
            if delta == 0:
                print(0)
            else:
                
                print(math.ceil(delta / 86400))
            return

solve()



from datetime import datetime, timezone, timedelta

def get_utc_timestamp(line):
    
    parts = line.split()
    dt_str = f"{parts[0]} {parts[1]}"
    offset_str = parts[2].replace("UTC", "")
    
    
    sign = 1 if offset_str[0] == '+' else -1
    h, m = map(int, offset_str[1:].split(':'))
    tz = timezone(timedelta(hours=sign*h, minutes=sign*m))
    
    
    dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S").replace(tzinfo=tz)
    return dt.timestamp()

start_ts = get_utc_timestamp(input())
end_ts = get_utc_timestamp(input())

print(int(end_ts - start_ts))



import math

def solve_radar():
    
    try:
        r = float(input())
        x1, y1 = map(float, input().split())
        x2, y2 = map(float, input().split())
    except EOFError:
        return

    dx = x2 - x1
    dy = y2 - y1
    
    
    a = dx**2 + dy**2
    b = 2 * (x1 * dx + y1 * dy)
    c = x1**2 + y1**2 - r**2

   
    if a == 0:
        print(f"{math.sqrt(x1**2 + y1**2) <= r and 0.0 or 0.0:.10f}")
        return

    discriminant = b**2 - 4*a*c

    if discriminant < 0:
       
        if x1**2 + y1**2 <= r**2:
            length = math.sqrt(dx**2 + dy**2)
        else:
            length = 0.0
    else:
        
        sqrt_disc = math.sqrt(discriminant)
        t1 = (-b - sqrt_disc) / (2 * a)
        t2 = (-b + sqrt_disc) / (2 * a)
        
      
        t_start = max(0, min(t1, t2))
        t_end = min(1, max(t1, t2))
        
        if t_start < t_end:
            
            total_dist = math.sqrt(dx**2 + dy**2)
            length = (t_end - t_start) * total_dist
        else:
            length = 0.0

    print(f"{max(0.0, length):.10f}")

solve_radar()



def solve_reflection():
    try:
        x1, y1 = map(float, input().split())
        x2, y2 = map(float, input().split())
    except EOFError:
        return

    
    
    total_y = abs(y1) + abs(y2)
    
    if total_y == 0: 
        x_res = x1 
    else:
        
        x_res = x1 + (x2 - x1) * (abs(y1) / total_y)
    
    print(f"{x_res:.10f} {0.0:.10f}")

solve_reflection()



import math

def solve_shortest_path():
    try:
        r = float(input())
        x1, y1 = map(float, input().split())
        x2, y2 = map(float, input().split())
    except EOFError:
        return

    
    d_ab = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
   
    dx, dy = x2 - x1, y2 - y1
    t = -(x1 * dx + y1 * dy) / (dx**2 + dy**2) if (dx**2 + dy**2) > 0 else 0
    

    t_clamped = max(0, min(1, t))
    closest_x = x1 + t_clamped * dx
    closest_y = y1 + t_clamped * dy
    dist_to_origin = math.sqrt(closest_x**2 + closest_y**2)

    if dist_to_origin >= r - 1e-9:
        
        print(f"{d_ab:.10f}")
    else:
        
        oa = math.sqrt(x1**2 + y1**2)
        ob = math.sqrt(x2**2 + y2**2)
        
        
        l1 = math.sqrt(max(0, oa**2 - r**2))
        l2 = math.sqrt(max(0, ob**2 - r**2))
        
       
        dot_product = x1*x2 + y1*y2
        cos_theta = dot_product / (oa * ob)
        
        theta = math.acos(max(-1.0, min(1.0, cos_theta)))
        
       
        alpha1 = math.acos(r / oa)
        alpha2 = math.acos(r / ob)
        
       
        arc_angle = theta - alpha1 - alpha2
        arc_length = r * max(0, arc_angle)
        
        print(f"{l1 + arc_length + l2:.10f}")

solve_shortest_path()



import sys

def solve():
    
    try:
        line = sys.stdin.readline()
        if not line:
            return
        m = int(line.strip())
    except ValueError:
        return

   
    g = 0  
    n = 0  

    for _ in range(m):
        command = sys.stdin.readline().split()
        if not command:
            continue
            
        scope = command[0]
        value = int(command[1])

        if scope == "global":
            g += value
        elif scope == "nonlocal":
            n += value
       
    print(f"{g} {n}")

if __name__ == "__main__":
    solve()
    


import importlib
import sys

def solve():
    
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    try:
        q = int(input_data[0])
    except ValueError:
        return

    for i in range(1, q + 1):
        try:
            
            module_path, attr_name = input_data[i].split()
        except (ValueError, IndexError):
            continue

        try:
            
            module = importlib.import_module(module_path)
            
            
            if hasattr(module, attr_name):
                attribute = getattr(module, attr_name)
                
                
                if callable(attribute):
                    print("CALLABLE")
                else:
                    print("VALUE")
            else:
                print("ATTRIBUTE_NOT_FOUND")
                
        except ImportError:
            
            print("MODULE_NOT_FOUND")
        except Exception:
            
            print("ATTRIBUTE_NOT_FOUND")

if __name__ == "__main__":
    solve()



import json
import re
import sys

def solve():
    
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    try:
        data = json.loads(input_data[0])
        q = int(input_data[1])
    except (ValueError, IndexError):
        return

    for i in range(2, 2 + q):
        query = input_data[i]
        
        
        tokens = re.findall(r'([^.\[\]]+)|\[(\d+)\]', query)
        
        current = data
        possible = True
        
        for key, index in tokens:
            try:
                if key: 
                    if isinstance(current, dict) and key in current:
                        current = current[key]
                    else:
                        possible = False
                        break
                elif index:
                    index_int = int(index)
                    if isinstance(current, list) and 0 <= index_int < len(current):
                        current = current[index_int]
                    else:
                        possible = False
                        break
            except (KeyError, IndexError, TypeError):
                possible = False
                break
        
        if possible:
            
            print(json.dumps(current, separators=(',', ':')))
        else:
            print("NOT_FOUND")

if __name__ == "__main__":
    solve()
    



import re

text=input()

if re.match("Hello",text):
    print("Yes")
else:
    print("No")

import re

p=input()
s=input()

if re.search(s,p):
    print("Yes")
else:
    print("No")


import re

s=input()
p=input()

matches = re.findall(p,s)

print(len(matches))



import re

text = input()


digits = re.findall(r'\d', text)


print(" ".join(digits))



import re

text = input()


pattern = r'^[A-Za-z].*[0-9]$'

if re.search(pattern, text):
    print("Yes")
else:
    print("No")


import re

text = input()


pattern = r'\S+@\S+\.\S+'

match = re.search(pattern, text)

if match:

    print(match.group())
else:
    print("No email")


import re

S = input()
P = input()
R = input()


result = re.sub(re.escape(P), R, S)

print(result)



import re

S = input()
D = input()


parts = re.split(D, S)

print(",".join(parts))


import re

text = input()


pattern = r'\b[A-Za-z]{3}\b'

matches = re.findall(pattern, text)

print(len(matches))



import re

text = input()


pattern = r'cat|dog'

if re.search(pattern, text):
    print("Yes")
else:
    print("No")


import re

text = input()


uppercase_letters = re.findall(r'[A-Z]', text)

print(len(uppercase_letters))



import re

text = input()


sequences = re.findall(r'\d{2,}', text)

print(" ".join(sequences))




import re

text = input()


words = re.findall(r'\w+', text)

print(len(words))


import re

text = input()


regex = re.compile(r'^\d+$')

if regex.match(text):
    print("Match")
else:
    print("No match")



import re

text = input()


def double_digit(match):
    digit = match.group(0)
    return digit * 2


result = re.sub(r'\d', double_digit, text)

print(result)



import re

text = input()


pattern = r'Name:\s*(.*),\s*Age:\s*(\d+)'

match = re.search(pattern, text)

if match:
    
    name = match.group(1)
    age = match.group(2)
    print(f"{name} {age}")



import re

text = input()


pattern = r'\d{2}/\d{2}/\d{4}'

matches = re.findall(pattern, text)

print(len(matches))


import re

S = input()
P = input()


matches = re.findall(re.escape(P), S)

print(len(matches))


import re

text = input()


regex = re.compile(r'\b\w+\b')


words = regex.findall(text)

print(len(words))




a=int(input())
nums=list(map(int,input().split()))
sum=0

for i in range(a):
    sum=sum+nums[i]**2
print(sum)

"""

a=int(input())
b=list(map(int,input().split()))
sum=0
def  myFunc(x):
    if x % 2 == 0:
        sum+=1
even=filter(myFunc,b)

print(even)