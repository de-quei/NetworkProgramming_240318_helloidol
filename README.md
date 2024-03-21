# helloidol

---

1. startproject helloidol
    1. python -m pip install django~=4.2 (4.2의 최신버전을 설치)
    2. django-admin startproject _helloidol_ . (현재 프로젝트 밑에 생성)
    3. python manage.py migrate
    4. python manage.py runserver


2. django setting
   1. setting > Languages and Frameworks
   2. root setting > apply


3. startapp _playground_
   1. Terminal
      1. python manage.py startapp _playground_
   2. helloidol/settings.py
      1. 'playground', in INSTALLED_APPS (앱 등록)


4. playground/
- 정보 전달 : urls -> views -> (models)templates
- 코드 작성 : (models -> )views -> templates -> urls
  1. views
     1. _say_hello()_