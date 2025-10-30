# Brokart E-commerce (Django)

A simple e-commerce web app built with Django. It includes product listing/detail pages, a basic cart page, and an account page scaffold. The project uses SQLite for development, stores uploaded images under `media/`, and serves static assets from `static/`.

## Tech stack
- Python 3.11
- Django 5.1.6
- SQLite (dev)
- Pillow (image handling)

## Project structure
```
ecommerce/
  brokart/                   # Django project root
    brokart/                # Project settings/urls
    products/               # Products app (models, views, urls)
    customers/              # Customers app (models, views, urls)
    orders/                 # Orders app (models, views, urls)
    themes/                 # Themes app (models)
    templates/              # HTML templates
    static/                 # Static assets (css, images)
    media/                  # User-uploaded media (created at runtime)
    manage.py
  README.md
```

## Getting started (Windows PowerShell)
1) Create and activate a virtual environment
```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2) Install dependencies
```
pip install django==5.1.6 pillow
```

3) Apply migrations
```
cd ecommerce/brokart
python manage.py migrate
```

4) Create an admin user (optional, for /admin)
```
python manage.py createsuperuser
```

5) Run the development server
```
python manage.py runserver
```

- App: `http://127.0.0.1:8000/`
- Admin: `http://127.0.0.1:8000/admin/`

## Core apps and URLs
- Products (`products`)
  - `/` → home page
  - `/product_list` → paginated product list
  - `/product_details/<pk>` → product detail
- Customers (`customers`)
  - `/customer/account` → account page scaffold
- Orders (`orders`)
  - `/orders/cart/` → cart page scaffold

## Models (high level)
- `products.Product`: title, price, description, images, priority, delete_status, timestamps
- `customers.Customer`: name, address, user (OneToOne), phone, delete_status, timestamps
- `orders.Order`: owner (Customer), order_status, delete_status, timestamps
- `orders.OrderedItem`: product, quantity, owner (Order)

## Static and media
- Static files are in `brokart/static/`. Templates reference CSS at `static/css/style.css` and images under `static/images/`.
- Uploaded images for `products.Product.images` are stored under `media/`.

Note: In development, media is served via `urls.py` with `static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)`. Ensure your settings define `MEDIA_URL` and `MEDIA_ROOT` appropriately.

## Database
- Default DB is SQLite: `brokart/db.sqlite3`.
- To reset the DB locally:
```
python manage.py flush
```

## Running tests
```
python manage.py test
```

## Next steps / suggestions
- Add authentication flows (sign up/login) and connect `Customer` creation.
- Implement cart operations and order placement.
- Add validations and admin configurations.
- Configure production-ready static/media handling and security settings. 
