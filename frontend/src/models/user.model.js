export class User {
    constructor(user) {
        this.id = user.id;
        this.email = user.email;
        this.first_name = user.first_name;
        this.last_name = user.last_name;
        this.mailing_address = user.mailing_address;
        this.mailing_phone_number = user.mailing_phone_number;
        this.city = user.city;
        this.state = user.state;
        this.zip = user.zip;
        this.store_id = user.store_id;
        this.is_retailer = user.is_retailer;
    }
}