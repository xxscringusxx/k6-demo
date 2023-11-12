from flask import Flask, render_template, request
from src import entrymethods 

app = Flask(__name__)
user_info_file = 'user_info.txt'
unique_entries = entrymethods.read_existing_entries(user_info_file)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/save', methods=['POST'])
def save():
    entry = entrymethods.create_entry(request)

    if entry in unique_entries:
        return 'Information already exists!'

    unique_entries.add(entry)
    entrymethods.add_entry_to_file(user_info_file, entry)

    return 'Information saved successfully!'

if __name__ == '__main__':
    app.run(debug=True)
