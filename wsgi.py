# from application import create_app

# application = create_app()

# if __name__ == "__main__":
#     application.run()

from app.main import app

if __name__ == '__main__':
    app.run()