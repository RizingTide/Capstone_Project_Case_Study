import mysql.connector
from mysql.connector import Error
import prettyprint as pp

database_connect = mysql.connector.connect(host='localhost',
                                database='creditcard_capstone',
                                user='root',
                                password='password')

cursor = database_connect.cursor()

def see_stuff():
    x=True
    while x!=False:
        print("MENU\n")
        print("1. See the transactions made by customers by ZIPCODE for a given MONTH and YEAR")
        print("2. See the NUMBER of transactions and TOTAL value by TYPE")
        print("3. See the NUMBER of transactions and TOTAL value by TYPE")
        print("4. QUIT/EXIT")
        action=int(input("What would you like to do? (Pick a num 1-4): "))
        if action == 1:
            zip=int(input("What zipcode?"))
            year=int(input("What year?: "))
            month=int(input("What month?: "))
            # print("hello")
            query="SELECT CDW_SAPP_CREDIT_CARD.TRANSACTION_TYPE, CDW_SAPP_CREDIT_CARD.TRANSACTION_VALUE, CDW_SAPP_CREDIT_CARD.TRANSACTION_ID, \
                CDW_SAPP_CUSTOMER.CUST_ZIP, CDW_SAPP_CREDIT_CARD.TIMEID FROM CDW_SAPP_CREDIT_CARD JOIN CDW_SAPP_CUSTOMER ON CDW_SAPP_CREDIT_CARD.CUST_SSN=CDW_SAPP_CUSTOMER.SSN \
                    WHERE YEAR(CDW_SAPP_CREDIT_CARD.TIMEID)={} AND MONTH(CDW_SAPP_CREDIT_CARD.TIMEID)={} \
            AND CDW_SAPP_CUSTOMER.CUST_ZIP={} ORDER BY DAY(CDW_SAPP_CREDIT_CARD.TIMEID);".format(year,month,zip)
            # query= f"SELECT cust_zip,transaction_id,transaction_type,transaction_value FROM cdw_sapp_credit_card cc JOIN cdw_sapp_customer c on ssn=cust_ssn WHERE MONTH(TIMEID)={month} AND YEAR(TIMEID)={year} AND CUST_ZIP={zip} ORDER BY DAY(TIMEID) DESC"
            cursor.execute(query)
            getting_data=cursor.fetchall()
            for i in getting_data:
                print(i)
        #2) Used to display the number and total values of transactions for a given type.m
        elif action == 2:
            types=input("What type of transactions do you want to see?: ")
            query="SELECT COUNT(TRANSACTION_VALUE), SUM(TRANSACTION_VALUE) FROM CDW_SAPP_CREDIT_CARD WHERE TRANSACTION_TYPE='{}';".format(types)
            cursor.execute(query)
            getting_data=cursor.fetchone()
            print(getting_data)
        #3) Used to display the total number and total values of transactions for branches in a given state.
        elif action == 3:
            state=input("For whhich state do you want to see transactions?")
            query="SELECT COUNT(TRANSACTION_ID), SUM(TRANSACTION_VALUE) FROM CDW_SAPP_CREDIT_CARD JOIN CDW_SAPP_BRANCH ON CDW_SAPP_CREDIT_CARD.BRANCH_CODE=CDW_SAPP_BRANCH.BRANCH_CODE WHERE CDW_SAPP_BRANCH.BRANCH_STATE='{}';".format(state)
            cursor.execute(query)
            getting_data=cursor.fetchone()
            print(getting_data)
        elif action == 4:
            x=False

def ddown_menu_account():
    print("List of Attributes")
    print("1. Email")
    print("2. Zipcode")
    print("3. City")
    print("4. Phone")
    print("5. Full Street Address")
    print("6. State")
    print("7. Name")
    print("8. Exit to main menu")

def check_account():
    x=True
    while x!=False:
        print("\nMENU\n")
        print("1. Check Account Details For A Customer")
        print("2. Modify Account Details For A Customer")
        print("3. Generate Monthly For A Credit Card Number For A Given Month And Year")
        print("4. Display Transactions Made By A Customer Between Two Dates")
        print("5. QUIT/EXIT")
        action=int(input("What would you like to do? (Pick a num 1-5): "))
        # action = pyip.inputInt("Enter your choice (1-7): ", min=1, max=8)
        if action == 1:
            SSN=input("Enter SSN of Account: ")
            query="SELECT * FROM CDW_SAPP_CUSTOMER WHERE SSN={}".format(SSN)
            cursor.execute(query)
            getting_data=cursor.fetchall()
            print(getting_data)
        #2) Used to display the number and total values of transactions for a given type.m
        elif action== 2:
            SSN=input("Enter SSN of Account: ")
            ddown_menu_account()
            new_action=int(input("Which attribute would you like to update? (Pick a num 1-8): "))
            if new_action==1:
                email=input("Please provide new email: ")
                query="UPDATE CDW_SAPP_CUSTOMER SET CDW_SAPP_CUSTOMER.CUST_EMAIL='{}' WHERE SSN ={}".format(email, SSN)
                cursor.execute(query)
                database_connect.commit()
            elif new_action==2:
                zipcode=int(input("Please enter new zipcode: "))
                query="UPDATE CDW_SAPP_CUSTOMER SET CDW_SAPP_CUSTOMER.CUST_ZIP={} WHERE SSN ={}".format(zipcode, SSN)
                cursor.execute(query)
                database_connect.commit()
                print("Zipcode has been updated succesfully!")
            elif new_action==3:
                city=input("Please enter new city: ")
                query="UPDATE CDW_SAPP_CUSTOMER SET CDW_SAPP_CUSTOMER.CUST_CITY ='{}' WHERE SSN ={}".format(city, SSN)
                cursor.execute(query)
                database_connect.commit()
            
        #     elif new_action==4:

        # #3) Used to display the total number and total values of transactions for branches in a given state.
        # elif action == 3:
            
        # elif action == 4:
        #     print()
        elif action == 5:
            x=False

see_stuff()
# check_account()