nameList = []

def storeName():
    name = input("Enter the name to be saved : ")
    name = name.strip().title()
    nameList.append(name)
    return name
def listNames():
    print("*"*30)
    print("Names in the List")
    print("*"*30)
    for name in nameList:
        print(name)
    print("*"*30)
def searchName(search):
    search = search.strip().title()
    found =False
    for name in nameList:
        if name == search:
            found = True
            break
    if found == True:    
        print("name exist in the list")
    else:
        print("Name doesnot exist..!")

print("*"*30)
print("name Management - Application")
print("*"*30)
while True:
    print("*"*30)
    print("*1. Enter a name")
    print("2. list the name")
    print("3. Search for a name")
    print("4. Exit")
    print("*"*30)

    choice = input("enter your choice ?")
    print("you have entered choice : ",choice)

    if int(choice) == 1:
        name = storeName()
        print("name {} added successfully!".format(name))
    elif int(choice) == 2:
        listNames()
    elif int(choice) == 3:
        name = input("Enter a name to be searched")
        searchName(name)
    elif int(choice) == 4:
        exit()
    else:
        print("Invalid Option..!")   
         

