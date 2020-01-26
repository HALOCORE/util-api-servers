
var express = require('express');

var app = express();

app.use(express.static('public'));

app.listen(8124 /* 端口号 */, function () {
  console.log('app is listening at port 8124');
});