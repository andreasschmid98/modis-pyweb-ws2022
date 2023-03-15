# modis

modis is a module information system for students of the faculty of computer science (HS Augsburg), developed within the
course agile web applications with python.

## Description

Basically, modis pursues the goal of simplifying and accelerating the process of obtaining information for modules by
bundling all module information on one website for students to access. In addition, modis gives lecturers and
administrators the possibility to edit module information as well as to add and delete modules.

## Preview

<img width="113" height="60" alt="login" src="https://user-images.githubusercontent.com/81109321/225359753-e777a3f8-b6ac-4539-ad85-dee9c9f2347b.png">

<img width="1128" alt="home" src="https://user-images.githubusercontent.com/81109321/225360233-a37b03da-efd7-4b9a-8ce0-d40020744c93.png">

<img width="1128" alt="fav" src="https://user-images.githubusercontent.com/81109321/225360968-95be90ce-05cb-45c9-8a17-20761d8047f7.png">

<img width="1128" alt="module" src="https://user-images.githubusercontent.com/81109321/225361280-95d385f2-a2ed-4c79-908d-491088626d09.png">


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
