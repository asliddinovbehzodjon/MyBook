<template>
  <div class="container mt-5">
    <div class="columns">
      <div class="column is-3" v-for="book in books">
        <div class="card">
          <div class="card-image">
            <figure class="image is-4by3">
              <img :src="book.image" alt="Placeholder image">
            </figure>
          </div>
          <div class="card-content">
            <div class="media">
              <div class="media-left">
                <figure class="image is-48x48">
                  <img :src="book.image" alt="Placeholder image">
                </figure>
              </div>
              <div class="media-content">
                <p class="title is-4">{{book.name}}</p>
                <p class="" v-for="(data,index) in book.category">
                  {{index+1}}.{{data}}
                </p>
              </div>
            </div>
        
            <div class="content">
              {{book.about}}
            </div>
          </div>
          <footer class="card-footer">
            <a href="#" class="card-footer-item"><i class="fa-solid fa-eye"></i></a>
            <a href="#" class="card-footer-item"><i class="fa-solid fa-download"></i></a>
            <a href="#" class="card-footer-item"><i class="fa-solid fa-bookmark"></i></a>
          </footer>
        </div>
      </div>
     
    </div>
  </div>
 
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import axios from 'axios'
export default {
  name: 'HomeView',
  components: {
    HelloWorld
  },
  data(){
    return {
      books :[]
    }
  },
  methods :{
    getbooks(){
      axios.get(`api/book/books/`).then(res=>{
                    this.books = res.data;
                    console.log(this.books)
                    
                })
    }
  },
  mounted(){
    this.getbooks()
  }
}
</script>
