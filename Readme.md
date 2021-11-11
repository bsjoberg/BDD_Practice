This is a repo used while I follow the TDD with Python book

Need django, selenium, geckodriver, behave

## Geckodriver
- https://github.com/mozilla/geckodriver/releases
- gunzip untar and then put driver in /usr/local/bin

## Running django
`python manage.py runserver`

## Run all tests
- `python manage.py test`

## Running unittests
- `python manage.py test lists`

## Running functional tests
- `rm db.sqlite3`
- `python manage.py migrate --noinput`
- `python manage.py test functional_tests`

## Running behave (BDD Tests)
Creating a duplicate set of functional tests but using behave's given when then with step definitions
- `behave`

## Misc
If the local database is removed run the following command to get it working again.
- `python manage.py migrate --run-syncdb`