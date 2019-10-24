# Image Forgery Detection (Copy Move) Using Sift
  
The objective of this project is to produce a program that can detect whether image forgery techniques, specifically copy-move, has been used to alter an image provided by the user to the program. The project has been uploaded to Github so that members of the general public have full access to this project. This application works by accepting an image uploaded by the user, then passing the input image into the program which utilizes the scale-invariant feature transformation (SIFT) algorithm to detect if a given image has been tampered with through copy-move forgery. Finally, the results returned will indicate whether the given image has been forged or not and is displayed to the user through the graphical user interface (GUI).  

The proposed approach to detect copy-move forgery in an image is based on the Scale Invariant Feature Transformation (SIFT) algorithm. The SIFT algorithm is used because it helps extract robust features from the image to detect if a part of an image was copy–moved. Generally, the copied region of the original image has an almost identical appearance to the region it was copied from besides any scaling or rotation transformation applied on it. Hence, the descriptor of keypoints extracted from the original region will be quite similar to the descriptor of the keypoints extracted from the forged region regardless of any transformations applied due to the use of the SIFT algorithm. Hence, with this concept, the general idea to detect if an image has been forged by applying copy-move attack is to match each of the SIFT features extracted from the image by finding keypoints that share almost similar characteristics which can be assessed base on its respective descriptor.

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

