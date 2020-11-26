from diaries.AbstractDiary import AbstractDiary


class NagataniDiaryNew(AbstractDiary):

    def get_date(self):
        return "2020-11-26"

    def get_summary(self):
        return "資料が全然そろってなくて焦った"

    def get_author(self):
        return "Nagatani"