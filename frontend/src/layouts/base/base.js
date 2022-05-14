import Loader from '@/components/Loader.vue'
const defaultLayout = 'default'

export default {
  name: "BaseLayout",
  components: { Loader },
  computed: {
    layout() {
      const layout = this.$route.meta.layout || defaultLayout;
      return () => import(`@/layouts/${layout}/index.vue`)
    }
  }
};
