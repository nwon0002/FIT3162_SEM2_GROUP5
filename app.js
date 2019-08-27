/* This is the server side of the application, it contains the code needed to run the server on localhost
express: web framework needed for localhost
fs: work with filesystem on computer
http: creates HTTP server that will listen to server ports so it can give back response to client side
 */

var fs = require('fs'), express = require('express'), http=require('http'), app = express();

/* This is the block code for server
The app is running at port 5000 */ 
var server = http.createServer(function(req, res){
  res.end(fs.readFileSync(__dirname + '/app.html'));
}).listen(5000, function(){
  console.log('app.js is listening at http://localhost:5000');
});

// app.get('/', function (req, res) {
//   res.send('Hello World!')
// })

// app.listen(5000, function () {
//   console.log('Example app.js listening on port 5000!')
// })