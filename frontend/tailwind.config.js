const purgecss = require('@fullhuman/postcss-purgecss')
const cssnano = require('cssnano')

const templatePath = '../web/templates/**/*.html'
const indexpath = './src/index.html'
const componentPath = './src/**/*.{js,ts,jsx,tsx}'

module.exports = {
  mode: 'jit',
  darkMode: 'media',
  content: [templatePath, indexpath, componentPath],
  theme: {
    extend: {},
  },
  plugins: [
    require('tailwindcss'),
    require('autoprefixer'),
    cssnano({
      preset: 'default'
    }),
    purgecss({
      content: [templatePath, indexpath, componentPath],
      enabled: true,
    })
  ]
}
