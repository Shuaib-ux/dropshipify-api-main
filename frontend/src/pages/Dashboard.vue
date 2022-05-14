<template>
  <div class="container px-6 pb-10 h-full overflow-y-auto mx-auto">
    <h2 class="my-6 text-2xl font-semibold text-gray-700 dark:text-gray-200">
      Dashboard
    </h2>

    <!-- Cards -->
    <div class="grid gap-6 mb-8 md:grid-cols-2 xl:grid-cols-4">
      <!-- Card -->
      <div
        class="
          flex
          items-center
          p-4
          bg-white
          rounded-lg
          shadow-xs
          dark:bg-gray-800
        "
      >
        <div
          class="
            p-3
            mr-4
            text-orange-500
            bg-orange-100
            rounded-full
            dark:text-orange-100 dark:bg-orange-500
          "
        >
          <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
            <path
              d="M13 6a3 3 0 11-6 0 3 3 0 016 0zM18 8a2 2 0 11-4 0 2 2 0 014 0zM14 15a4 4 0 00-8 0v3h8v-3zM6 8a2 2 0 11-4 0 2 2 0 014 0zM16 18v-3a5.972 5.972 0 00-.75-2.906A3.005 3.005 0 0119 15v3h-3zM4.75 12.094A5.973 5.973 0 004 15v3H1v-3a3 3 0 013.75-2.906z"
            ></path>
          </svg>
        </div>
        <div>
          <p class="mb-2 text-sm font-medium text-gray-600 dark:text-gray-400">
            Total clients
          </p>
          <p class="text-lg font-semibold text-gray-700 dark:text-gray-200">
            {{ clients }}
          </p>
        </div>
      </div>
      <!-- Card -->
      <div
        class="
          flex
          items-center
          p-4
          bg-white
          rounded-lg
          shadow-xs
          dark:bg-gray-800
        "
      >
        <div
          class="
            p-3
            mr-4
            text-green-500
            bg-green-100
            rounded-full
            dark:text-green-100 dark:bg-green-500
          "
        >
          <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
            <path
              fill-rule="evenodd"
              d="M4 4a2 2 0 00-2 2v4a2 2 0 002 2V6h10a2 2 0 00-2-2H4zm2 6a2 2 0 012-2h8a2 2 0 012 2v4a2 2 0 01-2 2H8a2 2 0 01-2-2v-4zm6 4a2 2 0 100-4 2 2 0 000 4z"
              clip-rule="evenodd"
            ></path>
          </svg>
        </div>
        <div>
          <p class="mb-2 text-sm font-medium text-gray-600 dark:text-gray-400">
            Revenue
          </p>
          <p class="text-lg font-semibold text-gray-700 dark:text-gray-200">
            £ {{ revenue }}
          </p>
        </div>
      </div>
      <!-- Card -->
      <div
        class="
          flex
          items-center
          p-4
          bg-white
          rounded-lg
          shadow-xs
          dark:bg-gray-800
        "
      >
        <div
          class="
            p-3
            mr-4
            text-blue-500
            bg-blue-100
            rounded-full
            dark:text-blue-100 dark:bg-blue-500
          "
        >
          <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
            <path
              d="M3 1a1 1 0 000 2h1.22l.305 1.222a.997.997 0 00.01.042l1.358 5.43-.893.892C3.74 11.846 4.632 14 6.414 14H15a1 1 0 000-2H6.414l1-1H14a1 1 0 00.894-.553l3-6A1 1 0 0017 3H6.28l-.31-1.243A1 1 0 005 1H3zM16 16.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0zM6.5 18a1.5 1.5 0 100-3 1.5 1.5 0 000 3z"
            ></path>
          </svg>
        </div>
        <div>
          <p class="mb-2 text-sm font-medium text-gray-600 dark:text-gray-400">
            New sales
          </p>
          <p class="text-lg font-semibold text-gray-700 dark:text-gray-200">
            {{ newSales }}
          </p>
        </div>
      </div>
    </div>

    <!-- New Table -->
    <div class="w-full overflow-hidden overflow-y-auto rounded-lg shadow-xs">
      <h4 class="my-4 text-lg font-semibold text-gray-700 dark:text-gray-200">
        Orders
      </h4>
      <div class="w-full overflow-x-auto">
        <table class="w-full whitespace-no-wrap">
          <thead>
            <tr
              class="
                text-xs
                font-semibold
                tracking-wide
                text-left text-gray-500
                uppercase
                border-b
                dark:border-gray-700
                bg-gray-50
                dark:text-gray-400 dark:bg-gray-800
              "
            >
              <th class="px-4 py-3">Order ID</th>
              <th class="px-4 py-3">Amount</th>
              <th class="px-4 py-3">Status</th>
              <th class="px-4 py-3">Date</th>
              <th class="px-4 py-3"></th>
            </tr>
          </thead>
          <tbody
            class="bg-white divide-y dark:divide-gray-700 dark:bg-gray-800"
          >
            <tr
              class="text-gray-700 dark:text-gray-400"
              v-for="order in orders"
              :key="order.order_id"
            >
              <td class="px-4 py-3 text-sm">{{ order.order_id }}</td>
              <td class="px-4 py-3 text-sm">£ {{ order.totalPrice }}</td>
              <td class="px-4 py-3 text-xs">
                <span
                  class="px-2 py-1 font-semibold leading-tight rounded-full"
                  :class="{
                    'text-yellow-700 bg-yellow-100 rounded-full dark:text-white dark:bg-yellow-600':
                      order.status === 1,
                    'text-green-700 bg-green-100 dark:bg-green-700 dark:text-green-100':
                      order.status === 2,
                  }"
                >
                  {{ order.orderStatus }}
                </span>
              </td>
              <td class="px-4 py-3 text-sm">{{ order.date }}</td>
              <td class="px-4 py-3 text-sm">
                <Button
                  v-if="order.status == 1"
                  @click="shipOrder(order.order_id)"
                  >Ship Order</Button
                >
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import Button from "@/components/Button.vue";
import { notificationService } from "../services/notification.service";

export default {
  name: "Dashboard",
  components: { Button },
  async mounted() {
    await this.$store.dispatch("storeModule/getStoreOrders");
  },
  data() {
    return {};
  },
  methods: {
    dateDelta(date) {
      const today = new Date();
      const difference = today - date;
      return parseInt(difference / (24 * 3600 * 1000 * 7));
    },
    shipOrder(orderId) {
      this.$store
        .dispatch("storeModule/shipOrder", orderId)
        .then(() => {
          notificationService.success(`Order status changed successfully`);
        })
        .catch(() => {
          notificationService.error(
            "Problem shipping order. Please try again later."
          );
        });
    },
  },
  computed: {
    orders() {
      return this.$store.state.storeModule.orders;
    },
    newSales() {
      let set = this.orders.filter(
        (order) => this.dateDelta(order.date_created) < 3
      );
      return set.reduce((total, order) => {
        return total + order.productsOrdered;
      }, 0);
    },
    revenue() {
      return this.orders.reduce((total, order) => {
        return total + order.totalPrice;
      }, 0);
    },
    clients() {
      return this.orders.length;
    },
  },
};
</script>
