from pydantic import BaseModel

class UserInfo(BaseModel):
    id: int
    username: str
    name: str
    role: str
    profile_visibility: str
    phone: str

    # 정적 팩토리 메서드
    @staticmethod
    def from_(user):
        return UserInfo(
            id=user.id,
            username=user.username,
            name=user.name,
            role=user.role,
            profile_visibility=user.profile_visibility,
            phone=user.phone
        )