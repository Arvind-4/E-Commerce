import type { Component } from 'solid-js'
import { Route, Routes } from 'solid-app-router'

import Homepage from './pages/Homepage'
import Aboutpage from './pages/Aboutpage'
import ProductListpage from './pages/ProductListpage'
import ProductDetailpage from './pages/ProductDetailpage'
import Categorypage from './pages/Categorypage'
import Errorpage from './pages/Errorpage'

import Header from './snippits/Header'

const App: Component = () => {
  return (
    <>
      <Header />
      <Routes>
        <Route path='/' element={<Homepage />} />
        <Route path='/about/' element={<Aboutpage />} />
        <Route path='/products/' element={<ProductListpage />} />
        <Route path='/categories/' element={<Categorypage />} />

        <Route path='/:id/detail-view/:slug/' element={<ProductDetailpage />} />

      </Routes>
    </>
  )
}

export default App
