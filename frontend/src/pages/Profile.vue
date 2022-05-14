<template>
  <div class="container px-6 mx-auto grid">
    <div class="flex items-center justify-between">
      <h2 class="my-6 text-2xl font-semibold text-gray-700 dark:text-gray-200">
        Profile
      </h2>
      <div class="min-w-24 flex items-center space-x-4">
        <Button @click="toggle()" v-if="!edit">Edit Profile</Button>
        <Button :type="'error'" @click="toggle()" v-if="edit">Cancel</Button>
        <Button @click="updateUser()" v-if="edit">Update</Button>
      </div>
    </div>

    <!-- Cards -->
    <div class="grid w-3/4 grid-cols-2 mx-auto gap-6 mb-8">
      <!-- Card -->
      <Card
        title="First Name"
        @input="user.first_name = $event"
        :data="user.first_name"
        :type="edit ? 'text' : ''"
      />
      <Card
        title="Last Name"
        @input="user.last_name = $event"
        :data="user.last_name"
        :type="edit ? 'text' : ''"
      />
      <Card
        title="Email"
        @input="user.email = $event"
        :data="user.email"
      />
      <Card
        title="ZIP"
        @input="user.zip = $event"
        :data="user.zip"
        :type="edit ? 'text' : ''"
      />
      <Card
        title="Mailing Address"
        @input="user.mailing_address = $event"
        :data="user.mailing_address"
        :type="edit ? 'text' : ''"
      />
      <Card
        title="Mailing Phone Number"
        @input="user.mailing_phone_number = $event"
        :data="user.mailing_phone_number"
        :type="edit ? 'tel' : ''"
      />
      <Card
        title="City"
        @input="user.city = $event"
        :data="user.city"
        :type="edit ? 'text' : ''"
      />
      <Card
        title="State"
        @input="user.state = $event"
        :data="user.state"
        :type="edit ? 'text' : ''"
      />
    </div>
  </div>
</template>

<script>
import Button from "../components/Button.vue";
import Card from "../components/Card.vue";
import { notificationService } from "../services/notification.service";
export default {
  name: "Profile",
  components: { Card, Button },
  data() {
    return {
      edit: false,
      user: this.$store.state.authModule.user,
    };
  },
  methods: {
    toggle() {
      this.edit = !this.edit;
    },
    updateUser() {
      this.$store
        .dispatch("authModule/updateUser", {
          first_name: this.user.first_name,
          last_name: this.user.last_name,
          mailing_address: this.user.mailing_address,
          mailing_phone_number: this.user.mailing_phone_number,
          city: this.user.city,
          state: this.user.state,
          zip: this.user.zip,
        })
        .then(() => {
          notificationService.success(`Profile updated successfully`);
        })
        .catch(() => {
          notificationService.error(
            "Problem shipping order. Please try again later."
          );
        });
      this.toggle();
    },
  },
};
</script>
