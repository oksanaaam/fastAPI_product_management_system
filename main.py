from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
from db.engine import SessionLocal

import schemas

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/products/", response_model=list[schemas.Product])
def get_all_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    products = crud.get_all_products(db=db)
    return products[skip: skip + limit]


@app.get("/products/{product_id}/", response_model=schemas.Product)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product_by_id(db=db, product_id=product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@app.post("/products/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    products = crud.get_product_by_name(db=db, name=product.name)
    if products:
        raise HTTPException(
            status_code=400,
            detail="Such name for product already exist"
        )

    return crud.create_product(db=db, product=product)


@app.put("/products/{product_id}/", response_model=schemas.Product)
def update_product(
        product_id: int,
        product: schemas.ProductUpdate,
        db: Session = Depends(get_db)
):
    updated_product = crud.update_product(db=db, product_id=product_id, product=product)
    if updated_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product


@app.delete("/products/{product_id}/", response_model=schemas.Product)
def delete_product(
        product_id: int,
        db: Session = Depends(get_db)
):
    deleted_product = crud.delete_product(db=db, product_id=product_id)
    return deleted_product
