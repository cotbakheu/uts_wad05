<script setup lang="ts">
import { ref, computed } from 'vue'
import type { InventoryItem } from '../../Inventory/type'
import swal from 'sweetalert2'
import Loading from '@/components/Loading.vue'

const emit = defineEmits<{
  (e: 'itemDeleted', id: number): void
}>()

const props = defineProps<{
  item: InventoryItem
}>()

const isLoading = ref(false)

const stockStatus = computed(() => {
  if (props.item.stock > 10) {
    return 'In Stock'
  } else if (props.item.stock > 0) {
    return 'Low Stock'
  } else {
    return 'Out of Stock'
  }
})

const deleteItem = async () => {
  isLoading.value = true
  try {
    const response = await fetch(`http://localhost:8000/inventory/${props.item.id}`, {
      method: 'DELETE',
    })

    if (!response.ok) {
      throw new Error('Failed to delete inventory item')
    }
    swal.fire({
      title: 'Deleted!',
      text: 'The inventory item has been deleted.',
      icon: 'success',
      confirmButtonText: 'OK',
    })
    // Emit an event to notify the parent component that the item has been deleted
    emit('itemDeleted', props.item.id)
  } catch (error) {
    swal.fire({
      title: 'Error!',
      text: 'Failed to delete the inventory item.',
      icon: 'error',
      confirmButtonText: 'OK',
    })
    console.error(error)
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <div class="card">
    <Loading :show="isLoading" />
    <div>
      <img :src="item.imageUrl" class="card-img-top" alt="{{ item.name }}" />
    </div>
    <div class="card-body">
      <h5 class="card-title">{{ item.name }}</h5>
      <p class="card-text"><strong>Location:</strong> {{ item.location }}</p>
      <div class="d-flex justify-content-between w-100 align-items-start mb-3">
        <span class="badge bg-primary">Category: {{ item.category }}</span>
        <div class="d-flex flex-column align-items-end gap-1">
          <span class="badge bg-success">Stock: {{ item.stock }}</span>
          <span class="badge bg-info" v-if="stockStatus === 'In Stock'">In Stock</span>
          <span class="badge bg-warning" v-if="stockStatus === 'Low Stock'">Low Stock</span>
          <span class="badge bg-danger" v-if="stockStatus === 'Out of Stock'">Out of Stock</span>
        </div>
      </div>
      <div class="d-flex justify-content-end align-items-center gap-2">
        <button @click="deleteItem" class="btn btn-danger"><i class="bi bi-trash"></i></button>
        <router-link
          :to="{ name: 'inventory-form', params: { id: item.id } }"
          class="btn btn-primary"
          ><i class="bi bi-pencil-square"></i
        ></router-link>
      </div>
    </div>
  </div>
</template>

<style scoped>
.card img {
  height: 270px;
  width: 100%;
}

.card {
  width: 18rem;
}

@media (max-width: 768px) {
  .card {
    width: 100%;
  }
}
</style>
