import { Component, Show } from 'solid-js'
import { For } from 'solid-js'

import { createResource } from 'solid-js'
import { baseUrl } from '../constants'
import { ProductInterface } from '../interface/product'
// import { products } from '../store/products'
import Product from '../snippits/Products'

const ProductListpage: Component = () => {
  console.log("baseUrl", baseUrl)
  const [products] = createResource<ProductInterface[]>(
    () => fetch(`${baseUrl}/api/products/list-view/`).then((res) => res.json())
    .catch((err) => console.log(err)),
    {
      initialValue: [],
    }
  )
  console.log('The Products is ', products())
  return (
    <>
      <div class='container mx-auto px-8'>
        <div class='mt-16'>
          <h3 class='text-gray-600 text-2xl font-medium'></h3>
          <div class='grid gap-6 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 mt-6'>
            <For each={products()}>
              {(product) => (
                <Show when={product}>
                <Product product={product} />
                </Show>
              )}
            </For>
          </div>
        </div>
      </div>
    </>
  )
}

export default ProductListpage
