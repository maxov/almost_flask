# Almost Flask


A Flask near-implementation in less than 10 lines.
Written with zero dependencies.
Works only with Python 3.

Heavily inspired by [almost-sinatra](https://github.com/rkh/almost-sinatra).

Features:

* simplified Flask class
* decorator routing syntax
* subset of route parameter syntax
* GET, POST, PUT, DELETE methods
* request object (args, path, method)
* stand alone usage
* thread safe

Perhaps after you've finished playing with almost_flask you should take a look
at [Flask](https://github.com/mitsuhiko/flask) for real, because it's quite rad.

## Installation

Copy the contents of `almost_flask.py` into your app file (at the top), that
way you also avoid running the wrong version by accident.

## Try it

    $ python3 example.py
    What Flask implementation should I use?
    [R]eal Flask
    [A]lmost Flask
    >>> A

## Performance??

    $ sloccount alomst_flask.py
    Total Physical Source Lines of Code (SLOC)                = 5
    Development Effort Estimate, Person-Years (Person-Months) = 0.00 (0.01)
     (Basic COCOMO model, Person-Months = 2.4 * (KSLOC**1.05))
    Schedule Estimate, Years (Months)                         = 0.04 (0.42)
     (Basic COCOMO model, Months = 2.5 * (person-months**0.38))
    Estimated Average Number of Developers (Effort/Schedule)  = 0.02
    Total Estimated Cost to Develop                           = $ 104
     (average salary = $56,286/year, overhead = 2.40).

    $ sloccount flask/ tests/
    Total Physical Source Lines of Code (SLOC)                = 6,618
    Development Effort Estimate, Person-Years (Person-Months) = 1.45 (17.46)
     (Basic COCOMO model, Person-Months = 2.4 * (KSLOC**1.05))
    Schedule Estimate, Years (Months)                         = 0.62 (7.41)
     (Basic COCOMO model, Months = 2.5 * (person-months**0.38))
    Estimated Average Number of Developers (Effort/Schedule)  = 2.36
    Total Estimated Cost to Develop                           = $ 196,519
     (average salary = $56,286/year, overhead = 2.40).

Generated using David A. Wheeler's 'SLOCCount'.
