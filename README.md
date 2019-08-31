<h1 align="center" > Image Forgery Detection Using Convolutional Neural Network <h1>
  
The objective of this proposed project is to produce a program that is capable of detecting whether image forgery techniques have been used to alter an image provided by the user to the program. The types of image forgery techniques that can be detected by this program would consist of copy-move and splicing. This program will be running on a web server which would allow members of the public to have free access to it for their own personal use and testing. The application works by accepting an image uploaded by the user, then running through two different CNN architectures (one for copy-move and one for splicing) that would detect if a given image has been forged or not. Finally, the results returned will indicate whether the given image has been forged or not and is displayed to the user through the web page. This project would consist of several major work activities such as the construction of the convolutional neural network, the pre-processing of the data used to train our neural networks and setting up the web page that would act as an interface between the user and our program.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What libraries you need to install:

```
socket.io
express
winston
```

### Installing

In terminal:

```
npm i socket.io
npm i express
npm i winston
```

## Deployment

1. Open terminal at your desired editor
2. Find path to where server.js is located
3. node server.js
4. Log on to ‘http://localhost:5000’

## Known Issues

- Unresponsive page design as our aim mainly focus on the functionality. The view is built according to 13 inches screen-size but it still looks nice when it comes to 15 inches screen-size by turning the page to full screen.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).  

## Authors

* **Nelson Wei Han, Wong** - *28488563* - [contact](nwon0002@student.monash.edu)
* **Nicholas Roosevelt, Wong** - *28839048* - [contact](nwon0007@student.monash.edu)
* **Khai Yuan, Chee** - *28909429* - [contact](kche0028@student.monash.edu)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Let's graduate fellas

