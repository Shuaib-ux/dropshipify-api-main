<template>
  <div
    class="
      relative
      bg-white
      hover:shadow-md
      rounded-xl
      max-h-80
      border border-gray-200
      p-2
    "
  >
    <div class="overflow-x-hidden rounded-lg relative mb-6">
      <img
        class="rounded-lg object-cover"
        :class="[quantity ? 'h-32 w-52' : 'h-52 w-full']"
        :src="product.image"
      />
      <div
        v-if="!retailer && !quantity && !wishListItem"
        @click="addToWishList()"
        class="
          absolute
          right-2
          top-2
          bg-white
          rounded-full
          p-2
          cursor-pointer
          group
        "
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-6 w-6 group-hover:opacity-70"
          :fill="isProductInWishList ? '#7C3AED' : 'none'"
          viewBox="0 0 24 24"
          :stroke="isProductInWishList ? '#7C3AED' : 'gray'"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"
          />
        </svg>
      </div>
      <div
        v-if="!retailer && wishListItem"
        @click="removeFromWishList()"
        class="
          absolute
          right-2
          top-2
          bg-white
          rounded-full
          p-2
          cursor-pointer
          group
        "
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          aria-hidden="true"
          role="img"
          class="h-6 w-6 group-hover:opacity-70"
          preserveAspectRatio="xMidYMid meet"
          viewBox="0 0 24 24"
        >
          <path
            fill="currentColor"
            d="M7 4V2h10v2h5v2h-2v15a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V6H2V4h5zM6 6v14h12V6H6zm3 3h2v8H9V9zm4 0h2v8h-2V9z"
          />
        </svg>
      </div>
      <div
        v-if="!retailer && orderItemId"
        @click="removeFromCart()"
        class="
          absolute
          right-2
          top-2
          bg-white
          rounded-full
          p-2
          cursor-pointer
          group
        "
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          aria-hidden="true"
          role="img"
          class="h-6 w-6 group-hover:opacity-70"
          preserveAspectRatio="xMidYMid meet"
          viewBox="0 0 24 24"
        >
          <path
            fill="currentColor"
            d="M7 4V2h10v2h5v2h-2v15a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V6H2V4h5zM6 6v14h12V6H6zm3 3h2v8H9V9zm4 0h2v8h-2V9z"
          />
        </svg>
      </div>
      <div
        v-if="retailer"
        @click="deleteProduct()"
        class="
          absolute
          flex
          space-x-2
          left-2
          top-2
          bg-white
          rounded-full
          p-2
          cursor-pointer
          group
        "
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          aria-hidden="true"
          role="img"
          class="h-6 w-6 group-hover:opacity-70"
          preserveAspectRatio="xMidYMid meet"
          viewBox="0 0 24 24"
        >
          <path
            fill="currentColor"
            d="M7 4V2h10v2h5v2h-2v15a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V6H2V4h5zM6 6v14h12V6H6zm3 3h2v8H9V9zm4 0h2v8h-2V9z"
          />
        </svg>
        <p>Delete</p>
      </div>
    </div>
    <div class="mt-4 pl-2 mb-4 relative flex justify-between">
      <div class="w-full">
        <p
          class="
            text-lg
            font-semibold
            text-gray-900
            mb-0
            truncate
            overflow-ellipsis
            w-full
          "
        >
          {{ product.name }}
        </p>
        <p class="text-md text-gray-800 mt-0">
          £ {{ product.price }}
          <span v-if="quantity">
            <span class="text-sm"> x{{ quantity }} </span>
            <span class="ml-3"> (£{{ quantity * product.price }}) </span>
          </span>
        </p>
      </div>
      <div
        v-if="!retailer && !quantity"
        class="
          flex flex-col-reverse
          mb-1
          mr-4
          group
          cursor-pointer
          absolute
          right-0
          top-8
        "
        @click="addToCart()"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-6 w-6 group-hover:opacity-50 opacity-70"
          fill="none"
          viewBox="0 0 24 24"
          stroke="black"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="1.5"
            d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"
          />
        </svg>
      </div>
    </div>
  </div>
</template>

<script>
import { notificationService } from "../services/notification.service";
export default {
  name: "Product",
  props: {
    product: {
      type: Object,
      required: true,
    },
    retailer: {
      type: Boolean,
      default: false,
    },
    quantity: {
      type: Number,
      required: false,
    },
    orderItemId: {
      required: false,
    },
    wishListItem: {
      default: false,
    },
  },
  async mounted() {
    await this.$store.dispatch("storeModule/getWishList");
  },
  methods: {
    addToCart() {
      this.$store
        .dispatch("storeModule/addToCart", this.product.id)
        .then(() => {
          if (this.wishListItem) {
            this.$store.dispatch("storeModule/removeFromWishList", this.product.id)
          }
          notificationService.success(
            `Added ${this.product.name} to cart successfully`
          );
        })
        .catch(() => {
          notificationService.error(
            "Please log in to add this product to your cart"
          );
        });
    },
    addToWishList() {
      this.$store
        .dispatch("storeModule/addToWishList", this.product.id)
        .then(() => {
          notificationService.success(
            `Added ${this.product.name} to wish list successfully`
          );
        })
        .catch(() => {
          notificationService.error(
            "Please log in to add this product to your wish list"
          );
        });
    },
    removeFromCart() {
      this.$store
        .dispatch("storeModule/removeFromCart", this.orderItemId)
        .then(() => {
          notificationService.success(`Product removed successfully`);
        })
        .catch((error) => {
          console.log(error.response);
        });
    },
    removeFromWishList() {
      this.$store
        .dispatch("storeModule/removeFromWishList", this.product.id)
        .then(() => {
          notificationService.success(`Product removed from wishlist successfully`);
        })
        .catch((error) => {
          console.log(error.response);
        });
    },
    deleteProduct() {
      notificationService.success('Product deleted')
    },
  },
  computed: {
    isProductInWishList() {
      return !!this.$store.state.storeModule.wishlist.find((product) => product.id === this.product.id)
    }
  }
};
</script>