import unittest

from python_repos import get_python_repos


class TestPythonRepos(unittest.TestCase):
    """Testing python_respon.py."""

    def test_status_code(self):
        """Test that the API call returns a 200 status code."""
        r = get_python_repos()
        self.assertEqual(r.status_code, 200)


unittest.main()
