import type { Component } from 'solid-js'
import { useLocation, useRoutes } from 'solid-app-router'

import { routes } from './router'
import Header from './snippits/Header'

const App: Component = () => {
  const location = useLocation()
  const exists = routes.some(route => route.path === location.pathname);
  if (exists === false) {
    return window.location.href = '/error/'
  }
  const URL = useRoutes(routes)
  return (
    <>
      <Header />
      <URL />
    </>
  )
}

export default App
