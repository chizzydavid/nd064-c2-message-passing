from __future__ import annotations
from app import db  
from sqlalchemy import BigInteger, Column, Date, DateTime, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import JSONB, UUID


class Person(db.Model):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    company_name = Column(String, nullable=False)


