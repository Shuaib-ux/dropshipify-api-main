<template>
  <div class="pb-10">
    <Navigation />
    <div class="container px-6 mt-6 mx-auto" v-if="routeName !== 'Stores'">
      <div class="w-40">
        <router-link
          class="
            mt-4
            text-sm
            font-medium
            text-purple-600
            dark:text-purple-400
            hover:underline
          "
          to="/stores"
        >
          <Button>Go Back to Stores</Button>
        </router-link>
      </div>
    </div>
    <slot />
  </div>
</template>

<script src="./default.js"></script>
