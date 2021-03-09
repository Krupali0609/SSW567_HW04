import unittest
from Testing import get_repository_details

class TestgetRepo(unittest.TestCase):
    def test_repo(self):
        expected = ['User: Krupali0609',
                    'Repository Name: HelloWorld Number of commits in Repository: 2',
                    'Repository Name: Software-Quality-Assurance-and-Testing-567 Number of commits in Repository: 2',
                    'Repository Name: SSW567_HW04 Number of commits in Repository: 9',
                    'Repository Name: Student-Repository Number of commits in Repository: 23',
                    'Repository Name: Triangle567 Number of commits in Repository: 11']

        self.assertEqual(get_repository_details('Krupali0609'), expected)

"""excution starts from here"""
if __name__ == '__main__':   
    unittest.main()
