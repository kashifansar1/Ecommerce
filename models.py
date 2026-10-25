from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), default="customer")
    address = db.Column(db.String(50), nullable=False)

    seller = db.relationship("Seller", back_populates="user", uselist=False ,cascade="all, delete-orphan")
    cart_items = db.relationship("Cart", back_populates="user" , cascade="all, delete-orphan")

class Category(db.Model):
    __tablename__ = "categories"

    cat_id = db.Column(db.Integer,primary_key=True)
    cat_name = db.Column(db.String(20),nullable=False)

    products = db.relationship("Product", back_populates="category")

class Seller(db.Model):
    __tablename__ = "sellers"

    seller_id = db.Column(db.Integer,primary_key=True)
    seller_name = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100),unique=True,nullable=False)
    phone = db.Column(db.String(20))
    address = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey('users.user_id'),nullable=False)

    user = db.relationship("User", back_populates="seller")
    products = db.relationship("Product", back_populates="seller" , cascade="all, delete-orphan")

class Customer(db.Model):
    __tablename__ = "customers"

    customer_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    city = db.Column(db.String(50))

    orders = db.relationship("Order", back_populates="customer" ,cascade="all, delete-orphan")

class Order(db.Model):
    __tablename__ = "orders"

    order_id = db.Column(db.Integer,primary_key=True)
    customer_id = db.Column(db.Integer,db.ForeignKey("customers.customer_id"), nullable=True)
    order_date = db.Column(db.Date, default=date.today)
    total_amount = db.Column(db.Numeric(10, 2),default=0.00)
    shipping_address = db.Column(db.String(250))
    phone_no = db.Column(db.String(15))

    customer = db.relationship("Customer", back_populates="orders")
    order_items = db.relationship("OrderItem", back_populates="order" , cascade="all, delete-orphan")

class Product(db.Model):
    __tablename__ = "products"

    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(50))
    price = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.cat_id"))
    pdc_seller_id = db.Column(db.Integer, db.ForeignKey("sellers.seller_id"))
    stock = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(255))

    category = db.relationship("Category", back_populates="products")
    seller = db.relationship("Seller", back_populates="products")
    order_items = db.relationship("OrderItem", back_populates="product")
    cart_items = db.relationship("Cart", back_populates="product")

class OrderItem(db.Model):
    __tablename__ = "order_items"

    item_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.order_id"))
    product_id = db.Column(db.Integer, db.ForeignKey("products.product_id"))
    quantity = db.Column(db.Integer)
    status = db.Column(db.String(50), default="Pending")

    order = db.relationship("Order", back_populates="order_items")
    product = db.relationship("Product", back_populates="order_items")

class Cart(db.Model):
    __tablename__ = "cart"

    cart_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    product_id = db.Column(db.Integer, db.ForeignKey("products.product_id"))
    quantity = db.Column(db.Integer, default=1)

    user = db.relationship("User", back_populates="cart_items")
    product = db.relationship("Product", back_populates="cart_items")




