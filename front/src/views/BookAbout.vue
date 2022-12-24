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
                    <router-link class="media" >
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
        <div class="column is-8">
            <h1 style="background-color: red;">Hello</h1>
        </div>
    </div>
</div>
</template>

<script>
import axios from 'axios';
export default {
    name: 'BookAbout',
    data(){
        return{
            book:'',
            
        }
    },
    methods:{
        getbook(){
            
            axios.get(`api/book/books/1/`).then(res =>{
                this.book = res.data
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
