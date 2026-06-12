# Instance Folder - SQLite Databases

This folder contains SQLite database files used by various Flask applications in this workspace. These are runtime databases created by Flask-SQLAlchemy when applications run.

## Overview

The `instance/` folder is a special directory in Flask applications used to store SQLite database files that should not be committed to version control. It contains data generated during application runtime.

## Database Files

| Database | Created By | Purpose |
|----------|------------|---------|
| `cafes.db` | Part - Project 88 Cafe And Wifi Website | Stores cafe listings with amenities |
| `posts.db` | Part - Project 67 Blog API | Stores blog posts |
| `users.db` | Part - Project 68 Flask Authenticator | Stores user accounts |

---

## Database: cafes.db

**Source Project**: [Part - Project 88 Cafe And Wifi Website](../Part%20-%20Project%2088%20Cafe%20And%20Wifi%20Website/README.md)

### Schema

```sql
CREATE TABLE cafe (
    id INTEGER PRIMARY KEY,
    name VARCHAR(250) UNIQUE NOT NULL,
    map_url VARCHAR(500) NOT NULL,
    img_url VARCHAR(500) NOT NULL,
    location VARCHAR(250) NOT NULL,
    seats VARCHAR(250) NOT NULL,
    has_toilet BOOLEAN NOT NULL,
    has_wifi BOOLEAN NOT NULL,
    has_sockets BOOLEAN NOT NULL,
    can_take_calls BOOLEAN NOT NULL,
    coffee_price VARCHAR(250)
);
```

### Fields

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key |
| name | VARCHAR(250) | Cafe name (unique) |
| map_url | VARCHAR(500) | Google Maps URL |
| img_url | VARCHAR(500) | Image URL |
| location | VARCHAR(250) | City/location |
| seats | VARCHAR(250) | Seating capacity |
| has_toilet | BOOLEAN | Has bathroom facilities |
| has_wifi | BOOLEAN | Has WiFi |
| has_sockets | BOOLEAN | Has power outlets |
| can_take_calls | BOOLEAN | Good for phone calls |
| coffee_price | VARCHAR(250) | Price of coffee |

---

## Database: posts.db

**Source Project**: [Part - Project 67 Blog API](../Part%20-%20Project%2067%20blog%20api/README.md)

### Schema

```sql
CREATE TABLE blog_post (
    id INTEGER PRIMARY KEY,
    title VARCHAR(250) UNIQUE NOT NULL,
    subtitle VARCHAR(250) NOT NULL,
    date VARCHAR(250) NOT NULL,
    body TEXT NOT NULL,
    author VARCHAR(250) NOT NULL,
    img_url VARCHAR(250) NOT NULL
);
```

### Fields

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key |
| title | VARCHAR(250) | Blog post title (unique) |
| subtitle | VARCHAR(250) | Post subtitle |
| date | VARCHAR(250) | Publication date |
| body | TEXT | Full blog content (HTML) |
| author | VARCHAR(250) | Author name |
| img_url | VARCHAR(250) | Featured image URL |

---

## Database: users.db

**Source Project**: [Part - Project 68 Flask Authenticator](../Part%20-%20Project%2068%20flask%20authenticator/README.md)

### Schema

```sql
CREATE TABLE user (
    id INTEGER PRIMARY KEY,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    name VARCHAR(1000) NOT NULL
);
```

### Fields

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key |
| email | VARCHAR(100) | User email (unique) |
| password | VARCHAR(100) | Hashed password (PBKDF2-SHA256) |
| name | VARCHAR(1000) | User's display name |

### Security Note

Passwords are hashed using PBKDF2-SHA256 with salt. Never store plain-text passwords.

---

## Viewing Database Contents

### Using SQLite3 Command Line

```bash
# Open database
sqlite3 instance/cafes.db

# List tables
.tables

# View table schema
.schema cafe

# Query data
SELECT * FROM cafe;

# Exit
.exit
```

### Using Python

```python
import sqlite3

conn = sqlite3.connect('instance/cafes.db')
cursor = conn.cursor()

# List all cafes
cursor.execute("SELECT * FROM cafe")
for row in cursor.fetchall():
    print(row)

conn.close()
```

### Using DB Browser for SQLite

1. Download "DB Browser for SQLite" from https://sqlitebrowser.org/
2. Open any .db file
3. Browse data, run queries, export to CSV

---

## Managing These Databases

### Backup

```bash
# Copy database file
copy instance\cafes.db backups\cafes_backup.db
```

### Reset/Delete

If you want to start fresh:

1. Stop the Flask application
2. Delete the .db file
3. Run the application again (it will recreate the database)

```bash
# Windows
del instance\cafes.db

# Mac/Linux
rm instance/cafes.db
```

### Data Export

```python
import csv
import sqlite3

conn = sqlite3.connect('instance/cafes.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM cafe")
rows = cursor.fetchall()

with open('cafes_export.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow([description[0] for description in cursor.description])
    writer.writerows(rows)

conn.close()
```

---

## .gitignore Entry

These database files should typically be in your `.gitignore` since they contain runtime data:

```gitignore
instance/
*.db
```

---

## Troubleshooting

### "Database locked" error

- Another process is using the database
- Close any applications accessing the database
- For SQLite, enable WAL mode for better concurrency

### Corrupted database

- Delete and recreate by running the application
- Restore from backup if available

### Permission denied

- Check file permissions
- Run terminal as administrator if needed

---

## Relationship Between Projects

```
Part - Project 67 Blog API → posts.db
    └─ Stores blog post data

Part - Project 68 Flask Authenticator → users.db
    └─ Stores user authentication data

Part - Project 88 Cafe & WiFi Website → cafes.db
    └─ Stores cafe directory data
```

---

## Notes

- These databases are created automatically when their respective Flask applications run
- Data persists between application runs
- Each database is independent and belongs to its source project
- No README is needed for individual source projects (see their own README.md files)

## License

(This folder contains data files for educational projects. I don't own anything and it's only for practicing.)