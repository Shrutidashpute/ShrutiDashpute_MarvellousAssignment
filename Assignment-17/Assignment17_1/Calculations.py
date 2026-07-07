import Arithmatic

def main():
    No1 = int(input("Enter first number: "))
    No2 = int(input("Enter second number: "))

    print("Addition :", Arithmatic.Add(No1, No2))
    print("Subtraction :", Arithmatic.Sub(No1, No2))
    print("Multiplication :", Arithmatic.Mult(No1, No2))
    print("Division :", Arithmatic.Div(No1, No2))

if __name__ == "__main__":
    main()