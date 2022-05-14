import { User } from "../../models/user.model";
import { AuthService } from "../../services/auth.service";
import { httpService } from "../../services/http.service";

const authService = new AuthService();

const state = {
    user: authService.getUser() || null,
    isAuthenticated: !!authService.getToken(),
    isRetailer: authService.getUser()?.is_retailer || false
};

const actions = {
    async login({ commit, dispatch }, userLogin) {
        const response = await httpService.post("login", userLogin);
        if (response.data.access_token) {
            authService.setToken(response.data.access_token);
            commit('authenticate')
            return dispatch('getUser')
        }
    },
    async logout({ commit }) {
        authService.logout();
        commit("logout");
    },
    async getUser({ commit }) {
        const response = await httpService.get("login");
        authService.setUser(response.data)
        commit('setUser', response.data)
        return state.user;
    },
    async register(context, userRegister) {
        await httpService.post("signup", userRegister);
    },
    async registerRetailer(context, store) {
        await httpService.post(`sign-up-retailer`, store.data);
        context.dispatch('getUser')
    },
    async updateUser(context, userUpdate) {
        await httpService.post(`update-user`, userUpdate);
        context.dispatch('getUser')
    },
};

const mutations = {
    setUser(state, user) {
        state.user = new User(user);
        state.isRetailer = state.user.is_retailer;
    },
    logout(state) {
        state.user = null;
        state.isAuthenticated = false;
    },
    authenticate(state) {
        state.isAuthenticated = true;
    }
};

export default { state, mutations, actions, namespaced: true };