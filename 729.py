class MyCalendar:

    def __init__(self):
        self.calendar = list()

    def book(self, start: int, end: int) -> bool:
        for booking in self.calendar:
            if start >= booking['end'] or end <= booking['start']:
                pass
            else:
                return False
        new = dict()
        new['start'] = start
        new['end'] = end
        self.calendar.append(new)
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
