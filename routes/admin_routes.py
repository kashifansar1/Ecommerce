from flask import Flask,render_template,request,redirect,session,flash,Blueprint,url_for
from services.admin.admin_services import AdminService


from auth.login_req import login_required
from auth.auth import role_required

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/dashboard')
@role_required('admin')
def dashboard():

    service = AdminService()

    return render_template(
        'admin/dashboard.html',
        total_products=service.total_products(),
        total_orders=service.total_orders(),
        total_users=service.total_users(),
        total_sellers=service.total_sellers()
    )

@admin_bp.route('/manage-products')
@role_required('admin')
def manage_products():

    service = AdminService()

    delete_id = request.args.get('delete')

    if delete_id:

        service.delete_product(delete_id)

        return redirect('/admin/manage-products')

    products = service.get_all_products()

    return render_template(
        'admin/manage-products.html',
        products=products
    )

@admin_bp.route('/delete-product/<int:product_id>')
@role_required('admin')
def delete_product(product_id):

    service = AdminService()

    service.delete_product(product_id)

    return redirect('/admin/manage-products')

@admin_bp.route('/manage-users' , methods=['GET', 'POST'])
@role_required('admin')
def manage_users():

    service = AdminService()

    # to change roles
    if request.method == 'POST':

        service.change_role(
            request.form['user_id'],
            request.form['role']
        )

        return redirect('/admin/manage-users')

    # to delete
    delete_id = request.args.get('delete')

    if delete_id:

        service.delete_user(delete_id)

        return redirect('/admin/manage-users')

    # getting all user
    users = service.get_latest_users()

    return render_template(
        'admin/manage-users.html',
        users=users
    )

@admin_bp.route('/categories', methods=['GET', 'POST'])
@role_required('admin')
def manage_categories():

    service = AdminService()

    delete_id = request.args.get('delete')

    if delete_id:

        service.delete_category(delete_id)

        return redirect('/admin/categories')

    if request.method == 'POST':

        service.add_category(
            request.form['category_name']
        )

        return redirect('/admin/categories')

    categories = service.get_all_categories()

    return render_template(
        'admin/categories.html',
        categories=categories
    )