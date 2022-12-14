"""Test the libaudiothek module."""

import unittest
from libaudiothek.libaudiothek import Audiothek, AudiothekSearchResult


class TestSearchMethods(unittest.TestCase):
    """Test the search method of the Audiothek class.
    This test will fail if the API is not available.
    """

    def test_search(self):
        """ There should be results for the search term 'Krimi'."""
        audiothek: Audiothek = Audiothek()
        result: AudiothekSearchResult = audiothek.search("Krimi")
        self.assertTrue(result.result_count > 0)
        self.assertTrue(len(result.items) > 0)
        self.assertTrue(len(result.program_sets) > 0)
        self.assertEqual(len(result.items) +
                         len(result.program_sets), result.result_count)

    def test_search_empty(self):
        """There should be no results for the search term 'oL16WfaRL2WVMlk3GkP7'."""
        audiothek: Audiothek = Audiothek()
        result: AudiothekSearchResult = audiothek.search(
            "oL16WfaRL2WVMlk3GkP7")
        self.assertTrue(result.result_count == 0)
        self.assertTrue(len(result.items) == 0)
        self.assertTrue(len(result.program_sets) == 0)
        self.assertEqual(len(result.items) +
                         len(result.program_sets), result.result_count)


if __name__ == '__main__':
    unittest.main()
