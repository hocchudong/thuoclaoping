from sqlalchemy import Column, DateTime, ForeignKey, Index, Integer, SmallInteger, String, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session


Base = declarative_base()
metadata = Base.metadata


class AuthGroup(Base):
    __tablename__ = 'auth_group'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False, unique=True)


class AuthGroupPermission(Base):
    __tablename__ = 'auth_group_permissions'
    __table_args__ = (
        Index('auth_group_permissions_group_id_permission_id_0cd325b0_uniq', 'group_id', 'permission_id', unique=True),
    )

    id = Column(Integer, primary_key=True)
    group_id = Column(ForeignKey('auth_group.id'), nullable=False)
    permission_id = Column(ForeignKey('auth_permission.id'), nullable=False, index=True)

    group = relationship('AuthGroup')
    permission = relationship('AuthPermission')


class AuthPermission(Base):
    __tablename__ = 'auth_permission'
    __table_args__ = (
        Index('auth_permission_content_type_id_codename_01ab375a_uniq', 'content_type_id', 'codename', unique=True),
    )

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    content_type_id = Column(ForeignKey('django_content_type.id'), nullable=False)
    codename = Column(String(100), nullable=False)

    content_type = relationship('DjangoContentType')


class AuthUser(Base):
    __tablename__ = 'auth_user'

    id = Column(Integer, primary_key=True)
    password = Column(String(128), nullable=False)
    last_login = Column(DateTime)
    is_superuser = Column(Integer, nullable=False)
    username = Column(String(150), nullable=False, unique=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(150), nullable=False)
    email = Column(String(254), nullable=False)
    is_staff = Column(Integer, nullable=False)
    is_active = Column(Integer, nullable=False)
    date_joined = Column(DateTime, nullable=False)


class AuthUserGroup(Base):
    __tablename__ = 'auth_user_groups'
    __table_args__ = (
        Index('auth_user_groups_user_id_group_id_94350c0c_uniq', 'user_id', 'group_id', unique=True),
    )

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('auth_user.id'), nullable=False)
    group_id = Column(ForeignKey('auth_group.id'), nullable=False, index=True)

    group = relationship('AuthGroup')
    user = relationship('AuthUser')


class AuthUserUserPermission(Base):
    __tablename__ = 'auth_user_user_permissions'
    __table_args__ = (
        Index('auth_user_user_permissions_user_id_permission_id_14a6b632_uniq', 'user_id', 'permission_id', unique=True),
    )

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('auth_user.id'), nullable=False)
    permission_id = Column(ForeignKey('auth_permission.id'), nullable=False, index=True)

    permission = relationship('AuthPermission')
    user = relationship('AuthUser')


class CheckHost(Base):
    __tablename__ = 'check_host'

    id = Column(Integer, primary_key=True)
    hostname = Column(String(45), nullable=False)
    ip_address = Column(String(39), nullable=False)
    user_id = Column(ForeignKey('auth_user.id'), nullable=False, index=True)

    user = relationship('AuthUser')


class CheckService(Base):
    __tablename__ = 'check_service'

    id = Column(Integer, primary_key=True)
    service_name = Column(String(45), nullable=False)
    ok = Column(Integer)
    warning = Column(Integer)
    critical = Column(Integer)
    interval_check = Column(Integer)


class CheckAlert(CheckService):
    __tablename__ = 'check_alert'

    service_id = Column(ForeignKey('check_service.id'), primary_key=True)
    email_alert = Column(String(100), nullable=False)
    telegram_id = Column(String(10), nullable=False)
    webhook = Column(String(200), nullable=False)


class CheckServiceHost(Base):
    __tablename__ = 'check_service_host'
    __table_args__ = (
        Index('check_service_host_service_id_host_id_56d890ff_uniq', 'service_id', 'host_id', unique=True),
    )

    id = Column(Integer, primary_key=True)
    service_id = Column(ForeignKey('check_service.id'), nullable=False)
    host_id = Column(ForeignKey('check_host.id'), nullable=False, index=True)

    host = relationship('CheckHost')
    service = relationship('CheckService')


class DjangoAdminLog(Base):
    __tablename__ = 'django_admin_log'

    id = Column(Integer, primary_key=True)
    action_time = Column(DateTime, nullable=False)
    object_id = Column(String)
    object_repr = Column(String(200), nullable=False)
    action_flag = Column(SmallInteger, nullable=False)
    change_message = Column(String, nullable=False)
    content_type_id = Column(ForeignKey('django_content_type.id'), index=True)
    user_id = Column(ForeignKey('auth_user.id'), nullable=False, index=True)

    content_type = relationship('DjangoContentType')
    user = relationship('AuthUser')


class DjangoContentType(Base):
    __tablename__ = 'django_content_type'
    __table_args__ = (
        Index('django_content_type_app_label_model_76bd3d3b_uniq', 'app_label', 'model', unique=True),
    )

    id = Column(Integer, primary_key=True)
    app_label = Column(String(100), nullable=False)
    model = Column(String(100), nullable=False)


class DjangoMigration(Base):
    __tablename__ = 'django_migrations'

    id = Column(Integer, primary_key=True)
    app = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    applied = Column(DateTime, nullable=False)


class DjangoSession(Base):
    __tablename__ = 'django_session'

    session_key = Column(String(40), primary_key=True)
    session_data = Column(String, nullable=False)
    expire_date = Column(DateTime, nullable=False, index=True)


class GetDataFping():
    def get_data_from_mysql(self):
        dict_users = {}
        users = s.query(AuthUser).all()
        for user in users:
            hosts_id = []
            ips = []
            hosts = s.query(CheckHost).filter(CheckHost.user_id == user.id).all()
            for host in hosts:
                hosts_id.append(host.id)
            services = s.query(CheckServiceHost).filter(CheckServiceHost.host_id.in_(hosts_id)).all()
            for service in services:
                if service.service.service_name == "PING":
                    ips.append(service.host.ip_address)
            dict_users[user.username] = ips
        return dict_users


e = create_engine("mysql+pymysql://thuoclao:thuoclao@192.168.30.61/thuoclao", echo=True)
s = Session(e)
SQL = GetDataFping()
data = SQL.get_data_from_mysql()
print(data)
