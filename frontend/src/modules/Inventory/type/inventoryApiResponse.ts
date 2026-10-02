import type { InventoryItem } from './inventoryType'

export type InventoryApiResponse = {
  data: InventoryItem[]
  message: string
  status: number
}
