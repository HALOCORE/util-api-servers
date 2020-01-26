
var express = require('express');

var app = express();

app.use('/static', express.static('static'));

app.listen(8124 /* 端口号 */, function () {
  console.log('app is listening at port 8124');
});