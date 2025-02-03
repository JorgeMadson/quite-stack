from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class MessageStatus(Base):
    __tablename__ = 'message_status'

    id = Column(Integer, primary_key=True, autoincrement=True)
    bulk_id = Column(String, nullable=False)
    message_id = Column(String, nullable=False)
    status_group = Column(String, nullable=False)
    status_name = Column(String, nullable=False)
    status_description = Column(String, nullable=False)
    error_id = Column(Integer)
    error_name = Column(String)
    error_description = Column(String)
    error_group = Column(String)
    error_permanent = Column(String)
    price_per_message = Column(Float)
    currency = Column(String)
    done_at = Column(DateTime)
    sent_at = Column(DateTime)
    sms_count = Column(Integer)
    callback_data = Column(JSON)
    recipient = Column(String)
    notification_type = Column(String)
    domain = Column(String)
    send_date_time = Column(DateTime)
    url = Column(String)
    recipient_info = Column(JSON)
    geo_location_info = Column(JSON)

# Configuração do banco de dados SQLite
engine = create_engine('sqlite:///message_status.db')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)