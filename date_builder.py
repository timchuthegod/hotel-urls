import datetime as dt

def planToUrls(location_list, num_days_list, starting_date, numAdults=4, numChildren=0):
	date_list = DateList(starting_date, num_days_list)
	return HotelUrls(location_list, date_list, numAdults, numChildren)
	
def DateList(starting_date, num_days_list):
	date_list =  [starting_date]
	cur_date = starting_date
	for d in num_days_list:
		cur_date += dt.timedelta(d)
		date_list.append(cur_date)
	return date_list

def dateTimeToString(datetime_object):
	return datetime_object.strftime("20%y-%m-%d")

def HotelUrls(location_list, date_list, numAdults=4, numChildren=0):
	a = "https://www.hotels.com/search.do?resolved-location=GEO_LOCATION%3A"
	b = "%7C65.2668743%7C-14.3948468%3AGEOCODE%3AUNKNOWN&q-destination="
	c = "&q-check-in="
	d = "&q-check-out="
	e = "&q-rooms=1&q-room-0-adults="
	f = "&q-room-0-children="
	g = " &sort-order=DISTANCE_FROM_LANDMARK"
	urls = []
	for i in range(len(location_list)):
		loc = location_list[i]
		date_in = date_list[i]
		date_out = date_list[i+1]
		url = a + loc + b + loc + c + dateTimeToString(date_in) + d + dateTimeToString(date_out) + e + str(numAdults) + f + str(numChildren) + g
		urls.append(url)
	return urls

# Utils to handle different input formats.
def GetLocationsAndDates(locations_and_days):
	# Turn pair of lists into list of pairs
	locs_list, days_list = map(list, zip(*locations_and_days))
	dates_list = DateList(starting_date, days_list)
	return (locs_list, dates_list)


