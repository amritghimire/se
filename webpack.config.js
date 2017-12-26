var path = require("path");
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');


module.exports = {
    context: __dirname,
    entry: './staticfiles/bundles/index.js',

    output: {
        path: path.resolve('./staticfiles/js/'),
        filename: 'index.js'
    }
};