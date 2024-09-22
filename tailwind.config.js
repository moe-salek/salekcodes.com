/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.{html,js}", "./staticfiles/**/*.{html,js}", "./static/**/*.{html,js}"],
  extend: {
    minHeight: {
      'screen': '100vh',
    },
  },
  plugins: [require('@tailwindcss/typography'),],
}

