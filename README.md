
# kart.me

It is a template for e-com website




## Run Locally

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



## Demo



Uploading Kart_me_demo.mp4…




## Authors

- [@hisenberggg](https://github.com/hisenberggg/)


## FAQ

#### What is the python version requirement?

Python >= 3.5
if python is less than

#### How to add products?

Go to http://localhost:8000/admin and add products in the products database

