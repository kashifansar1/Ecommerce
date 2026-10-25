from models import Cart, User,db

class CartService:

    def add_to_cart(self, user_id, product_id):

        cart_item = Cart.query.filter_by(
            user_id=user_id,
            product_id=product_id
        ).first()

        if cart_item:
            cart_item.quantity += 1

        else:
            cart_item = Cart(
                user_id=user_id,
                product_id=product_id,
                quantity=1
            )

            db.session.add(cart_item)

        db.session.commit()

        return cart_item
    
    def get_cart_items(self, user_id):

        return Cart.query.filter_by(user_id=user_id).all()
    

    def get_total_amount(self, user_id):

        cart_items = self.get_cart_items(user_id)

        total = 0

        for item in cart_items:
            total += item.product.price * item.quantity

        return total
    
    def remove_cart_item(self, cart_id):

        # But when you're searching by the primary key, get() is shorter and clearer.
        # we can use filterby too but that too long.
        cart_item = Cart.query.get(cart_id)

        if cart_item:
            db.session.delete(cart_item)
            db.session.commit()


    def increase_quantity(self, cart_id):

        cart_item = Cart.query.get(cart_id)

        if cart_item:
            cart_item.quantity += 1
            db.session.commit()


    def decrease_quantity(self, cart_id):

        cart_item = Cart.query.get(cart_id)

        if cart_item and cart_item.quantity > 1:
            cart_item.quantity -= 1
            db.session.commit()


    # For clearing cart items after order placed
    def clear_cart(self, user_id):

        cart_items = self.get_cart_items(user_id)

        for item in cart_items:
            db.session.delete(item)
