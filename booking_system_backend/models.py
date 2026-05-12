from enum import Enum
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BookingStatus(str, Enum):
    BOOKED = "booked"
    CANCELLED = "cancelled"
    CANCELED = "cancelled"  # American spelling alias
    COMPLETED = "completed"

class TaskCategory(str, Enum):
    WORK = "Work"
    PERSONAL = "Personal"
    URGENT = "Urgent"

class TaskPriority(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"

class TaskStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

class Flight(Base):
    __tablename__ = 'flights'
    flight_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    origin = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    departure_time = Column(String, nullable=False)
    arrival_time = Column(String, nullable=False)
    base_price = Column(Integer, nullable=False)  # Economy price (1x)
    economy_seats_available = Column(Integer, nullable=False)  # 60% of total
    business_seats_available = Column(Integer, nullable=False)  # 30% of total
    galaxium_seats_available = Column(Integer, nullable=False)  # 10% of total

class Booking(Base):
    __tablename__ = 'bookings'
    booking_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    flight_id = Column(Integer, ForeignKey('flights.flight_id'), nullable=False)
    status = Column(String, nullable=False)
    booking_time = Column(String, nullable=False)
    seat_class = Column(String, nullable=False, default='economy')  # economy/business/galaxium
    price_paid = Column(Integer, nullable=False)  # Actual price at booking time

class Task(Base):
    __tablename__ = 'tasks'
    task_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    title = Column(String(200), nullable=False)
    description = Column(String, nullable=True)
    category = Column(String, nullable=False)  # Work, Personal, Urgent
    priority = Column(String, nullable=False)  # Low, Medium, High, Critical
    status = Column(String, nullable=False, default='pending')  # pending, in_progress, completed
    created_at = Column(String, nullable=False)
    updated_at = Column(String, nullable=False)