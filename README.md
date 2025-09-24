# Inventory Management System

**Tech Stack:** Python, Flask, MySQL

## Overview
This is a mini backend project that allows you to **manage products in an inventory** using a REST API.  
You can **add, view, update, and delete products**, with all data stored in a MySQL database.

## Features
- Add a new product (name, quantity, price)
- View all products
- Update existing products
- Delete products
- Simple REST API endpoints

## Project Structure
inventory_app/
├── app.py # Main Flask application
├── database.py # MySQL connection and table creation
├── config.py # Database configuration
├── requirements.txt# Python dependencies
└── README.md # Project documentation

bash
Copy code

## Setup Instructions
1. **Clone the repository**  
```bash
git clone https://github.com/Sai1430/Inventory-Management-System.git
cd Inventory-Management-System
Install dependencies

bash
Copy code
pip install -r requirements.txt
Setup MySQL database

sql
Copy code
CREATE DATABASE inventory_db;
Update config.py with your MySQL username and password.

Run the Flask application

bash
Copy code
python app.py
The app runs at: http://127.0.0.1:5000

API Endpoints
Method	Endpoint	Description
POST	/products	Add a new product
GET	/products	Get all products
PUT	/products/<id>	Update a product by ID
DELETE	/products/<id>	Delete a product by ID

Sample JSON for POST /products
json
Copy code
{
    "name": "Laptop",
    "quantity": 10,
    "price": 50000
}
Sample JSON for PUT /products/<id>
json
Copy code
{
    "name": "Laptop Pro",
    "quantity": 8,
    "price": 55000
}
Notes
