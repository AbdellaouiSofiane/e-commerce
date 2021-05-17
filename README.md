# personal blog web site
> This is a e-commerce web site developped using Python Django.

## Requirements
* Python 3
* Redis
* Rabbitmq


## Installation

Navigate to a new folder using your command prompt and type :

`git clone https://github.com/AbdellaouiSofiane/e-commerce.git`

Navigate to the project directory (make sure to activate your virtual enviroment) and type :

`python -m pip install -r requirements.txt`

Launch the developpement server :

`python manage.py runserver`

Open another shell, navigate to the project directory with  activev virtual enviroment) and type:

`celery -A shop_project worker -l info`

Visite http://127.0.0.1:8000/ in your browser.

Note : This project make use of Redis and Rabbitmq, so make sure you have both servers running before you launch the website.


## Screenshots

![image](https://user-images.githubusercontent.com/62038668/118564727-1f584c80-b771-11eb-8cad-0a2901be7e03.png)

![image](https://user-images.githubusercontent.com/62038668/118564784-3c8d1b00-b771-11eb-8009-cbfc3cdbf27c.png)

![image](https://user-images.githubusercontent.com/62038668/118564837-53cc0880-b771-11eb-8a10-169204dc592a.png)

![image](https://user-images.githubusercontent.com/62038668/118564856-61818e00-b771-11eb-8d17-7ed780ecc6d0.png)

![image](https://user-images.githubusercontent.com/62038668/118564891-7bbb6c00-b771-11eb-9908-1590dbe27399.png)

![image](https://user-images.githubusercontent.com/62038668/118564937-91309600-b771-11eb-9418-7136abf93464.png)


## Features

* Create/Edit shopping cart using django session.
* Edit shopping cart quantities with jQuery.
* Coupon system.
* Send asynchronous emails to customers using celery.
* Integrate a payment gateway (braintree).
* Export orders to CSV files (using admin actions).
* Generate PDF invoices dynamically.
* Product recommendation engine.
* Internationalization (english and spanish)

## Tech Stack / Built With

1. [Django](https://docs.djangoproject.com/en/3.1/) - The Python framework
2. [rosetta](https://django-rosetta.readthedocs.io/)-  Django application
3. [parler](https://django-parler.readthedocs.io/en/stable/)- Django application
4. [braintree](https://pypi.org/project/braintree/)- Python package
5. [weasyprint](https://weasyprint.readthedocs.io/en/stable/index.html) - Python package

## Authors

Sofiane Abdellaoui - abdellaoui.sofiane.esb@gmail.com

## Credits

This project was inspired by chapter 7 to 9 from the book :

Django 3 By Example - Build powerful and reliable Python web applications from scratch (author Antonio Melé)
