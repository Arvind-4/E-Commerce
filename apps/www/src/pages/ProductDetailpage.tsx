import type { Component } from 'solid-js'
import { createResource, Show } from 'solid-js'

import { useParams } from 'solid-app-router'

import { ProductInterface } from '../interface/product'
import { navigateUser } from '../store/cart'
import { baseUrl } from '../constants'

async function fetchSingleProduct(id: string) {
  const response = await fetch(`${baseUrl}/api/products/${id}/detail-view/`)
  try {
    const data = await response.json()
    return data
  } catch(e) {
    return window.location.href = '/error/'
  }
}

const ProductDetailpage: Component = () => {
  const params = useParams()
  const [singleProduct ] = createResource<ProductInterface>(
    () => fetchSingleProduct(params.id)
  ) || undefined
  return (
    <>
      <section class="text-gray-700 body-font overflow-hidden bg-white">
        <div class="container px-5 py-24 mx-auto">
          <div class="lg:w-4/5 mx-auto flex flex-wrap">
            <img alt="ecommerce" class="lg:w-1/2 w-full object-cover object-center rounded border border-gray-200" src={singleProduct()?.image_url} />
            <div class="lg:w-1/2 w-full lg:pl-10 lg:py-6 mt-6 lg:mt-0">
              {/* <h2 class="text-sm title-font text-gray-500 tracking-widest">BRAND NAME</h2> */}
              <h1 class="text-gray-900 text-3xl title-font font-medium mb-1">{singleProduct()?.title}</h1>
              <p class="leading-relaxed py-2">{singleProduct()?.description}</p>
              <div class="flex">
                <span class="title-font font-medium text-2xl text-gray-900">${singleProduct()?.price}</span>
                <button class="flex ml-auto text-white bg-indigo-600 hover:bg-indigo-500 text-white border-0 py-2 px-6 focus:outline-none rounded" onClick={() => navigateUser(singleProduct()!)}>
                  <i class="fas fa-cart-plus"></i>
                </button>
              </div>
            </div>
          </div>
        </div>
      </section>
    </>
  )

}
export default ProductDetailpage


// const images = ['https://images.unsplash.com/photo-1506501139174-099022df5260?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=1351&q=80', 'https://images.unsplash.com/photo-1523438097201-512ae7d59c44?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=1350&q=80', 'https://images.unsplash.com/photo-1513026705753-bc3fffca8bf4?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=1350&q=80']
// // images must be an array of urls , if using Next JS this could something like
// // const images = ['/img/img1.png', '/img/img2.png', '/img/img3.png']
// // images must be an array of urls , if using Next JS this could something like
// // const images = ['/img/img1.png', '/img/img2.png', '/img/img3.png']


// const Carousel = () => {
//   // We will start by storing the index of the current image in the state.
//   const [currentImage, setCurrentImage] = React.useState(0);

//   // We are using react ref to 'tag' each of the images. Below will create an array of
//   // objects with numbered keys. We will use those numbers (i) later to access a ref of a
//   // specific image in this array.
//   const refs = images.reduce((acc, val, i) => {
//     acc[i] = React.createRef();
//     return acc;
//   }, {});

//   const scrollToImage = i => {
//     // First let's set the index of the image we want to see next
//     setCurrentImage(i);
//     // Now, this is where the magic happens. We 'tagged' each one of the images with a ref,
//     // we can then use built-in scrollIntoView API to do eaxactly what it says on the box - scroll it into
//     // your current view! To do so we pass an index of the image, which is then use to identify our current
//     // image's ref in 'refs' array above.
//     refs[i].current.scrollIntoView({
//       //     Defines the transition animation.
//       behavior: 'smooth',
//       //      Defines vertical alignment.
//       block: 'nearest',
//       //      Defines horizontal alignment.
//       inline: 'start',
//     });
//   };

//   // Some validation for checking the array length could be added if needed
//   const totalImages = images.length;

//   // Below functions will assure that after last image we'll scroll back to the start,
//   // or another way round - first to last in previousImage method.
//   const nextImage = () => {
//     if (currentImage >= totalImages - 1) {
//       scrollToImage(0);
//     } else {
//       scrollToImage(currentImage + 1);
//     }
//   };

//   const previousImage = () => {
//     if (currentImage === 0) {
//       scrollToImage(totalImages - 1);
//     } else {
//       scrollToImage(currentImage - 1);
//     }
//   };

//   // Tailwind styles. Most importantly notice position absolute, this will sit relative to the carousel's outer div.
//   const arrowStyle =
//     'absolute text-white text-2xl z-10 bg-black h-10 w-10 rounded-full opacity-75 flex items-center justify-center';

//   // Let's create dynamic buttons. It can be either left or right. Using
//   // isLeft boolean we can determine which side we'll be rendering our button
//   // as well as change its position and content.
//   const sliderControl = isLeft => (
//     <button
//       type="button"
//       onClick={isLeft ? previousImage : nextImage}
//       className={`${arrowStyle} ${isLeft ? 'left-2' : 'right-2'}`}
//       style={{ top: '40%' }}
//     >
//       <span role="img" aria-label={`Arrow ${isLeft ? 'left' : 'right'}`}>
//         {isLeft ? '◀' : '▶'}
//       </span>
//     </button>
//   );

//   return (
//     <div className="p-12 flex justify-center w-screen md:w-1/2 items-center">
//       <div className="relative w-full">
//         <div className="carousel">
//           {sliderControl(true)}
//           {images.map((img, i) => (
//             <div className="w-full flex-shrink-0" key={img} ref={refs[i]}>
//               <img src={img} className="w-full object-contain" />
//             </div>
//           ))}
//           {sliderControl()}
//         </div>
//       </div>
//     </div>
//   );
// };
