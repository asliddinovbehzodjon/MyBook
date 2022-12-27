<template>
    <div class="container">
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
                                    {{index+1}}.{{data.name}}
                                </a>
    
                                <p class="is-4 skeleton"><i class="fa-solid fa-circle-info"></i> &nbsp;{{book.about}}</p>
                                <!-- <p class="is-6 skeleton"><i class="fa-solid fa-file"></i> &nbsp;{{book.size}}</p> -->
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
    export default {
        name:'Category',
        data(){
            return{
                  id:this.$route.params.id,
                  category:'',
                  books:[]
            }
        },
        methods:{
            getbook(){
                axios.get(`api/book/category/${this.id}/`).then(res=>{
                         this.category = res.data.name,
                         this.books = res.data.books
                })
            }
        },
        mounted(){
            this.getbook()
        }
    }
</script>

<style lang="scss" scoped>

</style>