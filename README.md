
# Sleep Detection Application
This is a repository for detecting sleeps.

## What it does?
This app will detect if a person in the frame is sleeping or not.

## Where can be this app used?
This app can be used by car, bus or truck drivers. These people have to drive their vehicles all night. So, this app can be used by these people which can detect sleep and can raise an alarm thus preventing any serious accidents.

## How does it detects sleep?

### Libraries

#### OpenCV
OpenCV (Open Source Computer Vision Library) is an open source computer vision and machine learning software library. OpenCV was
built to provide a common infrastructure for computer vision applications and to accelerate the use of machine perception in the
commercial products. Being a BSD-licensed product, OpenCV makes it easy for businesses to utilize and modify the code.

#### dlib
Dlib is a modern C++ toolkit containing machine learning algorithms and tools for creating complex software in C++ to solve real
world problems. It is used in both industry and academia in a wide range of domains including robotics, embedded devices, mobile
phones, and large high performance computing environments.

### Geometry

#### EAR
EAR (Eye Aspect Ratio) gives the numerical representation of how much wide our eye is in the particular moment. The dlib library
can make a geometrical representation of our face and by calculating these points we can calculate the EAR index of our eye.
The formula for calculating EAR is (|p2-p6|+|p3-p5|)/2(p1-p4) where p1, p2, p3, p4, p5, p6 are geometrical cordinates of our eye
in face.

#### EAR vs Time
It can determine if a person’s eyes are closed if the Eye Aspect Ratio falls below a certain threshold.

### Python
Python is the main part of this project. The video is capturing by the webcam and then this video is processed frame-by-frame by
the Python using for loop and then doing the computational part on every frame.

## What web server have I used?
I've used Django for this project.

## What is Django?
Django is an open-source python web framework used for rapid development, pragmatic, maintainable, clean design, and secures
websites. A web application framework is a toolkit of all components need for application development. The main goal of the Django
framework is to allow developers to focus on components of the application that are new instead of spending time on already
developed components.

## Why have I used Django?

### Django is time-tested!
Django is the first framework to respond to new issues and vulnerabilities and alter other frameworks to make patches to
frameworks. The Latest release of it is focusing on new features and boundary case problems.

### Application Development!
Django was developed by online news operation team with an aim to create web applications using the Python programming language.
The framework has templates, libraries, and APIS which work together. In general, applications developed using Django can be
upgraded with minimal cost, changes, and additions and it make a lot of web development easier.

### Easy to use!
Django uses Python programming language which is a popular language in 2015 and now most choosing language by programmers who are
learning to code and applications of Django framework is widely used as it is free and open-source, developed and maintained by a
large community of developers.

### Operating System Independent!
Django framework runs on any platform like PC, Windows, Mac, Linux etc. It provides a layer between the developer and database
called ORM (object-relational mapper) which makes it possible to move or migrate our applications to other major databases with
few lines of code change.
