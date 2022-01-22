import type { Component } from 'solid-js'
import { Route, Routes } from 'solid-app-router'

import Homepage from './pages/Homepage'
import ProductListpage from './pages/ProductListpage'
import ProductDetailpage from './pages/ProductDetailpage'
import Categorypage from './pages/Categorypage'
import Contactpage from './pages/Contactpage'
import Aboutpage from './pages/Aboutpage'
import CategoryDetailpage from './pages/CategoryDetailpage'
import Errorpage from './pages/Errorpage'

import Header from './snippits/Header'

const App: Component = () => {
  return (
    <>
      <Header />
      <Routes>
        <Route path='/' element={<Homepage />} />
        <Route path='/products/' element={<ProductListpage />} />
        <Route path='/categories/' element={<Categorypage />} />
        <Route path='/contact-us/' element={<Contactpage />} />
        <Route path='/about-us/' element={<Aboutpage />} />

        <Route path='/category/:slug/' element={<CategoryDetailpage />} />
        <Route path='/:id/detail-view/:slug/' element={<ProductDetailpage />} />

      </Routes>
    </>
  )
}

export default App
