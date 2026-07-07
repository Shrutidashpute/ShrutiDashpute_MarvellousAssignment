import PrimeCheck

def ListPrime(Data):

    Sum = 0

    for Value in Data:
        if PrimeCheck.ChkPrime(Value):
            Sum = Sum + Value

    return Sum

def main():

    Size = int(input("Number of elements : "))

    Data = []

    for i in range(Size):
        No = int(input("Input Element : "))
        Data.append(No)

    print("Input Elements :", Data)

    Result = ListPrime(Data)

    print("Addition of prime numbers :", Result)

if __name__ == "__main__":
    main()
