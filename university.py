class Univ:
    def getunivdet(self):
        self.uname=input("Enter university name:")
        self.uloc=input("Enter University location:")
    def dispunivdet(self):
        print("university name:{}".format(self.uname))
        print("univ location:{}".format(self.uloc))
        print("-"*50)