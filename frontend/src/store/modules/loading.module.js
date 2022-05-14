const state = {
    loading: false
  };
  
  const actions = {
    async startLoading({ commit }) {
      commit("startLoading");
    },
    async stopLoading({ commit }) {
      commit("stopLoading");
    },
  };
  
  const mutations = {
    startLoading(state) {
      state.loading = true;
    },
    stopLoading(state) {
      state.loading = false;
    },
  };
  
  export default { state, mutations, actions, namespaced: true };