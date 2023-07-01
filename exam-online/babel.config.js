module.exports = {
  presets: [
    '@vue/cli-plugin-babel/preset',
    '@babel/preset-react',
    ['@babel/preset-env', {targets: {node: 'current'}}],
    ['@vue/babel-preset-jsx',
    {
    'injectH': false
    }]
  ],
  plugins: [
    "@babel/plugin-syntax-jsx"
  ]
}

