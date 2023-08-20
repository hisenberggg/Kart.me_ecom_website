![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

# kart.me

It is a template for e-com website


## Table of contents

- [Run locally](#runlocally)
- [Demo](#demo)
- [Author](#author)
- [FAQ](#faq)


## Run Locally <a id="runlocally"></a>

Clone the project

```bash
  git clone https://github.com/hisenberggg/Kart.me_ecom_website.git
```

Go to the project directory

```bash
  cd Kart.me_ecom_website
```

Create virtual environment

```bash
  py -m venv env 
  env\Scripts\activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Migrate User and create the super-user

```bash
  py manage.py migrate 
  py manage.py createsuperuser
```

Migrate each app (userauth and eshop)

```bash
  py manage.py makemigrations userauth 
  python manage.py migrate
```
```bash
  py manage.py makemigrations eshop 
  python manage.py migrate
```

Start the server

```bash
  py manage.py runserver
```



## Demo <a id="demo"></a>



https://github.com/hisenberggg/Kart.me_ecom_website/assets/65344317/b43806ac-a2ae-4bc8-b0ee-37036ebc583c





## Author <a id="author"></a>

  - Abhijeet Ringe <br>
  [![Linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/abhijeet-ringe-3ab01a195/)
  [![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/hisenberggg)


## FAQ  <a id="faq"></a>

#### What is the python version requirement?

Python >= 3.5
if python is less than

#### How to add products?

Go to http://localhost:8000/admin and add products in the products database

#### How to add/update product categories 

Go to eshop/models.py and edit the CATEGORY_CHOICE tuple
