from flask import render_template, Blueprint, current_app
from .models import StarDatabase

# Create a blueprint for routes
main = Blueprint('main', __name__)

@main.route('/')
def index():
    """
    Homepage route
    """
    return render_template('index.html')

@main.route('/stars')
def star_list():
    """
    Display list of all stars
    """
    # Use the data path from configuration
    db = StarDatabase(current_app.config['DATA_PATH'])
    stars = db.get_all_stars()
    
    
    return render_template(
        'star_list.html', 
        stars=stars.to_dict('records'), 
        columns=stars.columns.tolist(),
    )

@main.route('/star/<int:star_id>')
def star_details(star_id):
    """
    Display details of a specific star
    
    Args:
        star_id (int): Unique identifier for the star
    """
    db = StarDatabase(current_app.config['DATA_PATH'])
    star = db.get_star_by_id(star_id)
    
    return render_template('star_details.html', star=star)
