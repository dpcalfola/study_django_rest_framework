# psycopg2 options


### 1. psycopg2-binary
  * OK for development
  * Not good for production

### 2. psycopg2

* Compiles form source
* Required additional dependencies
  * List of package dependencies in docs
    1. C compiler
    2. python3-dev
    3. libpq-dev
  * Equivalent packages for Alpine
    1. postgresql-client
    2. build-base
    3. postgresql-dev
    4. musl-dev