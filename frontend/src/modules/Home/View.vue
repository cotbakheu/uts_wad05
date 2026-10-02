<script setup lang="ts">
import { ref, onMounted, watch, computed } from 'vue'
import InventoryCard from './Components/InventoryCard.vue'
import type { InventoryItem, InventoryApiResponse } from '../Inventory/type'
import Loading from '@/components/Loading.vue'

const inventoryList = ref<InventoryItem[]>([])
const searchQuery = ref('')
const orderBy = ref<'asc' | 'desc'>('asc')
const isLoading = ref(false)

const totalInventory = computed(() => inventoryList.value.length)
const warningStockCount = computed(
  () => inventoryList.value.filter((item) => item.stock >= 0 && item.stock <= 10).length,
)
const categoryAmount = computed(() => {
  const categorySet = new Set(inventoryList.value.map((item) => item.category))
  return categorySet.size
})
const totalUnits = computed(() => {
  return inventoryList.value.reduce((total, item) => total + item.stock, 0)
})

const fetchInventory = async () => {
  const queryParams = new URLSearchParams()
  if (searchQuery.value) {
    queryParams.append('name', searchQuery.value)
  }
  if (orderBy.value) {
    queryParams.append('order_by', orderBy.value)
  }
  isLoading.value = true
  try {
    const response = await fetch(`http://localhost:8000/inventory?${queryParams.toString()}`)
    if (!response.ok) {
      throw new Error('Failed to fetch inventory data')
    }
    const data: InventoryApiResponse = await response.json()
    inventoryList.value = data.data
  } catch (error) {
    console.error(error)
  } finally {
    isLoading.value = false
  }
}

const resetSearch = () => {
  searchQuery.value = ''
  orderBy.value = 'asc'
  fetchInventory()
}

const handleItemDeleted = (id: number) => {
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
    <Loading :show="isLoading" />
    <div class="header">
      <h1 class="title">Current Available Inventory</h1>
      <p class="description">Here you can find the current available inventory.</p>
      <button
        class="btn btn-primary"
        @click="$router.push({ name: 'inventory-form', params: { id: 'new' } })"
      >
        Add New Inventory
      </button>
      <br />
      <br />
    </div>
    <div
      class="mb-3 d-flex flex-column flex-md-row justify-content-between align-items-md-center gap-3"
    >
      <div class="d-flex flex-column flex-md-row gap-3">
        <input
          v-model="searchQuery"
          type="text"
          class="form-control"
          id="searchInventory"
          placeholder="Search Inventory by Name"
        />
        <button class="btn btn-primary" @click="fetchInventory">Search</button>
        <button class="btn btn-secondary" @click="resetSearch">Reset</button>
      </div>
      <div>
        <div class="dropdown">
          <button
            class="btn btn-secondary w-100 w-md-auto"
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
    <div class="text-center not-found" v-if="inventoryList.length === 0">
      <div class="not-found-icon mb-3">
        <i class="bi bi-search"></i>
      </div>
      <p>No inventory items found.</p>
    </div>
    <div class="d-flex flex-wrap gap-2 mb-3" v-if="inventoryList.length > 0">
      <span class="badge bg-primary">Total Items: {{ totalInventory }}</span>
      <span class="badge bg-warning">Warning Stock: {{ warningStockCount }}</span>
      <span class="badge bg-info">Category Amount: {{ categoryAmount }}</span>
      <span class="badge bg-success">Total Units: {{ totalUnits }}</span>
    </div>
    <div
      class="inventory-list"
      :class="[{ 'justify-content-between': totalInventory > 4, 'gap-5': totalInventory <= 4 }]"
    >
      <InventoryCard
        v-for="item in inventoryList"
        :key="item.id"
        :item="item"
        @item-deleted="handleItemDeleted"
      />
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
  gap: 20px;
}

.not-found {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 200px;
}

.not-found-icon {
  font-size: 48px;
  color: #6c757d;
}

.not-found p {
  font-size: 18px;
  color: #6c757d;
}

.form-control {
  width: 300px;
}

@media (max-width: 768px) {
  .form-control {
    width: 100%;
  }
}
</style>
