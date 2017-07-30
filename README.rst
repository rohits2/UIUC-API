UIUC CourseExplorer API
=======================
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

Advanced features
-----------------
If ::uiucapi.aioquery
is used instead of query, the get_course and get_section methods provided will be non-blocking coroutines instead of
blocking methods.

