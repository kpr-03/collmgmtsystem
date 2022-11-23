from Collegemgmt.college import college
class Student(college):
    def getstuddet(self):
        self.sno=int(input('Enter student Number:'))
        self.sname=input('Enter student name:')
        self.crs=input('Enter student course:')
        self.getcolldet()
        self.getunivdet()
        print("-"*50)
    def dispstuddet(self):
        self.dispunivdet()
        self.dispcolldet()
        print("-"*50)
        print("Student Number:{}".format(self.sno))
        print("Student Name:{}".format(self.sname))
        print("student course:{}".format(self.crs))
        print("-"*50)
