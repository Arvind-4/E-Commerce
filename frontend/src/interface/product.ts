export interface ProductInterface {
    id: string;
    title: string;
    slug: string;
    price: number;
    category?: CategoryInterface
    description: string;
    instock: boolean;
    offer_badge: boolean;
    popular_items: boolean;
    new_arrivals: boolean;
    width_field: number;
    height_field: number;
    image?: string;
    image_url?: string;
}

export interface CategoryInterface {
    category: string;
    text: string;
    slug: string;
}

export interface CartInterface {
    user: string;
    products: ProductInterface
    subtotal: number;
    total: number;
    updated: string;
    timestamp: string;
}

