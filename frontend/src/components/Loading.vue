```vue
<script setup lang="ts">
defineProps<{
  show: boolean
}>()
</script>

<template>
  <div v-if="show" class="loading-overlay">
    <div class="spinner-border text-primary" style="width: 3rem; height: 3rem" role="status">
      <span class="visually-hidden">Loading...</span>
    </div>
  </div>
</template>

<style scoped>
.loading-overlay {
  position: absolute;
  inset: 0;

  display: flex;
  align-items: center;
  justify-content: center;

  background: rgba(255, 255, 255, 0.7);

  z-index: 1000;
}
</style>
