export type Product = {
    code: string
    name: string
    category: string
    price: number
}

export type ProductsFilter = {
    category: string[]
    price: {
        min?: number,
        max?: number
    }
}
