<template>
  <div
    class="
      relative
      bg-white
      hover:shadow-md
      rounded-xl
      border border-gray-200
      p-2
      cursor-pointer
    "
    @click="goToStore()"
  >
    <div class="overflow-x-hidden rounded-lg relative mb-6">
      <img class="rounded-lg object-cover h-52 w-full" :src="store.image" />
    </div>
    <div class="mt-4 pl-2 mb-4 flex justify-between">
      <div>
        <p class="text-lg font-semibold text-gray-900 mb-2">
          {{ store.store_name }}
        </p>
        <p class="text-sm text-gray-900">
          {{ store.store_description }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "StoreTile",
  props: {
    store: {
      type: Object,
      required: true,
    },
  },
  methods: {
    goToStore() {
      this.$router.push({ name: "Store", params: { id: this.store.id } });
    },
  },
};
</script>