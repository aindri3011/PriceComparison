# Django Price Comparison

This is a Django project that provides a Price Comparison APIs and web application. The project includes Docker configuration for easy setup and deployment. Below, you will find step-by-step instructions on how to install and run this project locally.

## Features
- Creating Shop
- Creating Products
- Getting All products from Database
- Search products with price 
- Compare prices of each product from different stores.

## Requirements

- Python 3.8
- Docker Desktop

## Installation

### Clone the Repository

```bash
git clone https://github.com/aindri3011/PriceComparison.git
```

# Setup Environment Variables
- Create a .env file in the root of the project directory with the following content:

# MongoDB settings
MONGO_USERNAME= your_mongodb_username
MONGO_PASSWORD= your_mongodb_password
MONGO_CLUSTER= your_mongodb_cluster
MONGO_KEY = your_database_key

# Django secret key
SECRET_KEY= your_django_secret_key

# Build and Run the Docker Containers
Ensure you have Docker Desktop installed. Then, run the following command:

docker-compose up --build

## If you prefer to run the project without Docker, follow these steps:

### Setup Environment Variables

- Create a `.env` file as mentioned above.
  
- Create a virtual environment:

    ```bash
    python3 -m venv venv
    ```

- Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

- Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```
- Run the Django development server:

    ```bash
    python manage.py runserver
    ```
## Access the Application
Once the containers are up and running, you can access the Django application at:

http://localhost:8000


Configuration
# MongoDB Configuration
The project uses MongoDB as the database. Ensure you have a MongoDB instance running and configure the .env file with your MongoDB credentials.

# Usage
# API Endpoints

-Create Shop: POST /api/create-shop/

-Create Product: POST /api/create-product/

-List of all products from database: GET /api/get-product/?query_str=all

-Search Products By Product Name/ Store Name: GET /api/search-product/?search_string=Store1

# Contributing
Contributions are welcome! Please fork the repository and submit a pull request.


### Additional Notes

1. **Replace Placeholders**: Ensure you replace placeholders like `yourusername`, `yourrepository`, `your_mongodb_username`, `your_mongodb_password`, `your_mongodb_cluster`, `your_database_name`, and `your_django_secret_key` with actual values.

2. **Running Without Docker**: If users prefer to run the project without Docker, follow instructions for setting up a virtual environment, installing dependencies, and running the Django development server.

- By following this `README.md`, users will have a clear and concise guide to setting up and running your Django Networking API project.
