import Homepage from './pages/Homepage'
import ProductListpage from './pages/ProductListpage'
import Categorypage from './pages/Categorypage'
import Contactpage from './pages/Contactpage'
import Aboutpage from './pages/Aboutpage'
import Accountpage from './pages/Accountspage'

export const routes = [
  {
    path: '/',
    component: Homepage
  },
  {
    path: '/products/',
    component: ProductListpage,
  },
  {
    path: '/categories/',
    component: Categorypage,
  },
  {
    path: '/contact-us/',
    component: Contactpage,
  },
  {
    path: '/about-us/',
    component: Aboutpage,
  },
  {
    path: '/accounts/',
    component: Accountpage,
  },
]