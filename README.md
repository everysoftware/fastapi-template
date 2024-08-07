# FastAPI Template

A production-ready template for FastAPI projects ⚡

## Features

Main features of this template:

- **FastAPI**: Modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on
  standard Python type hints.
- **SQLAlchemy**: The Python SQL toolkit and Object Relational Mapper that gives application developers
  the full power and flexibility of SQL.
- **Alembic**: Lightweight database migration tool for usage with the SQLAlchemy Database Toolkit for
  Python.
- **Docker**: Set of platform as a service products that use OS-level virtualization to deliver software in
  packages called containers.
- **Uvicorn & Gunicorn**: Lightning-fast ASGI server implementation, using uvloop and httptools. Serving
  your FastAPI app with Uvicorn and Gunicorn.
- **JWT authentication**: JSON Web Tokens are an open, industry-standard RFC 7519 method for representing
  claims securely between two parties.

Best development experience with:

- **Poetry**: Tool for dependency management and packaging in Python.
- **Pre-commit**: A framework for managing and maintaining multi-language pre-commit hooks.
- **Ruff**: An extremely fast Python linter and code formatter, written in Rust.
- **Mypy**: An optional static type checker for Python that aims to combine the benefits of dynamic (or "duck") typing
  and static typing.
- **Makefile**: A Makefile is a simple way to organize commands, and it can be used to group and organize commands to
  run.
- **Pytest**: A framework that makes it easy to write simple and scalable tests.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/everysoftware/fastapi-template
```

2. Generate RSA keys:

```bash
openssl genrsa -out certs/private.pem 2048
openssl rsa -in certs/private.pem -pubout -out certs/public.pem
```

3. Create a `.env` file. Use the `.env.example` as a reference.
4. Run the application:

```bash
make up
```

**Made with love ❤️**
