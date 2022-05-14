<template>
  <div class="container px-6 mx-auto grid">
    <div class="flex items-center justify-center">
      <h2 class="my-6 text-2xl font-semibold text-gray-700 dark:text-gray-200">
        Wish List
      </h2>
    </div>
    <div v-if="wishlist.length < 1">
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
        <p>Your Wishlist is empty</p>
      </div>
    </div>
    <div v-else class="space-y-4">
      <div class="p-6 bg-white rounded-lg shadow-xs dark:bg-gray-800 space-y-4">
        <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 pb-3">
          <Product
            v-for="product in wishlist"
            :key="product.id"
            :product="product"
            :wishListItem="true"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Product from "../components/Product.vue";
export default {
  name: "WishList",
  components: { Product },
  async mounted() {
    await this.$store.dispatch("storeModule/getWishList");
  },
  data() {
    return {};
  },
  methods: {},
  computed: {
    wishlist() {
      return this.$store.state.storeModule.wishlist;
    },
  },
};
</script>
