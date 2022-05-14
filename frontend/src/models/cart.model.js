import { Product } from "./product.model";

export class Cart {
    constructor(cart) {
        this.store_id = cart.store_id;
        this.store_name = cart.store_name;
        this.store_description = cart.store_description;
        this.image = cart.image;
        this.orderItem = cart.orderItem.map((item) => new OrderItem(item));
    }

    get totalPrice() {
        return this.orderItem.reduce((total, item) => {
            return total + (item.product.price * item.quantity)
        }, 0)
    }

    get orderId() {
        return this.orderItem[0].order_id
    }
}

export class OrderItem {
    constructor(item) {
        this.id = item.id;
        this.order_id = item.order_id;
        this.quantity = item.quantity;
        this.product = new Product(item.product);
    }
}