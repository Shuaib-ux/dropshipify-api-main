<template>
  <div class="container px-6 mx-auto grid">
    <div class="my-8 text-center space-y-2">
      <h2 class="text-4xl font-semibold text-gray-700 dark:text-gray-200">
        Welcome to Dropshipify
      </h2>
      <h4 class="text-xl text-gray-700 dark:text-gray-200">
        Explore available stores
      </h4>
    </div>
    <div class="grid lg:grid-cols-4 xl:grid-cols-5 gap-4 p-6 bg-white rounded-lg shadow-xs dark:bg-gray-800">
      <StoreTile v-for="store in stores" :key="store.id" :store="store" />
    </div>
  </div>
</template>

<script>
import StoreTile from "@/components/StoreTile.vue";
export default {
  name: "Stores",
  components: { StoreTile },
  async mounted() {
    // Fetches all stores information from API
    await this.$store.dispatch("storeModule/getAllStores");
  },
  data() {
    return {
      user: this.$store.state.authModule.user,
    };
  },
  computed: {
    stores() {
      return this.$store.state.storeModule.stores;
    },
  },
};
</script>
