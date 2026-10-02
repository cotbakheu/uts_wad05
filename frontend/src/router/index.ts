import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../modules/Home/View.vue'
import InventoryForm from '../modules/Inventory/Form/View.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/inventory/:id',
      name: 'inventory-form',
      component: InventoryForm,
    },
  ],
})

export default router
