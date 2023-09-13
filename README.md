# Inventory Management System

The **Inventory Management System** is a command-line interface (CLI) based application written in Python. It serves as a tool for managing inventory in a shopping center. The system utilizes JSON for data storage, enabling real-time updates to the inventory and generating bills for customer purchases. Additionally, it provides features for monitoring inventory levels and ensuring data security.

## Intention and Motive of the Project

This project was one of my initial projects undertaken while learning Python and exploring more about data manipulation. It was a fun project that allowed me to apply my programming skills to solve a real-world problem. Through this project, I aimed to:

- Gain practical experience in Python programming.
- Learn how to work with JSON data for storage and retrieval.
- Understand the fundamentals of inventory management.
- Implement security measures to protect data.

## Features

### Billing.py

#### 1. Generation of Bills
   - The system generates bills for customer purchases, summarizing the items bought and their prices.

![Bill](https://user-images.githubusercontent.com/89451392/132208828-975c3379-e869-4e8d-97f6-9bd4274be1ab.jpg)

#### 2. Real-time Inventory Updates
   - Any changes made to the inventory are instantly reflected in the 'record.json' file.

#### 3. Inventory Level Notifications
   - If an item's quantity falls below a certain threshold, the system notifies the admin to replenish the stock.

#### 4. Email Billing
   - Bills can be sent to customers via email for their convenience.

![Email Billing](https://user-images.githubusercontent.com/89451392/150775270-fbdaf2dc-9063-4300-ae41-8ad05871443d.jpg)

#### 5. Sales Data Logging
   - All sales transactions are logged in 'sales.json' to maintain a record of sales activities.

![Sales Record](https://user-images.githubusercontent.com/89451392/132209911-9967a221-891f-484d-baf9-8912dbca9888.png)

### ModifyingInventory.py

#### 1. Inventory Management Operations
   - The application supports various inventory management operations, including creating, inserting, deleting, updating, and modifying items.

![Inventory Management](https://user-images.githubusercontent.com/89451392/132208939-0d85c6f3-ccf2-4981-8b5a-de653f629c58.png)

#### 2. Flexible Operations
   - You can perform inventory operations as many times as needed.

#### 3. Data Security
   - The system employs hash functions to enhance security, ensuring that only authorized individuals with correct credentials can access and modify the inventory.

![Access Denial](https://user-images.githubusercontent.com/89451392/132209367-890b6e04-1a79-4ccc-ae96-e19c46a5b486.png)

## Usage

1. Clone the repository to your local machine.
2. Install the required Python packages, if not already installed, using `pip install -r requirements.txt`.
3. Run the application using the command `python Billing.py` or `python ModifyingInventory.py` in the terminal.
