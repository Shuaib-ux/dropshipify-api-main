<template>
  <label class="block text-sm" :class="{ 'mb-4': spacing }">
    <span class="text-gray-700 dark:text-gray-400">{{ title }}</span>
    <textarea
      v-if="type == 'textarea'"
      class="
        block
        w-full
        mt-1
        text-sm
        dark:border-gray-600 dark:bg-gray-700
        focus:border-purple-400 focus:outline-none focus:shadow-outline-purple
        dark:text-gray-300 dark:focus:shadow-outline-gray
        form-input
      "
      rows="5"
      autocomplete="off"
      :value="value"
      :type="type"
      :name="inputName"
      :disabled="disabled"
      :required="required"
      :placeholder="placeholder"
      @input="$emit('input', $event.target.value)"
    ></textarea>
    <input
      v-else
      class="
        block
        w-full
        mt-1
        text-sm
        dark:border-gray-600 dark:bg-gray-700
        focus:border-purple-400 focus:outline-none focus:shadow-outline-purple
        dark:text-gray-300 dark:focus:shadow-outline-gray
        form-input
      "
      autocomplete="off"
      :value="value"
      :type="type"
      :step="step"
      :name="inputName"
      :disabled="disabled"
      :required="required"
      :placeholder="placeholder"
      @input="$emit('input', $event.target.value)"
      @change="$emit('change', $event)"
      @blur="$emit('blur', $event)"
    />
  </label>
</template>

<script>
export default {
  name: "Input",
  props: {
    value: {
      required: false,
    },
    title: {
      type: String,
    },
    type: {
      type: String,
      default: "text",
    },
    placeholder: {
      type: String,
    },
    step: {
      type: String,
    },
    disabled: {
      type: Boolean,
      default: false,
    },
    required: {
      type: Boolean,
      default: false,
    },
    spacing: {
      type: Boolean,
      default: true,
    },
  },
  computed: {
    inputName() {
      return this.$props.title?.toLocaleLowerCase().replaceAll(" ", "-");
    },
  },
};
</script>
