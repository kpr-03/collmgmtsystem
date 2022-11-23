from Collegemgmt.university import Univ
class college(Univ):

    def getcolldet(self):
        self.cname=input("Enter college name:")
        self.cloc=input("Enter college location:")
    def dispcolldet(self):
        print("college Name:{}".format(self.cname))
        print("college location:{}".format(self.cloc))
        print("-"*50)