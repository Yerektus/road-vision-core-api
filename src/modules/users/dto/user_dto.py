from dataclasses import dataclass


@dataclass
class CreateUserDto:
    username: str
    email: str
    password: str