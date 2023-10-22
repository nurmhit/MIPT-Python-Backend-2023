from models.comment import Comment


def get_ordered_comments_by_likes(comments: list[Comment]) -> list[Comment]:
    comments.sort(key=lambda comment: comment.like_count)
    comments.reverse()
    return comments
