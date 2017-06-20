BED_AVG_RANK = """select a.BedId, r.ParamKey, avg(r.ParamValue) as average, date
from Availabilities as a
left join Beds as b
on a.BedId = b.BedId
join RoomRating as r
on r.RoomId = b.RoomId
where 1=1
and date between '{check_in}' and '{check_out}'
and RenterId is NULL
group by date, r.ParamKey, b.BedId"""

ALL_BED_AVG_RANK = """select a.BedId, r.ParamKey, avg(r.ParamValue) as average, date
from Availabilities as a
left join Beds as b
on a.BedId = b.BedId
join RoomRating as r
on r.RoomId = b.RoomId
where 1=1
and RenterId is NULL
group by date, r.ParamKey, b.BedId"""


USER_PREFRENCES = """ select ParamKey, ParamValue
from Preferences
where 1=1
and UserId = '{user_id}'"""

BED_OFFER_INFO = """ select BedId as place, UserId, description, RoomId
from Beds
where 1=1
and BedId = '{BedId}' """

FULL_NAME_FROM_USER_ID = """ select FirstName, LastName
from Users
where UserId = '{user_id}' """

LAST_BED_ID_USAGE = """ select max(date) as last_usage
from Availabilities
where BedId = '{bed_id}'
and RenterId is not NULL """

GET_ROOM_PICTURE_PATH ="""
select PicturePath
from Rooms
where RoomId = '{room_id}' """

VALIDE_USER_AND_PASSWORD = """ SELECT EXISTS (
  SELECT * FROM Users WHERE UserId = '{user_id}' AND Password = '{password}'
) as valid"""

BED_ID_FROM_USER_ID = """
select BedId
from Beds
where UserId = '{user_id}' """