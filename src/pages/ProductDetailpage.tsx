import type { Component } from 'solid-js'
import { createMemo } from 'solid-js'

import { useParams, useNavigate } from 'solid-app-router'

import { products } from '../store/products'

const ProductDetailpage: Component = () => {
  const navigate = useNavigate()
  const { id } = useParams()
  const product = createMemo(() =>
    products().filter((p) => p.id === id)[0]
  )

  if (product() !== undefined) {

    return (
      <div>
        <div>{product().title}</div>
      </div>
    )
  } else {
    navigate('/', {
      replace: true
    })
  }
}

export default ProductDetailpage
