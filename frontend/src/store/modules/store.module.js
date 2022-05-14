import { Cart } from "../../models/cart.model";
import { Store } from "../../models/store.model";
import { Product } from "../../models/product.model";
import { httpService } from "../../services/http.service";
import { Order } from "../../models/order.model";


const state = {
    store: null,
    stores: [],
    carts: [],
    orders: [],
    products: [],
    wishlist: []
};

const actions = {
    async getAllStores({ commit }) {
        const response = await httpService.get(`get-stores`);
        commit('setStores', response.data.Stores)
    },
    async getStore({ commit }, storeId) {
        commit('emptyStore')
        const response = await httpService.get(`view-store-details/${storeId}`);
        commit('setStore', response.data)
    },
    async getProducts({ commit }, storeId) {
        // commit('emptyStore')
        const response = await httpService.get(`view-store-products/${storeId}`);
        commit('setProducts', response.data.Products)
    },
    async getStoreOrders({ commit }) {
        const response = await httpService.get(`get-store-orders`);
        commit('setOrders', response.data.Orders)
    },
    async getCart({ commit }) {
        const response = await httpService.get(`view-user-cart`);
        commit('setCarts', response.data.Cart)
    },
    async getWishList({ commit }) {
        const response = await httpService.get(`get-fav-products`);
        commit('setWishList', response.data.favProducts)
    },
    async addProduct({ dispatch }, data) {
        await httpService.post(`add-product`, data.product);
        dispatch('getProducts', data.storeId)
    },
    async addToCart(context, productId) {
        await httpService.post(`add-product-cart`, { product_id: productId });
        context.dispatch('getCart')
    },
    async addToWishList(context, productId) {
        await httpService.post(`add-product-fav`, { product_id: productId });
        context.dispatch('getWishList')
    },
    async removeFromCart(context, itemId) {
        await httpService.post(`remove-item-cart`, { order_item_id: itemId });
        context.dispatch('getCart')
    },
    async removeFromWishList(context, productId) {
        await httpService.post(`remove-fav-products`, { product_id: productId });
        context.dispatch('getWishList')
    },
    async shipOrder(context, orderId) {
        await httpService.post(`ship-orders`, { order_id: orderId });
        context.dispatch('getStoreOrders')
    },
    async checkout(context, orderId) {
        await httpService.post(`check-out-cart`, { order_id: orderId });
        context.dispatch('getCart')
    },
};

const mutations = {
    setStores(state, stores) {
        state.stores = stores.map((store) => new Store(store));
    },
    setProducts(state, products) {
        state.products = products.map((product) => new Product(product));
    },
    emptyStore(state) {
        state.store = null;
        state.products = [];
    },
    setCarts(state, carts) {
        state.carts = carts.map((cart) => new Cart(cart));
    },
    setWishList(state, wishlist) {
        state.wishlist = wishlist.map((product) => new Product(product));
    },
    setStore(state, store) {
        state.store = new Store(store)
    },
    setOrders(state, orders) {
        state.orders = orders.map((order) => new Order(order));
    },
};

export default { state, mutations, actions, namespaced: true };