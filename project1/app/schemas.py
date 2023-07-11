from typing import List, Union

from pydantic import BaseModel


class WalletBase(BaseModel):
    value: int


class WalletCreate(WalletBase):
    pass


class Wallet(WalletBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    wallets: List[Wallet] = []

    class Config:
        orm_mode = True