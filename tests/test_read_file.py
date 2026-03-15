# tests/test_read_file.py
import pytest
from report_coffee.read_file import get_students_info


def test_get_students_info_one_file(tmp_path):
    file = tmp_path / "test.csv"
    file.write_text("""student,date,coffee_spent,sleep_hours,study_hours,mood,exam
Алексей Смирнов,2024-06-01,450,4.5,12,норм,Математика
Дарья Петрова,2024-06-01,200,7.0,6,отл,Математика""")
    
    data = get_students_info([str(file)])
    assert len(data) == 2
    assert len(data["Алексей Смирнов"]) == 1
    assert data["Алексей Смирнов"][0]["coffee_spent"] == "450"



