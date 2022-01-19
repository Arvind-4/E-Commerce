import type { Component } from 'solid-js'

import { is_authenticated } from '../store/auth'

const Homepage: Component = () => {
  return (
    <div>
      {is_authenticated}
    </div>
  )
}

export default Homepage
