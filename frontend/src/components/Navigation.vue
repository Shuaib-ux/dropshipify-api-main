<template>
  <header class="z-10 py-4 bg-white shadow-md dark:bg-gray-800">
    <div
      class="
        container
        flex
        items-center
        justify-between
        h-full
        px-6
        mx-auto
        dark:text-purple-300
      "
    >
      <div class="flex items-center space-x-2 lg:space-x-16">
        <img
          class="w-6 h-6 lg:h-12 lg:w-12 cursor-pointer"
          @click="goToStores()"
          src="../assets/drop-logo.png"
          alt=""
        />
        <p v-if="!user"></p>
      </div>
      <ul class="flex items-center flex-shrink-0 space-x-6">
        <p
          v-if="user"
          class="
            text-sm
            font-medium
            text-purple-600
            dark:text-purple-400
            hover:underline
          "
        >
          <router-link v-if="!user.is_retailer" to="/retail-register">
            <Button>Create retailer account</Button>
          </router-link>
          <router-link
            v-if="user.is_retailer && layout !== 'dashboard'"
            to="/dashboard"
          >
            <Button>Go to Dashboard</Button>
          </router-link>
          <router-link
            v-if="user.is_retailer && layout == 'dashboard' && user.store_id"
            :to="'store/' + user.store_id"
          >
            <Button>Go to Store</Button>
          </router-link>
        </p>
        <!-- Profile menu -->
        <li class="relative">
          <button
            v-if="user"
            class="align-middle focus:shadow-outline-purple focus:outline-none"
            v-on:click="toggleProfileMenu"
            @keydown.escape="closeProfileMenu"
            aria-label="Account"
            aria-haspopup="true"
          >
            <p>{{ user.first_name }} {{ user.last_name }}</p>
          </button>
          <router-link
            v-if="!user"
            to="/login"
            class="align-middle focus:shadow-outline-purple focus:outline-none"
          >
            <p>Login</p>
          </router-link>
          <template v-if="isProfileMenuOpen">
            <ul
              x-transition:leave="transition ease-in duration-150"
              x-transition:leave-start="opacity-100"
              x-transition:leave-end="opacity-0"
              v-on:click="closeProfileMenu"
              @keydown.escape="closeProfileMenu"
              class="
                absolute
                right-0
                w-56
                p-2
                mt-2
                space-y-2
                text-gray-600
                bg-white
                border border-gray-100
                rounded-md
                shadow-md
                dark:border-gray-700 dark:text-gray-300 dark:bg-gray-700
              "
              aria-label="submenu"
            >
              <li class="flex">
                <router-link
                  class="
                    inline-flex
                    items-center
                    w-full
                    px-2
                    py-1
                    text-sm
                    font-semibold
                    transition-colors
                    duration-150
                    rounded-md
                    hover:bg-gray-100 hover:text-gray-800
                    dark:hover:bg-gray-800 dark:hover:text-gray-200
                  "
                  to="/profile"
                >
                  <svg
                    class="w-4 h-4 mr-3"
                    aria-hidden="true"
                    fill="none"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
                    ></path>
                  </svg>
                  <span>Profile</span>
                </router-link>
              </li>
              <li class="flex">
                <a
                  class="
                    inline-flex
                    items-center
                    w-full
                    px-2
                    py-1
                    cursor-pointer
                    text-sm
                    font-semibold
                    transition-colors
                    duration-150
                    rounded-md
                    hover:bg-gray-100 hover:text-gray-800
                    dark:hover:bg-gray-800 dark:hover:text-gray-200
                  "
                  @click="logout()"
                >
                  <svg
                    class="w-4 h-4 mr-3"
                    aria-hidden="true"
                    fill="none"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1"
                    ></path>
                  </svg>
                  <span>Log out</span>
                </a>
              </li>
            </ul>
          </template>
        </li>
        <router-link
          v-if="user && layout !== 'dashboard'"
          to="/wishlist"
          class="focus:shadow-outline-purple focus:outline-none"
          ><svg
            xmlns="http://www.w3.org/2000/svg"
            aria-hidden="true"
            role="img"
            width="1.5em"
            height="1.5em"
            preserveAspectRatio="xMidYMid meet"
            viewBox="0 0 24 24"
          >
            <path
              fill="currentColor"
              d="M16.5 3c-1.74 0-3.41.81-4.5 2.09C10.91 3.81 9.24 3 7.5 3C4.42 3 2 5.42 2 8.5c0 3.78 3.4 6.86 8.55 11.54L12 21.35l1.45-1.32C18.6 15.36 22 12.28 22 8.5C22 5.42 19.58 3 16.5 3zm-4.4 15.55l-.1.1l-.1-.1C7.14 14.24 4 11.39 4 8.5C4 6.5 5.5 5 7.5 5c1.54 0 3.04.99 3.57 2.36h1.87C13.46 5.99 14.96 5 16.5 5c2 0 3.5 1.5 3.5 3.5c0 2.89-3.14 5.74-7.9 10.05z"
            />
          </svg>
        </router-link>
        <router-link
          v-if="user && layout !== 'dashboard'"
          to="/cart"
          class="focus:shadow-outline-purple focus:outline-none"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            aria-hidden="true"
            role="img"
            width="1.5em"
            height="1.5em"
            preserveAspectRatio="xMidYMid meet"
            viewBox="0 0 24 24"
          >
            <g
              fill="none"
              stroke="currentColor"
              stroke-linejoin="round"
              stroke-width="2"
            >
              <path
                d="M5 7h13.79a2 2 0 0 1 1.99 2.199l-.6 6A2 2 0 0 1 18.19 17H8.64a2 2 0 0 1-1.962-1.608L5 7Z"
              />
              <path
                stroke-linecap="round"
                d="m5 7l-.81-3.243A1 1 0 0 0 3.22 3H2m6 18h2m6 0h2"
              />
            </g>
          </svg>
        </router-link>
      </ul>
    </div>
  </header>
</template>

<script>
import Button from "@/components/Button.vue";
export default {
  name: "Navigation",
  components: { Button },
  data() {
    return {
      isProfileMenuOpen: false,
      isNotificationsMenuOpen: false,
      isSideMenuOpen: false,
      dark: false,
    };
  },
  methods: {
    toggleTheme() {
      if (this.dark) {
        this.dark = false;
      } else {
        this.dark = true;
      }
    },
    toggleSideMenu() {
      if (this.isSideMenuOpen) {
        this.isSideMenuOpen = false;
      } else {
        this.isSideMenuOpen = true;
      }
    },
    toggleProfileMenu() {
      if (this.isProfileMenuOpen) {
        this.isProfileMenuOpen = false;
      } else {
        this.isProfileMenuOpen = true;
      }
    },
    toggleNotificationsMenu() {
      if (this.isNotificationsMenuOpen) {
        this.isNotificationsMenuOpen = false;
      } else {
        this.isNotificationsMenuOpen = true;
      }
    },
    closeNotificationsMenu() {
      this.isNotificationsMenuOpen = false;
    },
    closeProfileMenu() {
      this.isProfileMenuOpen = false;
    },
    logout() {
      this.$store
        .dispatch("authModule/logout")
        .then(() => this.$router.push({ name: "Login" }));
    },
    goToStores() {
      this.$router.push({ name: "Stores" });
    },
  },
  computed: {
    user() {
      return this.$store.state.authModule.user;
    },
    layout() {
      return this.$route.meta.layout;
    },
  },
};
</script>
