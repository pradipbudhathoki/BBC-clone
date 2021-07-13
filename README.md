## BBC-clone-Django

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/pradipbudhathoki/BBC-clone-Django.git
$ cd BBC-clone-Django
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

Once `pip` has finished downloading the dependencies:

```sh
(env)$ python manage.py runserver
```

And navigate to `http://127.0.0.1:8000/`.
