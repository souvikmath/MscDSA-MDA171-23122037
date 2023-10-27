#create a sportmart classs,where you will have
#-> inventory/shelf of items
#-> orders of customers
#create csv file which will store your inventory detalis and order detalis

#with  the help of file handling technqiues in python , read the file and create an object for trinity store and populate the inventory items and orders into the trinity store.
#to make  sure that you have added all the items in your file,use a display method to show your inventory and order history. 


#create a menu driven program that will
#create new orders and update the inventory accordingly
#Export the final data to the file



class sportmart:
    def __init__(self):
        self.inventory ={}
        self.orders ={}


    def  createInventory(self,ProductID,ProductName,Quantity,Price): #,invoice no
        temp ={
            "productid":ProductID,
            "productname":ProductName,
            "quantity" :Quantity,
            "price":Price
        
        } 
        self.inventory[ProductID] =temp         # self.inventory[invoice no]=temp

    def createOrder(self,orderid,Productid,quantity,price,total):
        temp={
            "orderid":orderid,
            "productid":Productid,
            "Quantity" :quantity,      
            "price":price,
            "total":total
        }

        self.orders[orderid]=temp

    def printOrder(self):
        print(self.orders)
        for item in self.orders:
             print(item)

    def printinventory(self):
        print(self.inventory)

trinity = sportmart()
orders =open("pythonsportmartorderid.csv","r")
o_header =orders.readline()
o_data =orders.readlines()
for data in o_data:
    temp=data.strip().split(',')
    trinity.createOrder(temp[0],temp[1],temp[2],temp[3])

trinity.printOrder()    
