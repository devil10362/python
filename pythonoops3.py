class dog():
    def __init__(self,breed="german",colour="black"):
        self.x=breed
        self.y=colour

    def dbreed(self):
        print("breed of dog is",self.x)  

    def dcolour(self):
        print("colour of dog is",self.y)  

    def main():
      z=dog()
      z.dbreed()
      z.dcolour() 
    
    if"__name__"=="__main__":
       main()