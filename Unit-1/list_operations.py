#Write a program to create a list and perform various operations on list using menu.

lst = [11, 22, 33, 44, 55]
lst2 = ['Meera', 'Mira']
print("Original list : ", lst)

print("Length of the List: ",len(lst))
print("Maximum value present in the list is : ",max(lst))
print("Minimum value present in the list is : ",min(lst))
print("Appending an object in the existing list :")
lst.append(66)
print("List after appending 66: ", lst)
print("Using the count() function : ",lst.count(11))
print("Using extend() function : ")
lst.extend(lst2)
print(lst)
print("Using the index() method : ", lst.index(11))
print("Using the insert() method : ", lst.insert(0,1))
print(lst)
print("Using the pop() function : ", lst.pop())
print(lst)
print("Using the remove() function : ", lst.remove(1))
print(lst)
print("Using the reverse() function : ", lst.reverse())
print(lst)
