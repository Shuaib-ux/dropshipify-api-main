<template>
  <div>
    <aside
      class="
        z-20
        flex-shrink-0
        hidden
        w-64
        overflow-y-auto
        bg-white
        dark:bg-gray-800
        md:block
        h-full
      "
    >
      <div class="py-4 text-gray-500 dark:text-gray-400">
        <p class="ml-6 text-lg font-bold text-gray-800 dark:text-gray-200">
          Dropshipify
        </p>
        <ul class="mt-6">
          <li class="relative px-6 py-3">
            <router-link
              class="
                inline-flex
                items-center
                w-full
                text-sm
                font-semibold
                transition-colors
                duration-150
                hover:text-gray-800
                dark:hover:text-gray-200
              "
              to="/dashboard"
            >
              <svg
                class="w-5 h-5"
                aria-hidden="true"
                fill="none"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"
                ></path>
              </svg>
              <span class="ml-4">Store Home</span>
            </router-link>
          </li>
        </ul>
        <ul>
          <li class="relative px-6 py-3">
            <router-link
              class="
                inline-flex
                items-center
                w-full
                text-sm
                font-semibold
                transition-colors
                duration-150
                hover:text-gray-800
                dark:hover:text-gray-200
              "
              to="/products"
            >
              <svg
                class="w-5 h-5"
                aria-hidden="true"
                fill="none"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"
                ></path>
              </svg>
              <span class="ml-4">Products</span>
            </router-link>
          </li>
        </ul>
      </div>
    </aside>
    <div
      v-if="isSideMenuOpen"
      x-transition:enter="transition ease-in-out duration-150"
      x-transition:enter-start="opacity-0"
      x-transition:enter-end="opacity-100"
      x-transition:leave="transition ease-in-out duration-150"
      x-transition:leave-start="opacity-100"
      x-transition:leave-end="opacity-0"
      class="
        fixed
        inset-0
        z-10
        flex
        items-end
        bg-black bg-opacity-50
        sm:items-center sm:justify-center
      "
    ></div>
    <aside
      class="
        fixed
        inset-y-0
        z-20
        flex-shrink-0
        w-64
        mt-16
        overflow-y-auto
        bg-white
        dark:bg-gray-800
        md:hidden
      "
      v-if="isSideMenuOpen"
      x-transition:enter="transition ease-in-out duration-150"
      x-transition:enter-start="opacity-0 transform -translate-x-20"
      x-transition:enter-end="opacity-100"
      x-transition:leave="transition ease-in-out duration-150"
      x-transition:leave-start="opacity-100"
      x-transition:leave-end="opacity-0 transform -translate-x-20"
      v-on:click="closeSideMenu"
      @keydown.escape="closeSideMenu"
    >
      <div class="py-4 text-gray-500 dark:text-gray-400">
        <router-link
          class="ml-6 text-lg font-bold text-gray-800 dark:text-gray-200"
          href="#"
        >
          Windmill
        </router-link>
        <ul class="mt-6">
          <li class="relative px-6 py-3">
            <router-link
              class="
                inline-flex
                items-center
                w-full
                text-sm
                font-semibold
                transition-colors
                duration-150
                hover:text-gray-800
                dark:hover:text-gray-200
              "
              to="/dashboard"
            >
              <svg
                class="w-5 h-5"
                aria-hidden="true"
                fill="none"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"
                ></path>
              </svg>
              <span class="ml-4">Store Home</span>
            </router-link>
          </li>
        </ul>
        <ul>
          <li class="relative px-6 py-3">
            <router-link
              class="
                inline-flex
                items-center
                w-full
                text-sm
                font-semibold
                transition-colors
                duration-150
                hover:text-gray-800
                dark:hover:text-gray-200
              "
              to="products"
            >
              <svg
                class="w-5 h-5"
                aria-hidden="true"
                fill="none"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"
                ></path>
              </svg>
              <span class="ml-4">Products</span>
            </router-link>
          </li>
        </ul>
      </div>
    </aside>
  </div>
</template>

<script>
export default {
  name: "Sidebar",
  data() {
    return {
      isPagesMenuOpen: false,
      isSideMenuOpen: false,
    };
  },
  methods: {
    togglePagesMenu() {
      if (this.isPagesMenuOpen) {
        this.isPagesMenuOpen = false;
      } else {
        this.isPagesMenuOpen = true;
      }
    },
    closeSideMenu() {
      this.isSideMenuOpen = false;
    },
  },
  computed: {
    user() {
      return this.$store.state.authModule.user;
    },
  },
};
</script>

<style scoped>
a {
  @apply lg:hover:text-purple-600;
}

a.router-link-exact-active {
  @apply text-purple-600 font-semibold;
}
</style>