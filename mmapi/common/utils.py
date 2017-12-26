"""
Helpers for the API views modules.
"""
from flask import jsonify, request


def get_request_data():
    """
    Get data from request

    :return: Json data or form data
    :rtype: dict
    """
    return request.get_json() or request.form


def validation_error(errors):
    """
    Returns the API's validation error response.

    :param errors: A dict of the errors.
    :type errors: dict
    :rtype: :class:`flask.wrappers.Response`
    """
    generic_errors = errors.pop('schema', [])

    response = jsonify({'fieldErrors': errors, 'genericErrors': generic_errors})
    response.status_code = 400
    return response
