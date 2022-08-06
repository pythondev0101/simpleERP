from flask import Blueprint


bp_datatables = Blueprint('datatables', __name__, template_folder='templates', static_folder='static', static_url_path='/static/datatables')


from . import user_datatable
from . import event_location_datatable