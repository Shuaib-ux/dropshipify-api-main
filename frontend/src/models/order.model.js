import { OrderItem } from "./cart.model";

export class Order {
    constructor(cart) {
        this.order_id = cart.order_id;
        this.date_created = new Date(cart.date_created);
        this.status = cart.status;
        this.orderItems = cart.orderItems.map((item) => new OrderItem(item));
    }

    get orderStatus() {
        switch (this.status) {
            case 0:
                return 'Not Ordered'
            case 1:
                return 'Pending'
            case 2:
                return 'Confirmed and Shipped'
            default:
                return 'Pending'
        }
    }

    get date() {
        return this.date_created.toDateString();
    }

    get productsOrdered() {
        return this.orderItems.reduce((total, item) => {
            return total + item.quantity
        }, 0)
    }

    get totalPrice() {
        return this.orderItems.reduce((total, item) => {
            return total + (item.product.price * item.quantity)
        }, 0)
    }
}