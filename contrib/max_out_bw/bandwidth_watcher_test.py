import os
import random
from tempfile import TemporaryFile, NamedTemporaryFile
import unittest
import requests

from bandwidth_watcher import BandwidthWatcher

class TestBandwidthWatcher(unittest.TestCase):

    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    def setUp(self):
        self.bww = BandwidthWatcher()


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


    def test_file_upload_null_file(self):
        """
        file_upload should handle when the file-obj arg is None.

        I'm going to arbitrarily pick the Python builtin exception
        ValueError, because the None file object is the wrong value.
        """
        self.assertRaises(ValueError, self.bww.file_upload, random.choice(self.bww.server_list), None)


    def test_file_upload_empty_server_string(self):
        """
        file_upload should handle empty server input - ''.

        Again, arbitrarily picking that it should raise ValueError if it gets this.
        Note that calls down the line from file_upload might raise exceptions
        subclassed from ValueError on their own...
        """
        tempfile = TemporaryFile()
        tempfile.write(os.urandom(10240))
        tempfile.seek(0)

        self.assertRaises(ValueError, self.bww.file_upload, '', tempfile)


    def test_file_upload_empty_server_none(self):
        """
        file_upload should handle empty server input - None.

        Again, arbitrarily picking that it should raise ValueError if it gets this.
        Note that calls down the line from file_upload might raise exceptions
        subclassed from ValueError on their own...
        """
        tempfile = TemporaryFile()
        tempfile.write(os.urandom(10240))
        tempfile.seek(0)

        self.assertRaises(ValueError, self.bww.file_upload, None, tempfile)


    def test_file_upload_file_went_away(self):
        """
        Your file got nuked out from under you. Now what?

        I assert that OSError should be raised, that's what comes from attempts to
        read files that have gone away (I think).  This test may need fixing.
        """
        tempfile = NamedTemporaryFile()
        tempfile.write(os.urandom(10240))
        tempfile.seek(0)
        os.remove(tempfile.name)

        self.assertRaises(OSError, self.bww.file_upload, random.choice(self.bww.server_list), tempfile)


    def test_file_upload_server_dns_fail(self):
        """
        Can't lookup a POST target server?

        This may pass now, though I'd make an argument against bubbling exceptions
        from requests up the food chain to code that shouldn't know about requests.
        (Note the expected exception here is a requests module exception.)  Probably
        file_upload should wrap all these in a single "IT NO WORKEE FOR NETWORKY REASONS"
        exception, which you'd define as a class in bandwidth_watcher.py - then rewrite
        this test to catch that exception, not requests.ConnectionError.
        """
        tempfile = TemporaryFile()
        tempfile.write(os.urandom(10240))
        tempfile.seek(0)

        self.assertRaises(requests.ConnectionError, self.bww.file_upload, 'http://thisdns-totes---doesntresolve.com/', tempfile)

    def test_file_upload_HTTP_error(self):
        # this is currently difficult because the requests.post() call isn't easily
        # mockable.  pastebin and ask gdorn and I on chat
        self.skipTest('writeme')


    def test_file_upload_connect_timeout(self):
        """
        Test server timing out.

        This may pass now, though I'd make an argument against bubbling exceptions
        from requests up the food chain to code that shouldn't know about requests.
        (Note the expected exception here is a requests module exception.)  Probably
        file_upload should wrap all these in a single "IT NO WORKEE FOR NETWORKY REASONS"
        exception, which you'd define as a class in bandwidth_watcher.py - then rewrite
        this test to catch that exception, not requests.Timeout.
        """
        tempfile = TemporaryFile()
        tempfile.write(os.urandom(10240))
        tempfile.seek(0)

        # @todo
        self.skipTest('find a host always guaranteed to *time out* even though it resolves, or mock')
        self.assertRaises(requests.Timeout, self.bww.file_upload, 'http://.com/', tempfile)



    def test_file_upload_zero_time(self):
        """
        File takes zero seconds to "upload."  Why?  Anybody's guess, but a lot of
        errors that you don't anticipate may look like that.  Or, a really fast
        connection.
        """
        self.skipTest('writeme')


    def file_upload_test(self, file_size, list_size):
        """
        Now that file-upload is battle tested, write a test for the garden path
        (expected behavior) of file_upload_test, *using mocks*.  Write several,
        depending on what can go wrong - e.g., the exceptions above that file_upload
        can raise.
        """
        self.skipTest('mchlweeks writeme - good practice')
