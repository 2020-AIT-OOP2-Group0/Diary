from diaries.AbstractDiary import AbstractDiary


class TommorowDiary(AbstractDiary):

    def get_date(self):
        return "2020-11-26"

    def get_summary(self):
        return "夕方会議の予定"

    def get_author(self):
        return "It's me"