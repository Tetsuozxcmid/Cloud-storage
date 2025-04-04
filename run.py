from app.main import create_app
import logging

flask_app = create_app()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    
    flask_app.run(host='127.0.0.1', port=8002)