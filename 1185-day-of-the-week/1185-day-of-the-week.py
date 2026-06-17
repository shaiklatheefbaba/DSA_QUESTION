class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days = ["Friday", "Saturday", "Sunday",
                "Monday", "Tuesday", "Wednesday", "Thursday"]

        month_days = [31, 28, 31, 30, 31, 30,
                      31, 31, 30, 31, 30, 31]

        def is_leap(y):
            return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)

        total_days = 0

        # Add days for complete years
        for y in range(1971, year):
            total_days += 366 if is_leap(y) else 365

        # Add days for complete months
        for m in range(month - 1):
            total_days += month_days[m]

            # Leap year adjustment for February
            if m == 1 and is_leap(year):
                total_days += 1

        # Add days in current month
        total_days += day - 1

        return days[total_days % 7]