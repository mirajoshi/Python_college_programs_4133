# Write a program to copy the cotent of a file to another file 

r = open("source.txt", "r")
content = r.read()
r.close()

w = open("destination.txt", "w")
w.write(content)
w.close()

print("=" * 45)
print("Source File Contents:")
print("=" * 45)
print(content)
print("=" * 45)
print("File copied successfully to destination.txt")
print("=" * 45)
