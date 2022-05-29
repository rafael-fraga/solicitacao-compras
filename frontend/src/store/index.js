
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: function () {
    return {
      products: []
    }
  },
  getters: {
    getProdutos (state) {
      return state.products;
    }
  },
  mutations: {
    addProducts (state, item){
      state.products.unshift(item);
    }
  },
  actions: {
  },
  modules: {
  }
})
