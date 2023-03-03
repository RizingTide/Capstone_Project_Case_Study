# Capstone_Project_Case_Study

<img width="653" alt="Screenshot 2023-03-03 at 7 52 55 AM" src="https://user-images.githubusercontent.com/118309470/222725054-a6e39e82-c4c7-4708-8df2-f0b4f640bc27.png">

The Credit Card System database is an independent system developed for managing activities such as registering new customers and approving or canceling requests, etc., using the architecture.
A credit card is issued to users to enact the payment system. It allows the cardholder to access financial services in exchange for the holder's promise to pay for them later. Below are three files that contain the customer’s transaction information and inventories in the credit card information.
- CDW_SAPP_CUSTOMER.JSON: This file has the existing customer details.
- CDW_SAPP_CREDITCARD.JSON: This file contains all credit card transaction information.
- CDW_SAPP_BRANCH.JSON: Each branch’s information and details are recorded in this file. 

<img width="486" alt="Screenshot 2023-03-03 at 7 55 17 AM" src="https://user-images.githubusercontent.com/118309470/222725499-36db3508-adeb-483f-b611-07cc8ef71e75.png">

<img width="1328" alt="Screenshot 2023-03-03 at 7 54 42 AM" src="https://user-images.githubusercontent.com/118309470/222725402-828c83bc-d11c-441f-ad1a-8e468d302c28.png">

Read the JSON files using PySpark and Created DataFrames:

<img width="1080" alt="Screenshot 2023-03-03 at 7 56 59 AM" src="https://user-images.githubusercontent.com/118309470/222726104-f0d2ae58-8a18-4839-9eef-ff8610d768ee.png">
<img width="1346" alt="Screenshot 2023-03-03 at 8 00 13 AM" src="https://user-images.githubusercontent.com/118309470/222726493-c42ec61a-ddd0-4bf6-9503-2cea56882295.png">

Loaded Them Into MySQL Database:

<img width="1086" alt="Screenshot 2023-03-03 at 8 01 20 AM" src="https://user-images.githubusercontent.com/118309470/222726649-76febcbb-36bc-45bf-9706-8e708ebc4770.png">

Here is a view of The Table on The MySQL Database:
<img width="1440" alt="Screenshot 2023-03-03 at 8 03 29 AM" src="https://user-images.githubusercontent.com/118309470/222727102-ca21dc1f-f46b-469c-b5f8-22f39a6151e1.png">

Next we needed to make a Console 

Here is a view of the Transactions Menu:

<img width="592" alt="Screenshot 2023-03-03 at 8 11 45 AM" src="https://user-images.githubusercontent.com/118309470/222728675-aac0bb2d-2cd6-41d8-98e4-d37c855f9643.png">

Here is a view of the Customers Menu:

<img width="1063" alt="Screenshot 2023-03-03 at 8 14 47 AM" src="https://user-images.githubusercontent.com/118309470/222729226-4557ac51-ed0f-4818-a553-d6ac2b30b29d.png">

Next we created some graphs/visualizations:

# Find and plot which transaction type has a high rate of transactions.

<img width="742" alt="Screenshot 2023-03-03 at 8 15 35 AM" src="https://user-images.githubusercontent.com/118309470/222729430-420245dd-b25b-4422-a2cf-9d3bbad806ea.png">

# Find and plot which state has a high number of customers.

<img width="665" alt="Screenshot 2023-03-03 at 8 16 34 AM" src="https://user-images.githubusercontent.com/118309470/222729630-450709da-70f4-485c-9d97-1b906a6b573c.png">

# Find and plot the sum of all transactions for the top 10 customers, and which customer has the highest transaction amount.

<img width="662" alt="Screenshot 2023-03-03 at 8 17 15 AM" src="https://user-images.githubusercontent.com/118309470/222729797-edaa4617-de7e-4f33-a107-2f0b44ef9ef5.png">

Now we connect to data from an onine Loan API to get more information on the banks transactions
Used Get requests and pyspark to create a data frame

<img width="923" alt="Screenshot 2023-03-03 at 8 19 01 AM" src="https://user-images.githubusercontent.com/118309470/222730178-440c32bf-e103-40f5-a415-8522464ced97.png">

Used pyspark and sql connector jdbc to write to MySQL Database

<img width="930" alt="Screenshot 2023-03-03 at 8 19 56 AM" src="https://user-images.githubusercontent.com/118309470/222730344-6ee122ce-96c5-49ec-a81a-74e1fb741882.png">

Here is a view from the MySQL Database

<img width="1387" alt="Screenshot 2023-03-03 at 8 22 25 AM" src="https://user-images.githubusercontent.com/118309470/222730949-0ba168ce-4d0c-4978-8c85-8217654f56ee.png">

Here are some Visualizations and Insights From The Data

# Find and plot the percentage of applications approved for self-employed applicants.

<img width="538" alt="Screenshot 2023-03-03 at 8 23 34 AM" src="https://user-images.githubusercontent.com/118309470/222731213-11e3e38b-2cfb-48c2-b48a-4e35213ad44e.png">

# Find the percentage of rejection for married male applicants.

<img width="416" alt="Screenshot 2023-03-03 at 8 24 29 AM" src="https://user-images.githubusercontent.com/118309470/222731375-068f8f0f-2201-4099-b90e-3a8dc7144bf3.png">

# Find and plot the top three months with the largest transaction data.

<img width="615" alt="Screenshot 2023-03-03 at 8 24 46 AM" src="https://user-images.githubusercontent.com/118309470/222731459-e3e8a050-0406-41af-9541-e75fce51255b.png">

# Find and plot which branch processed the highest total dollar value of healthcare transactions.

<img width="884" alt="Screenshot 2023-03-03 at 8 25 25 AM" src="https://user-images.githubusercontent.com/118309470/222731594-4f0e31ff-743e-4298-b820-1512bc0d5282.png">




