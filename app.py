from email import message
import os
import uuid as uuid
from ast import parse
import json
import base64
from curses.ascii import US
from distutils.log import debug
from flask import Flask, session
from flask_migrate import Migrate
from models import User, db, Store, Product,favourite_products
from flask_restful import Resource, reqparse, Api , abort
from flask_jwt_extended import jwt_required, create_access_token
from flask_jwt_extended import get_current_user
from models import User, db, Store, Product, Order, OrderItem
from werkzeug.utils import secure_filename
from flask_jwt_extended import  JWTManager
import cloudinary
import validators
from cloudinary.uploader import upload

from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify

#Instantiate a flask object 
app = Flask(__name__)
CORS(app)

#Instantiate Api object
api = Api(app)
#Setting the location for the sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
#Adding the configurations for the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True 
app.config["JWT_SECRET_KEY"] = "Dese.Decent.Pups.BOOYO0OST"
# cloudinary.config(cloud_name = os.getenv('CLOUD_NAME'), api_key=os.getenv('API_KEY'), 
#     api_secret=os.getenv('API_SECRET'))
# app.config.from_mapping(
#         CLOUDINARY_URL=os.environ.get('CLOUDINARY_URL') or 'Pegue a sua Key',
#     )
# cloudinary.config(cloud_name = "dropshipify", api_key='space time and the cosmos', 
#     api_secret="the turn of life")
cloudinary.config( 
  cloud_name = "dropshipify", 
  api_key = "628348882218943", 
  api_secret = "d6b7p9SwTrJ9g6EgbVPm9ceex-k" 
)
jwt = JWTManager(app)


#Link the app object to the Movies database 
db.init_app(app)
migrate = Migrate(app,db)

app.app_context().push()
#Create the databases
db.create_all() 

def add_orderItem(order, product_id):
    found_order_item_for_product = False
    print('Entering loop to find order item')
    for order_item in order.order_item:
        print('Entered loop to find order item')
        #check if we have a product in that order from order item
        print(product_id)
        print(order_item.product_id)
        if int(order_item.product_id) == int(product_id):
                #we found the product of that cart now we adding to it
                print('found a match for product id')
                found_order_item_for_product = True
                order_item.quantity+=1
                db.session.commit()
                break
    #if loop finished and we didnt find anything
    if not found_order_item_for_product:
        print("Didn't find the order item required so try creating new one ")
                #create order item mapped to product
        item = OrderItem( product_id = product_id, order=order)
        db.session.add(item)
        db.session.commit()
        
def get_Order_object(orders, product, user):
    
    # found_order_with_store = False
    # u_order = None
    print('about to enter loop to find order')
    for order in orders:
        print('entered loop to search for order matching store')
        if order.store_id == product.store_id and order.status==0:
            # u_order = order
            # print('found order that matches the store')
            # found_order_with_store = True
            # break
            return order
    # if not found_order_with_store:
    print('didnt find order in first place so creating new one')
    u_order = Order(store_id = product.store_id, 
                        user = user)
    db.session.add(u_order)
    db.session.commit()
    return u_order

class SignUpRetailer(Resource):
    #Declare the varriables to be passed as the post body
    parser = reqparse.RequestParser()                      
    parser.add_argument('store_name', type=str, required=True, help='Name of store required')    
    # parser.add_argument('file_name', type=str, required=True, help='File name required')    
    parser.add_argument('image', type=str, required=True, help='base 64 image text')  
    parser.add_argument('store_description', type=str, required=True, help='store description required')  
    @jwt_required()
    def post(self):
            app.logger.info('in signup retailer route')
            current_user = get_current_user()
            args = SignUpRetailer.parser.parse_args()
            if not current_user:
                abort(404,message="User not found")
            if current_user.is_retailer:
                abort(405,message="User Already has Store")
            # pic_filename = secure_filename(args['file_name'])
            #set pic name
            # pic_name = str(uuid.uuid1()) + "_" + pic_filename +'.png'
            new_store_name = Store.query.filter_by(store_name= args['store_name']).first()  
            if new_store_name:
                abort(409,message="Store name already taken")
            # try:
            
            try:
                photo_data = base64.b64decode(args['image'])
                upload_result = upload(photo_data)
                app.logger.info(args['store_name'], upload_result["secure_url"])
                new_store = Store(store_name = args['store_name'], 
                                store_icon = upload_result["secure_url"],
                                store_description = args['store_description'],
                                user = current_user )
                db.session.add(new_store)
                current_user.is_retailer = True
                db.session.commit()
                return {'message':'success'}, 201 
            except Exception as e:
                app.logger.info(e)
                abort(500, message = 'Error  while saving image')
                

                
