# Subcaptain

SubCaptain is a web application that allows users to stay on top and keep track of their subscription services. Users can create their own categories or use the premade ones to categorize the services. The app also shows the total cost of all services.

The app is available at: http://subcaptain.ollimyyrylainen.fi

## About
![App Screenshot](/screenshot.png)

### Built with

* Python
* Django
* PostgreSQL

### Getting started

#### Prerequisites

* Python
* pip

#### Usage

1. Clone the Repository:
```
git clone https://github.com/ollimyy/subcaptain subcaptain
cd subcaptain
```

2. Set Up a Virtual Environment (optional but recommended):
```
virtualenv --system-site-packages -p python3 env/
source env/bin/activate
```

3. Install Dependencies:
```
pip install -r requirements.txt
```

4. Set Up Database:
```
python manage.py migrate
```

5. Run the Application:
```
python manage.py runserver
```

6. Navigate to http://localhost:8000/ in your web browser to start using the application.

## Acknowledgements
* The styling used in this project: https://github.com/xz/new.css
* This project was built during the [Python - Idea to Production](https://terokarvinen.com/2023/python-web-idea-to-production/?fromSearch=idea%20to%20production) course.
