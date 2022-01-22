import { createResource } from "solid-js"
import { createMutable } from 'solid-js/store'

import { base_url } from "../constants"
import { CartInterface, ProductInterface } from "../interface/product"
import { is_authenticated } from "./auth"

export async function fetchUserCart() {
    if (is_authenticated === 'true') {
        const res = await fetch(`${base_url}/api/cart/`)
        const data = await res.json()
        return data
    } else {
        return []
    }
}


export const [cartproducts, { refetch }] = createResource<CartInterface[]>(
    () => fetchUserCart(),
    {
        initialValue: []
    }
)

export const dataRefetch = function () {
    refetch()
    return null
}

export const cart = createMutable({
    addProduct({ product }: { product: ProductInterface }) {
        try {
            const response = fetch(`${base_url}/api/cart/add/${product.slug}/${product.id}/`)
            return true
        } catch {
            return false

        }
    },
    removeProduct({ product }: { product: ProductInterface }) {
        try {
            const response = fetch(`${base_url}/api/cart/remove/${product.slug}/${product.id}/`)
            return true
        } catch {
            return false

        }
    }
})

export async function deleteProduct(product: ProductInterface) {
    if (is_authenticated === 'true') {
        const value = cart.removeProduct({ product })
        if (value) {
            alert(`${product.title} has been removed from Cart!`)
            dataRefetch()
        } else {
            alert(`Failed`)
        }

    } else {
        var url = window.location.pathname
        var login_redirect = `/accounts/sign-in/?next=${url}`
        window.location.href = url.replace(url, login_redirect)
    }
}

export async function navigateUser(product: ProductInterface) {
    if (is_authenticated === 'true') {
        const value = cart.addProduct({ product })
        if (value) {
            alert(`${product.title} has been added to the Cart!`)
            dataRefetch()
        } else {
            alert(`Failed`)
        }
    } else {
        var url = window.location.pathname
        var login_redirect = `/accounts/sign-in/?next=${url}`
        window.location.href = url.replace(url, login_redirect)
    }

}