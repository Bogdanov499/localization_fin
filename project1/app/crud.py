from sqlalchemy.orm import Session

import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_wallets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Wallet).offset(skip).limit(limit).all()


def create_user_wallet(db: Session, wallet: schemas.WalletCreate, user_id: int):
    db_wallet = models.Wallet(**wallet.dict(), owner_id=user_id)
    db.add(db_wallet)
    db.commit()
    db.refresh(db_wallet)
    return db_wallet