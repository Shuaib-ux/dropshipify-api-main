import base64
from email.policy import default
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import  check_password_hash
from datetime import datetime
import base64
#Instantiating sqlalchemy object
db = SQLAlchemy()

favourite_shops = db.Table('favourite_shops',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('favourite_shop_id', db.Integer, db.ForeignKey('store.id'))
)
favourite_niche = db.Table('favourite_niche',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('favourite_niche_id', db.Integer, db.ForeignKey('niche.id'))
)
favourite_products = db.Table('favourite_products',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('favourite_product_id', db.Integer, db.ForeignKey('product.id'))
)

store_niches = db.Table('store_niches',
    db.Column('store_id', db.Integer, db.ForeignKey('store.id')),
    db.Column('niche_id', db.Integer, db.ForeignKey('niche.id'))
)
product_niches = db.Table('product_niches',
    db.Column('product_id', db.Integer, db.ForeignKey('product.id')),
    db.Column('niche_id', db.Integer, db.ForeignKey('niche.id'))
)

'''end of many tp many tables'''

class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150) )
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    is_retailer = db.Column(db.Boolean(),default= False)
    mailing_address = db.Column(db.String(150))
    city = db.Column(db.String(150) )
    state = db.Column(db.String(150) )
    zip_ = db.Column(db.String(150) )
    mailing_phone_number = db.Column(db.String(150))
    store = db.relationship("Store", uselist=False, backref='user')
    orders = db.relationship("Order", backref='user',lazy='dynamic')
    favoutite_stores = db.relationship("Store",secondary = favourite_shops)
    favoutite_products = db.relationship("Product", secondary = favourite_products, backref ='products')
    favoutite_niche = db.relationship("Niche",secondary = favourite_niche)
    def __repr__(self):
        return '<User {}>'.format(self.email)
    # def set_password(self, password):
    #     self.password_hash = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    def json(self):        
        return {'id': self.id, 
                'email': self.email, 
                'first_name': self.first_name, 
                'last_name': self.last_name, 
                'is_retailer': self.is_retailer,
                'mailing_address': self.mailing_address,
                'city': self.city,
                'state': self.state,
                'zip': self.zip_,
                'store_id':self.store.id if self.store else None,
                'mailing_phone_number': self.mailing_phone_number}        
    def save_to(self):        
        db.session.add(self)        
        db.session.commit()
    def delete_(self):        
        db.session.delete(self)        
        db.session.commit()
    
    
class Store(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    store_name = db.Column(db.String(150),unique = True)
    store_icon = db.Column(db.String(150),nullable=True)
    store_description = db.Column(db.String(150))
    niches = db.relationship("Niche", secondary = store_niches)
    products = db.relationship("Product",backref='store', lazy='dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    orders = db.relationship("Order",backref='store',lazy='dynamic')
    
    def json(self):
        return {
            'id': self.id, 
            'store_name': self.store_name, 
            'store_description': self.store_description, 
            'user_id': self.user_id,
            'image': self.store_icon
            }    
    
class Product(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    price = db.Column(db.Numeric)
    product_name  = db.Column(db.String(150))
    asin = db.Column(db.String(150), nullable = True)
    product_link =  db.Column(db.String(500), nullable = True)
    number_available =  db.Column(db.Numeric)
    number_shipped =  db.Column(db.Numeric)
    number_clicks =  db.Column(db.Numeric, default = 0)
    description = db.Column(db.String(300))
    product_image  = db.Column(db.String(150))
    date_added = db.Column(db.DateTime(timezone = True) ,default = datetime.now)
    date_editted = db.Column(db.DateTime(timezone = True) ,default = datetime.now)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'))
    is_available = db.Column(db.Boolean, default=True)
    niche = db.relationship("Niche", secondary= product_niches)
    
    def json(self):   
        return {'id': self.id, 
                'product_name': self.product_name, 
                'price':str(self.price),
                'asin': self.asin,
                'product_link': self.product_link, 
                'number_available': int(self.number_available), 
                'number_shipped': int(self.number_shipped), 
                'description': self.description, 
                'date_added': str(self.date_added), 
                'image': self.product_image,
                }    
    
class Niche(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(150))
    
class Sales(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    date_sale = db.Column(db.DateTime(timezone = True) ,default = datetime.now)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    
class Order(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'))
    date_created = db.Column(db.DateTime(timezone = True) ,default = datetime.now)
    date_due = db.Column(db.DateTime(timezone = True) ,nullable = True)
    order_item = db.relationship("OrderItem", backref='order',lazy='dynamic')#1 to many
    status = db.Column(db.Numeric, default = 0)
    
class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Numeric, default = 1)
    