"""tests/test_card_service.py - Card Service Tests"""
import pytest
from datetime import datetime, timedelta
from src.services.card_service import CardService


class TestCardService:
    """ทดสอบ CardService"""
    
    def test_create_student_and_card(self):
        """ทดสอบสร้างนักศึกษาและบัตร"""
        service = CardService()
        student = service.create_student(
            student_id="67123456",
            first_name_th="ลิซ่า",
            last_name_th="Blackpink",
            first_name_en="Lisa",
            last_name_en="Blackpink",
            faculty="วิทยาศาสตร์"
        )
        card = service.create_card(student)
        assert card is not None
        assert card.student.student_id == "67123456"

    def test_get_card_by_student_id(self):
        """ทดสอบค้นหาบัตรตามรหัสนักศึกษา"""
        service = CardService()
        student = service.create_student(
            student_id="67123456",
            first_name_th="ลิซ่า",
            last_name_th="Blackpink",
            first_name_en="Lisa",
            last_name_en="Blackpink",
            faculty="วิทยาศาสตร์"
        )
        card = service.create_card(student)
        found_card = service.get_card_by_student_id("67123456")
        assert found_card is not None
        assert found_card.student.student_id == "67123456"
        assert found_card.card_number == card.card_number

    def test_get_active_cards(self):
        """ทดสอบดึงบัตรที่ยังใช้ได้"""
        service = CardService()
        student = service.create_student(
            student_id="67123456",
            first_name_th="ลิซ่า",
            last_name_th="Blackpink",
            first_name_en="Lisa",
            last_name_en="Blackpink",
            faculty="วิทยาศาสตร์"
        )
        card = service.create_card(student)
        active_cards = service.get_active_cards()
        assert len(active_cards) > 0
        assert card in active_cards

    def test_validate_card(self):
        """ทดสอบตรวจสอบบัตร"""
        service = CardService()
        student = service.create_student(
            student_id="67123456",
            first_name_th="ลิซ่า",
            last_name_th="Blackpink",
            first_name_en="Lisa",
            last_name_en="Blackpink",
            faculty="วิทยาศาสตร์"
        )
        card = service.create_card(student)
        validation = service.validate_card(card)
        assert validation["is_valid"] is True
        assert len(validation["errors"]) == 0

    def test_get_statistics(self):
        """ทดสอบดึงสถิติบัตร"""
        service = CardService()
        for i in range(5):
            student = service.create_student(
                student_id=f"6712345{i}",
                first_name_th="ลิซ่า",
                last_name_th="Blackpink",
                first_name_en="Lisa",
                last_name_en="Blackpink",
                faculty="วิทยาศาสตร์"
            )
            service.create_card(student)
        
        stats = service.get_statistics()
        assert stats["total_cards"] == 5
        assert stats["active_cards"] == 5
        assert stats["expired_cards"] == 0