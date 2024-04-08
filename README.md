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
     2. _say_hello_html()_
     3. _say_bye_html()_
     4. -> templates에 context 전달
  2. urls
     1. _playground/hello/_ -> _say_hello()_
     2. _playground/hello_html/_ -> _say_hello_html()_
  3. templates/playground/
     1. hello.html
     2. bye.html

5. helloidol/
   1. urls, playground/urls
      1. _playground/_ -> _hello/_ -> _say_hello()_
      2. _playground/_ -> _hello_html/_ -> _say_hello_html()_
      3. _playground/_ -> _bye_html/_ -> _say_bye_html()_
---
6. startapp mrsgreenapple
   1. Terminal
      1. python manage.py startapp mrsgreenapple
   2. helloidol/settings.py
      1. 'mrsgreenapple', in INSTALLED_APPS


7. mrsgreenapple/
   1. views
      1. ~~show_omori()~~
      2. ~~show_wakai()~~
      3. -> templates에 context 전달
      4. 정보를 하나로 묶고, 거기에서 꺼내오자
      5. show_member()
      6. image link -> image file(static)
      7. show_member_list()
   2. templates/mrsgreenapple
      1. ~~omori.html~~
         1. title : mrsgreenapple - omori
         2. h1 : mrsgreenapple
         3. h2 : omori
         4. img : omori's profile picture
            1. border-radius : 50%;
      2. ~~wakai.html~~
      3. member.html
         1. group_name, name, img_src
         2. `{% load static %} <img src="{% static img_src %}">`
         3. ```
            {% extends 'base.html' %} 
            {% block title %}{% endblock %}
            {% block content %}{% endblock %}
            ```
      4. member_list.html
         1. {% url '앱이름:path이름' %}
         2. {% url '앱이름:path이름' 변수=값 %}
         3. ```
            {% extends 'base.html' %} 
            {% block title %}{% endblock %}
            {% block content %}{% endblock %}
            ```
   3. urls
      1. ~~mrsgreenapple/ -> omori/ -> show_omori()~~
      2. ~~mrsgreenapple/ -> wakai/ -> show_wakai()~~
      3. `mrsgreenapple/ -> <member>/ -> show_member(member)`
      4. mrsgreenapple/ -> member_list/ -> show_member_list/
   4. static/mrsgreenapple/images/
      5. me.jpg


8. templates/
   1. base.html
      ```
      {% block title %}{% endblock %}
      {% block css %}{% endblock %}
      {% block content %}{% endblock %}
      ```
      
9. helloidol/
   1. in TEMPLATES in settings.py
      1. 'DIRS': [BASE_DIR / 'templates']