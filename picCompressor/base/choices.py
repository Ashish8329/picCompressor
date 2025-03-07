from enum import Enum

class ChoieEnum(Enum):
    @classmethod
    def get_value(cls, member):
        return cls[member].value[0]
    

class Status(ChoieEnum):
    PENDING = ("pending", "Pending")
    COMPLETED = ("completed", "Completed")
    REJECTED = ("rejected", "Rejected")