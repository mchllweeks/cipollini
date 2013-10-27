import requests
from random import choice
from tempfile import TemporaryFile

class BandwidthWatcher:
    # this will eventually need a list of speed test
    # sites we can use
    server_list = []
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
        upload = requests.post(server, data=file_object)
        return upload.content

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
        f.write(tempfile)

    def file_upload_test(self, file_size, list_size):
        """
        @param file_size size of file in bytes
        @param list_size number of servers to try
        @return list returns a list of transfer rates
        """
        f = self.get_file_object(file_size)
        servers = self.random_list_subset(self.server_list, size)
        transfer_rates = []
        for server in servers:
            transfer_rates.append(self.file_upload(server, f))
        return transfer_rates

    def quick_baseline(self):
        """
        @return list list of averages of all multiple file_upload_test calls
        """
        list_of_averages = []
        try1_small_file = self.file_upload_test(314572,5)
        for x in try1_small_file:
            sum_try1 = x + sum_try1
        try1_avg = sum_try1 / len(try1_small_file)
        list_of_averages.append(try1_avg)

        try2_small_file = self.file_upload_test(314572,5)
        for x in try2_small_file:
            sum_try2 = x + sum_try2
        try2_avg = sum_try2 / len(try2_small_file)
        list_of_averages.append(try2_avg)

        try3_small_file = self.file_upload_test(314572, 5)
        for x in try3_small_file:
            sum_try3 = x + sum_try3
        try3_avg = sum_try3 / len(try3_small_file)
        list_of_averages.append(try3_avg)

        try1_large_file = self.file_upload_test(2097152, 5)
        for x in try1_large_file:
            sum_try1 = x + sum_try1
        try1_avg = sum_try1 / len(try1_large_file)
        list_of_averages.append(try1_avg)

        try2_large_file = self.file_upload_test(2097152, 5)
        for x in try1_large_file:
            sum_try2 = x + sum_try2
        try2_avg = sum_try2 / len(try2_large_file)
        list_of_averages.append(try2_avg)

        return list_of_averages
