import unittest
from testAll_chrome import TestHome as TestHomeC
from testAll_firefox import TestHome as TestHomeF
from testAll_chrome import TestAbout as TestAboutC
from testAll_firefox import TestAbout as TestAboutF
from concurrencytest import ConcurrentTestSuite, fork_for_tests

def suite():
    suite = unittest.TestSuite()
    # Home page tests
    suite.addTest(TestHomeC('test_TC001_py3_doc_button'))
    suite.addTest(TestHomeC('test_TC002_blahblah_search'))
    suite.addTest(TestHomeC('test_TC004_assert_title'))
    suite.addTest(TestHomeF('test_TC001_py3_doc_button'))
    suite.addTest(TestHomeF('test_TC002_blahblah_search'))
    suite.addTest(TestHomeF('test_TC004_assert_title'))
    # About page tests 
    suite.addTest(TestAboutC('test_TC003_verify_upcoming_events_section_present'))
    suite.addTest(TestAboutC('test_TC005_assert_url'))
    suite.addTest(TestAboutF('test_TC003_verify_upcoming_events_section_present'))
    suite.addTest(TestAboutF('test_TC005_assert_url'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    suite = suite()
    concurrent_suite = ConcurrentTestSuite(suite, fork_for_tests(5))
    runner.run(concurrent_suite)