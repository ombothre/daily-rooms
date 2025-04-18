module.exports = {
  purge: ['./index.html', './src/**/*.{js,jsx,ts,tsx}'],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        skyblue: '#87CEEB',
        white: '#FFFFFF'
      }
    }
  },
  variants: {
    extend: {}
  },
  plugins: []
};
