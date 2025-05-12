# URL Shortener with QR Code Generator

A FastAPI-based URL shortening service that creates both short links and QR codes for easy URL sharing.

## Features

- URL shortening with unique identifiers
- QR code generation for each shortened URL
- Click tracking and statistics
- User authentication and authorization
- Secure storage of URLs and QR codes
- FastAPI-powered REST API

## Prerequisites

- Python 3.7+
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd <repository-name>
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the server:
```bash
uvicorn app.main:app --reload
```

2. Access the API documentation:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

- `POST /short_link` - Create a short URL and QR code
- `GET /{short_id}` - Redirect to original URL
- `GET /stats/{short_id}` - Get URL statistics
- `GET /qr/{short_id}` - Get QR code image
- `POST /register` - Register new user
- `POST /token` - Get authentication token

## Authentication

The API uses JWT tokens for authentication. To use protected endpoints:

1. Register a new user using `/register`
2. Get a token using `/token`
3. Include the token in the Authorization header: `Bearer <token>`

## Project Structure

```
.
├── app/
│   ├── core/
│   │   └── security.py
│   │   
│   ├── db/
│   │   ├── database.py
│   │   └── session.py
│   │   
│   ├── models/
│   │   └── models.py
│   │   
│   ├── routes/
│   │   ├── auth.py
│   │   └── url.py
│   │   
│   ├── schemas/
│   │   └── schemas.py
│   │   
│   └── main.py
│   
├── qrcodes/
│   
├── requirements.txt
│   
└── README.md
```

## Security Considerations

- Passwords are hashed using bcrypt
- JWT tokens are used for API authentication
- Database is protected against SQL injection
- QR codes are stored securely with unique identifiers

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 