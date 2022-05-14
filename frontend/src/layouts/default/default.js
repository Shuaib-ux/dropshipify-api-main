import Navigation from "@/components/Navigation.vue";
import Button from "@/components/Button.vue";

export default {
  name: "DefaultLayout",
  components: { Navigation, Button },
  computed: {
    routeName() {
      return this.$route.name
    }
  }
};
