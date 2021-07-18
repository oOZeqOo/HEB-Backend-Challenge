from flask import abort, jsonify, make_response


def abort_response(message, code=400):
    return abort(make_response(jsonify(message=message), code))


def bad_request():
    return make_response(jsonify(message="Bad Request"), 400)


def not_found():
    return make_response(jsonify(message="Not Found"), 404)


def unprocessable_entity():
    return make_response(jsonify(message="Unprocessable Entity"), 422)
