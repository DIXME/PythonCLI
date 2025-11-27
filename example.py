from cli import cli
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