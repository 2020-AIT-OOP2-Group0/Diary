from diaries.SampleDiary import DiarySample
from diaries.NagataniDiaryNew import NagataniDiaryNew

diaries = [DiarySample(), NagataniDiaryNew(), ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()