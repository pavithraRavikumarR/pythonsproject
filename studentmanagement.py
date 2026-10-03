class Student:
    def __init__(self,name,rollno,email,phone):
        self.name = name
        self.rollno = rollno
        self.email = email
        self.phone = phone
        
    def show_Details(self):
        print(self.name,self.rollno,self.email,self.phone)
        
        
        
        
std1 = Student("sadhana",56,"sadhana1234@gmail.com",1234567890)
