import type { Component } from 'solid-js'
import { useParams } from 'solid-app-router'
import { createMemo } from 'solid-js'
import { Show } from 'solid-js'

import { products } from '../store/products'

const ProductDetailpage: Component = () => {
  const params = useParams()
  const product: any = createMemo(() =>
    products().find((p) => p.id === params.id)
  )
  console.log('The product', product())
  return (
    <div>
      <Show when={product()} fallback={<div>Loading...</div>}>
        <div>{product().title}</div>
        <div>{product().price}</div>
      </Show>
    </div>
  )
}

export default ProductDetailpage
