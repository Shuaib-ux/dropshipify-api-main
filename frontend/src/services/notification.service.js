import Vue from 'vue';
import VueToast from 'vue-toast-notification';
import 'vue-toast-notification/dist/theme-default.css';

Vue.use(VueToast, { position: 'top-right' })

const notificationService = Vue.$toast;

export { notificationService }