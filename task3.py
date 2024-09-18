from datetime import datetime, timedelta
from typing import List


def schedule_gen(days: int, work_days: int, rest_days: int,
                 start_date: datetime) -> List[datetime]:
    shedule = []
    current_date = start_date
    count_days = 0

    for day in range(days):
        if count_days < days:
            for work_day in range(work_days):
                if len(shedule) < days:
                    shedule.append(current_date)
                    current_date += timedelta(days=1)
                    count_days += 1

            count_days += rest_days
            current_date += timedelta(days=rest_days)

    return shedule



assert (schedule_gen(days=5, work_days=2, rest_days=1,
                     start_date=datetime(2020, 1, 30)) ==
        [
            datetime(2020, 1, 30, 0, 0),
            datetime(2020, 1, 31, 0, 0),
            datetime(2020, 2, 2, 0, 0),
            datetime(2020, 2, 3, 0, 0)
        ])


