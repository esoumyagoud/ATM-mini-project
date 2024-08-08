name="soumya"
password="123"
user_name=input("Enter your name=")
password=int(input("Enter your password="))
s='''
    1.credit
    2.debit
    3.mini statement
    4.exit
'''
Amount=10000
if name==user_name and password==password:
    while True:
        print(s)
        option=int(input("Enter the option"))
        if option ==1:
            credit_amount=float(input("Enter the amount:"))
            print("Amount after credit:",Amount+credit_amount)
        if option==2:
            debit_amount=int(input("Enter the amount"))
            print("Amount after debit:",Amount-debit_amount)
        if option==3:
            print("Amount",Amount)
        if option==4:
            break
else:
    print("inncorrect")