class AddProduct(Resource):
    #Declare the varriables to be passed as the post body
    parser = reqparse.RequestParser()                      
    parser.add_argument('product_name', type=str, required=True, help='Name of product required')    
    # parser.add_argument('file_name', type=str, required=True, help='File name required')    
    parser.add_argument('image', type=str, required=True, help='base 64 image text')  
    parser.add_argument('price', type=float, required=True, help='Product Price')  
    parser.add_argument('product_link', type=str, required=False, help='External link to outside source of product') 
    parser.add_argument('asin', type=str, required=False, help='Product asin number') 
    parser.add_argument('number_available', type=int, required=True, help='Number of items required') 
    parser.add_argument('product_description', type=str, required=True, help='Product description required') 
    
    @jwt_required()
    def post(self):
            app.logger.info('in add product retailer route')
            args = AddProduct.parser.parse_args()
            user = get_current_user()
            if not user:
                abort(404,message="User not found")
            if not user.is_retailer:
                abort(403,message="User is not a retailer ")
            # pic_filename = secure_filename(args['file_name'])
            # #set pic name
            # pic_name = str(uuid.uuid1()) + "_" + pic_filename +'.png'
            try:
                valid = validators.url(args['image'])
                if valid:
                    image_url = args['image']
                else:
                    photo_data = base64.b64decode(args['image'])
                    upload_result = upload(photo_data)
                    image_url = upload_result["secure_url"]
                    app.logger.info(args['product_name'], image_url)
                new_product = Product(product_name = args['product_name'], 
                                    price = args['price'],
                                    asin = args['asin'], 
                                    product_link = args['product_link'],
                                    number_available = args['number_available'],
                                    description = args['product_description'],
                                    number_shipped = args['number_available'],
                                    product_image = image_url,
                                    store_id =  user.store.id
                                    )
                db.session.add(new_product)
                db.session.commit()
                return {"message":"succesful"},201 
            
                
                # with open("/static/store_image/"+pic_name+".jpg", "wb") as file:
                # with open("static/product_image/"+pic_name, "wb") as file:
                #     file.write(photo_data)
                # f.save(os.path.join('/static/store_image', pic_name))
                
                
            except Exception as e:
                print(e)
                app.logger.info(e)
                abort(500, message = 'Error  while saving image')


class ViewProductDetail(Resource):
    def get(self, product_id):
        product = Product.query.get_or_404(product_id)
        if not product:
            abort(404, message='Product doesnt exists')
        return  product.json() , 200

class UpdateUser(Resource):
    #Declare the varriables to be passed as the post body
    updateparser = reqparse.RequestParser()                      
    updateparser.add_argument('email', type=str, required=False, help='user mail required')    
    # updateparser.add_argument('password', type=str, required=False, help='password required')    
    updateparser.add_argument('first_name', type=str, required=False, help='user first name required')  
    updateparser.add_argument('last_name', type=str, required=False, help='user last name required')  
    updateparser.add_argument('mailing_address', type=str, required=False, help='mailing address required')  
    updateparser.add_argument('city', type=str, required=False, help='user city required')  
    updateparser.add_argument('state', type=str, required=False, help='user state required')  
    updateparser.add_argument('zip', type=str, required=False, help='user zip required')  
    updateparser.add_argument('mailing_phone_number', type=str, required=False, help='user mailing phone number required') 
    @jwt_required()  
    def post(self):
        args = UpdateUser.updateparser.parse_args()
        name_to_update = get_current_user()
        if not name_to_update:
            abort(404,message="User id not found")
        if args['email']:
            name_to_update.email = args['email']
        if args['last_name']:
            name_to_update.last_name = args['last_name']
        if  args['first_name']:
            name_to_update.first_name = args['first_name']
        if  args['mailing_address']:
            name_to_update.mailing_address = args['mailing_address']
        if args['city']:  
            name_to_update.city = args['city']
        if args['state']:
            name_to_update.state = args['state']
        if args['zip']:
            name_to_update.zip_ = args['zip']
        if  args['mailing_phone_number']:
            name_to_update.mailing_phone_number = args['mailing_phone_number']
        db.session.commit()
        return name_to_update.json(), 201 


