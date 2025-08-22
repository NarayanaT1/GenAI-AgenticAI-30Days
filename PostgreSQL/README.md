# PostgreSQL Essentials for Developers

**Branding:** © 2025 T S Narayana Reddy • CloudByteHub.ai  
**License:** MIT  
**Disclaimer:** Independent personal project. Not affiliated with any employer.  

## Overview
This showcase covers **PostgreSQL basics** for developers: setup, SQL examples, and tips.

### Topics
- Why PostgreSQL?
- Key Features (indexes, JSONB, extensions)
- Installation across Windows, macOS, Linux
- Basic SQL commands (create DB, tables, CRUD)
- Developer Tips (EXPLAIN, indexing, GUI tools)

### Example SQL
```sql
CREATE DATABASE mydb;
\c mydb

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(150) UNIQUE
);

INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');
SELECT * FROM users;
```

### Attribution
- License: MIT
- Branding: CloudByteHub.ai
- © 2025 T S Narayana Reddy
- Independent personal project. Not affiliated with any employer.
