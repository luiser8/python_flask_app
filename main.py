from app import app
from services.users import users
from services.home import home
from services.publications import publications

app.register_blueprint(home)
app.register_blueprint(publications)
app.register_blueprint(users)

# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)