class Login(Resource):
    #Declare the varriables to be passed as the post body
    parser = reqparse.RequestParser()                      
    parser.add_argument('email', type=str, required=True, help='user mail required')    
    parser.add_argument('password', type=str, required=True, help='password required') 
    def post(self):
        args = Login.parser.parse_args()
        email = args['email']
        password = args['password']
        print(email)
        print(password)
        user = User.query.filter_by(email = email).first()
        
        if user:

            if check_password_hash(user.password, password):
                print(user.first_name)
                #access_token = create_access_token(identity=json.dumps(user, cls=AlchemyEncoder))
                access_token = create_access_token(identity=user.email)
                return jsonify(access_token=access_token)
            else:
                abort(401, message = 'Email or Password incorrect')
        else:
            abort(401, message = 'No user associated with this mail')
    
    
    @jwt_required()  
    def get(self):
        user = get_current_user()
       
        return user.json()


def abort_if_email_exists(email):
    email_value = User.query.filter_by(email= email).first()  
    if email_value:
        abort(409,message="Email already exist")
        
class SignUp(Resource):
    #Declare the varriables to be passed as the post body
    parser = reqparse.RequestParser()                      
    parser.add_argument('email', type=str, required=True, help='user mail required')    
    parser.add_argument('password', type=str, required=True, help='password required')    
    parser.add_argument('first_name', type=str, required=True, help='user first name required')  
    parser.add_argument('last_name', type=str, required=True, help='user last name required')  
    parser.add_argument('mailing_address', type=str, required=True, help='mailing address required')  
    parser.add_argument('city', type=str, required=True, help='user city required')  
    parser.add_argument('state', type=str, required=True, help='user state required')  
    parser.add_argument('zip', type=str, required=True, help='user zip required')  
    parser.add_argument('mailing_phone_number', type=str, required=True, help='user mailing phone number required') 
    
    
    
    def post(self):
        args = SignUp.parser.parse_args()
        abort_if_email_exists(args['email'])
        new_user = User(email = args['email'],
                        password = generate_password_hash(args['password'], method='sha256'),
                        first_name = args['first_name'] , 
                        last_name = args['last_name'],
                        mailing_address = args['mailing_address'] ,
                        city= args['city'] ,
                        state = args['state'] ,
                        zip_ = args['zip'] ,
                        mailing_phone_number=args['mailing_phone_number'])
        db.session.add(new_user)        
        db.session.commit()
        return {'message':"succes"} , 201 
     
class Home(Resource):
    def get(self):
        return {'hey':'world'}

class AddToCart(Resource):
    #Declare the varriables to be passed as the post body
    parser = reqparse.RequestParser()                      
    parser.add_argument('product_id', type=str, required=True, help='Product Id required')    
    @jwt_required()
    def post(self):
        args = AddToCart.parser.parse_args()
        product_id = args['product_id']
        user = get_current_user()
        product = Product.query.get(product_id)
        if not product:
            abort(404, message = 'No product associated with this id')
        orders = user.orders
        u_order = get_Order_object( orders = orders, product = product,user = user )
        add_orderItem( order=u_order, product_id=product_id )
        return {"message":"succesful"}, 200
    
