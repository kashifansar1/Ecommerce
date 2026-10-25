from flask import Flask,render_template,request,redirect,session,flash
from services.auth_services import AuthService
from services.product_services import ProductService

# to commit operation we import db
from models import db

from routes.customer_routes import customer_bp
from routes.admin_routes import admin_bp
from routes.seller_routes import seller_bp

# For reading env file
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)

# register customer blueprint with app
app.register_blueprint(customer_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(seller_bp)

# Setting secret key
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Setting database connection
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+pymysql://{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}/"
    f"{os.getenv('DB_NAME')}"
)
app.config['SQLALCHEMY_ECHO'] = True
db.init_app(app) # creates engine

@app.route('/')
def home():

    category = request.args.get('category')
    price = request.args.get('price')

    #search box
    search = request.args.get('search')

    service = ProductService()
 
    categories = service.get_all_category()
    products = service.get_products(category=category,price=price ,search =search)

    return render_template(
        'customer/home.html',
        products=products,categories=categories
    )


@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        address = request.form['address']

        service = AuthService()

        success = service.register_user(
            name,
            email,
            password,
            address
        )

        if success:

            flash('Registration successful')

            return redirect('/login')

        flash('Email already exists')
        return redirect('/register')

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        service = AuthService()

        user = service.login(email, password)

        if user:

            session['user_id'] = user.user_id
            session['role'] = user.role
            session['user'] = user.name

            if session['role'] == "seller" :
                return redirect('/seller/dashboard')
            elif session['role'] == "admin" :
                return redirect('/admin/dashboard')
            
            else:
                return redirect('/customer/')

        return "Invalid Email or Password"

    return render_template('login.html')

@app.route('/logout')
def logout():

    session.clear()

    return redirect('/login')


if __name__ == "__main__":
    app.run(debug=True)