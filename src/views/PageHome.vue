<template>
  <div class="page-container">
    <product-list :products="products" />
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import ProductList from "@/components/ProductList.vue";
import products from "../assets/products.json"

@Component({
  components: {ProductList}
})
export default class PageHome extends Vue {
  get products() {
    return products
  }
}
</script>

<style class="scss" scoped>
.page-container {
  background-color: #eee;
}
</style>
