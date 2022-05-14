import Vue from 'vue'
import Vuex from 'vuex'
import authModule from "./modules/auth.module";
import storeModule from "./modules/store.module";
import loadingModule from "./modules/loading.module";

Vue.use(Vuex)

export default new Vuex.Store({
    modules: {
        authModule,
        storeModule,
        loadingModule,
    }
})