from flask import Blueprint

test_api = Blueprint('test_api', __name__)


@test_api.route('/test')
def test():
    return 'FLask blueprint works'
