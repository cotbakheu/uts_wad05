<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import type { CreateInventoryItem } from '../type'

const name = ref('')
const location = ref('')
const category = ref('')
const stock = ref(0)
const imageUrl = ref('')
const router = useRouter()

const sendInventoryData = async (inventory: CreateInventoryItem) => {
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
    router.push({ name: 'home' })
  } catch (error) {
    console.error(error)
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

  sendInventoryData(newInventory)
}
</script>

<template>
  <div class="container">
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

      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
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
