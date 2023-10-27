class student:
    def __init__(self):
        self.dicti = {}

    def add_Student(self , roll_no , name , course , english , maths , statistics):
        temp = { 
            "name" : name ,
            "course" : course , 
            "english" : english ,
            "maths" : maths ,
            "statistics" : statistics
        }
        self.dicti[roll_no] = temp
        print("Details added Successfully!")

    def search_student(self , roll_no):
        if roll_no in self.dicti:
            print(self.dicti[roll_no])

    def edit_student(self , roll_no , key_ , val):
        if roll_no in self.dicti:
            self.dicti[roll_no][key_] = val
            print("Detail edited successfully!")

    def delete_student(self , roll_no):
        del self.dicti[roll_no]
        print("Detail deleted successfully!")

    def print_student(self):
        print(self.dicti)
    
pd = student()
while True:
    print("1. Create STudent")
    print("2. Search student")
    print("3. Edit student")
    print("4. Delete Student")
    print("5. Print student")
    print("6. Exit")

    choice = int(input("Enter the choice from the above options: "))
    if choice == 1:
        roll_no = input("Enter the roll no of the student: ")
        name = input("Enter the name of the student: ")
        course = input("Enter the course of the student: ")
        english  = input("Enter the mark of english")
        maths = input("Enter the ,arks of maths: ")
        statistics = input("Enter the marks of statistics: ")
        pd.add_Student(roll_no , name , course , english , maths , statistics)

    if choice == 2:
        roll_no = input("Enter the roll number of the student: ")
        pd.search_student(roll_no)

    if choice == 3:
        roll_no = input("Enter the roll number of the student: ")
        key_ = input("Enter the column you want to edit: ")
        val = input("Enter the value you want to edit: ")
        pd.edit_student(roll_no , key_ , val)

    if choice == 4:
        roll_no = input("Enter the roll number of the student: ")
        pd.delete_student(roll_no)

    if choice == 5:
        pd.print_student()

    if choice == 6:
        print("Thankyou! Come again...")
        break
