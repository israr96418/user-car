
def get_database_url():
    url = "sqlite:///database.sqlite"
    # url = "mysql+mysqldb://bwithai:sana123@localhost:3306/notifications"
    # db_password = urllib.parse.quote_plus(settings.db_pass)
    # url = f"postgresql://{settings.db_user}:{db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}"
    return url