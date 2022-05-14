<template>
  <div
    class="flex items-center p-6 bg-white rounded-lg shadow-xs dark:bg-gray-800"
  >
    <div>
      <p class="mb-2 text-sm font-medium text-gray-600 dark:text-gray-400">
        {{ title }}
      </p>
      <Input
        :value="data"
        :spacing="false"
        :type="type"
        :required="required"
        v-if="type"
        @input="$emit('input', $event)"
      />
      <p class="text-lg font-semibold text-gray-700 dark:text-gray-200" v-else>
        {{ data }}
      </p>
    </div>
  </div>
</template>

<script>
import Input from "../components/Input.vue";
export default {
  name: "Card",
  components: {
    Input,
  },
  props: {
    title: {
      type: String,
      required: true,
    },
    data: {
      required: true,
    },
    type: {
      type: String,
      required: false,
    },
    required: {
      type: Boolean,
      default: true,
      required: false,
    },
  },
};
</script>