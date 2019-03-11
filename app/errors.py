from flask import render_template
from app import app, db


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()  # ensure that failed db session don´t interfere with regular db accesses
    return render_template('500.html'), 500

