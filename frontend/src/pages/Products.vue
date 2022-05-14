<template>
  <div class="container px-6 pb-10 mx-auto grid h-full">
    <h2 class="my-6 text-2xl font-semibold text-gray-700 dark:text-gray-200">
      Products
    </h2>
    <div class="grid lg:grid-cols-7 gap-x-6 h-full">
      <div
        class="
          lg:col-span-4
          grid grid-cols-2
          xl:grid-cols-3
          gap-4
          h-9.5/10
          overflow-y-auto
        "
      >
        <Product
          v-for="product in products"
          :key="product.id"
          :product="product"
          :retailer="true"
        />
      </div>
      <div
        class="lg:col-span-3 p-6 bg-white rounded-lg shadow-xs dark:bg-gray-800"
      >
        <h2 class="text-lg font-semibold text-gray-700 dark:text-gray-200">
          Add Product
        </h2>
        <form class="mt-4" @submit.prevent="createProduct()">
          <Input
            v-model="product_name"
            :title="'Name'"
            :required="true"
            :placeholder="'eg. Apple MacBook Pro'"
          />
          <Input
            v-model="price"
            :title="'Price (£)'"
            :type="'number'"
            :step="'.01'"
            :required="true"
            :placeholder="'eg. 5000'"
          />
          <Input
            v-model="product_description"
            :title="'Description'"
            :type="'textarea'"
            :required="true"
            :placeholder="'eg. This is a revolutionary product. First to every do it.'"
          />
          <Input
            v-model="product_link"
            :title="'Amazon Product Link'"
            :type="'url'"
            @blur="searchForAmazonProduct()"
            :placeholder="'eg. https://amazon.com/apple-mac-book'"
          />
          <Input
            :title="'Image' + ' - ' + file_name"
            :type="'file'"
            @change="selectImage($event)"
          />
          <div class="grid grid-cols-2 gap-x-6 mb-2">
            <Input
              v-model="number_available"
              :title="'Quantity Available'"
              :type="'number'"
              :required="true"
              :placeholder="'eg. 50'"
            />
            <Input v-model="asin" :title="'ASIN'" :placeholder="'eg. MXY-43'" />
          </div>
          <Button>Create</Button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import Button from "@/components/Button.vue";
import Product from "@/components/Product.vue";
import Input from "@/components/Input.vue";
import { notificationService } from "../services/notification.service";
import { amazonService } from "../services/amazon.service";
import { AuthService } from '../services/auth.service';

const authService = new AuthService()
const storeId = authService.getUser().store_id

export default {
  name: "Products",
  components: { Button, Product, Input },
  async mounted() {
    await this.$store.dispatch("storeModule/getProducts", storeId);
  },
  data() {
    return {
      product_name: "",
      image: "",
      product_description: "",
      price: "",
      product_link: "",
      number_available: "",
      asin: "",
      file_name: "",
    };
  },
  methods: {
    selectImage(event) {
      const image = event.target.files[0];
      const reader = new FileReader();
      reader.onload = (fileLoadedEvent) => {
        const base64 = fileLoadedEvent.target.result;
        this.image = base64.split("base64,")[1];
      };
      reader.readAsDataURL(image);
    },
    async createProduct() {
      if (this.image) {
        await this.$store
          .dispatch("storeModule/addProduct", {
            product: {
              product_name: this.product_name,
              image: this.image,
              product_description: this.product_description,
              price: this.price,
              product_link: this.product_link,
              number_available: this.number_available,
              asin: this.asin,
            },
            storeId: storeId,
          })
          .then(() => {
            this.clearForm();
            notificationService.success("Product created successfully");
          });
      } else {
        notificationService.error("Please upload a product image");
      }
    },
    clearForm() {
      this.product_name = "";
      this.file_name = "";
      this.image = "";
      this.product_description = "";
      this.price = "";
      this.product_link = "";
      this.number_available = "";
      this.asin = "";
    },
    async searchForAmazonProduct() {
      const asin = this.product_link.split("/dp/")[1].slice(0, 10);
      const response = await amazonService.get("product/", {
        params: { country: "UK", asin: asin, topReviews: "false" },
      });
      const amazonProduct = response.data;
      this.file_name = amazonProduct.title.slice(0, 15);
      this.product_name = amazonProduct.title;
      this.product_description = amazonProduct.description;
      this.price = amazonProduct.prices.current_price;
      this.image = amazonProduct.images[0];
      this.asin = amazonProduct.asin;
    },
  },
  computed: {
    products() {
      return this.$store.state.storeModule.products;
    },
  },
};
</script>
