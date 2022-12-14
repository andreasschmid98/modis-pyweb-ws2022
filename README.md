# modis

modis is a module information system for students of the faculty of computer science (HS Augsburg), developed within the
course agile web applications with python.

## Description

Basically, modis pursues the goal of simplifying and accelerating the process of obtaining information for modules by
bundling all module information on one website for students to access. In addition, modis gives lecturers and
administrators the possibility to edit module information as well as to add and delete modules.

## Installation guide

To start modis, the following GitHub repository must be cloned:

* https://github.com/andreasschmid98/modis-pyweb-ws2022

Then, all the required dependencies can be viewed in the requirements.txt file. Entering...

```bash
pip install -r requirements.txt 
```

in the PyCharm terminal will install all dependencies locally. Afterwards the project can be
started with...

```bash
py manage.py runserver 
```

Depending on the project structure it might be necessary to change the
directory with...

```bash
cd modis
```


## Accounts for testing

### Student

* username: student_test
* password: ModisWS2022!

### Lecturer

* username: lecturer_test
* password: ModisWS2022!
* username: lecturer_test_2
* password: ModisWS2022!

### Admin

* username: admin_test
* password: ModisWS2022!

## Author

Andreas Schmid
