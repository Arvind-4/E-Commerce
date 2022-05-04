let base_url = ''

if (process.env.NODE_ENV === 'production') {
    // base_url = String(process.env.SOLID_APP_BASE_URL)
    base_url = 'https://buyproductsonline.herokuapp.com'
} else {
    base_url = 'http://127.0.0.1:8000'
}

// base_url = 'http://127.0.0.1:8000'

// console.log('base_url', base_url)

export {
    base_url
}