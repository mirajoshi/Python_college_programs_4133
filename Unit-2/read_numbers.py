# Write a program to read a file that only has numbers and print total,  minimum and maximum number

f = open("numbers.txt","r")
content = f.readlines()
f.close()

numbers = []
for line in content:
    line = line.strip()
    if line:
        numbers.append(int(line))

print("=" * 40)
print("Numbers in File:")
print("=" * 40)
for n in numbers:
    print(n)

print("=" * 40)
print("Total   :", sum(numbers))
print("Maximum :", max(numbers))
print("Minimum :", min(numbers))
print("=" * 40)
