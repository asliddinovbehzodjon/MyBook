<template>
    <nav class="navbar  is-success" role="navigation" aria-label="main navigation">
        <div class="navbar-brand">
          <router-link to="/" class="navbar-item" >
            <p class="logo">MyBook</p>
          </router-link>
      
          <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" id="burger" data-target="navbarBasicExample" @click="isOpen = !isOpen" v-bind:class="{'is-active': isOpen}">
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
          </a>
        </div>
      
        <div id="navbarBasicExample" class="navbar-menu"  v-bind:class="{'is-active': isOpen}">
          <div class="navbar-start">
            <a class="navbar-item">
              <i class="fa-solid fa-house"></i> &nbsp; {{$t('Home')}}
            </a>
            <div class="navbar-item has-dropdown is-hoverable">
              <a class="navbar-link">
                <i class="fa-solid fa-arrow-down-short-wide"></i> &nbsp;{{$t('janr')}}
              </a>
      
              <div class="navbar-dropdown">
                <a class="navbar-item" v-for="item in categories">
                  <router-link :to="{name:'Category',params:{id:item.id}}">
                      {{ item.name }}
                  </router-link>
                </a>
               
              </div>
            </div>
            <a class="navbar-item" href="https://t.me/mybook_uzbot" target="_blank">
              <i class="fa-brands fa-telegram"></i> &nbsp;   Telegram bot
            </a>
            <a class="navbar-item" >
              <i class="fa-sharp fa-solid fa-pen"></i> &nbsp;  {{$t('blog')}}
            </a>
      
           
          </div>
      
          <div class="navbar-end">
            <div class="navbar-item has-dropdown is-hoverable">
              <a class="navbar-link">
                <i class="fa-solid fa-globe"></i>&nbsp; {{$t('language')}}
              </a>
      
              <div class="navbar-dropdown">
                <a class="navbar-item" @click="setlanguage('en')">
                  {{$t('english')}}
                </a>
                <a class="navbar-item"  @click="setlanguage('ru')">
                  {{$t('russian')}}
                </a>
               
              </div>
            </div>
            <a class="navbar-item">
              <i class="fa-solid fa-bookmark"></i>&nbsp; {{$t('favorites')}}
            </a>
          </div>
        </div>
      </nav>
</template>

<script>
import axios from 'axios';

    export default {
        data (){
            return {
                categories:[],
                isOpen: false,
               
            }
        },
        methods:{
            getcategories(){
               
                axios.get(`api/book/category/`).then(res=>{
                    this.categories = res.data
                    
                })
            },
            setlanguage(lang){
              this.$i18n.locale = lang;
              console.log(this.$i18n.locale)
              localStorage.setItem('language',lang)
              this.$router.go()
              
              
            }
        },
        mounted(){
            
            this.getcategories()
        },
        watch: {
    '$route' () {
      this.isOpen = false;
    
    
     
    },
   
    
    }
    
    }
</script>

<style lang="scss" scoped>
@import '../assets/css/navbar.css'
</style>