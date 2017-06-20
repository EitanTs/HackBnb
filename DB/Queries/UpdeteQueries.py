__author__ = 'Ido Bichler'

UPDATE_AVIBILITIES = """
UPDATE Availabilities
SET RenterId = '{user_id}'
WHERE 1=1
and BedId = '{bed_id}'
and date = '{check_in}'
"""