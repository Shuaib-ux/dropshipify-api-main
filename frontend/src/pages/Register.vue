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
              Register
            </h1>
            <form @submit.prevent="register()">
              <div class="grid grid-cols-2 gap-x-4">
                <Input
                  v-model="first_name"
                  :title="'First Name'"
                  :required="true"
                  :placeholder="'eg. Izzy'"
                />
                <Input
                  v-model="last_name"
                  :title="'Last Name'"
                  :required="true"
                  :placeholder="'eg. Freids'"
                />
              </div>
              <Input
                v-model="email"
                :title="'Email'"
                :type="'email'"
                :required="true"
                :placeholder="'eg. info@dropship.com'"
              />
              <Input
                v-model="password"
                :title="'Password'"
                :type="'password'"
                :required="true"
                :placeholder="'*************'"
              />
              <Input
                v-model="mailing_address"
                :title="'Mailing Address'"
                :required="true"
                :placeholder="'eg. 14, Houston Road'"
              />
              <Input
                v-model="mailing_phone_number"
                :title="'Phone Number'"
                :required="true"
                :type="'tel'"
                :placeholder="'eg. +44 0000000000'"
              />
              <div class="grid grid-cols-2 gap-x-4">
                <Input
                  v-model="city"
                  :title="'City'"
                  :required="true"
                  :placeholder="'eg. Chester'"
                />
                <Input
                  v-model="state"
                  :title="'State'"
                  :required="true"
                  :placeholder="'eg. Cheshire'"
                />
              </div>
              <Input
                v-model="zip"
                :title="'ZIP'"
                :required="true"
                :placeholder="'eg. CH1 4BJ'"
              />

              <Button>Create Account</Button>
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
                to="login"
              >
                Have an account already? Login.
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
  name: "Register",
  components: {
    Input,
    Button,
  },
  data() {
    return {
      email: "",
      password: "",
      first_name: "",
      last_name: "",
      mailing_address: "",
      city: "",
      state: "",
      zip: "",
      mailing_phone_number: "",
    };
  },
  methods: {
    register() {
      this.$store
        .dispatch("authModule/register", {
          email: this.email,
          password: this.password,
          first_name: this.first_name,
          last_name: this.last_name,
          mailing_address: this.mailing_address,
          mailing_phone_number: this.mailing_phone_number,
          city: this.city,
          state: this.state,
          zip: this.zip,
        })
        .then(() => {
          notificationService.success('Account Created successfully');
          this.$router.push({ name: "Login" });
        })
        .catch((error) => {
          notificationService.error(error.response.data.message)
        });
    },
  },
};
</script>