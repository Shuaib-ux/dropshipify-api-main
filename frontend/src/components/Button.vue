<template>
  <button
    class="
      px-4
      py-2
      w-full
      text-sm
      font-medium
      leading-5
      text-white
      transition-colors
      duration-150
      border border-transparent
      rounded-lg
      focus:outline-none focus:shadow-outline-purple
    "
    :class="{
      'bg-purple-600 hover:bg-purple-700 active:bg-purple-600':
        type == 'primary',
      'bg-gray-600 hover:bg-gray-700 active:bg-gray-600':
        type == 'secondary',
      'bg-red-600 hover:bg-red-700 active:bg-red-600':
        type == 'error',
    }"
    @click="$emit('click', $event)"
  >
    <slot />
  </button>
</template>

<script>
export default {
  name: "Button",
  props: {
    type: {
      type: String,
      default: "primary",
    },
    operation: {
      type: String,
      default: "submit",
    },
    fullWidth: {
      type: Boolean,
      default: false,
    },
    smaller: {
      type: Boolean,
      default: false,
    },
    disabled: {
      type: Boolean,
      default: false,
    },
  },
};
</script>