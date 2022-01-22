import { Link } from "solid-app-router";
import type { Component } from "solid-js";
import { For, Show } from "solid-js";

import { categories } from "../store/category";

const Categorypage: Component = () => {
  console.log(categories())
  return <>
    <div>
      <div class="container mx-auto px-4 lg:pt-10 lg:pb-64">
        <For each={categories()} fallback={<div>Loading ...</div>}>
          {(category) => (
            <div>
              <div class="flex flex-wrap mt-4 justify-center">
                <div class="grid grid-cols-1 sm:grid-cols-6 md:grid-cols-6 lg:grid-cols-6 xl:grid-cols-6 gap-4">
                  <div class="col-span-2 sm:col-span-1 xl:col-span-1">
                    {/* <img
                      alt={category.slug}
                      src="https://media.istockphoto.com/photos/vitamin-d-illuminated-by-the-rays-of-the-sun-on-grass-sunlight-is-an-picture-id1301094916?b=1&k=20&m=1301094916&s=170667a&w=0&h=QeBE-rB8f2yQkcUxvswEGK_RRpmpqBEBB1iFoFpJeYE="
                      class="h-24 w-24 rounded  mx-auto"
                    /> */}
                  </div>
                  <div class="col-span-2 sm:col-span-4 xl:col-span-4">
                    <Link href={`/category/${category.slug}/`} >
                      <h3 class="text-center font-semibold text-black">{category.category}</h3>
                    </Link>
                    <Show when={category.text} fallback={<div></div>}>
                      <p>
                        {category.text}
                      </p>
                    </Show>
                  </div>
                </div>
              </div>
            </div>
          )}
        </For>
      </div>
    </div>

  </>;
};

export default Categorypage;
