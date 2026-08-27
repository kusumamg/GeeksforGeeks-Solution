class Solution:
    def calculate(self, a: int, b: int, optr: int) -> None:
        if optr == 1:
            print(a + b, end="")
        elif optr == 2:
            print(a - b, end="")
        elif optr == 3:
            print(a * b, end="")
        else:
            print("Invalid Input", end="")
