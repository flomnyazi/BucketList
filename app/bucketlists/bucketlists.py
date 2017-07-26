import uuid
class BucketList(object):
    def __init__(self, name,user_id,bucketlist_id=None):
        self.name = name
        self.user_id = user_id
        self.bucketlist_id = uuid.uuid4().hex if bucketlist_id is None else bucketlist_id
        activities = {}
        