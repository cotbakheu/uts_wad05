<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import type { CreateInventoryItem, InventoryDetailApiResponse } from '../type'
import swal from 'sweetalert2'
import Loading from '@/components/Loading.vue'

const isLoading = ref(false)
const name = ref('')
const location = ref('')
const category = ref('')
const stock = ref(0)
const imageUrl = ref('')
const router = useRouter()
const params = router.currentRoute.value.params

const createInventory = async (inventory: CreateInventoryItem) => {
  try {
    const response = await fetch('http://localhost:8000/inventory', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(inventory),
    })

    if (!response.ok) {
      throw new Error('Failed to create inventory item')
    }

    const data = await response.json()
    await swal.fire({
      title: 'Success',
      text: 'Inventory item created successfully',
      icon: 'success',
    })
    router.push({ name: 'home' })
  } catch (error) {
    swal.fire({
      title: 'Error',
      text: 'Failed to create inventory item',
      icon: 'error',
    })
    console.error(error)
  }
}

const updateInventory = async (id: string, inventory: CreateInventoryItem) => {
  isLoading.value = true
  try {
    const response = await fetch(`http://localhost:8000/inventory/${id}`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(inventory),
    })

    if (!response.ok) {
      throw new Error('Failed to update inventory item')
    }

    const data = await response.json()
    await swal.fire({
      title: 'Success',
      text: 'Inventory item updated successfully',
      icon: 'success',
    })
    router.push({ name: 'home' })
  } catch (error) {
    await swal.fire({
      title: 'Error',
      text: 'Failed to update inventory item',
      icon: 'error',
    })
    console.error(error)
  } finally {
    isLoading.value = false
  }
}

const submitForm = (event: Event) => {
  event.preventDefault()
  const newInventory: CreateInventoryItem = {
    name: name.value,
    location: location.value,
    category: category.value,
    stock: stock.value,
    imageUrl: imageUrl.value,
  }

  if (params.id && params.id !== 'new') {
    updateInventory(params.id as string, newInventory)
  } else {
    createInventory(newInventory)
  }
}

const fetchInventoryData = async (id: string) => {
  isLoading.value = true
  try {
    const response = await fetch(`http://localhost:8000/inventory/${id}`)
    if (!response.ok) {
      throw new Error('Failed to fetch inventory data')
    }
    const responseData: InventoryDetailApiResponse = await response.json()
    const data = responseData.data
    name.value = data.name
    location.value = data.location
    category.value = data.category
    stock.value = data.stock
    imageUrl.value = data.imageUrl
  } catch (error) {
    swal
      .fire({
        title: 'Error',
        text: 'Failed to fetch inventory data',
        icon: 'error',
      })
      .then(() => {
        router.push({ name: 'home' })
      })
    console.error(error)
  } finally {
    isLoading.value = false
  }
}

onMounted(() => {
  if (params.id && params.id !== 'new') {
    fetchInventoryData(params.id as string)
  }
})
</script>

<template>
  <div class="container">
    <Loading :show="isLoading" />
    <div class="header">
      <h1>Create Inventory</h1>
      <p>This is the create inventory page of the Inventory App.</p>
    </div>
    <form class="w-50 mx-auto" @submit="submitForm">
      <div class="mb-3">
        <label for="inventoryName" class="form-label">Name</label>
        <input
          type="text"
          class="form-control"
          id="inventoryName"
          placeholder="Enter inventory name"
          v-model="name"
        />
      </div>
      <div class="mb-3">
        <label for="inventoryLocation" class="form-label">Location</label>
        <input
          type="text"
          class="form-control"
          id="inventoryLocation"
          placeholder="Enter inventory location"
          v-model="location"
        />
      </div>
      <div class="mb-3">
        <label for="inventoryCategory" class="form-label">Category</label>
        <input
          type="text"
          class="form-control"
          id="inventoryCategory"
          placeholder="Enter inventory category"
          v-model="category"
        />
      </div>
      <div class="mb-3">
        <label for="inventoryStock" class="form-label">Stock</label>
        <input
          type="number"
          class="form-control"
          id="inventoryStock"
          placeholder="Enter inventory stock"
          v-model="stock"
        />
      </div>
      <div class="mb-3">
        <label for="inventoryImage" class="form-label">Image URL</label>
        <input
          type="text"
          class="form-control"
          id="inventoryImage"
          placeholder="Enter inventory image URL"
          v-model="imageUrl"
        />
        <div class="display-image" v-if="imageUrl">
          <img :src="imageUrl" :alt="name" />
        </div>
      </div>

      <div class="d-flex justify-content-end">
        <button
          type="button"
          class="btn btn-secondary me-2"
          @click="$router.push({ name: 'home' })"
        >
          Cancel
        </button>
        <button type="submit" class="btn btn-primary">Submit</button>
      </div>
    </form>
    <br />
    <br />
  </div>
</template>

<style scoped>
.header {
  text-align: center;
  color: #000929;
}
.display-image {
  margin-top: 10px;
}

.display-image img {
  max-width: 100%;
  height: auto;
  border-radius: 5px;
}
</style>