class AddToFav(Resource):
    #Declare the varriables to be passed as the post body
    parser = reqparse.RequestParser()                      
    parser.add_argument('product_id', type=str, required=True, help='Product Id required')  

    @jwt_required()
    def post(self):
        args = AddToFav.parser.parse_args()
        product_id = args['product_id']
        user = get_current_user()
        print(user.last_name)
        # return {"hey":"works"},200
        product = Product.query.get(product_id)
        if not product:
            abort(404, message = 'No product associated with this id')
        user.favoutite_products.append(product)
        db.session.commit()
        return {"message":"succesful"},200

class ViewProductsByStore(Resource):
    def get(self,store_id):
        store = Store.query.get(store_id)
        if not store:
            abort(404, message='store doesnt exists')
        prod = store.products.order_by(Product.date_added.desc()).all()
        return {'Products': list(map(lambda x: x.json(),prod))}  

class ViewUserCart(Resource):
    @jwt_required()
    def get(self):
        user = get_current_user()
        cart = {'Cart' : []}
        for order in user.orders:
            if int(order.status) == 0:
                store = Store.query.get(order.store_id)
                storeitem = {'store_id': store.id, 
                            'store_name': store.store_name, 
                            'store_description': store.store_description, 
                            'image': store.store_icon,
                            'orderItem':[]}  
                for orderItem in order.order_item:  
                    product = Product.query.get(orderItem.product_id)
                    orderP = {'id': orderItem.id,
                            'order_id': orderItem.order_id, 
                            'quantity': int(orderItem.quantity),
                            'product':product.json()}  
                    storeitem['orderItem'].append(orderP)
                if len(storeitem['orderItem'])!=0:
                    cart['Cart'].append(storeitem)
        return cart, 200
        

class ViewStoreDetail(Resource):
    '''api to view store detail'''
    def get(self, store_id):
        store = Store.query.get(store_id)
        if not store:
            abort(404, message = 'Store with id not found')
        return store.json(), 200
            
class RemoveItemShoppingCart(Resource):
    #Declare the varriables to be passed as the post body
    parser = reqparse.RequestParser()                      
    parser.add_argument('order_item_id', type=str, required=True, help='order item Id required')    
    @jwt_required()
    def post(self):
        user = get_current_user()
        args = RemoveItemShoppingCart.parser.parse_args()
        order_item_id = args['order_item_id']
        order_item = OrderItem.query.get(order_item_id)
        if not order_item:
            abort(404, message = 'This order item with id doesnt exist')
        order = order_item.order
        print(order.id)
        if not order:
            abort(404, message = 'This order not associted with this order item')
        
        if  int(order.user_id)!=int(user.id):
            abort(401, message = "User has no permission to remove item ")
        if  int(order.status)!=0:
                abort(401, message = "Order doesnt have right status or is not actually in cart")
        try:
           
            db.session.delete(order_item)
            db.session.commit()
           
            return {"message": "removal succes"} , 200
        except Exception as e:
            app.logger.info(e)
            abort(500, message = "Something went awfully wrong probably order id doesnt exist")
                           
class checkOutCart(Resource):
    '''
    This checks out all the items from a particular store
    '''
    #Declare the varriables to be passed as the post body
    parser = reqparse.RequestParser()                      
    parser.add_argument('order_id', type=str, required=True, help='order Id required')    
    @jwt_required()
    def post(self):
        user = get_current_user()
        args = checkOutCart.parser.parse_args()
        order_id = args['order_id']
        order =  Order.query.get(order_id)
        if not order:
            abort(404, message = "Order Item doesnt exist")
        if order.status!=0:
            abort(405, message = "This isn't a cart item and can be checked out")
        order.status = 1
        db.session.commit()
        return {'message':"succes"}, 200

class getWishListItems(Resource):
    @jwt_required()
    def get(self):
        user = get_current_user()
        fav_products = {'favProducts' : []}
        for prod in user.favoutite_products:
            fav_products['favProducts'].append(prod.json())
        return fav_products, 200
            
