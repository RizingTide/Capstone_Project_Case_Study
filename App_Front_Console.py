import mysql.connector
from mysql.connector import Error
import prettyprint as pp
import datetime
database_connect = mysql.connector.connect(host='localhost',
                                database='creditcard_capstone',
                                user='root',
                                password='password')

cursor = database_connect.cursor()

def see_stuff():
    x=True
    while x!=False:
        print("TRANSACTIONS MENU\n")
        print("1. See the transactions made by customers by ZIPCODE for a given MONTH and YEAR")
        print("2. See the NUMBER of transactions and TOTAL value by TYPE")
        print("3. See the NUMBER of transactions and TOTAL value by TYPE")
        print("4. QUIT/EXIT\n")
        action=int(input("What would you like to do? (Pick a num 1-4): "))
        # 1) Used to display the transactions made by customers living in a given zip code for a given month and year. Order by day in descending order.
        if action == 1:
            zip=int(input("What zipcode?"))
            year=int(input("What year?: "))
            month=int(input("What month?: "))
            query="SELECT CDW_SAPP_CREDIT_CARD.TRANSACTION_TYPE, CDW_SAPP_CREDIT_CARD.TRANSACTION_VALUE, CDW_SAPP_CREDIT_CARD.TRANSACTION_ID, \
                CDW_SAPP_CUSTOMER.CUST_ZIP, CDW_SAPP_CREDIT_CARD.TIMEID FROM CDW_SAPP_CREDIT_CARD JOIN CDW_SAPP_CUSTOMER \
                    ON CDW_SAPP_CREDIT_CARD.CUST_SSN=CDW_SAPP_CUSTOMER.SSN \
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
            query="SELECT COUNT(TRANSACTION_ID), SUM(TRANSACTION_VALUE) FROM CDW_SAPP_CREDIT_CARD JOIN CDW_SAPP_BRANCH \
            ON CDW_SAPP_CREDIT_CARD.BRANCH_CODE=CDW_SAPP_BRANCH.BRANCH_CODE WHERE CDW_SAPP_BRANCH.BRANCH_STATE='{}';".format(state)
            cursor.execute(query)
            getting_data=cursor.fetchone()
            print(getting_data)
        elif action == 4:
            x=False

def ddown_menu_account():
    print("List of Attributes MENU")
    print("1. Email")
    print("2. Zipcode")
    print("3. City")
    print("4. Phone")
    print("5. Full Street Address")
    print("6. State")
    print("7. Name")
    print("8. Exit to main menu\n")

