import pytest


def test_parse_course_string_to_url():
    from utility.parse import __parse_course_string_to_url
    string = "CS 374 FA17 CRN66445"
    result = "https://courses.illinois.edu/cisapp/explorer/schedule/2017/fall/CS/374.xml?mode=cascade"
    assert __parse_course_string_to_url(string) == result


def test_parse_section_string_to_url():
    from utility.parse import __parse_section_string_to_url
    string = "CS 374 FA17 CRN66445"
    result = "https://courses.illinois.edu/cisapp/explorer/schedule/2017/fall/CS/374/66445.xml"
    assert __parse_section_string_to_url(string) == result


def test_extract_course_name():
    from utility.parse import __extract_course_name
    string1 = "CS 374 FA17 CRN66445"
    string2 = "CS 374 CRN66445"
    string3 = "CS 374    \n"
    result = ["CS", "374"]
    assert result == __extract_course_name(string1)
    assert result == __extract_course_name(string2)
    assert result == __extract_course_name(string3)


def test_extract_crn():
    from utility.parse import __extract_crn
    string1 = "CS 374 FA17 CRN66445"
    string2 = "CS 374 CRN66445"
    string3 = "CS 374"
    result = "66445"
    assert result == __extract_crn(string1)
    assert result == __extract_crn(string2)
    try:
        __extract_crn(string3)
        pytest.fail("There is no CRN in this string!")
    except:
        pass


def test_extract_course_time():
    from utility.parse import __extract_course_time
    string1 = "CS 374 FA17 CRN66445"
    string2 = "CS 374 CRN66445"
    string3 = "SP19 XJ34"
    string4 = "XJ34 SP19"
    result1 = ("fall", "2017")
    result2 = ("spring", "2019")
    assert result1 == __extract_course_time(string1)
    assert result1 == __extract_course_time(string2)
    assert result2 == __extract_course_time(string3)
    assert result2 == __extract_course_time(string4)
