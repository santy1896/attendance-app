from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit-attendance', methods=['POST'])
def submit_attendance():
    name = request.form['name']
    time_in = request.form['time_in']
    time_out = request.form['time_out']
    # Add code to save the attendance record to a database or file
    return 'Attendance recorded successfully!'

if __name__ == '__main__':
    app.run(debug=True)

