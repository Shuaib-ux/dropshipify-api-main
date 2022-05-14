<template>
  <div class="container px-6 mx-auto grid" v-if="store">
    <div class="my-6 text-center">
      <h2 class="text-4xl font-semibold text-gray-700 dark:text-gray-200">
        {{ store.store_name }}
      </h2>
      <h4 class="text-xl text-gray-700 dark:text-gray-200">
        {{ store.store_description }}
      </h4>
    </div>
    <div class="mb-10 text-center">
      <h4 class="text-sm">View Catalogue</h4>
      <h2 class="my-1 text-3xl font-semibold text-gray-700 dark:text-gray-200">
        Our Products
      </h2>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 xl:grid-cols-5 gap-4 p-6 bg-white rounded-lg shadow-xs dark:bg-gray-800">
      <Product
        v-for="product in products"
        :key="product.id"
        :product="product"
      />
    </div>
    <div v-if="!loading && products.length < 1">
      <h4 class="text-sm text-center bg-white p-6 rounded-lg">
        There are no products available at the moment
      </h4>
    </div>
  </div>
</template>

<script>
import Product from "../components/Product.vue";
export default {
  name: "Store",
  components: { Product },
  async mounted() {
    // Fetches store information from API
    await this.$store
      .dispatch("storeModule/getStore", this.$route.params.id)
      .catch(() => this.$router.push({ name: "Error;* Page does not exist" }));

    // Fetches store products from API
    await this.$store
      .dispatch("storeModule/getProducts", this.$route.params.id)
      .catch(() => this.$router.push({ name: "Error;* Page does not exist" }));

    // Updates Page title to store name and description
    document.title = `${this.store.store_name} • ${this.store.store_description}`;
  },
  data() {
    return {
      user: this.$store.state.authModule.user,
    };
  },
  computed: {
    store() {
      return this.$store.state.storeModule.store;
    },
    products() {
      return this.$store.state.storeModule.products;
    },
    loading() {
      return this.$store.state.loadingModule.loading;
    },
  },
};
</script>
