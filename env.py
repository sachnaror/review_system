SECRET_KEY=django-insecure-^e*6bw222=trhl5ksi+(*kdl^d(-xcji1ndz$%osizds$6x3tb
DEBUG=True
#OPENAI_API_KEY=
ALLOWED_HOSTS=127.0.0.1,localhost

# For SQLite
DATABASE_ENGINE=django.db.backends.sqlite3
DATABASE_NAME=db.sqlite3  # No need to use BASE_DIR here, handle it in settings.py

# Uncomment these for PostgreSQL or other databases

# DATABASE_ENGINE=django.db.backends.postgresql
# DATABASE_NAME=your-db-name
# DATABASE_USER=your-db-user
# DATABASE_PASSWORD=your-db-password
# DATABASE_HOST=localhost
# DATABASE_PORT=5432
