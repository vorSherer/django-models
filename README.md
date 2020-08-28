# Lab 27 - Django Models

### *Author: Thomas Sherer*, 2020-08-26

---

## Description
### Feature Tasks and Requirements
- [X] create __`blog_project`__ project
- [X] create __`blog`__ app
- [X] migrate data
- [X] create __`Post`__ model
	- [X] add __`title`__ as a __CharField__ with maximum length of 64 characters.
	- [X] add __`author`__ __ForeignKey__ related to Django's built in user model with __CASCADE__ delete option.
	- [X] add __`body` TextField__ <br>

- [X] add model to admin
- [ ] modify __`Post`__ model have user-friendly display in admin
- [X] create migrations and migrate data
- [X] create a superuser
- [X] Add a few posts via __Admin__ panel
- [X] Add __`templates`__ folder in root of project
	- [X] register __`templates`__ folder in project settings <br>

- [X] create __`HomePageView`__
	- [X] extend __`ListView`__
	- [X] give a template of __`home.html`__
	- [X] associate __`Post`__ model <br>

- [X] create __`home.html`__ template
	- [X] use __`Django Templating Language`__ to display each post's title <br>

- [X] create __`base.html`__ ancestor template
	- [X] add main html document
	- [X] use __`Django Templating Language`__ to allow child templates to insert content <br>

- [X] update __url patterns__ for app and project
- [X] view home page and confirm posts showing properly
- [ ] add __detail__ view
	- [ ] link __`post_detail.html`__ template
	- [ ] associate __`Post`__ model <br>

- [ ] create __`post_detail.html`__ template
	- [ ] template should extend __base__
	- [ ] content should display post title and body <br>

- [ ] update app __urlpatterns__ to handle detail view
	- [ ] account for primary key in url <br>

- [ ] add link in home page template to related post detail page <br>

## Implementation Notes
- The instructions are becoming more conceptual.
- All the concepts listed relate to key Django steps covered in the demo.
- If there is confusion about what, exactly, is required then ask the client *(aka the instructors.)*
- __TLDR__ - make your lab project like the demo project. <br>

---

<!-- My code is [here](./) <br> -->

---

### Collaborations and Attributions
__Skyler Burger__ helped with creating a false-positive test for Django tests.

<!-- __Merry Cimakasky__ helped with NN. -->

<!-- __Lee-Roy King__ helped with NN. -->

.gitignore content courtesy of https://www.toptal.com/developers/gitignore/api/django

<!-- __likegeeks.com__ helped with [understanding chr() and ord()](https://likegeeks.com/python-caesar-cipher/) -->

---
