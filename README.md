# DJANGO CLONE MEDIUM
Meng-clone Medium dengan menggunakan Django versi 4.2


## 1. SETUP


#### 1.1 Create project 'config'

        modified:   .gitignore
        modified:   README.md
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py
        new file:   requirements.txt


#### 1.2 Create app 'app/page'

        modified:   README.md
        new file:   app/page/__init__.py
        new file:   app/page/admin.py
        new file:   app/page/apps.py
        new file:   app/page/migrations/__init__.py
        new file:   app/page/models.py
        new file:   app/page/tests.py
        new file:   app/page/views.py
        modified:   config/settings.py


#### 1.3 Create homepage: templates, views, urls

        modified:   README.md
        new file:   app/page/templates/page/home_page.html
        new file:   app/page/urls.py
        modified:   app/page/views.py
        modified:   config/settings.py
        modified:   config/urls.py


#### 1.4 Add and load static files

        modified:   README.md
        modified:   app/page/templates/page/home_page.html
        modified:   config/settings.py
        new file:   config/static/css/bootstrap.min.css
        new file:   config/static/css/bootstrap.min.css.map
        new file:   config/static/css/style.css


#### 1.5 Add html template to homepage with template inheritance

        modified:   README.md
        new file:   app/page/templates/page/hero_header.html
        modified:   app/page/templates/page/home_page.html
        new file:   templates/base.html
        new file:   templates/footer.html
        new file:   templates/navbar.html


## 2. USERS 


#### 2.1 USERS - Create app 'app/user_profile'

        new file:   app/user_profile/__init__.py
        new file:   app/user_profile/admin.py
        new file:   app/user_profile/apps.py
        new file:   app/user_profile/migrations/__init__.py
        new file:   app/user_profile/models.py
        new file:   app/user_profile/tests.py
        new file:   app/user_profile/views.py


#### 2.2 USERS - Register 'app/user_profile' to settings.py

        modified:   README.md
        modified:   config/settings.py


