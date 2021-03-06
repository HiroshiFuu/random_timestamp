# random_timestamp
A Random Timestamp Generator

## Installation

**Dependences**

    * This app only

**Installation**

    *Installation with pip (recommended)*

        *Pip will download and install the package and take care of all the dependences.
        If you havn't pip on your system then install setuptools first after that run "easy_install pip".
        After that you can use pip in your terminal window.*

        * Use the stable release (recommended)::

            pip install random_timestamp

        * With pip you can also uninstall::

            pip uninstall random_timestamp


## Usage
The function **random_timestamp** takes **four** optional arguments:
```
random_timestamp(year=1900, month=1, day=1, part='DATE/TIME')
```

If **year** and **month** and **day** are not inputed, the timestamp will be randomly generated between _1900_ and today's date (_datetime.now().date())_).

If a later date after today is inputed, the output date will be today's date as well.
The optional **part** parameter is to select only the _date_ or _time_ portion of the timestamp to output.
```
>>> from random_timestamp import random_timestamp

>>> random_timestamp()
datetime.datetime(1986, 5, 31, 2, 50, 5)

>>> random_timestamp(2020)
datetime.datetime(2020, 2, 11, 12, 4, 51)

>>> random_timestamp(month=1)
datetime.datetime(1914, 1, 15, 22, 3, 58)

>>> random_timestamp(2020, 4, 16, 'DATE')
datetime.date(2020, 4, 16)

>>> random_timestamp(part='TIME')
datetime.time(10, 59, 6)
```

## License
This project is released under [GNU GENERAL PUBLIC LICENSE V3](https://www.gnu.org/licenses/gpl-3.0.en.html).