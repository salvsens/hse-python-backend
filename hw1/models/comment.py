import uuid
from datetime import datetime


class Comment:
    def __init__(self, author_id: uuid.UUID, text: str) -> None:
        self.author_id = author_id
        self.text = text
        self.create_data = datetime.now()
        self.update_data = self.create_data
        self.like_count = 0

    def edit_comment(self, new_text: str) -> None:
        self.text = new_text
        self.update_data = datetime.now()

    def like(self) -> None:
        self.like_count += 1

    def dislike(self) -> None:
        self.like_count -= 1

    def __repr__(self) -> str:
        return (
            f'Comment(author_id={self.author_id}, text={self.text!r}, '
            f'like_count={self.like_count}, '
            f'create_data={self.create_data:%Y-%m-%d %H:%M:%S}, '
            f'update_data={self.update_data:%Y-%m-%d %H:%M:%S})'
        )
