"""Routes for the application."""
from flask import render_template

def register_routes(app): # type: ignore
    """Register routes for the application."""
    @app.route('/') # type: ignore
    def index(): # type: ignore
        return render_template('index.html')

    @app.route('/home') # type: ignore
    def home_page(): # type: ignore
        return render_template('home-page.html')
    
    @app.route('/login') # type: ignore
    def login(): # type: ignore
        return render_template('login.html')

    @app.route('/registration') # type: ignore
    def registration(): # type: ignore
        return render_template('registration.html')

    @app.route('/about-us') # type: ignore
    def about_us(): # type: ignore
        return render_template('about-us.html')

    @app.route('/contact-us') # type: ignore
    def contact_us(): # type: ignore
        return render_template('contact-us.html')

    @app.route('/create-event') # type: ignore
    def create_event(): # type: ignore
        return render_template('create-event.html')
    
    @app.route('/event-details') # type: ignore
    def event_details(): # type: ignore
        return render_template('event-details.html')
    
    @app.route('/booking-history') # type: ignore
    def booking_history(): # type: ignore
        return render_template('booking-history.html')