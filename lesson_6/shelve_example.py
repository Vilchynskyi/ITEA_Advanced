import shelve

db_name = 'local.db'

# with shelve.open(db_name) as db:
#     db['Country'] = ('Ukraine', 'USA', 'Spain')
#
#     for c in db.items():
#         print(c)


def create_item(id, value):
    with shelve.open(db_name) as db:
        db[f'User_{id}'] = value


def get_item(id):
    with shelve.open(db_name) as db:
        try:
            result = db[f'User_{id}']
        except KeyError:
            return

        return result


def delete_item(key):
    with shelve.open(db_name) as db:
        return db.pop(key, None)


def clear_db():
    with shelve.open(db_name) as db:
        db.clear()


create_item('Name', 'Max')
create_item('Car', '+')

# delete_item('Name')
print(get_item('Name'), get_item('Car'))
