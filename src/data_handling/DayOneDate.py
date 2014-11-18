__author__ = 'TPei'
import datetime


class DayOneDate(object):

    def __init__(self):
        """
        new DayOneDate from today()
        """
        datetime_object = datetime.datetime.today()
        self.year = datetime_object.year
        self.month = datetime_object.month
        self.day = datetime_object.day

        self.hour = datetime_object.hour
        self.minute = datetime_object.minute
        self.second = datetime_object.second

    def __str__(self):
        """
        stringifying a DayOneDate should return a valid dayone timestamp string
        """
        formatter = "%02d"
        return str(self.year) + "-" + formatter % self.month + "-" + formatter % self.day + \
               "T" + formatter % self.hour + ":" + formatter % self.minute + ":" + formatter % self.second + "Z"

    def __eq__(self, other):
        members = [self.year, self.month, self.day, self.hour, self.minute, self.second]
        other_members = [other.year, other.month, other.day, other.hour, other.minute, other.second]

        for i in range(0, len(members)):
            if members[i] != other_members[i]:
                return False
        return True


    def from_dayone_stamp(self, date_string):
        """
        managing a dayonedate from a dayone timestamp
        """
        self.year = int(date_string[0:4])
        self.month = int(date_string[5:7])
        self.day = int(date_string[8:10])

        self.hour = int(date_string[11:13])
        self.minute = int(date_string[14:16])
        self.second = int(date_string[17:19])

    def to_datetime(self):
        """
        returns a datetime object
        """
        return datetime.datetime(self.year, self.month, self.day, self.hour, self.minute, self.second)

    def from_datetime(self, datetime_object):
        """
        managing a dayonedate from a datetime object
        """
        self.year = datetime_object.year
        self.month = datetime_object.month
        self.day = datetime_object.day

        self.hour = datetime_object.hour
        self.minute = datetime_object.minute
        self.second = datetime_object.second
        return self

    def get_weekday(self):
        """
        creates a datetime object from dayone xml date format
        :param datetime object
        :return: weekday (0-6)
        """
        return self.to_datetime().weekday()


if __name__ == '__main__':
    """
    monday = 0
    ...
    sunday = 6
    """
    date = "2014-11-12T13:12:05Z"

    mydate = DayOneDate()
    print mydate
    print mydate.get_weekday()
    print mydate.to_datetime()
    mydate.from_dayone_stamp(date)
    print mydate

    print mydate == mydate

