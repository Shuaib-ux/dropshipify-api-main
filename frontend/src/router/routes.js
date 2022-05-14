import Vue from "vue";
import VueRouter from "vue-router";
import { authGuard, metaWrapper, retailerGuard } from "./guard";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    redirect: "/login",
  },
  {
    path: "/dashboard",
    name: "Home",
    component: () => import("../pages/Dashboard.vue"),
    meta: { requiresAuth: true, isRetailer: true, layout: 'dashboard' }
  },
  {
    path: "/products",
    name: "Products",
    component: () => import("../pages/Products.vue"),
    meta: { requiresAuth: true, isRetailer: true, layout: 'dashboard' }
  },
  {
    path: "/cart",
    name: "Cart",
    component: () => import("../pages/Cart.vue"),
    meta: { requiresAuth: true }
  },
  {
    path: "/wishlist",
    name: "WishList",
    component: () => import("../pages/WishList.vue"),
    meta: { requiresAuth: true }
  },
  {
    path: "/login",
    name: "Login",
    component: () => import("../pages/Login.vue"),
    meta: { layout: 'authentication' }
  },
  {
    path: "/profile",
    name: "Profile",
    component: () => import("../pages/Profile.vue"),
    meta: { requiresAuth: true }
  },
  {
    path: "/register",
    name: "Register",
    component: () => import("../pages/Register.vue"),
    meta: { layout: 'authentication' }
  },
  {
    path: "/retail-register",
    name: "Register Retailer",
    component: () => import("../pages/RegisterRetailer.vue"),
    meta: { requiresAuth: true, layout: 'authentication' }
  },
  {
    path: "/stores",
    name: "Stores",
    component: () => import("../pages/Stores.vue"),
  },
  {
    path: "/store/:id",
    name: "Store",
    component: () => import("../pages/Store.vue"),
  },
  {
    path: "**",
    name: "Error;* Page does not exist",
    component: () => import("../pages/404.vue"),
    meta: { layout: 'error' }
  },
];


const router = new VueRouter({
  routes,
  mode: "history",
});

router.beforeEach((to, from, next) => {
  authGuard(to, next);
  retailerGuard(to, next);
  metaWrapper(to, from)
});

export default router;
