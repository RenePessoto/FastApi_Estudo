from sqlalchemy import select

from fast_zero.models import User


def test_create_user_on_db(session):
    user = User(
        username='user_teste',
        email='teste@teste.com.br',
        password='1234567',
    )
    session.add(user)
    session.commit()

    result = session.scalar(
        select(User).where(User.email == 'teste@teste.com.br')
    )

    assert result.username == 'user_teste'
