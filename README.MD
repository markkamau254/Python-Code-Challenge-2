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
## Project Breakdown
- ### **Home Page*
   **Features** ⚙️
- [x] **Search Bar** : Search transaction by entering transaction details on the input and click enter.
- [x] **Input Fields** : Add transaction details in the input fields as labled.
- [x] **Add Transaction** : Click this button to add transaction details in the form.
- [x] **Delete Button** : Click _Delete_ button to delete a transaction.

## prerequisites

    React.js

## System Requirements

- Node 18+
- JSON Server
- A browser capable of running JavaScript (Chrome, Firefox, Safari, or Edge)
- Operating System (Windows 10+, MacOS, Linux, etc.)
- A text editor capable of running JavaScript (Visual Studio Code, Vim, Nano, Emacs, Atom, Sublime Text, etc.)
- RAM >= 4GB
- Disk space >= 1GB

## Installation

To use this repo, follow these steps:

### Alternative One

1.  Open the terminal/CLI on your computer.

2.  If you don't have JSON server installed in the terminal, install it globally using the following command:

        npm install -g json-server

3.  Clone the repository by running the following command:

        git clone https://github.com/markkamau254/Code-Challenge-3.git

4.  Change directory to the repo folder:

        cd deploying_a_local_server

5.  Open it in your Code Editor of choice. If you use VS Code, run the command:

        code .
    
6   Run json-server, run the command:

      json-server --watch src/db.json .
      
7   Open the app on your browser, run the command:

      npm start .

### Alternative Two

- On the top right corner of this page there is a button labelled Fork.

- Click on that button to create a copy of the repository to your own account.

- Follow the process described in Alternative One above.

- Remember to replace your username when cloning.

      git clone https://github.com/markkamau254/Code-Challenge-3.git

  
## **You can check the deployed website by clicking the live link below** 👇 
You can view the deployed project [here](https://the-iron-bank.vercel.app/).

##**Author**
Mark Kamau

