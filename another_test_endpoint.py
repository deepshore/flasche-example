from flask import request
from flask_restx import Resource

from ..flasche import flask_setup

# Namespace to group endpoints
namespace = flask_setup.api.namespace(
    'another-test',
    description='Another endpoint for testing'
)


@namespace.route("")
class AnotherTestEndpoint(Resource):
    status = 200

    @staticmethod
    @flask_setup.api.doc(responses={201: 'OK', 400: 'Invalid Argument', 500: 'Internal Server Error'})
    @flask_setup.metrics.summary('another_test_by_status', 'Test Request latencies by status', labels={
        'code': lambda r: r.status_code
    })
    def get():
        if 'fail' in request.args:
            return 'Not OK', 400
        else:
            return 'OK'
