"""Route declaration."""
from flask import current_app as app
from flask import render_template, g
import os
import toml
from datetime import datetime, timedelta


# Load the weeks data from the TOML file
toml_path = os.path.join(app.root_path, 'weeks.toml')
with open(toml_path, 'r') as f:
    course_data = toml.load(f)
weeks_data = course_data['weeks']
milestones_data = course_data.get('milestones', [])
PAPER_DUE = '2027-01-31'


@app.before_request
def before_request():
    # Make the weeks and milestones available in all templates
    g.weeks = weeks_data
    g.milestones = milestones_data


@app.context_processor
def inject_course_data():
    return dict(milestones=g.milestones, due=PAPER_DUE)


    
@app.route('/')
def index():
    # Render the index page with the weeks data
    return render_template('index.html',
                           week='index',
                           weeks=g.weeks)

@app.route('/assessment/')
def assessment():
    # Stand-alone assessment page with the milestones for each component
    return render_template('assessment.html',
                           week='assessment',
                           weeks=g.weeks)

@app.route('/week/<week_key>/')
def week(week_key):
    if week_key in g.weeks:
        # Pass the data for the specific week to the template
        return render_template(f'weeks/{week_key}.html',
                               weeks=g.weeks,
                               week=week_key)
    elif week_key == 'tones':
        return render_template(f'weeks/{week_key}.html',
                               weeks=g.weeks,
                               week=week_key)
    else:
        return "Week not found", 404

