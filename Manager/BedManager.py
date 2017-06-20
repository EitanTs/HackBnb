__author__ = 'Ido Bichler'

from Objects.RentUser import RentUser
from Serializers.BedSerializer import BedSerializer


class BedManager(object):
    def __init__(self, user_id, check_in, check_out):
        self.rent_user = RentUser(user_id)
        self.check_in = check_in
        self.check_out = check_out

    def get_relevant_beds_scores(self):
        relevant_beds = BedSerializer(self.check_in, self.check_out).serialize_bed_objects()
        for bed_object in relevant_beds:
            bed_object.calc_score(self.rent_user)
        relevant_beds.sort(key=self._get_bed_score)
        return relevant_beds

    def get_bed_data(self):
        return [bed.get_bed_offer_data() for bed in self.get_relevant_beds_scores()]

    @staticmethod
    def _get_bed_score(bed_object):
        return bed_object.score