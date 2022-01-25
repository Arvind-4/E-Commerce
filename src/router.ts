import Homepage from './pages/Homepage'
import ProductListpage from './pages/ProductListpage'
import ProductDetailpage from './pages/ProductDetailpage'
import Categorypage from './pages/Categorypage'
import Contactpage from './pages/Contactpage'
import Aboutpage from './pages/Aboutpage'
import CategoryDetailpage from './pages/CategoryDetailpage'

export const routes = [
    {
      path: "/",
      component: Homepage
    },
    {
      path: "/products/",
      component: ProductListpage,
    },
    {
      path: "/categories/",
      component: Categorypage,
    },
    {
      path: "/contact-us/",
      component: Contactpage,
    },
    {
      path: "/about-us/",
      component: Aboutpage,
    },
    {
      path: "/category/:slug/",
      component: CategoryDetailpage,
    },
    {
      path: "/:id/detail-view/:slug/",
      component: ProductDetailpage,
    },
    {
        path: '/accounts/sign-in/'
    },
    {
        path: '/accounts/sign-up/'
    },
    {
        path: '/accounts/sign-out/'
    },
    {
        path: '/accounts/password-reset/'
    },
    {
        path: '/accounts/password-reset-done/'
    },
    {
        path: '/accounts/password-reset-confirm/:uidb64/:token/'
    },
    {
        path: '/accounts/password-reset-complete/'
    },
    {
        path: '/accounts/change-password/'
    },
  ]