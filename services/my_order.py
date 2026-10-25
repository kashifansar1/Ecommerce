from models import User, Customer, Cart, Order, OrderItem, Product, db

class Myorder:

    def my_order_items(self , user_id):

        return Order.query.filter_by(
            customer_id=user_id
        ).order_by(Order.order_date.desc()).all()
    
    def cancel_order_item(self, user_id, item_id):

        order_item = OrderItem.query.get(item_id)

        if not order_item:
            return False

        if order_item.order.customer_id != user_id:
            return False

        if order_item.status == "Cancelled":
            return False

        # fetching product before cancelling to manage inventry
        product = Product.query.get(
            order_item.product_id)

        product.stock += order_item.quantity

        order_item.status = "Cancelled"

        db.session.commit()

        return True