import { createResource } from "solid-js"

import { base_url } from "../constants";
import { ProductInterface } from "../interface/product";

export const [products] = createResource<ProductInterface[]>(
  () => fetch(`${base_url}/api/products/list-view/`).then((res) => res.json()),
  {
    initialValue: [],
  }
)

export async function fetchSingleProduct(id: string) {
  const response = await fetch(`${base_url}/api/products/${id}/detail-view/`)
  try {
    const data = await response.json()
    return data
  } catch(e) {
    return window.location.href = '/error/'
  }
}