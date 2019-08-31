/* This is the server side implementation */

/* Declare libraries */
var http= require('http'), 
    fs = require('fs'), 
    path =require('path'), 
    express = require('express'), 
    socket=require('socket.io'), 
    winston = require('winston'), 
    app = express();

/* Join path from server to public folder: */
app.use(express.static(path.join(__dirname, 'public')));

/* Server creation, at port 5000 */
var server = http.createServer(app).listen(5000, function() {
    console.log("Listening at: http://localhost:5000");
});

/* server observer */
socket.listen(server).on("connection", function(socket){
    logger.info("A client has connected to this port.");
});


/* Time stamp (logging purposes)*/
var tsFormat = () => (new Date()).toLocaleTimeString();

/* Winston Logger */
var logger = winston.createLogger({

    transports: [
      /* color output of logger to console */
      new (winston.transports.Console)({ 
          timestamp: tsFormat,
          colorize: true ,
          level : 'info'
      })
    ]

});
logger.info("Thank you for using this program!");