# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

### Development
- Run application: `python app.py`
- Install dependencies: `pip install -r requirements.txt`

## Architecture

The project is a multi-vendor e-commerce platform built with Python and Flask, following a layered architecture:

- **Entry Point**: `app.py` handles configuration and application initialization.
- **Data Layer**: `models.py` contains SQLAlchemy models defining the database schema (MySQL).
- **Route Layer**: Located in `routes/`, using Flask Blueprints to separate concerns:
    - `admin_routes.py`: Platform management.
    - `customer_routes.py`: Shopping and checkout.
    - `seller_routes.py`: Vendor inventory and order management.
- **Service Layer**: Located in `services/`, containing the core business logic to keep routes thin:
    - `auth_services.py`: User registration and authentication.
    - `product_services.py`: Catalog and search logic.
    - `cart_services.py`: Shopping cart management.
    - `order_services.py`: Order processing.
    - `services/admin/` and `services/seller/`: Specialized logic for administrative and vendor roles.
- **Frontend**: Jinja2 templates in `templates/` (split by role) and static assets in `static/`.
- **Authentication**: Custom logic in `auth/` (including `login_req.py` for access control).

## Project Structure
- `app.py`: Application entry point.
- `models.py`: SQLAlchemy models.
- `routes/`: HTTP Route handlers.
- `services/`: Business logic layer.
- `static/`: CSS, Images, and JS assets.
- `templates/`: HTML views.
