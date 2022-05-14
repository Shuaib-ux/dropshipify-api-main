<template>
  <div
    v-if="loading"
    class="
      fixed
      top-0
      left-0
      z-30
      h-screen
      w-screen
      bg-black bg-opacity-10
      flex flex-col
      items-center
      justify-center
    "
  >
    <div class="animate-spin text-purple-500">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        aria-hidden="true"
        role="img"
        width="2.5rem"
        height="2.5rem"
        preserveAspectRatio="xMidYMid meet"
        viewBox="0 0 24 24"
      >
        <path
          fill="currentColor"
          d="M3.055 13H5.07a7.002 7.002 0 0 0 13.858 0h2.016a9.001 9.001 0 0 1-17.89 0zm0-2a9.001 9.001 0 0 1 17.89 0H18.93a7.002 7.002 0 0 0-13.858 0H3.055z"
        />
      </svg>
    </div>
  </div>
</template>

<script>
export default {
  name: "Loader",
  computed: {
    loading() {
      return this.$store.state.loadingModule.loading;
    },
  },
};
</script>