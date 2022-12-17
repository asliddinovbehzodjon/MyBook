<template>
    <nav class="navbar  is-success" role="navigation" aria-label="main navigation">
        <div class="navbar-brand">
          <a class="navbar-item" href="https://bulma.io">
            <img src="../assets/images/book.jpg" width="55" height="40" class="img">
          </a>
      
          <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
          </a>
        </div>
      
        <div id="navbarBasicExample" class="navbar-menu">
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
                  {{item.name}}
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
        }
    
    }
</script>

<style lang="scss" scoped>
@import '../assets/css/navbar.css'
</style>