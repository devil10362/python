class name:
    def __init__(self):
        print("this is from constructor method")
    def receive(self):
        print("this is receive function message")
    def sender(self):
        print("this is message from sender function")

def check():
    x=name()
    x.receive()
    x.sender()

if __name__=="__main__":
    check()   