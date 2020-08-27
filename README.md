# Lab 27 - Django Models

### *Author: Thomas Sherer*, 2020-08-26

---

## Description
### Feature Tasks and Requirements
- create __`blog_project`__ project
- create __`blog`__ app
- migrate data
- create __`Post`__ model
	- add __`title`__ as a __CharField__ with maximum length of 64 characters.
	- add __`author`__ __ForeignKey__ related to Django's built in user model with __CASCADE__ delete option.
	- add __`body` TextField__ <br>

- add model to admin
- modify __`Post`__ model have user friendly display in admin
- create migrations and migrate data
- create a superuser
- Add a few posts via __Admin__ panel
- Add __`templates`__ folder in root of project
	- register __`templates`__ folder in project settings <br>

- create __`HomePageView`__
	- extend __`ListView`__
	- give a template of __`home.html`__
	- associate __`Post`__ model <br>

- create __`home.html`__ template
	- use __`Django Templating Language`__ to display each post's title <br>

- create __`base.html`__ ancestor template
	- add main html document
	- use __`Django Templating Language`__ to allow child templates to insert content <br>

- update __url patterns__ for app and project
- view home page and confirm posts showing properly
- add __detail__ view
	- link __`post_detail.html`__ template
	- associate __`Post`__ model <br>

- create __`post_detail.html`__ template
	- template should extend __base__
	- content should display post title and body <br>

- update app __urlpatterns__ to handle detail view
	- account for primary key in url <br>

- add link in home page template to related post detail page <br>

## Implementation Notes
- The instructions are becoming more conceptual.
- All the concepts listed relate to key Django steps covered in the demo.
- If there is confusion about what, exactly, is required then ask the client (aka the instructors.)
- __TLDR__ - make your lab project like the demo project. <br>

---

<!-- My code is [here](./) <br> -->

---

### Collaborations and Attributions
<!-- __Skyler Burger__ helped immensely when trying to import a corpus of english words when 'import' wasn't working for the cipher-breaker function. -->

<!-- __Merry Cimakasky__ helped with NN. -->

<!-- __Lee-Roy King__ helped with NN. -->

.gitignore content courtesy of https://www.toptal.com/developers/gitignore/api/django

<!-- __likegeeks.com__ helped with [understanding chr() and ord()](https://likegeeks.com/python-caesar-cipher/) -->

---
