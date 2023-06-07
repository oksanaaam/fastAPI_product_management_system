
## Technologies
- Python
- FastAPI
- SQLAlchemy
- Pydantic

### Installation

1. Clone the repo
`git clone https://github.com/oksanaaam/fastAPI_product_management_system.git`
2. Open the project folder in your IDE
3. Open a terminal in the project folder
4. If you are using PyCharm - it may propose you to automatically create venv for your project and install requirements in it, but if not:
```
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
```

5. Set up the database:

- Create a PostgreSQL database.
- Update the database connection details in the `db.engine` module.
6. Run the application:
`uvicorn main:app --reload`

The API will be available at http://localhost:8000.

## API Usage
API documentation will be available at http://localhost:8000/docs
![img.png](img%20for%20README%2Fimg.png)

### Get All Products
![img_1.png](img%20for%20README%2Fimg_1.png)

- Endpoint: GET /products/
- Parameters:
- receives a product's name, description and price in JSON format

### Get a Product
![img_4.png](img%20for%20README%2Fimg_4.png)

- Endpoint: GET /products/{product_id}/
- Parameters:
- product_id (path parameter): ID of the product to retrieve

### Create a Product
![img_2.png](img%20for%20README%2Fimg_2.png)

- Endpoint: POST /products/
- Request Body: JSON object with the following fields:
- name (string): Name of the product
- description (string): Description of the product
- price (float): Price of the product

### Update a Product
![img_5.png](img%20for%20README%2Fimg_5.png)

- Endpoint: PUT /products/{product_id}/
- Parameters:
- product_id (path parameter): ID of the product to update
- Request Body: JSON object with the following fields (any or all can be provided):
- name (string): Updated name of the product
- description (string): Updated description of the product
- price (float): Updated price of the product

### Delete a Product
![img_6.png](img%20for%20README%2Fimg_6.png)

- Endpoint: DELETE /products/{product_id}/
- Parameters:
- product_id (path parameter): ID of the product to delete
