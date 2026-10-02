import type { InventoryItem } from './inventoryType'

type ApiResponse<T> = {
  data: T
  message: string
  status: number
}

export type InventoryApiResponse = ApiResponse<InventoryItem[]>

export type InventoryDetailApiResponse = ApiResponse<InventoryItem>
