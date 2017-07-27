# webpack 

+ use ECMAScript6 syntax with webpack, babel transpiler
```js
let login = (username,password) => {
  if (username !== 'user' && password !== 'pass')
    console.log('incorrect login!');
}
// require('./login');
export {login}
import {login} from "./login"
login('user','pass');
```
+ `webpack -d` or `webpack-dev-server -d` adds source maps support for .js files in webpack. `-p` option also minifies.
+ `debugger;` forces a breakpoint.
+ use several bundle files for **lazy loading**
```js
var webpack = require('webpack');
var commonsPlugin = new webpack.optimize.CommonsChunkPlugin('shared.js');
```
In the `module.exports` section of webpack.config.js add separate entries like:
```js
entry: { about: 'about_page.js', home: 'home_page.js' }
```
, also specify the plugin `plugins: [commonsPlugin]`
and specify the multiple outputs, will match the key in the entries object
```js
output: {
  path: path.resolve('/build/js/'),
  publicPath: '/public/assets/js/',
  filename: "[name].js"
}
```
+ css and style loaders
```bat
npm install css-loader style-loader --save-dev
```
reference it inside `module: { loaders: [] }` with *chain* syntax
```js
{test:/.\css$/, exclude:/node_modules/, loader:"style-loader!css-loader"}
```
Resulting css will get included inside `head->style` tags. No reference as files per se in network style tab in dev console.
+ LESS & SASS
```cmd
npm install sass-loader less-loader --save-dev
```
`app.css` renamed to `app.scss`. Add new loader too: 
```js
{test:/.\scss$/, exclude:/node_modules/, loader:"style-loader!css-loader!sass-loader"}
```
Extension is less instead of scss, loader is less instead of sass.
+ create separate css bundle
```cmd
npm install extract-text-webpack-plugin --save-dev
```
```js
var etp = require('extract-text-webpack-plugin');
/*...*/
plugins: [new etp("styles.css")]
/*...*/
loader: etp.extract (loader_params)
```

[Home](https://github.com/illegitimis/Tutorial) | [JS](JS.md)
