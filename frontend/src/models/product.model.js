export class Product {
    constructor(product) {
        this.id = product.id;
        this.product_name = product.product_name;
        this.price = new Number(product.price).toFixed(2);
        this.asin = product.asin;
        this.product_link = product.product_link;
        this.number_available = product.number_available;
        this.number_shipped = product.number_shipped;
        this.description = product.description;
        this.date_added = product.date_added;
        this.image = product.image;
    }

    get name() {
        return this.product_name;
    }
}