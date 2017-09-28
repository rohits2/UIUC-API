UIUC CourseExplorer API
=======================

.. image:: https://api.codacy.com/project/badge/Grade/df755ff6ff664a6da27953e0fbc57644
   :alt: Codacy Badge
   :target: https://www.codacy.com/app/singhrohit2/UIUC-API?utm_source=github.com&utm_medium=referral&utm_content=rohits2/UIUC-API&utm_campaign=badger
.. image:: https://circleci.com/gh/rohits2/UIUC-API/tree/master.svg?style=shield
What is this?
-------------
This is an interface to the UIUC Course Explorer API.  It allows for the easy querying of class statuses from inside Python.
This library supports both async and standard queries to the API, as well as querying for specific CRNs.

Basic usage
-----------
The API is very simple to use:
::
    from uiucapi.query import get_course
    course = get_course("CS 374 FA17")
    for section in course.sections:
        print(section.registration_status)

Object Types
------------
Requests to the UIUC API will return one of the following objects, with the following properties:

- Course
    - subject
    - name
    - description
    - credit_hours
    - gened_categories
    - sections
- Section
    - crn
    - section_number
    - registration_status
    - start_date
    - end_date
- GenedCategory
    - code
    - description



Advanced features
-----------------
If :code:`uiucapi.aioquery` is used instead of query, the :code:`get_course` and :code:`get_section` methods provided will be non-blocking coroutines instead of
blocking methods.

