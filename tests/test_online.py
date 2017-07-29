from pytest import fail


def async_runner(function):
    import asyncio
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(function)


def test_async_get_section():
    from uiucapi.aioquery import get_section
    course1 = "AAS 100 SP12 CRN54572"
    course2 = "AAS 100 SP12 CRN54573"
    section1 = async_runner(get_section(course1))
    assert section1.crn == 54572
    assert section1.registration_status == "UNKNOWN"
    try:
        async_runner(get_section(course2))
        fail("This section does not exist!")
    except IOError:
        pass


def test_async_get_course():
    from uiucapi.aioquery import get_course
    course1 = "AAS 100 SP12 CRN54572"
    course2 = "AAS 99 SP12 CRN54573"
    result1 = async_runner(get_course(course1))
    assert result1.credit_hours == 3
    assert result1.name == "Intro Asian American Studies"
    assert len(result1.sections) == 9
    try:
        async_runner(get_course(course2))
        fail("This course does not exist!")
    except IOError:
        pass


def test_sync_get_section():
    from uiucapi.query import get_section
    course1 = "AAS 100 SP12 CRN54572"
    course2 = "AAS 100 SP12 CRN54573"
    section1 = get_section(course1)
    assert section1.crn == 54572
    assert section1.registration_status == "UNKNOWN"
    try:
        async_runner(get_section(course2))
        fail("This section does not exist!")
    except IOError:
        pass


def test_sync_get_course():
    from uiucapi.query import get_course
    course1 = "AAS 100 SP12 CRN54572"
    course2 = "AAS 99 SP12 CRN54573"
    result1 = get_course(course1)
    assert result1.credit_hours == 3
    assert result1.name == "Intro Asian American Studies"
    assert len(result1.sections) == 9
    try:
        get_course(course2)
        fail("This course does not exist!")
    except IOError:
        pass
