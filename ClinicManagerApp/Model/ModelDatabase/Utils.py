import enum


class UserRole(enum.Enum):
    ADMIN = 0
    DOCTOR = 1
    NURSE = 2


class PersonSex(enum.Enum):
    MALE = 0
    FEMALE = 1


class MedicineUnit(enum.Enum):
    BOTTLE = 0
