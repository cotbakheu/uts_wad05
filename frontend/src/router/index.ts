import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../modules/Home/View.vue'
import CreatePropertyView from '../modules/CreateProperty/View.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/create-property',
      name: 'create-property',
      component: CreatePropertyView,
    },
  ],
})

export default router
