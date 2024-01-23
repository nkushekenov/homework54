from rest_framework_jwt.utils import jwt_payload_handler, jwt_encode_handler

def custom_jwt_payload_handler(user):
    payload = jwt_payload_handler(user)
    payload['custom_field'] = user.custom_field
    return payload

def generate_jwt_token(user_id):
    payload = {'user_id': user_id}
    return jwt_encode_handler(payload)