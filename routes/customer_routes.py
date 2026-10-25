from flask import Flask,render_template,request,redirect,session,flash,Blueprint,url_for

from services.product_services import ProductService
from services.cart_services import CartService
from services.order_services import OrderService
from services.my_order import Myorder

from auth.login_req import login_required

customer_bp = Blueprint('customer',__name__,url_prefix='/customer')

@customer_bp.route('/')
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

@customer_bp.route('/add-to-cart/<int:product_id>')
def add_to_cart(product_id):

    service = CartService()

    service.add_to_cart(
        session['user_id'],
        product_id
    )

    return redirect('/customer/')

@customer_bp.route('/cart')
@login_required
def cart():

    service = CartService()

    cart_items = service.get_cart_items(
        session['user_id']
    )

    total_amount = service.get_total_amount(session['user_id'])

    return render_template('customer/cart.html',
        cart_items=cart_items, total_amount=total_amount)

@customer_bp.route('/remove-cart/<int:cart_id>')
def remove_cart(cart_id):

    service = CartService()

    service.remove_cart_item(cart_id)

    return redirect('/customer/cart')

@customer_bp.route('/increase-quantity/<int:cart_id>')
def increase_quantity(cart_id):

    service = CartService()

    service.increase_quantity(cart_id)

    return redirect('/customer/cart')

@customer_bp.route('/decrease-quantity/<int:cart_id>')
def decrease_quantity(cart_id):

    service = CartService()

    service.decrease_quantity(cart_id)

    return redirect('/customer/cart')


@customer_bp.route('/place_order', methods=['GET', 'POST'])
@login_required
def place_order():

    service = OrderService()

    user = service.get_user(
        session['user_id']
    )

    if request.method == 'POST':

        address = request.form['address']
        phone = request.form['phone']

        success, message = service.place_order(
            session['user_id'],
            address,
            phone
        )

        flash(message)

        if not success:
            return redirect('/customer/cart')
        
        return redirect('/customer/my_order')

    return render_template(
        'customer/place_order.html',
        user=user
    )


@customer_bp.route('/my_order')
@login_required
def my_orders():

    service = Myorder()

    orders = service.my_order_items(
        session['user_id']
    )

    return render_template(
        'customer/my_order.html',
        orders=orders
    )

@customer_bp.route('/cancel_order/<int:item_id>')
def cancel_order(item_id):

    service = Myorder()

    service.cancel_order_item(
        session['user_id'],
        item_id
    )

    return redirect('/customer/my_order')

