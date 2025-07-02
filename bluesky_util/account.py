
"""
Account models and database integration for BlueSky Utility.

This module defines ORM and Pydantic models for BlueSky accounts, and provides
async methods for saving/loading account data to/from PostgreSQL.
"""

from pydantic import BaseModel, Field
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, Integer, Text, JSON, select
import importlib.util
import os

Base = declarative_base()


class BlueSkyAccountORM(Base):
    """
    SQLAlchemy ORM model for the 'accounts' table.
    Represents a BlueSky account record in the database.
    """
    __tablename__ = "accounts"
    handle = Column(String, primary_key=True)
    display_name = Column(String)
    description = Column(Text)
    joined_date = Column(String)
    follower_count = Column(Integer)
    following_count = Column(Integer)
    avatar = Column(String)
    did = Column(String)
    posts = Column(JSON)


class BlueSkyAccount(BaseModel):
    """
    Pydantic model for BlueSky account data.

    Provides async methods to save/load account data to/from PostgreSQL.
    """
    handle: str
    display_name: Optional[str] = ""
    description: Optional[str] = ""
    joined_date: Optional[str] = ""
    follower_count: int = 0
    following_count: int = 0
    avatar: Optional[str] = ""
    did: Optional[str] = ""
    posts: List[dict] = Field(default_factory=list)

    async def save_to_postgresql(self, db_url: str = None):
        """
        Save this BlueSkyAccount instance to PostgreSQL.

        Args:
            db_url: Optional database URL. If not provided, uses DB_URL from secrets.
        """
        db_url = db_url or DB_URL
        engine = create_async_engine(db_url, echo=False)
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
        async with async_session() as session:
            async with session.begin():
                account = BlueSkyAccountORM(
                    handle=self.handle,
                    display_name=self.display_name,
                    description=self.description,
                    joined_date=self.joined_date,
                    follower_count=self.follower_count,
                    following_count=self.following_count,
                    avatar=self.avatar,
                    did=self.did,
                    posts=self.posts
                )
                await session.merge(account)
            await session.commit()
        await engine.dispose()

    @classmethod
    async def load_from_postgresql(cls, handle: str, db_url: str = None):
        """
        Load a BlueSkyAccount from PostgreSQL by handle.

        Args:
            handle: The BlueSky account handle to load.
            db_url: Optional database URL. If not provided, uses DB_URL from secrets.

        Returns:
            BlueSkyAccount instance if found, else None.
        """
        db_url = db_url or DB_URL
        engine = create_async_engine(db_url, echo=False)
        async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
        async with async_session() as session:
            result = await session.execute(select(BlueSkyAccountORM).where(BlueSkyAccountORM.handle == handle))
            account_orm = result.scalar_one_or_none()
        await engine.dispose()
        if account_orm:
            return cls(
                handle=account_orm.handle,
                display_name=account_orm.display_name,
                description=account_orm.description,
                joined_date=account_orm.joined_date,
                follower_count=account_orm.follower_count,
                following_count=account_orm.following_count,
                avatar=account_orm.avatar,
                did=account_orm.did,
                posts=account_orm.posts or []
            )
        return None

# Load secrets from secrets.py if it exists
secrets_path = os.path.join(os.path.dirname(__file__), 'secrets.py')
if os.path.exists(secrets_path):
    spec = importlib.util.spec_from_file_location('secrets', secrets_path)
    secrets = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(secrets)
else:
    raise RuntimeError('secrets.py not found. Please copy secrets_example.py to secrets.py and fill in your credentials.')

DB_URL = f"postgresql+asyncpg://{secrets.POSTGRES_USER}:{secrets.POSTGRES_PASSWORD}@{secrets.POSTGRES_HOST}:{secrets.POSTGRES_PORT}/{secrets.POSTGRES_DB}"
