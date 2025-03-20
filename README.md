# Makaduu-Bookstore
A simple Django-based e-commerce website for selling books in Kenya. Features book listings, a shopping cart, M-Pesa payments, and a minimal checkout process tailored for the local market.

## Features
- Book browsing and searching
- User authentication (Customer & Publisher accounts)
- Shopping cart functionality
- M-Pesa payment integration
- Publisher dashboard for book management
- Newsletter subscription
- Responsive design

## Prerequisites
- Python 3.12+
- Django 5.1+
- Virtual environment

## Installation & Setup

1. Clone the repository
```bash
git clone https://github.com/yourusername/Makaduu-Bookstore.git
cd Makaduu-Bookstore
```

2. Create and activate virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up the database
```bash
python manage.py migrate
```

5. Create a superuser
```bash
python manage.py createsuperuser
```

6. Run the development server
```bash
python manage.py runserver
```

## Usage

### For Customers
1. Browse books on the homepage
2. Create an account or login
3. Add books to cart
4. Proceed to checkout
5. Complete payment via M-Pesa

### For Publishers
1. Register as a publisher
2. Wait for account verification
3. Access publisher dashboard
4. Manage book inventory:
   - Add new books
   - Update existing books
   - Track orders

### For Administrators
1. Access admin panel at `/admin`
2. Manage users, books, and orders
3. Verify publisher accounts
4. Monitor transactions

## Project Structure
```
Makaduu-Bookstore/
├── apps/
│   ├── accounts/     # User authentication
│   ├── books/        # Book management
│   ├── cart/         # Shopping cart
│   ├── checkout/     # Payment processing
│   ├── core/         # Core functionality
│   └── orders/       # Order management
├── makaduu/          # Project settings
├── media/           # User-uploaded files
└── static/          # Static files
```

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.
