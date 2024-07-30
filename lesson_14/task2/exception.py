class GroupFullError(Exception):
    def __init__(self, message="Cannot add more than 10 students to the group."):
        self.message = message
        super().__init__(self.message)