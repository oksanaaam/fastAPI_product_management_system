from fastapi import HTTPException
from sqlalchemy.orm import Session
from db import models

import schemas


def get_product_by_id(db: Session, product_id: int) -> models.Product:
    return db.query(models.Product).filter(models.Product.id == product_id).first()


def get_product_by_name(db: Session, name: str) -> models.Product:
    return db.query(models.Product).filter(models.Product.name == name).first()


def get_all_products(db: Session) -> list[models.Product]:
    return db.query(models.Product).all()


def create_product(
        db: Session,
        product: schemas.ProductCreate
) -> models.Product:
    db_product = models.Product(
        name=product.name,
        description=product.description,
        price=product.price
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(
        db: Session,
        product_id: int,
        product: schemas.ProductUpdate
) -> models.Product:
    db_product = get_product_by_id(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    if product.name:
        db_product.name = product.name
    if product.description:
        db_product.description = product.description
    if product.price:
        db_product.price = product.price

    db.commit()
    db.refresh(db_product)

    return db_product


def delete_product(db: Session, product_id: int) -> schemas.Product:
    db_product = get_product_by_id(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(db_product)
    db.commit()

    return db_product
