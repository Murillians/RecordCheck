import functools
import RecordChecker
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for,session
)
from werkzeug.exceptions import abort

bp = Blueprint('recordsearch', __name__,url_prefix='/recordsearch')
@bp.route('/recordsearch', methods=('GET', 'POST'))

def search():
    if request.method == 'POST':
        query = request.form['query']
        error= None
        if not query:
            error='Have to search something!'
        flash(error)
        return redirect(url_for('recordsearch.results',query=query))
    return render_template('recordsearch/recordsearch.html')
@bp.route('/results/<query>')
def results(query):
    records = RecordChecker.spotifySearch(query)
    return render_template('recordsearch/results.html',records=records)

