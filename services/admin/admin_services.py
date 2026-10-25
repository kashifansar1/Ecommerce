from models import *

class AdminService:

    def total_products(self):
        return Product.query.count()

    def total_orders(self):
        return Order.query.count()

    def total_users(self):
        return User.query.count()

    def total_sellers(self):
        return Seller.query.count()
    
    # for removing products
    def get_all_products(self):

        return Product.query.all()


    def delete_product(self, product_id):

        product =  Product.query.get(product_id)

        if product:

            db.session.delete(product)

            db.session.commit()

    # for managing users
    def get_latest_users(self):

        return User.query.order_by(
            User.user_id.desc()
        ).all()


    def delete_user(self, user_id):

        user = User.query.get(user_id)

        if user:

            db.session.delete(user)

            db.session.commit()

    # To change roles
    def change_role(self, user_id, role):

        user = User.query.get(user_id)

        if not user:
            return False

        user.role = role

        db.session.commit()

        return True
    
        # manage categories
    def get_all_categories(self):

        return Category.query.order_by(
            Category.cat_id.desc()
        ).all()


    def add_category(self, cat_name):

        category = Category(
            cat_name=cat_name
        )

        db.session.add(category)

        db.session.commit()


    def delete_category(self, cat_id):

        category = Category.query.get(cat_id)

        if category:

            db.session.delete(category)

            db.session.commit()