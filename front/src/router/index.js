import { createRouter, createWebHistory } from 'vue-router'
import Main from '../views/Main.vue'
const routes = [
  {
    path: '/',
    name: 'home',
    component: Main
  },
  {
    path:'/book/:id/',
    name:'BookAbout',
    component:() => import("@/views/BookAbout.vue"),
   },
   {
    path:'/category/:id/',
    name:'Category',
    component:() => import("@/views/Category.vue"),
   },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
