<template>
  <PageLoader v-if="loading"> </PageLoader>
  <div v-if="!loading">
    <nav>
      <Navbar />
    </nav>
    <router-view/>
    <Footer />
  </div>
</template>
<script>
import Navbar from './components/navbar.vue'
import Footer from './components/footer.vue'
import PageLoader from './components/pageloader.vue'
    export default {
        data(){
          return {
            loading:true,
          }
        },
        components:{
          Navbar,Footer,PageLoader
        },
        mounted(){
          setTimeout(() => {
      this.loading = false;
    }, 1500);
  }
        }

    
</script>
<style lang="scss">
@import '../node_modules/bulma'
</style>
