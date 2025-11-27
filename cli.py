# create cli from custom class
import os

class cli:
    def __init__(self, options):
        # so the key is going to be a hash map that is as follows
        # "option name, ex exit": functiontodoaction()
        # we  will just order these with numbers and orginize them with numbers
        self.options = options
    
    def make(self):
        # print out the ordered list
        middle = round(len(self.options)/2)
        keys = list(self.options.keys()) # do this here always so that if its updated we can just get the new version (this is kindaof the whole point of having a make method)
        string = ""
        half = keys[:middle]
        # use half beacuse the spaces only need to be between first half
        lengths = [len(key) for key in half]
        maxL = max(lengths)
        dists = [
            (maxL - length) * " "
            if not (lengths.index(length) + 1 > 9)
            else (maxL - length - 1) * " "
            for length in lengths
        ]
        for i in range(0,middle):
            string+=f"{i+1}. {keys[i]}{dists[i]}  {middle+i+1}. {keys[middle+i]}\n"
        self.string = string
        return string
    
    def print(self):
        print(self.string)
    
    def do(self, i):
        self.options[list(self.options.keys())[i-1]]()
    
    def loop(self):
        while True:
            os.system("cls")
            self.print()

            try:
                a = int(input("option > "))
            except:
                a = "a"
            if a == str(a):
                print("[-] Invalid input")
            else:
                c.do(a)
                os.system("pause")
            



commands = {
    "print user input": lambda: print(input("Enter something: ")),
    "print hello": lambda: print("Hello!"),
    "add two numbers": lambda: print("2 + 3 =", 2 + 3),
    "show list length": lambda: print("Length of [1,2,3]:", len([1, 2, 3])),
    "convert to string": lambda: print("String of 123:", str(123)),
    "convert to int": lambda: print("Int of '42':", int("42")),
    "convert to float": lambda: print("Float of '3.14':", float("3.14")),
    "absolute value": lambda: print("abs(-9) =", abs(-9)),
    "round number": lambda: print("round(3.6) =", round(3.6)),
    "find max": lambda: print("max(1, 5, 3) =", max(1, 5, 3)),
    "find min": lambda: print("min(1, 5, 3) =", min(1, 5, 3)),
    "sum list": lambda: print("sum([1,2,3]) =", sum([1, 2, 3])),
    "sort list": lambda: print("sorted([3,1,2]) =", sorted([3, 1, 2])),
    "hex representation": lambda: print("hex(255) =", hex(255)),
    "binary representation": lambda: print("bin(10) =", bin(10)),
    "power example": lambda: print("pow(2, 5) =", pow(2, 5)),
    "zip example": lambda: print("zip([1,2],[3,4]):", list(zip([1,2],[3,4]))),
    "enumerate example": lambda: print("enumerate(['a','b']):", list(enumerate(['a','b']))),
    "type example": lambda: print("type(123):", type(123)),
    "hash example": lambda: print("hash('hello'):", hash("hello")),
    "range example": lambda: print("list(range(5)):", list(range(5))),
    "exit": exit
}

c = cli(commands)
c.make()
c.loop()