from app import app, db

from user_page.blueprint import user_page
from confirm_email.blueprint import confirm_email

import views

app.register_blueprint(user_page, url_prefix='/user_page')
app.register_blueprint(confirm_email, url_prefix='/confirm_email')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)