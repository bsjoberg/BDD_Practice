This is a repo used while I follow the TDD with Python book

Need django, selenium, geckodriver

## Geckodriver
- https://github.com/mozilla/geckodriver/releases
- gunzip untar and then put driver in /usr/local/bin

## Running django
`python manage.py runserver`

## Running unittests
- `python manage.py tests`

## Running functional tests
- `rm db.sqlite3`
- `python manage.py migrate --noinput`
- `python tests/functional_tests.py`