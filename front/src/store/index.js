import { createStore } from 'vuex'

export default createStore({
  state: {
    cart:JSON.parse(localStorage.getItem('cart'))|| []
  },
  getters: {
    cart:(state)=>state.cart
  },
  actions: {
    addtocart({commit},book){
      commit('addbook',book)}

  },
  mutations: {
    addbook(state,mybook){
      const addedbook = state.cart.find((book)=> book.book ==mybook )
      
      if(addedbook){
        alert("Already added")
      }
      else{
        state.cart.push({...mybook,book:mybook})
        alert('Added')
        
        localStorage.setItem('cart', JSON.stringify(state.cart))
        console.log(localStorage.getItem('cart'))
      }
    }
    
        
   
  },
  modules: {
  }
})
