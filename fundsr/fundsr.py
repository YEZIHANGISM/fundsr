from datetime import datetime, timedelta
from pytz import timezone, country_timezones
from holiday import holiday


class FundSR(object):
	def __init__(self, year, month, day, hour):
		self.date, self.rdate = self.free_charge_days(year, month, day, hour)
		self._dayformat = {
				1: "一",
				2: "二",
				3: "三",
				4: "四",
				5: "五",
				6: "六",
				7: "天"
			}

	def __repr__(self):
		return (
			"申购确认日：{dy}-{dm}-{dd} 星期{w}\n" \
			"最短赎回日：{ry}-{rm}-{rd} 星期{rw}" \
			.format(dy=self.date.year, dm=self.date.month, 
					dd=self.date.day, w=self._dayformat[self.date.isoweekday()],
					ry=self.rdate.year, rm=self.rdate.month, 
					rd=self.rdate.day, rw=self._dayformat[self.rdate.isoweekday()]
			)
		)

	def free_charge_days(self, year:int, month:int, day:int, hour:int):
		tz = timezone(country_timezones('cn')[0])
		date = datetime(year, month, day, hour, minute=0, second=0, tzinfo=tz)

		# 调整申购日
		date = self._regulate_date(date, hour)

		# 赎回日
		rdate = date + timedelta(days=7)
		return {date, rdate}


	def _regulate_date(self, date, hour):
		# holiday = holiday
		week = date.isoweekday()

		if week > 5:
			hour = 16
		date = self._is_playday(date+timedelta(days=1), hour, holiday)

		return date

	def _is_playday(self, date, hour, holiday):
		week = date.isoweekday()

		if date.month in holiday.keys() and date.day not in holiday[date.month] and week <= 5:
			if hour > 15:
				return self._is_playday(date+timedelta(days=1), 10, holiday)
			else:
				return date
		return self._is_playday(date+timedelta(days=1), hour, holiday)

class Fund:
	def minrday(self, year, month, day, hour):
		return FundSR(year, month, day, hour)


fundsr = Fund()
minrday = fundsr.minrday