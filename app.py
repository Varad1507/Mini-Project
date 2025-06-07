from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
notes = []  # simple in-memory storage

@app.route('/')
def index():
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['GET', 'POST'])
def add_note():
    if request.method == 'POST':
        note = request.form['note']
        notes.append(note)
        return redirect(url_for('index'))
    return render_template('add_note.html')

@app.route('/delete/<int:index>')
def delete_note(index):
    if 0 <= index < len(notes):
        notes.pop(index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=8080)
