import pytest
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, select, insert, update, delete
from sqlalchemy.orm import sessionmaker
import sqlalchemy.exc as exc

# Строка подключения к базе данных

DATABASE_URL = "postgresql://postgres:238416@localhost:5432/QA"

# Создаем основу и метаданные
engine = create_engine(DATABASE_URL)
metadata = MetaData()

# Объявляем таблицы
users = Table('users', metadata, autoload_with=engine)
subjects = Table('subject', metadata, autoload_with=engine)
students = Table('student', metadata, autoload_with=engine)
group_students = Table('group_student', metadata, autoload_with=engine)
teachers = Table('teacher', metadata, autoload_with=engine)

# Создаем сессию
Session = sessionmaker(bind=engine)


@pytest.fixture(scope='function')
def db_session():
    session = Session()
    yield session
    session.close()


@pytest.mark.positive_test_db
def test_add_subject(db_session):
    new_subject_title = "Тестовый предмет"
    ins = insert(subjects).values(
        subject_title=new_subject_title).returning(subjects.c.subject_id)
    result = db_session.execute(ins)
    db_session.commit()

    subject_id = result.scalar_one()

    # Проверка: предмет существует в базе
    sel = select(subjects).where(subjects.c.subject_id == subject_id)
    row = db_session.execute(sel).first()
    assert row is not None and row.subject_title == new_subject_title

    # Удаляем созданный предмет
    del_stmt = delete(subjects).where(subjects.c.subject_id == subject_id)
    db_session.execute(del_stmt)
    db_session.commit()


@pytest.mark.positive_test_db
def test_update_student_level(db_session):

    temp_user_id = 999999  # уникальный ID для теста

    # Создаем студента
    ins_student = insert(students).values(
        user_id=temp_user_id,
        level='Начальный',
        education_form='Очная',
        subject_id=1
        )

    db_session.execute(ins_student)
    db_session.commit()

    # Обновляем уровень студента
    new_level = 'Продвинутый'
    upd = update(students).where(
        students.c.user_id == temp_user_id).values(level=new_level)
    db_session.execute(upd)
    db_session.commit()

    # Проверка обновления
    sel = select(students).where(students.c.user_id == temp_user_id)
    row = db_session.execute(sel).first()
    assert row is not None and row.level == new_level

    # Удаляем временного студента после теста
    del_stmt = delete(students).where(students.c.user_id == temp_user_id)
    db_session.execute(del_stmt)
    db_session.commit()


@pytest.mark.positive_test_db
def test_delete_group_student(db_session):
    # Создаем временную связь студент-группа для теста
    temp_user_id = 888888  # уникальный ID для теста
    temp_group_id = 12345   # произвольный ID группы

    # Вставляем связь
    ins_link = insert(group_students).values(
        user_id=temp_user_id, group_id=temp_group_id)

    db_session.execute(ins_link)
    db_session.commit()

    # Теперь удаляем связь как часть теста
    del_stmt = delete(group_students).where(
        (group_students.c.user_id == temp_user_id) &
        (group_students.c.group_id == temp_group_id))

    db_session.execute(del_stmt)

    # Проверка удаления: связь больше не существует
    sel_after_del = select(group_students).where(
        (group_students.c.user_id == temp_user_id) &
        (group_students.c.group_id == temp_group_id))

    result_after_del = db_session.execute(sel_after_del).first()

    assert result_after_del is None


@pytest.mark.negative_test_db
def test_update_nonexistent_student(db_session):
    # обновление несуществующего студента
    non_existent_user_id = 9999999  # ID, которого нет в базе

    # Попытка обновить несуществующего пользователя
    upd = update(students).where(
        students.c.user_id == non_existent_user_id).values(level='Эксперт')
    result = db_session.execute(upd)
    db_session.commit()

    # Проверяем, что ни одна строка не была обновлена
    assert result.rowcount == 0


@pytest.mark.negative_test_db
def test_delete_nonexistent_group_student(db_session):
    # Негативный тест: попытка удалить несуществующую связь студент-группа
    non_existent_user_id = 777777
    non_existent_group_id = 88888

    del_stmt = delete(group_students).where(
        (group_students.c.user_id == non_existent_user_id) &
        (group_students.c.group_id == non_existent_group_id))
    result = db_session.execute(del_stmt)
    db_session.commit()

    # Проверяем, что удалено ничего не было
    assert result.rowcount == 0


@pytest.mark.negative_test_db
def test_insert_subject_with_null_title():
    # Попытка вставить  None в обязательное поле subject_title
    with pytest.raises(exc.IntegrityError):
        # Выполняем вставку с None для subject_title
        stmt = insert(subjects).values(subject_title=None)
        with engine.connect() as conn:
            conn.execute(stmt)
            conn.commit()
