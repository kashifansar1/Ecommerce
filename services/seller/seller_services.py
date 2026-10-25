from models import Seller, Product, OrderItem , Category ,db , Customer , Order , User


class SellerService:

    def get_seller(self, user_id):

        return Seller.query.filter_by(
            user_id=user_id
        ).first()


    def get_dashboard_stats(self, user_id):

        seller = self.get_seller(user_id)

        total_products = Product.query.filter_by(
            pdc_seller_id=seller.seller_id
        ).count()

        total_stock = sum(
            product.stock
            for product in Product.query.filter_by(
                pdc_seller_id=seller.seller_id
            ).all()
        )

        total_orders = OrderItem.query.join(
            Product
        ).filter(
            Product.pdc_seller_id == seller.seller_id
        ).count()

        return {
            'total_products': total_products,
            'total_orders': total_orders,
            'total_stock': total_stock
        }
    
    
    # managing products of seller
    
    def get_categories(self):

        return Category.query.all()


    def get_products(self, user_id):

        seller = self.get_seller(user_id)

        return Product.query.filter_by(
            pdc_seller_id=seller.seller_id
        ).all()

    # adding products
    def add_product(
        self,
        user_id,
        product_name,
        price,
        stock,
        category_id,
        image_url):

        seller = self.get_seller(user_id)

        product = Product(
            product_name=product_name,
            price=price,
            stock=stock,
            category_id=category_id,
            pdc_seller_id=seller.seller_id,
            image_url = image_url
        )

        db.session.add(product)

        db.session.commit()


    def delete_product(
        self,
        user_id,
        product_id
    ):

        seller = self.get_seller(user_id)

        product = Product.query.filter_by(
            product_id=product_id,
            pdc_seller_id=seller.seller_id
        ).first()

        if product:

            db.session.delete(product)

            db.session.commit()

    # Managing orders
    
    def get_orders(self, user_id):

        seller = self.get_seller(user_id)

        seller_order = OrderItem.query.join(
                            Product,
                            OrderItem.product_id == Product.product_id
                        ).join(
                            Order,
                            OrderItem.order_id == Order.order_id
                        ).join(
                            Customer,
                            Order.customer_id == Customer.customer_id
                        ).join(
                            User,
                            Customer.customer_id == User.user_id
                        ).filter(
                            Product.pdc_seller_id == seller.seller_id
                        ).all()

        return seller_order

    def update_order_status(self,item_id,status):

        item = OrderItem.query.get(item_id)

        if item:

            item.status = status

            db.session.commit()