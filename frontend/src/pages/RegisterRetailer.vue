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
              Create Store
            </h1>
            <form @submit.prevent="createStore()">
              <Input
                v-model="store.data.store_name"
                :title="'Store Name'"
                :required="true"
                :placeholder="'eg. Fruits by Izzy'"
              />
              <Input
                v-model="store.data.store_description"
                :type="'textarea'"
                :title="'Store Description'"
                :required="true"
                :placeholder="'eg. Very nice description fro your store'"
              />
              <Input
                :type="'file'"
                :title="'Image'"
                :required="true"
                @change="selectImage($event)"
              />

              <Button>Create Store</Button>
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
                to="/profile"
              >
                Back to Profile
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
import { AuthService } from "../services/auth.service";

const authService = new AuthService();
export default {
  name: "RegisterRetailer",
  components: {
    Input,
    Button,
  },
  data() {
    return {
      store: {
        data: {
          store_name: "",
          image: "",
          store_description: "",
        },
      },
    };
  },
  methods: {
    createStore() {
      this.$store
        .dispatch("authModule/registerRetailer", {
          ...this.store,
          userId: this.user.id,
        })
        .then(() => {
          notificationService.success("Store Created successfully");
          this.$router.push({ name: "Profile" });
        })
        .catch((error) => {
          notificationService.error(error.response.data.message)
        });
    },
    selectImage(event) {
      const image = event.target.files[0];
      const reader = new FileReader();
      reader.onload = (fileLoadedEvent) => {
        const base64 = fileLoadedEvent.target.result;
        this.store.data.image = base64.split('base64,')[1];
      };
      reader.readAsDataURL(image);
    },
  },
  computed: {
    user() {
      return authService.getUser();
    },
  },
};
</script>