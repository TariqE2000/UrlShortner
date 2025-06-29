import uuid
from datetime import datetime
class urlModel:
    def __init__(self, created_at: datetime, updated_at: datetime, id: uuid.UUID=None, long_url: str=None, short_url=None):
        self.id = id or uuid.uuid4()
        self.long_url = long_url
        self.short_url = short_url
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()
        