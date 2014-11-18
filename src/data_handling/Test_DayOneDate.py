__author__ = 'TPei'
import unittest
from DayOneDate import DayOneDate
import datetime


class TestDayOneDate(unittest.TestCase):

    def test_creation(self):
        today = DayOneDate()
        self.assertEqual(today.year, datetime.datetime.today().year)
        self.assertEqual(today.month, datetime.datetime.today().month)
        self.assertEqual(today.day, datetime.datetime.today().day)
        self.assertEqual(today.hour, datetime.datetime.today().hour)
        self.assertEqual(today.minute, datetime.datetime.today().minute)

    def test_stringify(self):
        today = DayOneDate()
        formatter = "%02d"
        compare = str(today.year) + "-" + formatter % today.month + "-" + formatter % today.day + \
               "T" + formatter % today.hour + ":" + formatter % today.minute + ":" + formatter % today.second + "Z"
        self.assertEqual(str(today), str(compare))

    def test_to_datetime(self):
        today = DayOneDate()
        tdt = datetime.datetime(today.year, today.month, today.day, today.hour, today.minute, today.second)
        self.assertEqual(today.to_datetime(), tdt)

    def test_from_datetime(self):
        today = DayOneDate()
        tdt = datetime.datetime(today.year, today.month, today.day, today.hour, today.minute, today.second)
        compare = DayOneDate().from_datetime(tdt)
        self.assertEqual(today, compare)

    def test_equals(self):
        today = DayOneDate()
        second = today
        self.assertTrue(today == second)
        second = DayOneDate().from_datetime(datetime.datetime.today() - datetime.timedelta(1))
        self.assertFalse(today == second)


if __name__ == '__main__':
    unittest.main()