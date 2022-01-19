import { createResource } from "solid-js"

import { base_url } from "../constants"
import { CategoryInterface } from "../interface/product"

export const [categories] = createResource<CategoryInterface[]>(
    () => fetch(`${base_url}/api/category/list/`).then((res) => res.json()),
    {
        initialValue: [],
    }
)