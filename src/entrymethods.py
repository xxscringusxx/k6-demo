def create_entry(request):
    name = request.form['name']
    age = request.form['age']
    address = request.form['address']

    entry = f'{name},{age},{address}'
    return entry

