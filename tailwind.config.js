/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./main/templates/main/*.html",
    "./main/templates/main/includes/*.html",
    "./templates/*.html",
  ],
  theme: {
    fontFamily: {
      poppins: ['Poppins'],
    },
    extend: {
      width: {
        '10p': '10%',
        '15p': '15%',
        '20p': '20%',
        '30p': '30%',
        '40p': '40%',
        '50p': '50%',
        '60p': '60%',
        '70p': '70%',
        '80p': '80%',
        '90p': '90%',
      },
      colors: {
        primary: '#125615',
        secondary: '#BEBDBD',
        tertiary: '#FFC805',
        background: '#EBEBEB',
      },
    },
  },
  plugins: [],
}
