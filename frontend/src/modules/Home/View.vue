<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import InventoryCard from './Components/InventoryCard.vue'
import type { InventoryItem, InventoryApiResponse } from '../Inventory/type'

const inventoryList = ref<InventoryItem[]>([])
const searchQuery = ref('')
const orderBy = ref<'asc' | 'desc'>('asc')

const fetchInventory = async () => {
  const queryParams = new URLSearchParams()
  if (searchQuery.value) {
    queryParams.append('name', searchQuery.value)
  }
  if (orderBy.value) {
    queryParams.append('order_by', orderBy.value)
  }
  try {
    const response = await fetch(`http://localhost:8000/inventory?${queryParams.toString()}`)
    if (!response.ok) {
      throw new Error('Failed to fetch inventory data')
    }
    const data: InventoryApiResponse = await response.json()
    inventoryList.value = data.data
  } catch (error) {
    console.error(error)
  }
}

const resetSearch = () => {
  searchQuery.value = ''
  orderBy.value = 'asc'
  fetchInventory()
}

watch(orderBy, () => {
  fetchInventory()
})

onMounted(() => {
  fetchInventory()
})
</script>

<template>
  <div class="container py-5">
    <div class="header">
      <h1 class="title">Current Available Inventory</h1>
      <p class="description">Here you can find the current available inventory.</p>
      <button
        class="btn btn-primary"
        @click="$router.push({ name: 'inventory-form', params: { id: 'new' } })"
      >
        Add New Inventory
      </button>
    </div>
    <div class="mb-3 d-flex justify-content-between align-items-center">
      <div class="d-flex gap-3">
        <input
          v-model="searchQuery"
          type="text"
          class="form-control"
          id="searchInventory"
          placeholder="Search Inventory by Name"
          style="width: 300px"
        />
        <button class="btn btn-primary" @click="fetchInventory">Search</button>
        <button class="btn btn-secondary" @click="resetSearch">Reset</button>
      </div>
      <div>
        <div class="dropdown">
          <button
            class="btn btn-secondary"
            type="button"
            data-bs-toggle="dropdown"
            aria-expanded="false"
          >
            Order By <i class="bi bi-filter"></i>
          </button>
          <ul class="dropdown-menu">
            <li>
              <button
                @click="orderBy = 'asc'"
                class="dropdown-item"
                :class="{ active: orderBy === 'asc' }"
                type="button"
              >
                ASC <i class="bi bi-sort-alpha-down"></i>
              </button>
            </li>
            <li>
              <button
                @click="orderBy = 'desc'"
                class="dropdown-item"
                :class="{ active: orderBy === 'desc' }"
                type="button"
              >
                DESC <i class="bi bi-sort-alpha-up"></i>
              </button>
            </li>
          </ul>
        </div>
      </div>
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
  justify-content: space-between;
}
</style>
