import type { Component } from 'solid-js'
import { Routes, Route, useRoutes, useNavigate, Navigate } from 'solid-app-router'

import { routes } from './router'
import Header from './snippits/Header'

import CategoryDetailpage from './pages/CategoryDetailpage'
import ProductDetailpage from './pages/ProductDetailpage'
import Errorpage from './pages/Errorpage'

const App: Component = () => {
  const navigate = useNavigate()
  const URL = useRoutes(routes)
  return (
    <>
      <Header />
      <URL />
      <Routes>
        <Route path="/category/:slug/" element={<CategoryDetailpage />} />
        <Route path="/:id/detail-view/" element={<ProductDetailpage />} />
      </Routes>
      <Routes>
        {/* <Navigate href={'/error/'} /> */}
      </Routes>
    </>
  )
}

export default App
