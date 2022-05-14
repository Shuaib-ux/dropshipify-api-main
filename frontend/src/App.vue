<template>
  <div class="min-h-screen bg-gray-50 dark:bg-gray-900" id="app">
    <BaseLayout>
      <router-view></router-view>
    </BaseLayout>
  </div>
</template>

<script>
import BaseLayout from "@/layouts/base/index.vue";
import { notificationService } from "./services/notification.service";
export default {
  name: "App",
  components: {
    BaseLayout,
  },
  mounted() {
    setInterval(() => {
      if(this.$route.meta.requiresAuth) {
        this.$store
          .dispatch("authModule/getUser")
          .catch(() => {
            notificationService.error("Your token has expired. Please log in");
            this.$store.dispatch("authModule/logout");
            this.$router.push({ name: "Login" });
          });
      }
    }, 300000);
  },
};
</script>
