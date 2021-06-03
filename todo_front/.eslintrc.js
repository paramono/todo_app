module.exports = {
  root: true,
  env: {
    browser: true,
    node: true,
  },
  parserOptions: {
    parser: 'babel-eslint',
  },
  extends: [
    '@nuxtjs',
    'plugin:nuxt/recommended',
  ],
  plugins: [],
  // add your custom rules here
  rules: {
    "space-before-function-paren": "never",
    "no-console": "off",
    // "no-unused-vars": "off",
    "comma-dangle": ["off"],
    "camelcase": "off",
    "vue/singleline-html-element-content-newline": "off",
    "vue/max-attributes-per-line": ["error", {
        "singleline": 5,
        "multiline": {
            "max": 1,
            "allowFirstLine": true
        }
    }]

  }
}
