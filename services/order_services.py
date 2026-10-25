from models import User, Customer, Cart, Order, OrderItem, Product, db
from services.cart_services import CartService

class OrderService:

    def __init__(self):
        self.cart_services = CartService()

    def validate_stock(self, cart_items):

        for item in cart_items:

            if item.product.stock == 0:

                return (
                    False,
                    f"{item.product.product_name} is out of stock"
                )

            if item.quantity > item.product.stock:

                return (
                    False,
                    f"Only {item.product.stock} units available for {item.product.product_name}"
                )

        return True, None
        

    def place_order(self, user_id, address, phone):

        # creating customer from user if not exists
        self.create_customer_if_not_exists(user_id)

        # getting cart items of the user
        cart_items = self.cart_services.get_cart_items(user_id)

        success, message = self.validate_stock(
            cart_items
        )

        if not success:
            return False, message

        # creating order
        order = self.create_order(
            user_id,
            address,
            phone
        )

        # inserting items of order_id
        self.create_order_items(
            order.order_id,
            cart_items
        )

        # managing inventry
        self.update_stock(
            cart_items
        )

        # clearing cart after prder placed
        self.cart_services.clear_cart(
            user_id
        )

        db.session.commit()

        return True, "Order placed successfully!"
    
    def create_customer_if_not_exists(self, user_id):

        customer = Customer.query.get(user_id)

        if not customer:

            user = User.query.get(user_id)

            customer = Customer(
                customer_id=user.user_id,
                first_name=user.name
            )

            db.session.add(customer)


    
    def create_order(self, user_id, address, phone):

        order = Order(
            customer_id=user_id,
            shipping_address=address,
            phone_no=phone
        )

        db.session.add(order)
        db.session.flush()

        return order
    
    def create_order_items(self, order_id, cart_items):

        for item in cart_items:

            order_item = OrderItem(
                order_id=order_id,
                product_id=item.product_id,
                quantity=item.quantity
            )

            db.session.add(order_item)

    def update_stock(self, cart_items):

        for item in cart_items:

            product = Product.query.get(
                item.product_id
            )

            product.stock -= item.quantity

    def get_user(self , user_id):

        return User.query.get(user_id)
    


    

    