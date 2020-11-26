from diaries.SampleDiary import DiarySample
from diaries.TomorrowDiary import TomorrowDiary

diaries = [
    DiarySample(), 
    TomorrowDiary(),
    ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
