module.exports = {
  root: true,
  env: {
    browser: true,
    es6: true,
    node: true
  },
  ignorePatterns: ['node_modules/', '**/coverage/*', '**/dist/*', '**/types/*', '**/__mocks__/*', '**/*.d.ts', '**/*.js'],
  parser: 'vue-eslint-parser',
  parserOptions: {
    parser: '@typescript-eslint/parser',
    extraFileExtensions: ['.vue'],
    project: './tsconfig.json'
  },
  plugins: [
    '@typescript-eslint'
  ],
  extends: [
    'airbnb-typescript/base'
  ],
  rules: {
    // maximum line length
    'max-len': ['error', { code: 125, tabWidth: 2 }],
    // disallow console.log, allow console.warn and console.error
    'no-console': ['error', { allow: ['warn', 'error'] }],
    // allow functions to be used before their definition
    '@typescript-eslint/no-use-before-define': ['error', { functions: false }],
    // don't check classes are exported using default when there is only one export
    'import/prefer-default-export': 'off',
    // allow changes in properties of parameters
    'no-param-reassign': ['error', { props: false }],
    // allow circular import references,
    'import/no-cycle': 'off',
    // allow class methos without this
    'class-methods-use-this': 'off',
    // ignore error caused by monorepo and path aliases
    'import/no-unresolved': 'off',
    // ignore enforcement of consistent linebreak style
    'linebreak-style': 0,
  }
}