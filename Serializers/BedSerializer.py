__author__ = 'fuck'
from DB.SqlExecuter import SqlExecuter
from DB.Queries import SelectQueries
from Objects.Bed import Bed

class BedSerializer(object):
    def __init__(self, check_in, check_out):
        self.check_in = check_in
        self.check_out = check_out

    @property
    def query(self):
        if self.check_in is None and self.check_out is None:
            return SelectQueries.ALL_BED_AVG_RANK
        return SelectQueries.BED_AVG_RANK.format(check_in=self.check_in, check_out=self.check_out)

    def _get_beds_json(self):
        data = SqlExecuter().get_table_content_as_json(self.query)
        beds_dict = {}
        for row in data:
            bed_id = row.get('BedId')
            param_key = row.get('ParamKey')
            param_value = row.get('average')
            date = row.get('Date')
            if beds_dict.get(bed_id):
                beds_dict[bed_id][param_key] = param_value
                if date not in beds_dict[bed_id]['dates']:
                    beds_dict[bed_id]['dates'].append(date)
            else:
                beds_dict[bed_id] = {param_key: param_value}
                beds_dict[bed_id]['dates'] = [date]
        return beds_dict

    def serialize_bed_objects(self):
        beds_dict = self._get_beds_json()
        return [Bed(bed, beds_dict[bed]) for bed in beds_dict.keys()]