def check_account():
    x=True
    while x!=False:
        print("\nCUSTOMER MENU\n")
        print("1. Check Account Details For A Customer")
        print("2. Modify Account Details For A Customer")
        print("3. Generate Monthly For A Credit Card Number For A Given Month And Year")
        print("4. Display Transactions Made By A Customer Between Two Dates")
        print("5. QUIT/EXIT\n")
        action=int(input("What would you like to do? (Pick a num 1-5): "))
        # action = pyip.inputInt("Enter your choice (1-7): ", min=1, max=8)
        if action == 1:
            SSN=input("Enter SSN of Account: ")
            query="SELECT * FROM CDW_SAPP_CUSTOMER WHERE SSN={};".format(SSN)
            cursor.execute(query)
            getting_data=cursor.fetchall()
            print(getting_data)
        #2) Used to display the number and total values of transactions for a given type.m
        elif action== 2:
            SSN=input("Enter SSN of Person Account: ")
            ddown_menu_account()
            new_action=int(input("Which attribute would you like to update? (Pick a num 1-8): "))
            if new_action==1:
                email=input("Please provide new email: ")
                query="UPDATE CDW_SAPP_CUSTOMER SET CDW_SAPP_CUSTOMER.CUST_EMAIL='{}' WHERE SSN ={};".format(email, SSN)
                cursor.execute(query)
                database_connect.commit()
                print("Email has been updated successfully!")
            elif new_action==2:
                zipcode=int(input("Please enter new zipcode: "))
                query="UPDATE CDW_SAPP_CUSTOMER SET CDW_SAPP_CUSTOMER.CUST_ZIP={} WHERE SSN ={};".format(zipcode, SSN)
                cursor.execute(query)
                database_connect.commit()
                print("Zipcode has been updated successfully!")
            elif new_action==3:
                city=input("Please enter new city: ")
                query="UPDATE CDW_SAPP_CUSTOMER SET CDW_SAPP_CUSTOMER.CUST_CITY ='{}' WHERE SSN ={};".format(city, SSN)
                cursor.execute(query)
                database_connect.commit()
                print("City has been updated sucessfully!")
            elif new_action==4:
                phone=input("Enter new phone # please. FORMAT: (XXX)XXX-XXXX :" )
                query="UPDATE CDW_SAPP_CUSTOMER SET CDW_SAPP_CUSTOMER.CUST_PHONE = '{}' WHERE SSN={};".format(phone, SSN)
                cursor.execute(query)
                database_connect.commit()
                print("City has been updated sucessfully!")
            elif new_action==5:
                st_name=input("Enter new street name: ")
                apt_num=input("Enter apt/house # ")
                full_addy=st_name+","+apt_num
                query = "UPDATE CDW_SAPP_CUSTOMER SET CDW_SAPP_CUSTOMER.STREET_NAME.APT_NO = '{}' WHERE SSN={};".format(full_addy, SSN)
                cursor.execute(query)
                database_connect.commit()
                print("Full Street Address has been updated sucessfully!")
            elif new_action==6:
                state=input("Enter new state name. (Format: XX) :")
                state=state.upper()
                query="UPDATE CDW_SAPP_CUSTOMER SET CDW_SAPP_CUSTOMER.CUST_STATE = '{}' WHERE SSN={};".format(state, SSN)
                cursor.execute(query)
                database_connect.commit()
                print("State has been updated sucessfully!")
            elif new_action==7:
                first=input("Enter first name: ")
                middle=input("Enter middle name: ")
                last=input("Enter last name: ")
                query="UPDATE CDW_SAPP_CUSTOMER SET CDW_SAPP_CUSTOMER.FIRST_NAME = '{}', CDW_SAPP_CUSTOMER.MIDDLE_NAME ='{}', \
                CDW_SAPP_CUSTOMER.LAST_NAME = '{}' WHERE SSN={};".format(first, middle, last, SSN)
                cursor.execute(query)
                database_connect.commit()
                print("Full name has been updated sucessfully!")
            elif new_action==8:
                continue

        # 3) Used to generate a monthly bill for a credit card number for a given month and year.
        elif action == 3:
            credit = input("Provide Credit Card No: ")
            year = int(input("For Which Year? (Format: XXXX)"))
            month = int(input("For Which Month? (Format: XX)"))
            query = "SELECT * FROM CDW_SAPP_CREDIT_CARD WHERE CREDIT_CARD_NO = '{}' AND YEAR(TIMEID)={} AND MONTH(TIMEID)={};".format(credit, year, month)
            cursor.execute(query)
            getting_data=cursor.fetchall()
            print(getting_data)
        # 4) Used to display the transactions made by a customer between two dates. Order by year, month, and day in descending order.
        elif action == 4:
            credit = input("Provide Credit Card No: ")
            start= input("Provide the BEGINNING date (Format: YYYYMMDD): ")
            end= input("Provide the END date (Format: YYYYMMDD): ")
            start_time = datetime.strptime(start, '%Y%m%d').date()
            end_time = datetime.strptime(end, 'Y%m%d').date()
            query="SELECT * FROM CDW_SAPP_CREDIT_CARD WHERE CREDIT_CARD_NO = '{}' AND TIMEID BETWEEN '{}' AND '{}' \
            ORDER BY YEAR(TIMEID) DESC, MONTH(TIMEID) DESC, DAY(TIMEID) DESC;".format(credit, start, end)
            cursor.execute(query)
            getting_data=cursor.fetchall()
            print(getting_data)
        elif action == 5:
            x=False

def all_menus():
    choices = {
        'Customer Menu': '2',
        'Transaction Menu': '1',
        'Exit': '3'
    }
    print("\nMenu Choice\n")
    print("1. Transaction Menu")
    print("2. Customer Menu")
    print("3. Exit\n")
    while True:
        choice = input("Which Menu do you want to use? (Please input # 1-3): ")
        if choice == choices['Customer Menu']:
            check_account()
        elif choice == choices['Transaction Menu']:
            see_stuff()
        elif choice == choices['Exit']:
            print("Goodbye!")
            break

all_menus()