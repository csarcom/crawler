====================
Cheesecake challange
====================

Export the project path to PYTHONPATH::	
	
	$ export PYTHONPATH=<YOUR_PATH>/cheesecake:$PYTHONPATH

Setup env::

    virtualenv ../env/cheesecake
    source ../env/cheesecake/bin/activate

Create DB::

    python manage.py migrate

Create User::

    python manage.py createsuperuser --email admin@example.com --username admin

Create Token::

    python manage.py drf_create_token admin

Running tests::
    
    python manage.py test --pattern="test_*.py"

Running crawler::

    scrapy crawl gizmodo

To get the token::

    POST in http://localhost:8000/api-token-auth/

    {
        "username": "admin",
        "password": "admin123"
    }

URLs::

    - http://<host:port>/api-token-auth/ using POST
        Data: {"username": <USERNAME>, "password": <PASSWORD>}
    - http://<host:port>/posts/ using GET
        Header: Authorization   Token <TOKEN>
    