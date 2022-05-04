import { Component, createSignal, Show } from "solid-js";
import axios from "axios";

import { base_url } from "../constants";

const [search, setSearch] = createSignal("");
const [data, setData] = createSignal([]);

export const SearchBox: Component = () => {
  async function searchData(e: any) {
    setSearch(e.currentTarget.value)
    const endpoint = `${base_url}/api/search/`
    if (search().length >  0){
      const res = await axios.get(endpoint, { params: { q: JSON.stringify(search()) } });
      console.log(res.data.hits)
      setData(res.data.hits)
    }
  }
    return (
        <>
        <div class='relative mt-6 max-w-lg mx-auto'>
            <span class='absolute inset-y-0 left-0 pl-3 flex items-center'>
              <i class="fas fa-search"></i>
            </span>
            <input
              class='w-full border rounded-md pl-10 pr-4 py-2 focus:border-blue-500 focus:outline-none focus:shadow-outline'
              type='text'
              value={search()}
              onkeyup={(e) => searchData(e)}
              placeholder='Search'
            />
              <Show
                when={data().length > 0 && search() !== ""}
                fallback={<div></div>}
              >
              <ol class='text-center'>
          
                <li>
                  {data().map((item: any) => (
                    <div class=''>
                      {item.item}
                      </div>
                  ))}
                </li>
              </ol>
          </Show>
          </div>
        
        </>
    )
}