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


#### 2.3 USERS - LOGIN: Create login page: templates, views, urls

        modified:   README.md
        new file:   app/user_profile/templates/user_profile/login.html
        new file:   app/user_profile/urls.py
        modified:   app/user_profile/views.py
        modified:   config/urls.py
        new file:   templates/base_without_navbar.html


#### 2.4 USERS - LOGIN: Add user login logic to login_view

        modified:   README.md
        modified:   app/user_profile/templates/user_profile/login.html <<-- Modified
        modified:   app/user_profile/views.py <<-- Add logic

        NOTE:

        1. Showed usename(email) and password credentials in the terminal 

        :)


#### 2.5 USERS - LOGIN: Informing-User-Login-With-Django-Messages-Framework-Structure

        modified:   README.md
        modified:   app/user_profile/templates/user_profile/login.html << -- Modified username input from email to username
        modified:   app/user_profile/views.py << -- Add more logic
        modified:   templates/base.html << -- Incluce message
        new file:   templates/messages.html << -- Add adn loop the message

        NOTE:

        1. Sukses: user bisa login
           username: admin
           password: admin

        2. Redirect logged in user to homepage


#### 2.6 USERS - LOGOUT: Creating-Logout-View-and-Adding-Urls

        modified:   README.md
        modified:   app/user_profile/urls.py <<-- Add path for logout
        modified:   app/user_profile/views.py <<-- Create logout_view with logic
        modified:   templates/navbar.html <<-- Add links to sign-in and sign-out

        NOTE:

        Logged in user SUKSES logout.

        :)


#### 2.6 USERS - LOGIN: Adding-Login-Controls length charater of the username

        modified:   README.md
        modified:   app/user_profile/views.py <<-- add logic to login_vew, username MUST BE at least 6 char 
        new file:   config/static/js/bootstrap.bundle.min.js
        new file:   config/static/js/bootstrap.bundle.min.js.map
        modified:   templates/base_without_navbar.html <<-- include message framework

        NOTE:

        Sukses kontrol jumlah karakter username