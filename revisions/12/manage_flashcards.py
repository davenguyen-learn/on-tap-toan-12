"""
CÔNG CỤ QUẢN LÝ VÀ TRUY VẤN KHO FLASHCARD TOÁN 12 (SQLITE)
Cách dùng:
  - Liệt kê tất cả flashcard: python manage_flashcards.py list
  - Lọc theo chương (c1 .. c6): python manage_flashcards.py list --chapter c1
  - Lọc theo độ khó: python manage_flashcards.py list --difficulty "Vận dụng cao"
  - Tìm kiếm từ khóa: python manage_flashcards.py search "Bayes"
  - Xuất ra file Anki / CSV: python manage_flashcards.py export-anki anki_deck.csv
"""

import sqlite3
import argparse
import csv
import json
import os
import sys

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

DB_PATH = os.path.join(os.path.dirname(__file__), "data", "math12_flashcards.db")

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def list_cards(chapter=None, difficulty=None):
    conn = get_db()
    query = "SELECT id, chapter_name, topic, difficulty, front_content, back_type, final_answer FROM flashcards WHERE 1=1"
    params = []
    if chapter:
        query += " AND chapter_id = ?"
        params.append(chapter)
    if difficulty:
        query += " AND difficulty = ?"
        params.append(difficulty)
    
    rows = conn.execute(query, params).fetchall()
    print(f"\n📚 TỔNG CỘNG TÌM THẤY {len(rows)} FLASHCARDS:")
    print("=" * 80)
    for r in rows:
        print(f"[{r['id']}] {r['chapter_name']} | Chủ đề: {r['topic']} | Mức độ: {r['difficulty']}")
        print(f"   🔹 Đề bài: {r['front_content'][:100]}...")
        print(f"   🎯 Dạng: {r['back_type']} | Đáp án: {r['final_answer']}")
        print("-" * 80)
    conn.close()

def search_cards(keyword):
    conn = get_db()
    query = """
    SELECT id, chapter_name, topic, difficulty, front_content, back_type, back_strategy, back_solution, final_answer
    FROM flashcards
    WHERE front_content LIKE ? OR topic LIKE ? OR back_type LIKE ? OR back_strategy LIKE ?
    """
    kw = f"%{keyword}%"
    rows = conn.execute(query, (kw, kw, kw, kw)).fetchall()
    print(f"\n🔍 KẾT QUẢ TÌM KIẾM TỪ KHÓA '{keyword}' ({len(rows)} kết quả):")
    print("=" * 80)
    for r in rows:
        print(f"[{r['id']}] {r['chapter_name']} | {r['topic']} ({r['difficulty']})")
        print(f"   🔹 Đề bài: {r['front_content']}")
        print(f"   🎯 Dạng toán: {r['back_type']}")
        print(f"   💡 Hướng giải: {r['back_strategy'][:120]}...")
        print(f"   🏁 Đáp án: {r['final_answer']}")
        print("-" * 80)
    conn.close()

def export_anki(filename="anki_math12.csv"):
    conn = get_db()
    rows = conn.execute("SELECT chapter_name, topic, difficulty, front_content, back_type, back_strategy, back_pitfalls, back_solution, final_answer FROM flashcards").fetchall()
    
    with open(filename, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerow(["Front", "Back", "Tags"])
        for r in rows:
            front = f"<h3>{r['chapter_name']} - {r['topic']} ({r['difficulty']})</h3><p>{r['front_content']}</p>"
            back = f"""<b>🎯 DẠNG TOÁN:</b> {r['back_type']}<br><br>
<b>💡 HƯỚNG GIẢI:</b><br>{r['back_strategy']}<br><br>
<b>⚠️ LƯU Ý & CẠM BẪY:</b><br>{r['back_pitfalls']}<br><br>
<b>📝 LỜI GIẢI CHI TIẾT:</b><br>{r['back_solution']}<br><br>
<b>🏁 ĐÁP SỐ:</b> {r['final_answer']}"""
            tags = f"{r['topic'].replace(' ', '_')} {r['difficulty'].replace(' ', '_')}"
            writer.writerow([front, back, tags])

    print(f"\n✅ Đã xuất thành công {len(rows)} thẻ sang file Anki chuẩn Tab-Separated: {filename}")
    conn.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Quản lý kho flashcard Toán 12 SQLite")
    subparsers = parser.add_subparsers(dest="command")

    # List command
    list_p = subparsers.add_parser("list", help="Liệt kê danh sách flashcards")
    list_p.add_argument("--chapter", help="Mã chương: c1, c2, c3, c4, c5, c6")
    list_p.add_argument("--difficulty", help="Mức độ: Nhận biết, Thông hiểu, Vận dụng, Vận dụng cao")

    # Search command
    search_p = subparsers.add_parser("search", help="Tìm kiếm theo từ khóa")
    search_p.add_argument("keyword", help="Từ khóa cần tìm")

    # Export Anki command
    export_p = subparsers.add_parser("export-anki", help="Xuất ra file tương thích phần mềm Anki (.csv/.tsv)")
    export_p.add_argument("filename", nargs="?", default="anki_math12.csv", help="Tên file xuất")

    args = parser.parse_args()

    if args.command == "list":
        list_cards(args.chapter, args.difficulty)
    elif args.command == "search":
        search_cards(args.keyword)
    elif args.command == "export-anki":
        export_anki(args.filename)
    else:
        list_cards()
