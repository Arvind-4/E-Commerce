import type { Component } from "solid-js";
import { createMemo, For } from "solid-js";

import { useParams } from "solid-app-router";

import { products } from "../store/products";
import Product from "../snippits/Products";
import { ProductInterface } from "../interface/product";

const CategoryDetailpage: Component = () => {
  const { slug } = useParams()
  console.log('The Slug is ', slug)
  const filtered_products = createMemo(() =>
    products().filter((c) => c.category?.slug === slug)
  )

  console.log('The filtered os ', filtered_products())
  return (
    <>
      <div class='container mx-auto px-8'>
        <div class='mt-16'>
          <h3 class='text-gray-600 text-2xl font-medium'></h3>
          <div class='grid gap-6 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 mt-6'>
            <For each={filtered_products()}>
              {(cat_products: ProductInterface) => (
                <Product product={cat_products} />
              )}
            </For>
          </div>
        </div>
      </div>
    </>
  )
}

export default CategoryDetailpage