from saunter.testcase.remotecontrol import SaunterTestCase


class Suite101BaseTestCase(SaunterTestCase):
    """
    Suite101 Base TestCase, inherits from the Saunter Test TestCase

    This will allow us to create our own custom asserts or base test case methods
    without modifying the Saunter Base TestCase
    """

    def our_custom_assert(self):
        pass
