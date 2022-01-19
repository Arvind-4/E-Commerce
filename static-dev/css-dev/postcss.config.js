module.exports = {
  plugins: {
    // tailwindcss: {},
    // autoprefixer: {},
    // ...(process.env.NODE_ENV === 'production' ? { cssnano: {} } : {})
    tailwindcss: {},
    autoprefixer: {},
    cssnano: { preset: "default" }
  },
}
