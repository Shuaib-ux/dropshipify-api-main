<template>
  <div class="container px-6 mx-auto grid">
    <div class="flex items-center justify-center">
      <h2 class="my-6 text-2xl font-semibold text-gray-700 dark:text-gray-200">
        Cart
      </h2>
    </div>
    <div v-if="carts.length < 1">
      <div
        class="
          p-6
          bg-white
          text-center
          rounded-lg
          shadow-xs
          dark:bg-gray-800
          space-y-4
        "
      >
        <p>Your Cart is empty</p>
      </div>
    </div>
    <div v-else class="space-y-4">
      <div
        class="p-6 bg-white rounded-lg shadow-xs dark:bg-gray-800 space-y-4"
        v-for="cart in carts"
        :key="cart.store_id"
      >
        <div
          class="
            flex flex-col
            space-y-3
            md:space-y-0 md:flex-row
            items-center
            justify-between
          "
        >
          <div class="flex items-center space-x-3">
            <router-link :to="'/store/' + cart.store_id">
              <h4
                class="text-lg font-semibold text-gray-700 dark:text-gray-200"
              >
                {{ cart.store_name }}
              </h4>
            </router-link>
          </div>
          <div class="flex items-center space-x-4">
            <p>
              <span
                class="text-base font-semibold text-gray-700 dark:text-gray-200"
                >Total Cart Price:</span
              >
              £{{ cart.totalPrice }}
            </p>
            <div class="w-32">
              <Button @click="checkout(cart.orderId)">Checkout</Button>
            </div>
          </div>
        </div>
        <h4 class="text-base text-gray-700 dark:text-gray-200">
          Ordered Items
        </h4>
        <div
          class="
            grid grid-cols-2
            md:grid-cols-3
            lg:grid-cols-4
            xl:grid-cols-6
            gap-4
            pb-3
          "
        >
          <Product
            v-for="item in cart.orderItem"
            :key="item.product.id"
            :product="item.product"
            :quantity="item.quantity"
            :orderItemId="item.id"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Button from "../components/Button.vue";
import Product from "../components/Product.vue";
import { notificationService } from "../services/notification.service";
export default {
  name: "Cart",
  components: { Product, Button },
  async mounted() {
    await this.$store.dispatch("storeModule/getCart");
  },
  data() {
    return {};
  },
  methods: {
    checkout(orderId) {
      this.$store
        .dispatch("storeModule/checkout", orderId)
        .then(() => {
          notificationService.success(`Order placed successfully`);
        })
        .catch(() => {
          notificationService.error(
            "Problem placing order. Please try again later."
          );
        });
    },
  },
  computed: {
    carts() {
      return this.$store.state.storeModule.carts;
    },
  },
};
</script>
