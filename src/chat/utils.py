from sqlalchemy.engine.row import Row

def validate_to_dict(row: Row):
    dict_row = dict()
    for key in row.keys():
        dict_row[key] = row[key]
    return dict_row