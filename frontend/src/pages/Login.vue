<template>
  <div class="flex items-center p-6 bg-gray-50 dark:bg-gray-900">
    <div
      class="
        flex-1
        h-full
        max-w-4xl
        mx-auto
        overflow-hidden
        bg-white
        rounded-lg
        shadow-xl
        dark:bg-gray-800
      "
    >
      <div class="flex flex-col overflow-y-auto md:flex-row">
        <div class="h-32 md:h-auto md:w-1/2">
          <img
            aria-hidden="true"
            class="object-cover w-full h-full dark:hidden"
            src="../assets/img/login-office.jpeg"
            alt="Office"
          />
          <img
            aria-hidden="true"
            class="hidden object-cover w-full h-full dark:block"
            src="../assets/img/login-office-dark.jpeg"
            alt="Office"
          />
        </div>
        <div class="flex items-center justify-center p-6 sm:p-12 md:w-1/2">
          <div class="w-full">
            <h1
              class="
                mb-4
                text-xl
                font-semibold
                text-gray-700
                dark:text-gray-200
              "
            >
              <img class="w-10 h-10 mb-4 cursor-pointer" @click="goToStores()" src="../assets/drop-logo.png" alt="" />
              Login
            </h1>
            <form @submit.prevent="login()">
              <Input
                v-model="email"
                :title="'Email'"
                :type="'email'"
                :required="true"
                :placeholder="'info@dropship.com'"
              />
              <Input
                v-model="password"
                :title="'Password'"
                :type="'password'"
                :required="true"
                @keyup.enter="login()"
                :placeholder="'*************'"
              />

              <Button>Log in</Button>
            </form>

            <hr class="my-8" />

            <p class="mt-1">
              <router-link
                class="
                  text-sm
                  font-medium
                  text-purple-600
                  dark:text-purple-400
                  hover:underline
                "
                to="register"
              >
                Register
              </router-link>
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Input from "@/components/Input";
import Button from "@/components/Button";
import { notificationService } from "../services/notification.service";
export default {
  name: "Login",
  components: {
    Input,
    Button,
  },
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    login() {
      this.$store
        .dispatch("authModule/login", {
          email: this.email,
          password: this.password,
        })
        .then((res) => {
          if (res.is_retailer) {
            this.$router.push({ name: "Home" });
          } else {
            this.$router.push({ name: "Stores" });
          }
        })
        .catch(() => {
          notificationService.error("Invalid credentials.");
          this.password = "";
        });
    },
    goToStores() {
      this.$router.push({name: 'Stores'})
    }
  },
};
</script>