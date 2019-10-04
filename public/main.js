/* This is for the main functionality fo the client page, and interaction with the server */

/* Class constructor 
Link sections to html page
*/
function ImageForgeryDetection(){
    this.socket = io.connect();
    this.uploadButton = document.getElementById("Upload Button");

    /* Button-related events and socket observers setup */
}