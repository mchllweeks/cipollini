from random import choice

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
        return self.max_bw

    def file_upload(self, server, file_object):
        """
        @param server string
        @param file_object file like object
        @return int average transfer rate
        """
        pass

    @staticmethod
    def random_list_subset(lst, size):
        """
        @param lst list
        @param size int
        @return list a random subset of lst
        """
        new_list = []
        x = 0
        while x <= size:
            new_list.append(choice(lst))
            x += 1
        return new_list

    def get_file_object(self, size):
        """
        @param size file size in megabytes
        """
        pass

    def quick_baseline(self):
        """
        """
        f = self.get_file_object(1)
        servers = self.random_list_subset(self.server_list, 5)
        transfer_rates = []
        for server in servers:
            transfer_rates.append(self.file_upload(server, f))
