<template>
  <nav>
    <Navbar />
  </nav>
  <router-view/>
</template>
<script>
import Navbar from './components/navbar.vue'
    export default {
        components:{
          Navbar
        }
    }
</script>
<style lang="scss">
@import '../node_modules/bulma'
</style>
