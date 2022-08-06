from werkzeug.datastructures import ImmutableMultiDict



def format_date(date_to_format, format=None):
    if date_to_format is None:
        return ''
    
    return str(date_to_format)


def convert_to_dict(val):
    if type(val) == ImmutableMultiDict:
        return val.to_dict(flat=True)
    return None