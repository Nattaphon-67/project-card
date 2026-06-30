"""tests/test_student.py - Student Model Tests"""
import pytest
from src.models.student import Student
from src.models.student_card import StudentCard
from src.services.card_service import CardService
from datetime import datetime, timedelta


class TestStudent:
    """ทดสอบ Student Model"""
    
    def test_create_student(self):
        """ทดสอบสร้างนักศึกษา"""
        student = Student(
            student_id="67123456",
            first_name_th="ลิซ่า",
            last_name_th="Blackpink",
            first_name_en="Lisa",
            last_name_en="Blackpink",
            faculty="วิทยาศาสตร์"
        )
        assert student.student_id == "67123456"
        assert student.get_full_name_th() == "ลิซ่า Blackpink"
        assert student.get_full_name_en() == "LISA BLACKPINK"

    def test_student_to_dict(self):
        """ทดสอบแปลงเป็น dictionary"""
        student = Student(
            student_id="67123456",
            first_name_th="ลิซ่า",
            last_name_th="Blackpink",
            first_name_en="Lisa",
            last_name_en="Blackpink",
            faculty="วิทยาศาสตร์"
        )
        data = student.to_dict()
        assert "student_id" in data
        assert "full_name_th" in data
        assert "full_name_en" in data

