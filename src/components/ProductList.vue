<template>
  <div>
    <h3>Product lists ({{ filteredProducts.length }} products)</h3>
    <div>
      <button v-for="category of categories" :key="category" @click.prevent="filterOnCategory(category)">
        {{ category }}
      </button>
    </div>
    <div>
      <product-item v-for="product of filteredProducts" :key="product.code" :product="product" />
    </div>
  </div>
</template>

<script lang="ts">
import {Component, Prop, Vue} from 'vue-property-decorator'
import {Product, ProductsFilter} from "@/types/product";
import ProductItem from "@/components/ProductItem.vue";
@Component({
    components: {ProductItem}
})
export default class ProductList extends Vue {
  @Prop({ type: Array, required: true })
  products!: Product[]
  filter: ProductsFilter = {
    category: [],
    price: {}
  }

  get categories() {
    return [...new Set(this.products.map(item => item.category))]
  }

  get filteredProducts() {
    return this.products.filter((product) => {
      return this.filter.category.includes(product.category)
    })
  }

  filterOnCategory(category: string) {
    if (this.filter.category.includes(category)) {
      this.filter.category = this.filter.category.filter((cat) => cat != category)
    } else {
      this.filter.category.push(category)
    }
  }
}
</script>

<style lang="scss" scoped>

</style>
