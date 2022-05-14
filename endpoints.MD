# THis contains the endpoints and their body and url

## 1 Login
```
https://flask-dropshipfy-api.herokuapp.com/login
```
### 1.A Post

#### body :
```
{
    "email": "admin@gmail.com",
    "password": "elysium8"
}
```
#### Response
```
 {
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY0OTk1MDg2MSwianRpIjoiYmM5MmVjZGItY2Y0NC00MTJiLWFiNjUtNzdjNzNmMmQ2MTU5IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImFsZXhAZ21haWwuY29tIiwibmJmIjoxNjQ5OTUwODYxLCJleHAiOjE2NDk5NTE3NjF9.FxThYQIJlx9DyPbsTzWo7r5gUe-5iZ695Dco5_eugHM"
}
```
### 1.B Get
```
https://flask-dropshipfy-api.herokuapp.com/login

headers={"Authorization": "Bearer "+ access_token}
```
#### body:
```
{
    "id": 1,
    "email": "admin@gmail.com",
    "first_name": "Admin",
    "last_name": "admin",
    "is_retailer": false,
    "mailing_address": "14 Denbigh,Chester,United Kingdom",
    "city": "Chester",
    "state": "Chester",
    "zip": "23424",
    "store_id": null,
    "mailing_phone_number": "+000000000"
}
```

## 2 Sign Up
```
https://flask-dropshipfy-api.herokuapp.com/signup
```
### body:

```
{
    "email":"admin@gmail.com",
    "password":"elysium8",
    "first_name":"Admin", 
    "last_name":"admin",
    "mailing_address":"14 Denbigh,Chester,United Kingdom",                                          
    "city":"Chester",
    "state" : "Chester", 
    "zip":"23424",
    "mailing_phone_number":"+000000000"
}
```
## 3 Sign Up as Retailer and Create store
```
https://flask-dropshipfy-api.herokuapp.com/sign-up-retailer
```

### body:

```
{
    "store_name": "Rag and Bones",
    "image": "image as base64 string",
    "store_description": "Sharpest market"
}
```
## 4 View store details

### Get request 
no Header Authentication required
```
https://flask-dropshipfy-api.herokuapp.com/view-store-details/<int:store_id>
```
### Response
```
{
    "id": 1,
    "store_name": "Rag and Bones ",
    "store_description": "Sharpest on the market",
    "user_id": 2,
    "image": "https://res.cloudinary.com/dropshipify/image/upload/v1649952772/pptqfhg5k8fi7tjnohzj.jpg"
}
```
## 5 Get Products by store id
```
https://flask-dropshipfy-api.herokuapp.com/view-store-products/<int:store_id>
```
### Response
```
{'Products': [
    {'id': 3, 'product_name': 'Ahoka Dior', 'price': '90.0000000000', 'ansii': '2348n3', 'product_link': 'https:r4rr4', 'number_available': 977, 'number_shipped': 977, 'description': 'premium ashoka bag to store you beatiful hand for mrraige', 'date_added': '2022-04-04 22:04:14.906626'}, 
    {'id': 2, 'product_name': 'Ahoka Dior', 'price': '90.0000000000', 'ansii': '2348n3', 'product_link': 'https:r4rr4', 'number_available': 977, 'number_shipped': 977, 'description': 'premium ashoka bag to store you beatiful hand for mrraige', 'date_added': '2022-04-04 21:59:14.859265'}, 
    {'id': 1, 'product_name': 'Blue Dior', 'price': '23.3000000000', 'ansii': '2343', 'product_link': 'https:r4rr4', 'number_available': 63, 'number_shipped': 63, 'description': 'Bad man looking good in dior', 'date_added': '2022-04-04 20:55:28.656010'}]}
```

## 6 Add product by store owner header auth
```
https://flask-dropshipfy-api.herokuapp.com/add-product
```
authentication header required for user/ store owner
### body
```
{
    "product_name": "Desktop tv",
    "image":"https://m.media-amazon.com/images/I/91fAU6mxFsL.jpg" or base64 link,
    "product_description": "Desktop tv for tabular",
    "price": "90",
    "product_link": "https:r4rr4",
    "number_available": 977,
    "asin": "2348n3"
}
```
## 7 View product detail by id
```
https://flask-dropshipfy-api.herokuapp.com/view-product-detail/<int:product_id>
```



## 8 ADD product to cart
```
https://flask-dropshipfy-api.herokuapp.com/add-product-cart
```
### body
```
{"product_id":"1"})
```

## 9 ADD product to User Fav or wish list
```
https://flask-dropshipfy-api.herokuapp.com/add-product-fav
```
### body
```
{"product_id":"1"})
```


 ## 10 View user Cart
 Header authentication required
 ## Get request
