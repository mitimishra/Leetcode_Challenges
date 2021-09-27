with open('even_odd.txt') as f:
    lines = f.readlines()

count=0
even = 0
odd = 0
for line in lines:
    count += 1
    # print(type(line))
    if (int(line)%2) == 0:
        print(f'line {count}: {line} -- even')
        even +=1
    else:
        print(f'line {count}: {line} -- odd')
        odd +=1

print(f'Even Numbers in the File {even}')
print(f'Odd Numbers in the File {odd}')
