import unittest

from bandwidth_watcher import BandwidthWatcher

class TestBandwidthWatcher(unittest.TestCase):

    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    def setUp(self):
        self.bww = BandwidthWatcher()

    #def random_list_subset(self, lst, size):
    #    """
    #    @param lst list
    #    @param size int
    #    @return list a random subset of lst
    #    """
    #    new_list = []
    #    x = 0
    #    while x <= size:
    #        new_list.append(choice(lst))
    #        x += 1
    #    return new_list


    def test_random_list_subset(self):
        """
        Basic checks on BandwidthWatcher.random_list_subset.
        """

        sublist_size = 2
        sublist = self.bww.random_list_subset(self.l, sublist_size)

        returned_len = len(sublist)
        self.assertEqual(returned_len, sublist_size,
                         "Asked for a sublist of length %d, got one of length %d." % (sublist_size, returned_len))

        for entry in sublist:
            self.assertTrue(entry in self.l,
                            "Found an entry in sublist that isn't in parent list. wtf?")


    def test_random_list_subset_is_a_set(self):
        """
        Check that the subset is actually a set, e.g. there are no duplicate
        entries.
        """

        sublist_size = 10
        sublist = self.bww.random_list_subset(self.l, sublist_size)

        for entry in sublist:
            self.assertEqual(sublist.count(entry), 1,
                             "Found a non-unique entry in list representing a subset")


    def test_random_list_subset_size(self):
        """
        Test that the subset is actually the size we want.  This flushes out
        other duplicate-related, setness-related bugs.
        """
        sublist_size = 15
        sublist = self.bww.random_list_subset(self.l, sublist_size)
        returned_len = len(sublist)
        self.assertEqual(returned_len, sublist_size,
                         "Returned subset list was size %d but we wanted size %d" % (returned_len, sublist_size))
