#204
#a=int(input())
#nums=list(map(int,input().split()))

#count=0
#for x in nums:
#    if x>0:
#        count+=1
#print(count)

#205
#n = int(input())
#if n <= 0:
#    print("NO")
#else:

#    while n % 2 == 0:
#        n = n // 2
    
   
#    if n == 1:
#        print("YES")
#    else:
#        print("NO")


#206
#a=int(input())
#nums=list(map(int,input().split()))
#print(max(nums))

#207
"""
n = int(input())
a = list(map(int, input().split()))


max_val = a[0]
max_pos = 1


for i in range(1, n):
    if a[i] > max_val:
        max_val = a[i]
        max_pos = i + 1  

print(max_pos)

#208

a=int(input())
b=1
while(b<=a):
    print(b,end=" ")
    b=b*2

#209
a=int(input())
nums=list(map(int,input().split()))

mx=max(nums)
mn=min(nums)

for i in range(a):
    if(nums[i] == mx):
        nums[i] = mn

print(*(nums))

#210
a=int(input())
nums=list(map(int,input().split()))

nums.sort()
print(*nums[::-1])


#211

n, l, r = map(int, input().split())
a = list(map(int, input().split()))
a[l-1:r] = a[l-1:r][::-1]
print(*a)



#212
a=int(input())
nums=list(map(int,input().split()))

for i in range(a):
    print(nums[i]*nums[i], end=" ")


#213
import math

def check_prime():
    try:
       
        line = input().strip()
        if not line:
            return
        x = int(line)

        
        if x <= 1:
            print("No")
            return

      
        if x == 2:
            print("Yes")
            return

  
        if x % 2 == 0:
            print("No")
            return

 
        is_prime = True
        for i in range(3, int(math.sqrt(x)) + 1, 2):
            if x % i == 0:
                is_prime = False
                break

        if is_prime:
            print("Yes")
        else:
            print("No")

    except ValueError:
        pass

if __name__ == "__main__":
    check_prime()


def solve():
   
    try:
        n = int(input())
        
        elements = list(map(int, input().split()))
    except (EOFError, ValueError):
        return

    
    counts = {}
    for x in elements:
        counts[x] = counts.get(x, 0) + 1

    max_freq = -1
    result_element = float('inf')

    
    for x, freq in counts.items():
        if freq > max_freq:
            max_freq = freq
            result_element = x
        elif freq == max_freq:
        
            if x < result_element:
                result_element = x

    print(result_element)

if __name__ == "__main__":
    solve() 



#215
import sys


line = sys.stdin.readline()
if line:
    n = int(line.strip())

   
    unique_surnames = set()

    for _ in range(n):
        surname = sys.stdin.readline().strip()
        if surname:
            unique_surnames.add(surname)

    
    print(len(unique_surnames))

import sys


line1 = sys.stdin.readline()
if line1:
    n = int(line1.strip())
    
   
    line2 = sys.stdin.readline()
    elements = line2.split()
    
    seen = set()
    results = []

   
    for i in range(n):
        x = elements[i]
        if x in seen:
            results.append("NO")
        else:
            results.append("YES")
            seen.add(x)
    
 
    print('\n'.join(results))



import sys

def solve():
   
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    
    n = int(input_data[0])
   
    phone_numbers = input_data[1:]

    
    counts = {}

    for number in phone_numbers:
        
        counts[number] = counts.get(number, 0) + 1


    result = 0
    for phone in counts:
        if counts[phone] == 3:
            result += 1

    print(result)

if __name__ == "__main__":
    solve()



import sys

def solve():
    
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    n = int(input_data[0])
   
    strings = input_data[1:n+1]

    
    first_occurrence = {}

    for i in range(len(strings)):
        current_string = strings[i]
       
        if current_string not in first_occurrence:
            first_occurrence[current_string] = i + 1

    
    sorted_unique_strings = sorted(first_occurrence.keys())


    for s in sorted_unique_strings:
        print(f"{s} {first_occurrence[s]}")

if __name__ == "__main__":
    solve()



import sys

def solve():
   
    data = sys.stdin.read().split()
    if not data:
        return

    
    n = int(data[0])
    
    
    dorama_counts = {}
    
    
    ptr = 1
    for _ in range(n):
        name = data[ptr]
        count = int(data[ptr + 1])
        
        
        if name in dorama_counts:
            dorama_counts[name] += count
        else:
            dorama_counts[name] = count
            
        ptr += 2

    
    sorted_names = sorted(dorama_counts.keys())

   
    for name in sorted_names:
        print(f"{name} {dorama_counts[name]}")

if __name__ == "__main__":
    solve()

"""
import sys

def solve():

    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    n = int(input_data[0])
    document = {}
    output = []

    for i in range(1, n + 1):
        parts = input_data[i].split()
        command = parts[0]
        key = parts[1]

        if command == "set":
            value = parts[2]
            
            document[key] = value
        
        elif command == "get":
            if key in document:
                output.append(document[key])
            else:
                output.append(f"KE: no key {key} found  in the  document")

    
    sys.stdout.write("\n".join(output) + "\n")

if __name__ == "__main__":
    solve()