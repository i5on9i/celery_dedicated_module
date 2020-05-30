
import celery
from pworker.db import engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class SqlAlchemyTask(celery.Task):
    """An Celery Task that ensures that the connection the the
    database is closed on task completion"""
    _session = None

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        if self._session is not None:
            self._session.remove()

    @property
    def session(self):
        if self._session is None:
            # scoped_session: docs.sqlalchemy.org/en/latest/orm/session.html
            self._session = scoped_session(
                sessionmaker(autocommit=False, autoflush=False, bind=engine))

        return self._session

