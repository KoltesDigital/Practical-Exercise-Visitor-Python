# Practical Exercise - Visitor - Python

This exercise relies on the TeTask project, the upcoming next-generation task scheduler. It shows a typical use case where the visitor pattern could be used, mainly because the data implement a composite pattern.

## Virtual environment

Install `pipenv`:

```
pip install pipenv
```

> Note: On Linux it may be `pip3` instead of `pip`.

Install dependencies:

```
pipenv install --dev
```

> Note: On Linux `pipenv` may not be available, so run `python -m pipenv install --dev`.

Now you can run the following commands:

Run application:

```
pipenv run python -m tetask
```

Run linter:

```
pipenv run pylint tetask
```

Run unit tests:

```
pipenv run pytest
```
