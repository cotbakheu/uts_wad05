<script setup lang="ts">
import { ref, onMounted } from 'vue'
import InventoryCard from './Components/InventoryCard.vue'
import type { InventoryItem, InventoryApiResponse } from '../Inventory/type'

const inventoryList = ref<InventoryItem[]>([])

const fetchInventory = async () => {
  try {
    const response = await fetch('http://localhost:8000/inventory')
    if (!response.ok) {
      throw new Error('Failed to fetch inventory data')
    }
    const data: InventoryApiResponse = await response.json()
    inventoryList.value = data.data
  } catch (error) {
    console.error(error)
  }
}

onMounted(() => {
  fetchInventory()
})
</script>

<template>
  <div class="container py-5">
    <div class="header">
      <h1 class="title">Current Available Inventory</h1>
      <p class="description">Here you can find the current available inventory.</p>
    </div>
    <div class="inventory-list">
      <InventoryCard v-for="item in inventoryList" :key="item.id" :item="item" />
    </div>
  </div>
</template>

<style scoped>
.header {
  text-align: center;
  color: #000929;
}
.title {
  font-size: 36px;
  font-weight: bold;
  margin-bottom: 16px;
}
.description {
  font-size: 18px;
}

.inventory-list {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  justify-content: center;
}
</style>
