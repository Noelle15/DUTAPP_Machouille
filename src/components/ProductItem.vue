<template>
  <div class="product-item">
    {{ product.code }}:{{ product.name }}:{{ product.category }}:{{ product.price }}
  </div>
</template>

<script lang="ts">
import {Component, Prop, Vue} from 'vue-property-decorator'
import { Product } from "@/types/product"

@Component
export default class ProductItem extends Vue {
  @Prop({ type: Object, required: true })
  product!: Product
}
</script>

<style lang="scss" scoped>
.product-item {

}
</style>
