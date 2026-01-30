# Write a program to display the use of local, global and nonlocal variables

a = 10
def outer_function():
    b = 20

    def inner_function():
        c = 15
        nonlocal b
        global a

        a += 5
        b += 5
        c += 5

        print("Local variable c : ", c)

    inner_function()
    print("Nonlocal variable b : ", b)

outer_function()
print("Global variable a : ", a)
