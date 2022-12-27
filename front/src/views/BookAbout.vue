<template>
<div class="container mb-5 mt-5">
    <div class="columns">
        <div class="column is-4">
            <div class="card crads">
                <div class="card-image">
                    <figure class="image is-5by3 skeleton">
                        <img :src="book.image" alt="{{book.name}}" class="big">
                    </figure>
                </div>
                <div class="card-content">
                    <div class="media">
                        <div class="media-left">

                        </div>
                        <div class="media-content">
                            <p class="is-4 name skeleton"><i class="fa-solid fa-book"></i> &nbsp;{{book.name}}</p>
                            <p class="is-6 author skeleton"><i class="fa-solid fa-feather"></i> &nbsp;{{book.author}}</p>

                            <p class="skeleton"><i class="fa-solid fa-arrow-down-short-wide"></i> &nbsp;{{$t('category')}}</p>
                            <a class="mine skeleton" v-for="(data,index) in book.category">
                                {{index+1}}.{{data}}
                            </a>

                            <p class="is-4 skeleton"><i class="fa-solid fa-circle-info"></i> &nbsp;{{book.about}}</p>
                            <p class="is-6 skeleton"><i class="fa-solid fa-file"></i> &nbsp;{{book.size}}</p>
                        </div>

                    </div>

                </div>
                <footer class="card-footer">
                    <a class="card-footer-item"><i class="fa-solid fa-eye" style="color:green"></i>&nbsp; {{book.viewed}}</a>
                    <a :href="book.file" class="card-footer-item" @click="download(book.id)" target="_blank"><i class="fa-solid fa-download" style="color:green"></i>&nbsp; {{book.downloaded}}</a>
                    <a @click="addtocart(book.id)" class="card-footer-item"><i class="fa-solid fa-bookmark" style="color:green"></i></a>
                </footer>
            </div>
        </div>
        <div class="column is-8">
           <input type="text" name="" id="" :placeholder="($t('entercomment'))" class="comment" v-model="description">
           <button  class="button is-success" @click="postcomment()"> {{$t('add')}}</button>
           <article class="message is-success skeleton" v-for="comment in comments">
            <div class="message-header">
              <p><i class="fa-solid fa-user"></i>&nbsp Kitobxon</p>
              <p>{{formatDate(book.added)}}</p>
              
            </div>
            <div class="message-body">
              {{ comment.description }}
            </div>
            <hr>
            
          </article>
        </div>
    </div>
    <div class="columns">
        <div class="column is-3" v-for="book in books"  v-show="book.id!=id"> 
            <div class="card crads" v-show="book.id!=id">
                <div class="card-image">
                    <figure class="image is-5by3 skeleton">
                        <img :src="book.image" :alt="book.name" class="big">
                    </figure>
                </div>
                <div class="card-content">
                    
                    <router-link class="media" :to="{name:'BookAbout',params:{id:book.id}}">
                        <div class="media-left">
                        
                        </div>
                        <div class="media-content">
                            <p class="is-4 name skeleton"><i class="fa-solid fa-book"></i> &nbsp;{{book.name}}</p>
                            <p class="is-6 author skeleton"><i class="fa-solid fa-feather"></i> &nbsp;{{book.author}}</p>

                            <p class="skeleton"><i class="fa-solid fa-arrow-down-short-wide"></i> &nbsp;{{$t('category')}}</p>
                            <a class="mine skeleton" v-for="(data,index) in book.category">
                                {{index+1}}.{{data}}
                            </a>

                            <p class="is-4 skeleton"><i class="fa-solid fa-circle-info"></i> &nbsp;{{book.about}}</p>
                            <p class="is-6 skeleton"><i class="fa-solid fa-file"></i> &nbsp;{{book.size}}</p>
                        </div>

                    </router-link>

                </div>
                <footer class="card-footer">
                    <a class="card-footer-item"><i class="fa-solid fa-eye" style="color:green"></i>&nbsp; {{book.viewed}}</a>
                    <a :href="book.file" class="card-footer-item" @click="download(book.id)" target="_blank"><i class="fa-solid fa-download" style="color:green"></i>&nbsp; {{book.downloaded}}</a>
                    <a @click="addtocart(book.id)" class="card-footer-item"><i class="fa-solid fa-bookmark" style="color:green"></i></a>
                </footer>
            </div>
        </div>

    </div>
</div>
</template>

<script>
import axios from 'axios';
import moment from 'moment'
export default {
   
    data() {
        return {
            book: '',
            comments:[],
            id:this.$route.params.id,
            description:'',
            books:[]

        }
    },
    methods: {
        viewed() {
            axios.get(`api/book/books/${this.id}/addview/`);
            
        },
        postcomment(){
            axios.post(`api/book/comments/`,{
                book:this.id,
                description:this.description
            })
            this.getbook()
            this.description =''
        },
        getbook() {
            axios.get(`api/book/books/${this.id}/`).then(res => {
                this.book = res.data,
                this.comments = res.data.comments
              
               
            })
        },
        getlikebooks() {
            axios.get(`api/book/like/${this.id}/`).then(res => {
                this.books = res.data
                
              
               
            })
        },
        formatDate(date) {
                return moment(date).format('DD/MM/YYYY hh:mm');
            },
    },
    mounted() {
        this.viewed()
        this.getbook(),
        this.getlikebooks()
    }
}
</script>

<style lang="scss" scoped>
@import '../assets/css/bookabout.css';
.skeleton{
 
    animation: skeleton-loading 2s ease alternate;
   }
   @keyframes skeleton-loading{
       0%{
           background-color:hsl(200, 20%, 70%);
           opacity: 0;
           color:hsl(200, 20%, 70%);
           border-radius: 10px;
       }
       100%{
           background-color:hsl(200, 20%, 95%); 
           border-radius:10px;
           color: hsl(200, 20%, 95%);
       }
   }  
</style>
