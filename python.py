#1
"""
rows = 5

for i in range(rows):
    for j in range(rows - i - 1):
        print(' ', end='')
    for k in range(2 * i + 1):
        print('*', end='')
    print()
"""
#2increasing number of spaces followed by decreasing digits on each line
"""
rows = 6
for i in range(1, rows + 1):
    for j in range(i-1):
        print(' ', end='')
    for k in range(6,i,-1):
        print(k-i, end='')
    
        
    
    print()
"""
#3 solid square pattern of stars
"""
size = 5


for i in range(size):
    for j in range(size):
        
        print('*', end='')
    
    print()
"""
#4 hollow square pattern with a border of stars
"""
size = 5

for i in range(size):
    for j in range(size):
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()

"""
#5 solid diamond pattern using stars
"""
size = 5

for i in range(size):
    for j in range(size - i - 1):
        print(' ', end='')
    for k in range(2 * i + 1):
        print('*', end='')
    print()

for i in range(size - 2, -1, -1):
    for j in range(size - i - 1):
        print(' ', end='')
    for k in range(2 * i + 1):
        print('*', end='')
    print()
"""
#6hollow diamond pattern.
"""
size = 5

for i in range(size):
    for j in range(size - i - 1):
        print(' ', end='')
    for k in range(2 * i + 1):
        if k == 0 or k == 2 * i:
            print('*', end='')
        else:
            print(' ', end='')
    print()

for i in range(size - 2, -1, -1):
    for j in range(size - i - 1):
        print(' ', end='')
    for k in range(2 * i + 1):
        if k == 0 or k == 2 * i:
            print('*', end='')
        else:
            print(' ', end='')
    print()
"""
#7hollow right triangle pattern.
"""
size = 5

for i in range(size):
    for j in range(size):
        if j == 0 or j == i or i == size - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
"""
#8right-angled triangle with its hypotenuse on the right and a vertical line at the base
"""
size = 5

for i in range(size):
    for j in range(size):
        if j == size - 1 or j == size - i - 1 or i == size - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()

"""
#9ight-aligned triangle pattern of stars
"""
size = 5

for i in range(size):
    for j in range(size - i):
        print('*', end='')
    print()

"""
#10(Star Pattern)
"""
size = 7

for i in range(size):
    for j in range(size):
        if j == i or j == size - i - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
"""
#11 heart pattern
"""
n = int(input("Enter value of n: "))

for i in range(n // 2, n + 1, 2):
    for j in range(1, n - i, 2):
        print(" ", end="")
    for j in range(1, i + 1):
        print("*", end="")
    for j in range(1, n - i + 1):
        print(" ", end="")
    for j in range(1, i + 1):
        print("*", end="")
    print()

for i in range(n, 0, -1):
    for j in range(i, n):
        print(" ", end="")
    for j in range(1, (i * 2)):
        print("*", end="")
    print()
"""
#12 eight star pattern
"""
size = 5

for i in range(size):
    for j in range(size):
        if i == 0 or i == size - 1 or i == size // 2 or j == 0 or j == size - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
"""
#13 plus sign pattern
"""  
size = 5

for i in range(size):
    for j in range(size):
        if i == size // 2 or j == size // 2:
            print('*', end='')
        else:
            print(' ', end='')
    print()

"""
#14inverted pyramaid
"""
size = 5

for i in range(size, 0, -1):
    for j in range(size - i):
        print(' ', end='')
    for k in range(2 * i - 1):
        print('*', end='')
    print()
"""
#15 hollow square star pattern with diagonal
"""

N = int(input("enter number:"))

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == 1 or i == N or j == 1 or j == N or i == j or j == (N - i + 1):
            print('*', end='')
        else:
            print(' ', end='')
    print()

"""


















    
