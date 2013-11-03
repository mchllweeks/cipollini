import requests
import time
from random import choice
from tempfile import TemporaryFile

class Timer:
    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start


class BandwidthWatcher:
    # this will eventually need a list of speed test
    # sites we can use
    server_list = ['http://httpbin.org/', 'http://eu.httpbin.org/', 'http://www.posttestserver.com/',
                   'https://posttestserver.com/post.php', 'http://greensuisse.zzl.org/product/dump/dump.php',
                   'http://www.newburghschools.org/testfolder/dump.php']
    max_bw = None
    min_bw = None

    def get_max_bw(self):
        """
        @return int
        """
        if not self.max_bw and not self.min_bw:
            self.max_bw = max(self.quick_baseline())
            self.min_bw = min(self.quick_baseline())
        return self.max_bw, self.min_bw

    def file_upload(self, server, file_object):
        """
        @param server string
        @param file_object file like object
        @return int average transfer rate
        """
        files = {'file': open(file_object, 'rb')}
        with Timer() as t:
            p = requests.post(server, files=files)
            p.content
        return t.interval

    @staticmethod
    def random_list_subset(lst, size):
        """
        @param lst list
        @param size int
        @return list a random subset of lst
        """
        new_list = []
        x = 0
        while x < size:
            rchoice = choice(lst)
            if rchoice not in new_list:
                new_list.append(rchoice)
                x += 1
        return new_list

    def get_file_object(self, size):
        """
        @param size file size in bytes
        """
        f = open('dev/urandom')
        f.read(size)
        tempfile = TemporaryFile()
        return f.write(tempfile)

    def file_upload_test(self, file_size, list_size):
        """
        @param file_size size of file in bytes
        @param list_size number of servers to try
        @return list returns a list of transfer rates
        """
        f = self.get_file_object(file_size)
        servers = self.random_list_subset(self.server_list, list_size)
        transfer_rates = []
        for server in servers:
            transfer_rates.append(self.file_upload(server, f))
        return transfer_rates

    def quick_baseline(self):
        """
        @return list list of averages of all multiple file_upload_test calls
        """
        list_of_averages = []

        for x in range(1, 3):
            x = x + 1
            try_small_file = self.file_upload_test(314572,5)
            for y in try_small_file:
                sum_try = y + sum_try
            try_avg = sum_try / len(try_small_file)
            list_of_averages.append(try_avg)

        return list_of_averages
