import Vue from "vue";
import store from './store';
import App from "./App.vue";
import router from "./router/routes";
import "@/assets/styles/main.css";


Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
