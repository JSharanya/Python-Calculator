
def welcom():
    print("\t-------------------WELCOME TO CALCULAOR-------------------------\n")
    print("\t  _______________ENJOY YOUR MATHAMATICAL___________________\n")

def add(M,N):
    return M+N

def subract(M,N):
    return M-N

def mltiply(M,N):
    return M*N

def divide(M,N):
    return M/N

def reminder(M,N):
    return M%N

def calcutate():

    print("Select Your Operation:")
    print("1.Add        : +")
    print("2.Subract    : -")
    print("3.Mltiply    : *")
    print("4.Divide     : /")
    print("5.Reminder   : %")

    choice=input("Enter the you operatior    : ")
   
    num_1=float(input("Enter the First number     : "))
    num_2=float(input("Enter the Seacond number   : "))

    if choice =='+':
        print(num_1,"+" ,num_2, "=",add(num_1,num_2))
    elif choice=='-':
        print(num_1,"-" ,num_2, "=",subract(num_1,num_2))
    elif choice=='*':
        print(num_1,"*" ,num_2, "=",mltiply(num_1,num_2))
    elif choice=='/':
        print(num_1,"/" ,num_2, "=",divide(num_1,num_2))
    elif choice=='%':
        print(num_1,"%" ,num_2, "=",reminder(num_1,num_2))
    else:
        print('\n\"You have not typed a valid operator please run the program again\"')

    Next_calculat()

def Next_calculat():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    cal_again=input("\nLet's Move next Calcutation:(Y/N):")
    if cal_again.upper()=='Y':
        calcutate()
    elif cal_again.upper()=='N':
        print("\t SEE YOU AGAIN !!!!!!!!\n")
    else:
        Next_calculat()

welcom()  
calcutate()
        
            
            





