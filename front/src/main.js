import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import i18n from './i18n'
const language = localStorage.getItem('language') || 'en'

axios.defaults.baseURL = `https://mybookme.pythonanywhere.com/${language}/`
createApp(App).use(i18n).use(store).use(router).mount('#app')
