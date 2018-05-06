import unittest


class RecentlyUsedList(object):

    def __init__(self):
        self.list = []

    def add_number(self, number):
        capacity = 10
        if len(self.list) == capacity:
            self.list.pop()
        if number in self.list:
            self.list.remove(number)
        self.list.insert(0, number)


class RecentlyUsedTests(unittest.TestCase):

    def setUp(self):
        self.recently_used = RecentlyUsedList()

    def test_empty_list(self):
        self.assertTrue(not self.recently_used.list)

    def test_one_number_index_zero_should_be_self(self):
        self.recently_used.add_number('810-923-4093')
        self.assertEquals(1, len(self.recently_used.list))
        self.assertEquals('810-923-4093', self.recently_used.list[0])

    def test_last_number_in_first_out(self):
        self.recently_used.add_number('810-923-4093')
        self.recently_used.add_number('810-923-4437')
        self.assertEquals('810-923-4437', self.recently_used.list[0])

    def test_capacity_is_ten(self):
        for index, number in enumerate(range(11)):
            self.recently_used.add_number('810-923-409{}'.format(index % 10))
        self.assertEquals(10, len(self.recently_used.list))
        self.assertEquals('810-923-4091', self.recently_used.list.pop())

    def test_adding_a_duplicate_number_moves_to_front_of_list(self):
        self.recently_used.add_number('810-923-4093')
        self.recently_used.add_number('810-923-4437')
        self.recently_used.add_number('810-923-4093')
        self.assertEquals(2, len(self.recently_used.list))
        self.assertEquals('810-923-4093', self.recently_used.list[0])
