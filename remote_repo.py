print("Hello World, zakki here, good to see you!!")

class Bagi():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def hasil(self):
        self.rslt = self.a // self.b
        return("Hasil bagi {} dengan {} adalah {}".format(self.a, self.b, self.rslt))
    def print(self):
        print("Semangat yoo, kau pasti bisa")
        
    def try1(self):
        print("ya pastilah semangat")

    def try2(self):
        return(self.a**self.b)
    
    def try3(self):
        return(self.a*self.b)
    
    def try4(self):
        return(self.a/self.b)

    def try5(self):
        return(self.a*self.b**2)
    
import socket

def cek_sinyal():
    
    try:
        socket.gethostbyname("www.google.com")
        return False
    except:
        return True
