# court-cli

> court cases from the command line

Install the required libraries (`requests`, `fire`, `beautifulsoup4`):

`pip install -r requirements.txt`

## case36.py

This file handles [registers of action](http://www.36thdistrictcourt.org/online-services/case-inquiry-schedule) for 36th District Court cases.

You can use this from the command line, with an action and parameters.

### action

- `display` prints register of actions to the terminal
- `download` will download the register of actions as `<casenum>_<timestamp>.txt`

### parameters

- `cnum` is a case number
- `ctype` is the type of case. current options are:
  - `LT` for landlord-tenant
  - `CC` for.. civil and criminal? (most are this type)

### example usage

```python
python case36.py display --cnum 135046942 --ctype CC
```

```python
python case36.py download --cnum 16322063 --ctype LT
```
