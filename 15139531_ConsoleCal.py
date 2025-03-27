def displayMenu():
    print("1.Add numbers\n2.Subtract numbers\n3.Multiply Numbers\n4.Divide Numbers")
def Addnumbers(n1,n2):
    return f'{n1}+{n2}={n1+n2}'
def Subtractnumbers(n1,n2):
    return f'{n1}-{n2}={n1-n2}'
def Multiplynumbers(n1,n2):
    return f'{n1}*{n2}={n1*n2}'
def Dividenumbers(n1,n2):
    if n2==0:                               #this will check check the dividing number is zero
        return 'Can not divide by zero!'   # if yes it will print the message
    return f'{n1}/{n2}={n1/n2}'

while True:
    try:
        num1 = float(input('Enter First number : '))
        num2 = float(input('Enter the second number : '))
        displayMenu()
        choice = input('Enter choice 1/2/3/4 : ')

        if choice == '1':
            print(Addnumbers(num1, num2))
        elif choice == '2':
            print(Subtractnumbers(num1, num2))
        elif choice == '3':
            print(Multiplynumbers(num1, num2))
        elif choice == '4':
            print(Dividenumbers(num1, num2))
        else:
            print('Invalid choice!')
    except ValueError:
        print("Invalid Entry    Enter Numbers only !")
    print('='*25)
    c=input('Do you want another calculation? press y to continue ')
    if c!='y':
        print('Calculator exiting...')
        break