```
https://flask-dropshipfy-api.herokuapp.com/view-user-cart
```
### Responce Sample
```
{'Cart': [
    {'store_id': 1, 'store_name': 'Soul Dwellers', 'store_description': 'Premium looking bags for top achievers', 'image': '780854cc-b443-11ec-8e19-a683e764bbf9_babe.png', 'orderItem': [
        {'id': 1, 'order_id': 1, 'quantity': 1, 'product': 
        {'id': 3, 'product_name': 'Ahoka Dior', 'price': '90.0000000000', 'ansii': '2348n3', 'product_link': 'https:r4rr4', 'number_available': 977, 'number_shipped': 977, 'description': 'premium ashoka bag to store you beatiful hand for mrraige', 'date_added': '2022-04-04 22:04:14.906626', 'image': 'image base64'}}, 
        {'id': 2, 'order_id': 1, 'quantity': 1, 'product': 
        {'id': 2, 'product_name': 'Ahoka Dior', 'price': '90.0000000000', 'ansii': '2348n3', 'product_link': 'https:r4rr4', 'number_available': 977, 'number_shipped': 977, 'description': 'premium ashoka bag to store you beatiful hand for mrraige', 'date_added': '2022-04-04 21:59:14.859265', 'image': 'image base64'}},
        {'id': 4, 'order_id': 1, 'quantity': 2, 'product':
        {'id': 1, 'product_name': 'Blue Dior', 'price': '23.3000000000', 'ansii': '2343', 'product_link': 'https:r4rr4', 'number_available': 63, 'number_shipped': 63, 'description': 'Bad man looking good in dior', 'date_added': '2022-04-04 20:55:28.656010', 'image': 'image base64'}}]}, 
    {'store_id': 2, 'store_name': 'ALAR', 'store_description': 'Controlled quality content to kidnap seals', 'image': 'c553ecde-b66c-11ec-9c29-acde48001122_AlAR_pic.png', 'orderItem': [
        {'id': 5, 'order_id': 2, 'quantity': 2, 'product': 
        {'id': 6, 'product_name': 'Sily Socks', 'price': '12.0000000000', 'ansii': '2348324n3', 'product_link': 'https:r4rr4', 'number_available': 3, 'number_shipped': 3, 'description': 'Crispy socks for dark nights', 'date_added': '2022-04-07 13:24:12.147564', 'image': 'image base64'}}]}]}
```

 ## 11 Remove item entirely from cart
 ```
 https://flask-dropshipfy-api.herokuapp.com/remove-item-cart
 ```

 ### Post request
Authorisation Header require

 ### body
```
{"order_item_id":"1"})
```
Element must belong to user 

## 12 Check out order from cart belonging to store by changing the status

```
 https://flask-dropshipfy-api.herokuapp.com/check-out-cart
```

### Body
```
{"order_id":"1"})
```

## 13 Get favourite products of user
```
 https://flask-dropshipfy-api.herokuapp.com/get-fav-products/
```


## 14 Get store current order list
status 1 means pending awaiting order by store owner
and 2 means confirmed and shipped
### get request
```
 https://flask-dropshipfy-api.herokuapp.com/get-store-orders
```

### Body

```
{'Orders': 
    [ {'order_id': 1, 'date_created': '2022-04-07 13:01:44.847284', 'date_due': 'None', 'status': 1, 'orderItems': 
        [
            {'id': 2, 'order_id': 1, 'quantity': 1, 'product': 
                {'id': 2, 'product_name': 'Ahoka Dior', 'price': '90.0000000000', 'ansii': '2348n3', 'product_link': 'https:r4rr4', 'number_available': 977, 'number_shipped': 977, 'description': 'premium ashoka bag to store you beatiful hand for mrraige', 'date_added': '2022-04-04 21:59:14.859265', 'image': 'static/product_image/15d820ea-b45a-11ec-9216-a683e764bbf9_Ahoka.png'}
            }
        ]
    }
    ]
}
```


## 15 Change status from pending to shipped

```
 https://flask-dropshipfy-api.herokuapp.com/ship-orders
```

### Body
```
{"order_id":"1"})
```
## 16 update user profile
```
 https://flask-dropshipfy-api.herokuapp.com/update-user
```
### Body post
```
{
                    "email": "admin@gmail.com",
                    "first_name": "Admin",
                    "last_name": "admin",
                    "mailing_address": "Northwest England",
                    "city": "Uk",
                    "state": "Uk",
                    "zip": "100242",
                    "mailing_phone_number": "35356757",
},
```

## 17 Get all availavle stores

```
 https://flask-dropshipfy-api.herokuapp.com/get-stores
```
### Body responce example
```
{
    'Stores': [
        {'id': 1, 'store_name': 'Soul Dwellers', 'store_description': 'Premium looking bags for top achievers', 'user_id': 1, 'image': 'static/store_image/780854cc-b443-11ec-8e19-a683e764bbf9_babe.png'},

        {'id': 2, 'store_name': 'ALAR', 'store_description': 'Controlled quality content to kidnap seals', 'user_id': 3, 'image': 'static/store_image/c553ecde-b66c-11ec-9c29-acde48001122_AlAR_pic.png'},

        {'id': 3, 'store_name': 'Life', 'store_description': 'We sell life and jones mainly', 'user_id': 4, 'image': 'static/store_image/44bddd84-bae8-11ec-b812-acde48001122_life_main.png'}, 

        {'id': 4, 'store_name': 'baron stores', 'store_description': 'We sell life and jones inly', 'user_id': 6, 'image': 'static/store_image/18c2f8de-baef-11ec-9907-acde48001122_life_main.png'}, 
        {'id': 5, 'store_name': 'Bass drum drum', 'store_description': 'We sell the best drums for parties', 'user_id': 5, 'image': 'static/store_image/eed5ae94-baef-11ec-a983-acde48001122_life_main_x.png'}
    ]
}
```

## 18 Remove item from wish list

```
 https://flask-dropshipfy-api.herokuapp.com/remove-fav-products
```
### Body
```
{   
    "product_id":"1"
}
```