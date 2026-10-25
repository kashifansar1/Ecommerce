from models import Product , Category

class ProductService:

    def get_products(self, category=None, price=None ,search = None):

        query = Product.query

        if category:
            query = query.filter_by(category_id=category)

        if price == "high":
            query = query.order_by(Product.price.desc())

        elif price == "low":
            query = query.order_by(Product.price.asc())

        if search:
            query = query.filter(Product.product_name.ilike(f"%{search}%"))


        return query.all()
    
    def get_all_category(self):
        return Category.query.all()