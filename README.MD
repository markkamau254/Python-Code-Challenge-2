# Coffee Shop Domain OOP Assignment

## Overview
This assignment evaluates your understanding of Object-Oriented Programming (OOP) principles using Python. You will work with a Coffee Shop domain where there are three models: Customer, Coffee, and Order. Your task is to implement the relationships between these classes and define methods to manage and manipulate their attributes.

### Domain Details
- Customer has many orders.
- Coffee has many orders.
- Order belongs to both a Customer and a Coffee.
- Coffee and Customer share a many-to-many relationship via Order.

## Repository Setup
### 1.  Clone the Repository.
To get started with the project, clone the repository to your local machine:

        git clone <your-repo-url>
        cd <your-repo-folder>

### 2.  Create and Activate Virtual Environment.
Create a virtual environment to manage project dependencies:

        # Create virtual environment
        python3 -m venv venv
        
        # Activate the virtual environment
        # For Linux/macOS
        source venv/bin/activate
        
        # For Windows
        venv\Scripts\activate

### 3.  Install Dependencies.
If there are any dependencies, install them using pip:


        # pip install -r requirements.txt

### 4.  Running the Application
To run the application, navigate to the project directory and execute the following command:


        # python main.py

This will execute the Python program, allowing you to interact with the models and test the relationships between Customer, Coffee, and Order.
###########################################################################################################333333
## Project Structure
The project follows a well-structured folder layout for easy navigation:


        # .
                ├── main.py                
                ├── customer.py            
                ├── coffee.py             
                ├── order.py               
                ├── tests/
                │   └── customer_test.py    
                ├── README.md              
                └── requirements.txt       

### **Folder and File Explanation:**
- main.py: This file will be the entry point of the application, where you can create instances of the classes and test them.
- customer.py, coffee.py, order.py: These files contain the classes representing the models Customer, Coffee, and Order.
- tests/: A folder for unit testing. Add additional test files as necessary to ensure your code works as expected.
- requirements.txt: Contains a list of dependencies (if required). If your project doesn't have any specific dependencies, this file can remain empty.

## Task Details
You need to complete the following methods in the respective classes:

### **Customer Class:**
- __init__(self, name)
- name property
- orders()
- coffees()
- create_order(coffee, price)
- Class method most_aficionado(coffee)


### **Coffee Class:**
- __init__(self, name)
- name property
- orders()
- customers()
- num_orders()
- average_price()


### **Order Class:**
- __init__(self, customer, coffee, price)
- price property
- customer property
- coffee property


- ### **Key Concepts Covered**
- [x] Classes and Instances: Creating classes for Customer, Coffee, and Order with appropriate methods and properties.
- [x] Object Relationships: Establishing many-to-many relationships between Customer and Coffee through Order.
- [x] Data Validation: Ensuring valid input through custom setter methods.
- [x] Class and Instance Methods: Differentiating between class methods (such as finding the most frequent customer) and instance methods.


### 3.  Testing.
Unit tests for the Customer class are provided in the tests/ directory. To run the tests, execute the following command:

        # python -m unittest discover tests

You can add more tests for other classes to ensure your code is robust and error-free.



##**Author**
Mark Kamau

