clean-pyc:
  find . -name '*.pyc' -exec rm --force {} +
  find . -name '*.pyo' -exec rm --force {} +
  find . -name '*~' -exec rm --force  {} +

isort:
  sh -c "isort --skip-glob=.tox --recursive . "

lint:
  flake8 --exclude=.tox

test: clean-pyc
  python manage.py test

run:
  python manage.py runserver