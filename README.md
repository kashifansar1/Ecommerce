# E-Commerce v2

A professional multi-vendor e-commerce platform built with Python and Flask. This application allows customers to shop for products, sellers to manage their own inventory, and administrators to oversee the entire platform.

## 🚀 Features

### 🛒 Customer Experience
- **Product Discovery:** Browse products with category filtering, price range filtering, and a full-text search box.
- **Shopping Cart:** Add products to a persistent cart before proceeding to checkout.
- **User Accounts:** Secure registration and login system.
- **Order Management:** Place orders with detailed shipping information.

### 🏪 Seller Dashboard
- **Inventory Management:** Sellers can list, edit, and manage their own products.
- **Store Profile:** Dedicated seller profiles linked to user accounts.
- **Stock Tracking:** Manage product availability and stock levels.

### 🛠️ Administrative Control
- **Platform Oversight:** Dedicated admin dashboard for site-wide management.
- **Role-Based Access Control:** Distinct permissions for Admin, Seller, and Customer roles.

## 🛠️ Technical Stack

- **Backend:** Python 3.x, Flask
- **Database:** MySQL (via Flask-SQLAlchemy)
- **Frontend:** Jinja2 Templates, HTML5, CSS3
- **Environment:** `python-dotenv` for secure configuration

## 📁 Project Structure

```text
ecommerce_v2/
├── app.py              # Application entry point & configuration
├── models.py           # Database schema & SQLAlchemy models
├── routes/             # HTTP Route handlers (Blueprints)
│   ├── admin_routes.py  # Admin panel logic
│   ├── customer_routes.py # Shopping & Checkout logic
│   └── seller_routes.py   # Vendor management logic
├── services/            # Business logic layer
│   ├── auth_services.py    # User registration & login
│   └── product_services.py # Catalog & Search logic
├── static/              # CSS, Images, and JS assets
├── templates/          # HTML views
└── requirements.txt    # Project dependencies
```

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.x
- MySQL Server

### Step-by-Step Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd ecommerce_v2
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   # Windows:
   .\venv\Scripts\activate
   # Unix/macOS:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   Create a `.env` file in the root directory and add your credentials:
   ```env
   SECRET_KEY=your_super_secret_key
   DB_USER=your_mysql_user
   DB_PASSWORD=your_mysql_password
   DB_HOST=localhost
   DB_NAME=ecommerce_db
   ```

5. **Initialize the database:**
   Ensure your MySQL server is running and the database specified in `.env` exists. Run the application to initialize tables:
   ```bash
   python app.py
   ```

## 🛣️ Roadmap
- [ ] Implement password hashing (security hardening).
- [ ] Add `Flask-Migrate` for database migrations.
- [ ] Integrate a payment gateway (e.g., Stripe or PayPal).
- [ ] Implement a comprehensive unit testing suite.
- [ ] Add an image upload system for product photos.
