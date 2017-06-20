__author__ = 'Ido Bichler'
from Configuration import REVIEW_PARAMS, BED_PLACES
from DB.Queries import SelectQueries
from DB.SqlExecuter import SqlExecuter

class Bed(object):

    DEFAULT_SCORE = len(REVIEW_PARAMS) / 2 + 1

    def __init__(self, bed_id, bed_dict):
        self.bed_id = bed_id
        self.bed_dict = bed_dict
        self.dates = bed_dict.get('dates')
        self.score = None

    def calc_score(self, renter_preferences_json):
        score = 0
        for param in REVIEW_PARAMS:
            bed_param_score = self.bed_dict.get(param)
            if not bed_param_score:
                bed_param_score = self.DEFAULT_SCORE
            renter_param_score = renter_preferences_json.get_preferences().get(param)
            if not renter_param_score:
                renter_param_score = self.DEFAULT_SCORE
            score += int(bed_param_score) * int(renter_param_score)
        total_score = float(score) / len(REVIEW_PARAMS)
        self.score = total_score

    def get_bed_offer_data(self):
        query = SelectQueries.BED_OFFER_INFO.format(BedId=self.bed_id)
        data = SqlExecuter().get_table_content_as_json(query)[0]
        data['building'] = data['place'].split('_')[0]
        data['room'] = data['place'].split('_')[1]
        data['bed'] = BED_PLACES[int(data['place'].split('_')[2])].decode('utf-8')
        data['owner'] = self._get_user_name(data['UserId'])
        data['last_use'] = self._get_last_bed_usage()
        data['picture_path'] = self._get_picture_path(data['RoomId'])
        data['bed_avg'] = self.bed_dict
        data['score'] = self.score
        data['room_id_display'] = data['RoomId'].replace('_', '')
        data['dates'] = self.dates
        data['bed_id'] = self.bed_id
        return data

    @staticmethod
    def _get_user_name(user_id):
        user_name_query = SelectQueries.FULL_NAME_FROM_USER_ID.format(user_id=user_id)
        name_dict = SqlExecuter().get_table_content_as_json(user_name_query)[0]
        return name_dict.get('FirstName') + ' ' + name_dict.get('LastName')

    def _get_last_bed_usage(self):
        last_bed_usage = SelectQueries.LAST_BED_ID_USAGE.format(bed_id=self.bed_id)
        return SqlExecuter().get_table_content_as_json(last_bed_usage)[0]['last_usage']

    @staticmethod
    def _get_picture_path(room_id):
        query = SelectQueries.GET_ROOM_PICTURE_PATH.format(room_id=room_id)
        return SqlExecuter().get_table_content_as_json(query)[0]['PicturePath']

    @staticmethod
    def get_bed_id_by_user(user_id):
        query = SelectQueries.BED_ID_FROM_USER_ID.format(user_id=user_id)
        return SqlExecuter().get_table_content_as_json(query)[0]['BedId']