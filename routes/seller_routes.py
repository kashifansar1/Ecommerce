from flask import Flask,render_template,request,redirect,session,flash,Blueprint,url_for

from auth.auth import role_required

from services.seller.seller_services import SellerService

# for storing image we need this
import uuid
from werkzeug.utils import secure_filename
import os

seller_bp = Blueprint('seller',__name__,url_prefix='/seller')

@seller_bp.route('/dashboard')
def dashboard():

    service = SellerService()

    stats = service.get_dashboard_stats(
        session['user_id']
    )

    return render_template(
        'seller/dashboard.html',
        total_products=stats['total_products'],
        total_orders=stats['total_orders'],
        total_stock=stats['total_stock']
    )

@seller_bp.route('/seller-product', methods=['GET', 'POST'])
def manage_products():

    service = SellerService()

    delete_id = request.args.get('delete')

    if delete_id:

        service.delete_product(
            session['user_id'],
            delete_id
        )

        return redirect('/seller/seller-product')
    

    if request.method == 'POST':

                # getting request to store pro image file
        image = request.files.get('image')

        if not image:
            flash("Please select an image")
            return redirect('/seller/seller-product')

        filename = f"{uuid.uuid4()}_{secure_filename(image.filename)}"

        image.save(os.path.join(
                'static/uploads',
                filename
            )
        )

        service.add_product(
            session['user_id'],
            request.form['product_name'],
            request.form['price'],
            request.form['stock'],
            request.form['category_id'],
            filename
        )

        return redirect('/seller/seller-product')

    products = service.get_products(
        session['user_id']
    )

    categories = service.get_categories()

    return render_template(
        'seller/seller-product.html',
        products=products,
        categories=categories
    )


@seller_bp.route('/manage-orders',methods=['GET', 'POST'])
def manage_orders():

    service = SellerService()

    if request.method == 'POST':

        service.update_order_status(
            request.form['item_id'],
            request.form['statuss']
        )

        return redirect('/seller/manage-orders')

    orders = service.get_orders(
        session['user_id']
    )

    status = [
        'Pending',
        'Packed',
        'Shipped',
        'Delivered',
        'Cancelled'
    ]

    return render_template(
        'seller/manage-orders.html',
        orders=orders,
        status=status
    )