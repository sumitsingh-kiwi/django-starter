"""
custom exception handler
"""
# third party imports
from rest_framework.views import exception_handler


def dict_list_exception_handler(error_message, response):
    """
    handle dict, list type error response
    :param error_message:
    :param response:
    :return:
    """

    if isinstance(response, dict):
        response_key = list(response.keys())[0]
        if isinstance(response[response_key], list):
            error_message.update({'detail': response[response_key][0]})
        elif isinstance(response[response_key], dict):
            error_message.update({'detail': response[response_key][list(response[response_key].keys())[0]][0]})
        else:
            error_message.update({'detail': response[response_key]})

    elif isinstance(response, list):
        error_message.update({'detail': response[0]})

    return error_message


def custom_exception_handler(exc, context):
    """
    Call REST framework's default exception handler first,
    to get the standard error response.
    :param exc: exception object
    :param context:
    :return:
    """

    response = exception_handler(exc, context)
    error_message = {}
    if response:
        exception = {'errors': response.data}
        if str(response.status_code) in ['403', '404', '405']:
            error_message.update(**response.data)
        error_message = dict_list_exception_handler(error_message, response.data)

        # add the error_message in response data
        exception.update(error_message)
        response.data = exception
    return response
