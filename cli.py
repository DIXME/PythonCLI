# create cli from custom class
import os

class cli:
    def __init__(self, options):
        # so the key is going to be a hash map that is as follows
        # "option name, ex exit": functiontodoaction()
        # we  will just order these with numbers and orginize them with numbers
        self.options = options
    
    def refresh(self):
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
        if self.string == "":
            self.refresh()
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
                self.do(a)
                os.system("pause")
