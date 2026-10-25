from models import User , db

class AuthService:

    def login(self, email, password):

        user = User.query.filter_by(
            email=email,
            password=password
        ).first()

        return user
    
    # Method for checking if exits
    def user_exists(self, email):

        user = User.query.filter_by(email=email).first()

        return user

    # For creating user
    def create_user(self,
        name,
        email,
        password,
        address
        ):

        user = User(
            name=name,
            email=email,
            password=password,
            address=address
        )

        db.session.add(user)

        db.session.commit()

        return user

    # calling methods for registration
    def register_user(
        self,
        name,
        email,
        password,
        address):

        if self.user_exists(email):
            return False

        self.create_user(
            name,
            email,
            password,
            address
        )

        return True