

# Howard University Computer Science

Computer Science Howard is a web-application that facilitates the progress-tracking of students. It is built with [Python][0] using the [Django Web Framework][1].

This project has the following basic apps:

* User Accounts (Manages the User-accounts of the students.)
* Events (Events application to CRUD Events, which can be registered by students) [In Progress.]
* Blogs (Blogs application to maintain a basic blog to allow students to write about interesting topics in the field of CS.)[In Progress]
* Forums (Discussion Forum to discuss about issues related class-assignments to professor-reliability) [In Progress.]

## Installation

### Quick start

To set up a development environment quickly, first install Python 3. It
comes with virtualenv built-in. So create a virtual env by:

    1. `$ python3 -m venv cs_howard`
    2. `$ . cs_howard/bin/activate`

Install all dependencies:

    pip install -r requirements.txt

Run migrations:

    python manage.py migrate

### Note
Tangled dependencies of packages used on different versions of Django. 

Fork the repo and send pull requests for contributing to this project.


[0]: https://www.python.org/
[1]: https://www.djangoproject.com/
