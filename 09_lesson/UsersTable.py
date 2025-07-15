from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Subject(Base):
    __tablename__ = 'subject'

    subject_id = Column(Integer, primary_key=True, autoincrement=True)
    subject_title = Column(String)


def test_add_subject_with_orm(db_session):
    new_subject = Subject(subject_title="Мой предмет")
    db_session.add(new_subject)
    db_session.commit()

    # Проверка
    assert new_subject.subject_id is not None

    # Получение из базы
    retrieved = db_session.query(Subject).filter_by(
        subject_id=new_subject.subject_id).first()
    assert retrieved is not None and retrieved.subject_title == "Мой предмет"

    # Удаление после теста
    db_session.delete(retrieved)
    db_session.commit()
