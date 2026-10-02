<script setup lang="ts">
import type { InventoryItem } from '../../Inventory/type'

defineProps<{
  item: InventoryItem
}>()
</script>

<template>
  <div class="card" style="width: 18rem">
    <div>
      <img :src="item.imageUrl" class="card-img-top" alt="{{ item.name }}" />
    </div>
    <div class="card-body">
      <h5 class="card-title">{{ item.name }}</h5>
      <p class="card-text"><strong>Location:</strong> {{ item.location }}</p>
      <div class="d-flex justify-content-between align-items-center mb-2">
        <span class="badge bg-primary">Category: {{ item.category }}</span>
        <span class="badge bg-success">Stock: {{ item.stock }}</span>
      </div>
      <div>
        <router-link
          :to="{ name: 'inventory-form', params: { id: item.id } }"
          class="btn btn-primary w-100"
          >Edit</router-link
        >
      </div>
    </div>
  </div>
</template>

<style scoped>
.card img {
  height: 270px;
  width: 100%;
}
</style>
