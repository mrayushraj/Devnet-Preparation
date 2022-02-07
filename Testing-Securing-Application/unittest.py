"""The assertion methods are:

assertEqual(a, b): Checks a == b

assertNotEqual(a, b): Checks a != b

assertTrue(x): Checks bool(x) is True

assertFalse(x): Checks bool(x) is False

assertIs(a, b): Checks a is b

assertIsNot(a, b): Checks a is not b

assertIsNone(x): Checks x is None

assertIsNotNone(x): Checks x is not None

assertIn(a, b): Checks a in b

assertNotIn(a, b): Checks a not in b

assertIsInstance(a, b): Checks isinstance(a, b)

assertNotIsInstance(a, b): Checks not isinstance(a, b)"""


import unittest

class TestTools(unittest.TestCase):
    def setUp(self):
        self.tools = Tools('admin')
    
    def test_true_when_greater(self):
        self.assertTrue(self.tools.is_greater(5, 4))
   
    def test_user(self):
        self.assertEqual(self.tools.user, 'admin')

    def test_false_when_equal(self):
        self.assertFalse(self.tools.is_greater(5, 5))
    
    def tearDown(self):
        self.tools.dispose()

if __name__ == '__main__':
    unittest.main()






##################################################################################################


import pytest


@pytest.fixture
def tools_lib():
    import tools

    return tools.Tools('admin')


def test_true_when_greater(tools_lib):
    assert tools_lib.is_greater(5, 4)


def test_user(tools_lib):
    assert tools_lib.user == 'admin'


def test_false_when_equal(tools_lib):
    assert not tools_lib.is_greater(5, 5)



"""
Notice that there is no boilerplate like in the unittest framework. You do not extend any TestCase class. 
If you want, you can still group your tests in classes, but it is not necessary. The pytest execution runner 
will pick up methods in which names are prefixed with "test_" or use "_test" at the end of the method name.
"""


"""By using the yield keyword instead of return, you pass the yielded object (generator) to the test method, 
and when the test method finishes with the work, the process continues at the method that yielded the object. 
After the yield keyword, you can write your teardown logic, which will be executed right after the test ends. 
You are also able to write standard xUnit fixture methods for setup and teardown. More examples can be found 
in the pytest documentation (https://docs.pytest.org/en/latest/fixture.html).
"""


"""
def test_normal_login(app):
    login = app.login('admin', 'pass')
    assert login.msg == 'success’

The test uses expected values for the username and password; the actual implementation
 if the credentials are correct can be mocked instead of using a proper staging or production 
 database. This request is expected to succeed, so you compare the output of the login message 
 with the keyword success because this is the string that the application returns on successful login attempts.


def test_empty_username_login(app):
    login = app.login('', 'pass')
    assert login.msg == 'ERR:username_empty'
"""



"""

CODE AVERAGE: 


If there is a good amount of test coverage, with meaningful tests, you can have confidence that when you do some code changes, it did not affect any other parts of the application. The code coverage can be calculated by dividing the number of lines of code tested with the total number of lines of code. The various coverage tools use also more sophisticated methods to get the real result of how many statements and conditions are tested, functions and function calls, lines of code, and so on. In Python, the coverage module can be used for testing the code coverage of your programs. It can be installed using the command pip install coverage.

To run the coverage tool on your test_login module, which contains tests for the login module, you first need to execute the command coverage run -source login -m pytest test_login. After the command finishes, you can see the report by issuing the command coverage report. The report looks like this:

~ coverage report
Name       Stmts   Miss  Cover
------------------------------
login.py    15      4       73%
You can see that your current tests for the login module cover 73 percent of the statements. Besides statement coverage, branch coverage also can be calculated. The difference between statement and branch coverage is that for statement coverage, you only need to test a statement once, no matter if it is a decision statement or not. For example, having a statement if(a): # do something, and a test that checks assert a is True, you achieved 100 percent statement coverage, but only 50 percent branch coverage, because you did not test the other possibility with assert a is False.

This is how you run the branch coverage:

~ coverage run --source login --branch -m login_test.py 
================test session starts ================
platform linux -- Python 3.7.3, pytest-5.3.0, py-1.8.0, pluggy-0.13.1
rootdir: /tests
collected 5 items                                                                                                                                                      

login_test.py .....                                                                        [100%]

================5 passed in 0.11s ================
The report now includes the branch coverage calculation for the login application module. As you can see in the next output, it is slightly lower that with statement-only coverage.

~ coverage report
Name       Stmts   Miss Branch BrPart  Cover
--------------------------------------------
login.py      15       4      9          3          71%
Unit tests can be used for TDD. TDD promotes the idea that you write the tests before you write your application logic. With TDD, test cases serve as a contract with the application that specifies how a certain unit under test (function, method, class, and so on) should behave. Observe the following process of TDD.
"""

