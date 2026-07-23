def main():
    try:
        fobj = open("Demo.txt","r")      
        print("File gets opened")

        print("File offset is : ",fobj.tell())  # Offset = 0

        Data = fobj.read(10)

        print(Data)

        print("File offset is : ",fobj.tell()) # Offset = 10

        Data = fobj.read(10)

        print(Data)
 
        print("File offset is : ",fobj.tell()) # Offset = 20

        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()