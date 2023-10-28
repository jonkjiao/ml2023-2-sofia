

def main():
    N = int(input("Dear Classmates, Please Enter a positive integer N: ")) 
    list = []  

  
    for i in range(1, N + 1):
        number = int(input(f"Enter number {i} of {N}: "))
        list.append(number)

    X = int(input("Enter an integer X: "))  

   
    if X in list:
        index = list.index(X) + 1  
        print(index)
    else:
        print(-1) 

if __name__ == "__main__":
    main() 
