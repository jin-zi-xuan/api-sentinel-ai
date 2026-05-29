from app.core.logging import get_logger, setup_logging
from app.db.session import Base, engine

logger = get_logger(__name__)


def init_db() -> None:
    Base.metadata.create_all(bind=engine)
    logger.info("Database tables initialized.")


if __name__ == "__main__":
    setup_logging()
    init_db()
