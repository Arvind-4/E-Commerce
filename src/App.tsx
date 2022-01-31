import type { Component } from 'solid-js'
import { Routes, Route, useRoutes } from 'solid-app-router'

import { routes } from './router'
import Header from './snippits/Header'

import CategoryDetailpage from './pages/CategoryDetailpage'
import ProductDetailpage from './pages/ProductDetailpage'

const App: Component = () => {
  const URL = useRoutes(routes)
  return (
    <>
      <Header />
      <URL />
      <Routes>
        <Route path="/category/:slug/" element={<CategoryDetailpage />} />
        <Route path="/:id/detail-view/" element={<ProductDetailpage />} />
      </Routes>
    </>
  )
}

export default App
