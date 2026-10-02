export type InventoryItem = {
  id: number
} & CreateInventoryItem

export type CreateInventoryItem = {
  name: string
  category: string
  stock: number
  location: string
  imageUrl: string
}
