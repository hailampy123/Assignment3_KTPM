import unittest
from testings.create_competition import CreateCompetition

# Load tests from test sase
create_competition_test = unittest.TestLoader().loadTestsFromTestCase(CreateCompetition)

# Create TestSuite
test_suite = unittest.TestSuite([create_competition_test])

# Run
unittest.TextTestRunner(verbosity=2).run(test_suite)
