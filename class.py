class computers:
    def __init__(self,cpu,ram): #
        self.cpu=cpu
        self.ram=ram
        print('inside init method')

    def config(self):
        print('configuration is',self.cpu,'and',self.ram)

comp1=computers('i7','16gb') #object or instance
comp1.config()


        
