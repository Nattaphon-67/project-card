"""main.py - Main Entry Point"""
import sys
from pathlib import Path

# เพิ่ม path สำหรับ import
sys.path.insert(0, str(Path(__file__).parent))

from src.models.student import Student
from src.models.student_card import StudentCard
from src.services.card_service import CardService
from src.views.card_renderer import CardRenderer


def main():
    """ฟังก์ชันหลัก"""
    print("=" * 60)
    print("ระบบจัดการบัตรนักศึกษา - มหาวิทยาลัยราชภัฏนครปฐม")
    print("=" * 60)
    
    # สร้าง Service
    service = CardService()
    
    # สร้างข้อมูลนักศึกษา (ตัวอย่างจากบัตร)
    student_data = {
        "student_id": "674259006",
        "first_name_th": "ณัฐพล",
        "last_name_th": "กลิ่นจุ่น",
        "first_name_en": "Nattaphon",
        "last_name_en": "Klinjun",
        "faculty": "คณะวิทยาศาสตร์และเทคโนโลยี",
        "photo_path": "assets/photos/nattaphon.jpg",
    }
    
    # สร้างนักศึกษา
    student = service.create_student(**student_data)
    print(f"\n✅ สร้างนักศึกษา: {student}")
    
    # สร้างบัตร
    card = service.create_card(student, expire_years=4, card_type="VISA")
    print(f"✅ สร้างบัตร: {card}")
    
    # ตรวจสอบบัตร
    validation = service.validate_card(card)
    print(f"\n📋 ผลการตรวจสอบบัตร:")
    print(f" Valid: {validation['is_valid']}")
    if validation['errors']:
        print(f" Errors: {validation['errors']}")
    if validation['warnings']:
        print(f" Warnings: {validation['warnings']}")
    
    # แสดงข้อมูลบัตร
    print(f"\n📄 ข้อมูลบัตร:")
    print(f" Card Number: {card.formatted_card_number}")
    print(f" CVV: {card.cvv}")
    print(f" Issue Date: {card.issue_date.strftime('%d/%m/%Y')}")
    print(f" Expire Date: {card.expire_date_thai}")
    print(f" Days Until Expire: {card.get_days_until_expire()}")
    
    # สร้างไฟล์ HTML
    renderer = CardRenderer(card)
    html_content = renderer.render_html()
    output_file = "student_card.html"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"\n✅ สร้างไฟล์ HTML: {output_file}")
    
    # สถิติ
    stats = service.get_statistics()
    print(f"\n📊 สถิติ:")
    print(f" Total Cards: {stats['total_cards']}")
    print(f" Active Cards: {stats['active_cards']}")
    print(f" Expired Cards: {stats['expired_cards']}")


if __name__ == "__main__":
    main()