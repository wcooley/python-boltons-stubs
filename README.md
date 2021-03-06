Contained herein are PEP 561 type stubs for the
[`boltons`](https://pypi.org/project/boltons/) package.

These have mostly been generated using
[`MonkeyType`](https://pypi.org/project/MonkeyType/) and
[`pytest-monkeytype`](https://pypi.org/project/pytest-monkeytype/); as such,
they are limited to what is tested by default with the types included in the
tests and to what has been manually created.

To install:
```
pip install --editable git+https://github.com/wcooley/python-boltons-stubs#egg=boltons-stubs
```

To do:
* Add missing classes & functions.
* Make parameter types as general as possible and return types as specific
as necessary.
