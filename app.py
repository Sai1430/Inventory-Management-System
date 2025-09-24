# app.py
from flask import Flask, request, jsonify
from database import get_connection, init_db

app = Flask(__name__)
init_db()

@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data['name']
    quantity = data['quantity']
    price = data['price']
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, quantity, price) VALUES (%s, %s, %s)", (name, quantity, price))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Product added successfully"}), 201

@app.route('/products', methods=['GET'])
def get_products():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    products = [{"id": r[0], "name": r[1], "quantity": r[2], "price": r[3]} for r in rows]
    return jsonify(products)

@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.get_json()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET name=%s, quantity=%s, price=%s WHERE id=%s",
                   (data['name'], data['quantity'], data['price'], id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Product updated successfully"})

@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Product deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
