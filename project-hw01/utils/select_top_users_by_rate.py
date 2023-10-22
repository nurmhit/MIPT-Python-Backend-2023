from models.user import User


def select_top_users_by_rate(users: list[User], top_size: int) -> list[User]:
    users.sort(key=lambda user: user.rate)
    users.reverse()
    return users[: top_size]
