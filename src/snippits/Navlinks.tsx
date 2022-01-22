import type { Component } from "solid-js";
import { Switch, Match } from "solid-js";

import { is_authenticated } from '../store/auth'
import { logoutUser } from '../store/auth'

export const Navlinks: Component = () => {
  return <>
    <a
      class='mt-3 text-gray-600 hover:underline sm:mx-3 sm:mt-0'
      href='/'
    >
      Home
    </a>
    <a
      class='mt-3 text-gray-600 hover:underline sm:mx-3 sm:mt-0'
      href='/products/'
    >
      Products
    </a>
    <a
      class='mt-3 text-gray-600 hover:underline sm:mx-3 sm:mt-0'
      href='/categories/'
    >
      Categories
    </a>
    <a
      class='mt-3 text-gray-600 hover:underline sm:mx-3 sm:mt-0'
      href='/contact-us/'
    >
      Contact
    </a>
    <a
      class='mt-3 text-gray-600 hover:underline sm:mx-3 sm:mt-0'
      href='/about-us/'
    >
      About
    </a>
    <Switch fallback={<div>Not Found</div>}>
      <Match when={is_authenticated === 'true'}>
        <a
          class='mt-3 text-gray-600 hover:underline sm:mx-3 sm:mt-0'
          onclick={() => logoutUser()}
        >
          Sign Out <i class="fas fa-sign-out-alt"></i>
        </a>

      </Match>
      <Match when={is_authenticated !== 'true'}>
        <a
          class='mt-3 text-gray-600 hover:underline sm:mx-3 sm:mt-0'
          href='/accounts/sign-in/'
        >
          Sign In <i class="fas fa-sign-in-alt"></i>
        </a>
        <a
          class='mt-3 text-gray-600 hover:underline sm:mx-3 sm:mt-0'
          href='/accounts/sign-up/'
        >
          Sign Up <i class="fas fa-user-plus"></i>
        </a>
      </Match>
    </Switch>
  </>
};
