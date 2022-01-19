import { createResource } from "solid-js"

import { base_url } from "../constants";
import { ProductInterface } from "../interface/product";

export const [products] = createResource<ProductInterface[]>(
  () => fetch(`${base_url}/api/products/list-view/`).then((res) => res.json()),
  {
    initialValue: [],
  }
)