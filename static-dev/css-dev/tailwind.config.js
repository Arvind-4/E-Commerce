// module.exports = {
//   mode: 'jit',
//   content: ['../../templates/**/*.html'],
//   darkmode: false,
//   theme: {
//     extend: {},
//   },
//   plugins: [],
// }

const purgecss = require('@fullhuman/postcss-purgecss')
const cssnano = require('cssnano')

module.exports = {
  mode: 'jit',
  darkMode: 'media',
  content: ['../../templates/**/*.html'],
  plugins: [
    require('tailwindcss'),
    require('autoprefixer'),
    cssnano({
      preset: 'default'
    }),
    purgecss({
      // content: ['./layouts/**/*.html', './src/**/*.vue', './src/**/*.jsx'],
      content: ['../../templates/**/*.html'],
      enabled: true,
    })
  ]
}