<template>
    <nav class="navbar  is-success" role="navigation" aria-label="main navigation">
        <div class="navbar-brand">
          <a class="navbar-item" href="https://bulma.io">
            <img src="../assets/images/book.jpg" width="55" height="40">
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
              Home
            </a>
      
            <a class="navbar-item">
              Documentation
            </a>
      
            <div class="navbar-item has-dropdown is-hoverable">
              <a class="navbar-link">
                More
              </a>
      
              <div class="navbar-dropdown">
                <a class="navbar-item" v-for="item in categories">
                  {{item.name}}
                </a>
               
              </div>
            </div>
          </div>
      
          <div class="navbar-end">
            <div class="navbar-item">
              <div class="buttons">
                <a class="button is-primary">
                  <strong>Sign up</strong>
                </a>
                <a class="button is-light">
                  Log in
                </a>
              </div>
            </div>
          </div>
        </div>
      </nav>
</template>

<script>
import axios from 'axios';

    export default {
        data (){
            return {
                categories:[]
            }
        },
        methods:{
            getcategories(){
                axios.get('api/book/category/').then(res=>{
                    this.categories = res.data
                    console.log(this.categories)
                })
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