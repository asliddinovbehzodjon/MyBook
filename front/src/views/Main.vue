<template>
  <div class="container mt-5">
    
 <div class="searchbar has-text-centered">
  <input type="text" :placeholder="$t('search')">
  <button class="button is-success" >{{$t('searchbook')}}</button>
 </div>
 
    <div class="columns">
      <div class="column is-3" v-for="book in books">
        <div class="card crads">
          <div class="card-image">
            <figure class="image is-5by3 ">
              <img :src="book.image" alt="{{book.name}}" class="big">
            </figure>
          </div>
          <div class="card-content">
            <div class="media">
              <div class="media-left">

              </div>
              <div class="media-content">
                <p class="is-4 name"><i class="fa-solid fa-book"></i> &nbsp;{{book.name}}</p>
                <p class="is-6 author"><i class="fa-solid fa-feather"></i> &nbsp;{{book.author}}</p>

                <p><i class="fa-solid fa-arrow-down-short-wide"></i> &nbsp;{{$t('category')}}</p>
                <a class="mine" v-for="(data,index) in book.category">
                  {{index+1}}.{{data}}
                </a>
                
                <p class="is-4"><i class="fa-solid fa-circle-info"></i> &nbsp;{{book.about}}</p>
                <p class="is-6"><i class="fa-solid fa-file"></i> &nbsp;{{book.size}}</p>
              </div>
             
            </div>
        
           
          </div>
          <footer class="card-footer">
            <a  class="card-footer-item"><i class="fa-solid fa-eye" style="color:green"></i>&nbsp; {{book.viewed}}</a>
            <a :href="book.file" class="card-footer-item" @click="download(book.id)" target="_blank"><i class="fa-solid fa-download" style="color:green"></i>&nbsp; {{book.downloaded}}</a>
            <a  @click="addtocart(book.id)" class="card-footer-item"><i class="fa-solid fa-bookmark" style="color:green"></i></a>
          </footer>
        </div>
      </div>
     
    </div>
  </div>
 
</template>
<style>
@import '../assets/css/main.css'
</style>
<script>
import axios from 'axios'
import { mapActions } from 'vuex';
export default {
  name: 'Main',
  
  data(){
    return {
      books :[]
    }
  },
  methods :{
    ...mapActions(['addtocart']),
    download(id){
        axios.get(`api/book/books/${id}/adddownloaded/`);
        this.getbooks()
    },

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
