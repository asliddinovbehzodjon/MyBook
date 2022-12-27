<template>
<div class="container mt-5">

    <div class="searchbar has-text-centered">
        <input type="text" autocomplete="on" :placeholder="$t('search')" v-model="key" @input="autocomplete()"  list="books" required>
        <button class="button is-success" @click="searchmybook()">{{$t('searchbook')}}</button>
        <datalist id="books" v-if="autobooks">
            <option :value="book.name" v-for="book in autobooks" :key="book.id">{{book.name}}</option>
            </datalist>
    </div>
   <div v-show="searchbooks.length">
    <h1 class="has-text-centered title is-4 mt-5 mb-5" style="color:green">
        {{$t('searched')}}
   </h1>
    <div class="columns" v-if="searchbooks">
        <div class="column is-3" v-for="book in searchbooks">
            <div class="card crads">
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
    <div class="center mt-3" v-show="searchbooks.length">
        <div class="pagination">
            <a @click="searchprevious()" :disabled="previoushas">Orqaga</a>
            <a v-if="searchcurrent_page_num">{{searchcurrent_page_num}} ta {{searchall_pages}} dan</a>
            <a v-else>0 ta 0 dan</a>
            <a @click="searchnext()" :disabled="nexthas">Oldinga</a>
        </div>
    </div>
   </div>
    <h1 class="has-text-centered title is-4 mt-5 mb-5" style="color:green">
         {{$t('moredownload')}}
    </h1>
    <div class="columns">
        <div class="column is-3" v-for="book in books">
            <div class="card crads">
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
<div class="center mt-3">
    <div class="pagination">
        <a @click="previous()" :disabled="previoushas">Orqaga</a>
        <a v-if="current_page_num">{{current_page_num}} ta {{all_pages}} dan</a>
        <a v-else>0 ta 0 dan</a>
        <a @click="next()" :disabled="nexthas">Oldinga</a>
    </div>
</div>

</template>

<style>
@import '../assets/css/main.css';

.center {
    text-align: center;
}

.pagination {
    display: inline-block;
}

.pagination a {
    color: black;
    float: left;
    padding: 8px 16px;
    text-decoration: none;
    transition: background-color .3s;
    border: 1px solid #ddd;
    margin: 0 4px;
}

.pagination a.active {
    background-color: #4CAF50;
    color: white;
    border: 1px solid #4CAF50;
}

.pagination a:hover:not(.active) {
    background-color: #ddd;
}

a {
    border-radius: 10px;
}
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

<script>
import axios from 'axios'
import {
    mapActions
} from 'vuex';
export default {
    name: 'Main',

    data() {
        return {
            books: [],
            searchbooks:[],
            all_pages:'',
            current_page_num:'',
            nexthas:'',
            previoushas:'',
            key:'',
            autobooks:'',
            searchall_pages:'',
            searchcurrent_page_num:'',
            searchnexthas:'',
            searchprevioushas:'',
        }
    },
    methods: {
        ...mapActions(['addtocart']),
        searchmybook(){
            axios.get( `/api/book/books/?search=${this.key}`).then(res =>{
                    this.searchbooks = res.data.results
                    this.searchall_pages = res.data.all_pages
                    this.searchcurrent_page_num = res.data.current_page_num
                    this.searchnexthas =res.data.next
                    this.searchprevioushas = res.data.previous
                    
                 
                })
        },
        autocomplete(){
                    axios.get( `api/book/booklist/`).then(res =>{
                    this.autobooks = res.data
                
                 
                })
            },
        download(id) {
            axios.get(`api/book/books/${id}/adddownloaded/`);
            console.log('Added')
            this.getbooks()
        },
        searchprevious() {
            axios.get(`${this.searchprevioushas}`).then((res) => {
                this.searchbooks = res.data.results
                this.searchall_pages = res.data.all_pages
                this.searchcurrent_page_num = res.data.current_page_num
                this.searchnexthas =res.data.next
                this.searchprevioushas = res.data.previous
                
                
             } )
        },
        previous() {
            axios.get(`${this.previoushas}`).then((res) => {
                this.books = res.data.results
                this.all_pages = res.data.all_pages
                this.current_page_num = res.data.current_page_num
                this.nexthas =res.data.next
                this.previoushas = res.data.previous
                
                
             } )
        },
        next() {
            axios.get(`${this.nexthas}`).then((res) => {
                this.books = res.data.results
                this.all_pages = res.data.all_pages
                this.current_page_num = res.data.current_page_num
                this.nexthas =res.data.next
                this.previoushas = res.data.previous
                
             } )
        },
        searchnext() {
            axios.get(`${this.searchnexthas}`).then((res) => {
                this.searchbooks = res.data.results
                this.searchall_pages = res.data.all_pages
                this.searchcurrent_page_num = res.data.current_page_num
                this.searchnexthas =res.data.next
                this.searchprevioushas = res.data.previous
                
             } )
        },
        getbooks() {
            axios.get(`api/book/books/`).then((res) => {
                this.books = res.data.results
                this.all_pages = res.data.all_pages
                this.current_page_num = res.data.current_page_num
                this.nexthas =res.data.next
                this.previoushas = res.data.previous
                
             } )
        }
    },
    mounted() {
        this.getbooks()
    }
}
</script>
