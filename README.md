# Image Forgery Detection (Copy Move) Using Sift
  
The objective of this proposed project is to produce a program that is capable of detecting whether image forgery techniques have been used to alter an image provided by the user to the program. The types of image forgery techniques that can be detected by this program would consist of copy-move and splicing. This program will be running on a web server which would allow members of the public to have free access to it for their own personal use and testing. The application works by accepting an image uploaded by the user, then running through two different CNN architectures (one for copy-move and one for splicing) that would detect if a given image has been forged or not. Finally, the results returned will indicate whether the given image has been forged or not and is displayed to the user through the web page. This project would consist of several major work activities such as the construction of the convolutional neural network, the pre-processing of the data used to train our neural networks and setting up the web page that would act as an interface between the user and our program.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Modules Needed:

```
NumPy
Matplotlib
Scipy
OpenCV v3.4.2.16
OpenCV-contrib v3.4.2.16
imutils
Pillow
```

### Installing

In terminal:

```
pip install numpy
pip install matplotlib
pip install scipy
pip install opencv-python==3.4.2.16
pip install opencv-contrib-python==3.4.2.16
pip install imutils
pip install Pillow==6.2.0
```

## Deployment

1. Open desired terminal, for ease of use, we will be using Pycharm.
2. Run, app.py
3. Follow instructions on GUI.

## Known Issues

- Unresponsive page design as our aim mainly focus on the functionality.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).  

## Authors

* **Nelson Wei Han, Wong** - *28488563* - nwon0002@student.monash.edu
* **Nicholas Roosevelt, Wong** - *28839048* - nwon0007@student.monash.edu
* **Khai Yuan, Chee** - *28909429* - kche0028@student.monash.edu


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Let's graduate fellas

