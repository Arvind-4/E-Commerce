import { Component } from 'solid-js'
import { createSignal, Show, Switch, Match, For } from 'solid-js'

import { CartInterface, ProductInterface } from '../interface/product'
import { cartproducts } from '../store/cart'
import { deleteProduct } from '../store/cart'
import { Navlinks } from './Navlinks'

const Header: Component = () => {

  const [isCartOpen, setisCartOpen] = createSignal(false)
  const [isNavOpen, setNavOpen] = createSignal(false)
  return (
    <>
      <header>
        <div class='container mx-auto px-6 py-3'>
          <div class='flex items-center justify-between'>
            <div class='hidden w-full text-gray-600 md:flex md:items-center'>
              <i class="fas fa-map-marker-alt"></i>
              <span class='mx-1 text-sm'>  Chennai</span>
            </div>
            <div class='w-full text-gray-700 md:text-center text-2xl font-semibold'>
              E-commerce
            </div>
            <div class='flex items-center justify-end w-full'>
              <button onclick={() => setisCartOpen(!isCartOpen())}>
                <div class='flex flex-row cursor-pointer truncate p-2 px-4  rounded'>
                  <div></div>
                  <div class='flex flex-row-reverse ml-2 w-full'>
                    <div class='relative'>
                      <div class='absolute text-xs rounded-full -mt-1 -mr-2 px-1 font-bold top-0 right-0 bg-red-700 text-white'>
                        <For each={cartproducts()} fallback={<div>0</div>} >
                          {(carto: CartInterface) => (
                            <span>{carto.products.length}</span>
                          )}
                        </For>
                      </div>
                      <svg
                        xmlns='http://www.w3.org/2000/svg'
                        width='100%'
                        height='100%'
                        fill='none'
                        viewBox='0 0 24 24'
                        stroke='currentColor'
                        stroke-width='2'
                        stroke-linecap='round'
                        stroke-linejoin='round'
                        class='feather feather-shopping-cart w-6 h-6 mt-2'
                      >
                        <circle cx='9' cy='21' r='1'></circle>
                        <circle cx='20' cy='21' r='1'></circle>
                        <path d='M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6'></path>
                      </svg>
                    </div>
                  </div>
                </div>
              </button>
              <Show when={isCartOpen()} fallback={<div></div>}>
                <div class='absolute mt-96 rounded-b border-t-0 z-10 h-80 flex-grow overflow-y-auto'>
                  <For each={cartproducts()} fallback={<div></div>}>
                    {(cart) => (
                      <div class='shadow-xl w-64'>
                        <div>
                          {cart.products.map((cp: ProductInterface) => (
                            <div
                              class='p-2 flex bg-white hover:bg-gray-100 cursor-pointer border-b border-gray-100'
                              style=''
                            >
                              <div class='p-2 w-12'>
                                <img
                                  src={cp.image_url}
                                  alt={cp.slug}
                                />
                              </div>
                              <div class='flex-auto text-sm w-32'>
                                <div class='font-bold'>{cp.title}</div>
                                {/* <div class='truncate'>{cp.price}</div> */}
                                {/* <div class='text-gray-400'>Qt: 2</div> */}
                              </div>
                              <div class='flex flex-col w-18 font-medium items-end'>
                                <div class='w-4 h-4 mb-6 hover:bg-red-200 rounded-full cursor-pointer text-red-700'>
                                  <button onclick={() => deleteProduct(cp)}>
                                    <i class="far fa-trash-alt"></i>
                                  </button>
                                </div>
                                ${cp.price}
                              </div>
                            </div>
                          ))}
                        </div>
                        <p class='text-center py-1'>The Sub-Total is {cart.subtotal}</p>
                        <div class='p-4 justify-center flex'>

                          <button
                            class='text-base  undefined  hover:scale-110 focus:outline-none flex justify-center px-4 py-2 rounded font-bold cursor-pointer hover:bg-teal-700 hover:text-teal-100 bg-teal-100 text-teal-700 border duration-200 ease-in-out border-teal-600 transition'
                          >
                            Checkout ${cart.total}
                          </button>
                        </div>
                      </div>
                    )}
                  </For>
                </div>
              </Show>
              <div class='flex sm:hidden'>
                <button onClick={() => setNavOpen(!isNavOpen())}
                  type='button'
                  class='text-gray-600 hover:text-gray-500 focus:outline-none focus:text-gray-500'
                  aria-label='toggle menu'
                >
                  <svg viewBox='0 0 24 24' class='h-6 w-6 fill-current'>
                    <path
                      fill-rule='evenodd'
                      d='M4 5h16a1 1 0 0 1 0 2H4a1 1 0 1 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2z'
                    ></path>
                  </svg>
                </button>
              </div>
            </div>
          </div>
          <nav class='sm:flex sm:justify-center sm:items-center mt-4'>
            <div class='hidden lg:flex flex-row md:flex flex-row'>
              <Navlinks />
            </div>
          </nav>
          <Switch fallback={''}>
            <Match when={isNavOpen()}>
              <nav class='sm:flex sm:justify-center sm:items-center mt-4'>
                <div class='flex flex-col sm:flex-row'>
                  <Navlinks />
                </div>
              </nav>
            </Match>
          </Switch>
          <div class='relative mt-6 max-w-lg mx-auto'>
            <span class='absolute inset-y-0 left-0 pl-3 flex items-center'>
              <i class="fas fa-search"></i>
            </span>
            <input
              class='w-full border rounded-md pl-10 pr-4 py-2 focus:border-blue-500 focus:outline-none focus:shadow-outline'
              type='text'
              placeholder='Search'
            />
          </div>
        </div>
      </header>
    </>
  )
}

export default Header
