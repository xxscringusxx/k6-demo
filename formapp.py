from flask import Flask, render_template, request, redirect, url_for
from src.entrymethods import create_entry
from src.filemanager import FileManager

app = Flask(__name__)
user_info_file = 'user_info.txt'
file_manager = FileManager(user_info_file)

# Define existing_entries as a global variable
existing_entries = file_manager.read_existing_entries()

@app.route('/', methods=['GET', 'POST'])  # Allow both GET and POST requests
def index():
    if request.method == 'POST':
        entry = create_entry(request)

        if entry not in existing_entries:
            file_manager.add_entry_to_file(entry)
            existing_entries.add(entry)

    entries = [{'name': name, 'age': age, 'address': address} for name, age, address in (entry.split(',') for entry in existing_entries)]
    return render_template('form.html', entries=entries)

@app.route('/delete', methods=['POST'])
def delete():
    entry_to_delete = request.form['entry']

    if entry_to_delete in existing_entries:
        existing_entries.remove(entry_to_delete)
        file_manager.write_entries_to_file(existing_entries)  # Update the file without the deleted entry

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
