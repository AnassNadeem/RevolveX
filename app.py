from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

# Ensure the "reviews.db" file exists and create the reviews table if it doesn't
if not os.path.isfile('reviews.db'):
    conn = sqlite3.connect('reviews.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            review TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('indexs.html')

@app.route('/reviews_page')
def reviews_page():
    # Fetch reviews from the database
    conn = sqlite3.connect('reviews.db')
    c = conn.cursor()
    c.execute('SELECT * FROM reviews')
    reviews = c.fetchall()
    conn.close()

    return render_template('reviews.html', reviews=reviews)

@app.route('/submit_review', methods=['POST'])
def submit_review():
    # Get user review data from the form
    username = request.form.get('username')
    review = request.form.get('review')

    # Insert review into the database
    conn = sqlite3.connect('reviews.db')
    c = conn.cursor()
    c.execute('INSERT INTO reviews (username, review) VALUES (?, ?)', (username, review))
    conn.commit()
    conn.close()

    # Redirect to the "reviews_page" after submitting the review
    return redirect(url_for('reviews_page'))

# Additional routes
@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/work')
def work():
    return render_template('work.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/reviews')
def reviews():
    return render_template('reviews.html')

@app.route('/indexs')
def indexs():
    return render_template('indexs.html')

if __name__ == '__main__':
    app.run(debug=True)