class getOrderListReteailer(Resource):
    @jwt_required()
    def get(self):
        user = get_current_user()
        store = user.store
        if not store:
             abort(404, message = "User doesn't own a store")
        ordersList = {'Orders' : []}
        for order in store.orders:
            if int(order.status) != 0:  
                order_cache = {'order_id': order.id, 
                                'date_created': str(order.date_created),  
                                'date_due': str(order.date_due),
                                'status':int(order.status),
                                'orderItems':[]}  
                for orderItem in order.order_item:  
                    product = Product.query.get(orderItem.product_id)
                    orderP = {'id': orderItem.id,
                            'order_id': orderItem.order_id, 
                            'quantity': int(orderItem.quantity),
                            'product':product.json()}  
                    order_cache['orderItems'].append(orderP)
                
                ordersList['Orders'].append(order_cache)
            
        return ordersList, 200
    
class convertOrderToPending(Resource):
    '''
    This route enable retailers to turn a pending order to shipped
    '''
    #Declare the varriables to be passed as the post body
    parser = reqparse.RequestParser()                      
    parser.add_argument('order_id', type=str, required=True, help='order Id required')
    @jwt_required()
    def post(self):
        user = get_current_user()
        args = convertOrderToPending.parser.parse_args()
        order_id = args['order_id']
        order = Order.query.get(order_id)
        if int(order.store_id)!=int(user.store.id): #if order belongs to retailer he has/she has permsion
             abort(401, message = "User not authorised to change status")
        if int(order.status)!=1:
            abort(401, message = "You can only change a pending order")
        
        order.status = 2 #order status of 2 means 2
        db.session.commit()
        return {'message':"succes"}, 200
        
class getAllStores(Resource):
    '''
    Returns all the stores available from the data base possible sorting 
    algorithms implemented later for priority
    '''
    def get(self):
        stores = Store.query.all()
        storeOut = {"Stores": []}
        for store in stores :
            storeOut["Stores"].append(store.json())
        return storeOut, 200

class removeFromWishList(Resource):
    parser = reqparse.RequestParser()                      
    parser.add_argument('product_id', type=str, required=True, help='product  item Id required')  
    @jwt_required()
    def post(self):
        user = get_current_user()
        args = removeFromWishList.parser.parse_args()
        product_id = args['product_id']
        product = Product.query.get(product_id)
        if not product:
            abort(404, message = 'No product associated with this id')
        user.favoutite_products.remove(product)
        db.session.commit()
        return {"message":"succesful"},200
        
        

        
        
    
        
# jwt = JWT(app, authenticate, identity)  # Auto Creates /auth endpoint
@jwt.user_lookup_loader
def user_lookup_callback(jwt_header, jwt_payload):
    if jwt_header:
        email = jwt_payload["sub"]
        user = user = User.query.filter_by(email = email).first()
        return user
    else:
        # return None / null
        return None

api.add_resource(Home, '/')
api.add_resource(SignUp, '/signup')
api.add_resource(Login, '/login')
api.add_resource(SignUpRetailer, '/sign-up-retailer')
api.add_resource(UpdateUser, '/update-user')


api.add_resource(AddProduct, '/add-product')
api.add_resource(ViewProductDetail, '/view-product-detail/<int:product_id>')
api.add_resource(ViewProductsByStore, '/view-store-products/<int:store_id>')
api.add_resource(ViewStoreDetail, '/view-store-details/<int:store_id>')
api.add_resource(getOrderListReteailer, '/get-store-orders')
api.add_resource(convertOrderToPending, '/ship-orders')
api.add_resource(getAllStores, '/get-stores')


api.add_resource(AddToCart, '/add-product-cart')
api.add_resource(AddToFav, '/add-product-fav')
api.add_resource(ViewUserCart, '/view-user-cart')
api.add_resource(RemoveItemShoppingCart, '/remove-item-cart')
api.add_resource(checkOutCart, '/check-out-cart')
api.add_resource(getWishListItems, '/get-fav-products')
api.add_resource(removeFromWishList, '/remove-fav-products')


if __name__=='__main__':        
    #Run the applications
    app.run(debug=True) 
    
          
    
