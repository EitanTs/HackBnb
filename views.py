"""
Routes and views for the flask application.
"""

from flask import render_template, Flask, request, session, url_for, redirect
from Tables.TableUsers import TableUsers
from Tables.TableRooms import TableRooms
from Tables.TableRoomRating import TableRoomRating
from Tables.TableBeds import TableBeds
from Tables.TableAvailabilities import TableAvailabilities
from Tables.TablePreferences import TablePreferences
from Objects.Bed import Bed
from Manager.BedManager import BedManager
from Manager.LoginManager import LoginManager
from DB.Queries import UpdeteQueries
from DB.SqlExecuter import SqlExecuter
import Configuration

app = Flask(__name__)
app.secret_key = '123'


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/show_login')
def show_login():
    return render_template('Login.html')


@app.route('/sign_in')
def sign_in():
    return render_template('SignInForm.html')


@app.route('/sign_up_first_step', methods=['POST'])
def first_sign_in_step():
    form = request.form
    session['user_id'] = form.get('user_id')
    table_user = TableUsers(user_id=form.get('user_id'), password=form.get('password'),
                            first_name=form.get('first_name'), last_name=form.get('last_name'),
                            phone_number=form.get('phone_number'), voip=form.get('voip'), is_owner=form.get('owner'))
    if not table_user.is_exist('UserId', form.get('user_id')):
        SqlExecuter().insert_object_to_db(table_user)
    return render_template('SignInSecondStep.html', param_list=Configuration.REVIEW_PARAMS)


@app.route('/sign_in_owner', methods=['POST'])
def owner_sign_in():
    form = request.form
    building = form.get('building')
    room_number = form.get('room_number')
    bed_number = form.get('bed_number')
    description = form.get('description')
    bed_id = generate_bed_id(room_number=room_number, building=building,
                             bed_number=bed_number)
    room_id = generate_room_id(building=building, room_number=room_number)

    bed_object = TableBeds(bed_id=bed_id, user_id=session['user_id'], bed_number=bed_number, room_id=room_id,
                           description=description)
    room_table = TableRooms(room_id=room_id, building=building,
                            room_number=room_number)

    if not bed_object.is_exist('BedId', bed_id):
        SqlExecuter().insert_object_to_db(bed_object)
    if not room_table.is_exist('RoomId', room_id):
        SqlExecuter().insert_object_to_db(room_table)

    rating_object = TableRoomRating(room_id=room_id, param_key='description', param_value=form.get('description'),
                                    user_id=session['user_id'])
    SqlExecuter().insert_object_to_db(rating_object)

    for param in Configuration.REVIEW_PARAMS:
        rating_object = TableRoomRating(room_id=room_id, param_key=param, param_value=form.get(param),
                                        user_id=session['user_id'])
        SqlExecuter().insert_object_to_db(rating_object)

    return render_template('index.html')


@app.route('/sign_in_renter', methods=['POST'])
def renter_sign_in():
    form = request.form
    for param in Configuration.REVIEW_PARAMS:
        rating_object = TablePreferences(param_key=param, param_value=form.get(param), user_id=session['user_id'])
        SqlExecuter().insert_object_to_db(rating_object)

    return render_template('index.html')


@app.route('/get_beds/<check_in>/<check_out>')
def get_beds(check_in, check_out):
    beds_objects = BedManager(session['user_id'], check_in, check_out).get_bed_data()
    # beds_objects = BedManager('tom', check_in, check_out).get_bed_data() or []
    return render_template('beds.html', bed_objects=beds_objects)


@app.route('/login', methods=['POST'])
def login():
    form = request.form
    is_valid = LoginManager(form.get('user_id'), form.get('password')).is_valid()
    if is_valid:
        return render_template('index.html')
    return render_template('login.html')


@app.route('/review', methods=['POST'])
def enter_bed_review():
    form = request.form
    room_id = form.get('room_id')
    current_user = session['user_id']
    rating_object = TableRoomRating(room_id=room_id, param_key='description', param_value=form.get('description'),
                                    user_id=current_user)
    SqlExecuter().insert_object_to_db(rating_object)

    for param in Configuration.REVIEW_PARAMS:
        rating_object = TableRoomRating(room_id=room_id, param_key=param, param_value=form.get(param),
                                        user_id=current_user)
        SqlExecuter().insert_object_to_db(rating_object)
        return render_template('index.html')


@app.route('/add_availabilities/<check_in>')
def add_availabilities(check_in):
    # form = request.form
    # check_in = form.get('check_in')
    # check_out = form.get('check_out')
    current_user = session['user_id']
    bed_id = Bed.get_bed_id_by_user(current_user)
    availabilities_object = TableAvailabilities(bed_id=bed_id, date=check_in, user_id=current_user, renter_id=None)
    is_exist_query = availabilities_object.IS_EXIST_QUERY.format(table_name=availabilities_object.table_name,
                                                                 column_key='BedId', column_value=bed_id)
    is_exist_query += " and date='{check_in}'".format(check_in=check_in)
    if not availabilities_object.is_exist('', '', query=is_exist_query):
        SqlExecuter().insert_object_to_db(availabilities_object)

    return render_template('index.html')


@app.route('/rent_room/<bed_id>/<check_in>')
def rent_room(bed_id, check_in):
    print session['user_id'], bed_id, check_in
    update_query = UpdeteQueries.UPDATE_AVIBILITIES.format(user_id=session['user_id'], bed_id=bed_id, check_in=check_in)
    SqlExecuter().execute_query(update_query)
    #return render_template('index.html')
    return redirect("/", code=200)


def generate_bed_id(building, room_number, bed_number):
    return Configuration.BED_ID_FORMAT.format(building=building, room_number=room_number, bed_number=bed_number)


def generate_room_id(building, room_number):
    return Configuration.ROOM_ID_FORMAT.format(building=building, room_number=room_number)
