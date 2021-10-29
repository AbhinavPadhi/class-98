def swapfile():
    file1 = input("enter file 1 name:- ")
    file2 = input("enter file2  name:- ")

    with open(file1, 'r') as a:
        file1data = a.read()

    with open(file2, 'r') as b:
        file2data = b.read()

    with open(file1, 'w') as a:
        a.write(file2data)

    with open(file2, 'w') as b:
        b.write(file1data)

swapfile()