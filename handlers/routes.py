from flask import render_template, redirect, request, url_for, send_file
from flask_login import login_user, logout_user, current_user, login_required
from flask import session
from flask import jsonify

from io import BytesIO

from app.models.User import User
from app.models.Object import Object


def register_routes(app, db):
    @app.route('/', methods=['GET', 'POST'])
    @login_required
    def index():
        files = []
        if request.method == 'POST':
            file = request.files['file']
            upload = Object(filename=file.filename, data=file.read(
            ), user_name=current_user.name, user_id=current_user.id)
            db.session.add(upload)
            db.session.commit()
        files = Object.query.all()
        return render_template('index.html', user=current_user, db=db, files=files)

    @app.route('/download/<upload_id>')
    def download(upload_id):
        upload = Object.query.filter_by(id=upload_id).first()
        return send_file(BytesIO(upload.data), download_name=upload.filename, as_attachment=True)

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'GET':
            return render_template('register.html')
        elif request.method == 'POST':
            name = request.form.get('name')
            password = request.form.get('password')
            user = User(name=name, password=password)
            db.session.add(user)
            db.session.commit()
            if not name or not password:
                return jsonify({'error': 'Missing name or password'}), 400
            token = user.get_token()
            login_user(user)
            
            return redirect(url_for('index'))

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'GET':
            return render_template('login.html')
        elif request.method == 'POST':
            name = request.form.get('name')
            password = request.form.get('password')
            user = User.authenticate(name, password)
            if user:
                login_user(user)
                session['user_id'] = user.id
            return redirect(url_for('index'))
        else:
            fail = "Authentication failed, user does not exist"
            return redirect(url_for('index',fail=fail))

    @app.route('/delete/<upload_id>', methods=['GET', 'POST'])
    @login_required
    def delete(upload_id):
        upload = Object.query.filter_by(id=upload_id).first()
        if upload and upload.user_id == current_user.id:
            db.session.delete(upload)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            return "You are not authorized to delete this file", 403

    @app.route('/logout', methods=['GET', 'POST'])
    def logout():
        logout_user()
        return redirect(url_for('index'))
