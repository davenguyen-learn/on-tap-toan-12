"""
HỆ THỐNG SINH BÀI TẬP & FLASHCARD TOÁN 12 TỰ ĐỘNG BẰNG GEMINI AI
================================================================
Công cụ sinh kho câu hỏi chất lượng cao, đa dạng cấu trúc, chống lặp đề,
bám sát 100% chương trình Toán 12 GDPT 2018 và đề thi tốt nghiệp THPT mới.

Cách sử dụng:
  python generate_flashcards_ai.py --api-key "AIzaSy..." --target 1000
"""

import urllib.request
import urllib.error
import json
import sqlite3
import os
import sys
import time
import argparse
import random

# Thiết lập UTF-8 cho console Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

REV_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(REV_DIR, "data")
DB_PATH = os.path.join(DATA_DIR, "math12_flashcards.db")
JSON_PATH = os.path.join(DATA_DIR, "flashcards_data.json")

os.makedirs(DATA_DIR, exist_ok=True)

# ==============================================================================
# BẢN ĐỒ CHUYÊN ĐỀ & DẠNG TOÁN CHI TIẾT THEO SGK GDPT 2018 (SYLLABUS BLUEPRINT)
# ==============================================================================
SYLLABUS = {
    "c1": {
        "name": "Chương 1: Khảo sát hàm số",
        "topics": [
            {
                "topic": "Tính đơn điệu của hàm số",
                "subtopics": [
                    "Đọc khoảng đồng biến, nghịch biến trực tiếp từ Bảng biến thiên hoặc Đồ thị f(x) và f'(x)",
                    "Tìm tham số m để hàm đa thức bậc 3 đồng biến/nghịch biến trên R (dấu tam thức bậc 2)",
                    "Tìm m để hàm bậc 3 đơn điệu trên khoảng (a; b) bằng cô lập tham số m và khảo sát hàm số g(x)",
                    "Hàm phân thức bậc nhất/bậc nhất y = (ax+b)/(cx+d) đơn điệu trên khoảng (a; b) kèm điều kiện điểm gián đoạn",
                    "Hàm phân thức bậc hai/bậc nhất y = (ax^2+bx+c)/(px+q) đơn điệu trên từng khoảng xác định",
                    "Đơn điệu hàm hợp y = f(u(x)) và hàm tổng g(x) = f(x) - h(x) dựa vào đồ thị đạo hàm f'(x)"
                ]
            },
            {
                "topic": "Cực trị của hàm số",
                "subtopics": [
                    "Xác định điểm cực trị, giá trị cực trị từ Bảng biến thiên và Đồ thị (phân biệt x_CĐ, y_CĐ, toạ độ điểm cực trị)",
                    "Cực trị hàm bậc 3 thỏa mãn hệ thức Viet và điều kiện hình học (tam giác tạo bởi 2 cực trị, diện tích, khoảng cách)",
                    "Phương trình đường thẳng đi qua 2 điểm cực trị của hàm phân thức bậc 2/bậc 1 (đạo hàm tử chia đạo hàm mẫu)",
                    "Cực trị của hàm trị tuyệt đối y = |f(x)| (công thức m + n số cực trị và nghiệm đơn)",
                    "Cực trị của hàm y = f(|x|) và y = |f(x) + m| có số điểm cực trị cho trước",
                    "Đếm số điểm cực trị của hàm hợp g(x) = f(u(x)) khi biết đồ thị hoặc BBT của f'(x)"
                ]
            },
            {
                "topic": "Giá trị lớn nhất và Giá trị nhỏ nhất (Min/Max)",
                "subtopics": [
                    "Tìm Min/Max của hàm số cơ bản trên đoạn [a; b] và trên khoảng (a; b)",
                    "Tìm tham số m để giá trị lớn nhất/nhỏ nhất của hàm số trên đoạn [a; b] đạt giá trị cho trước",
                    "Min/Max của hàm trị tuyệt đối max|f(x) + m| trên đoạn [a; b]",
                    "Min/Max hàm nhiều biến quy về khảo sát hàm 1 biến bằng phương pháp đổi biến/đặt ẩn phụ"
                ]
            },
            {
                "topic": "Đường tiệm cận của đồ thị hàm số",
                "subtopics": [
                    "Xác định số lượng tiệm cận đứng, ngang trực tiếp từ Bảng biến thiên qua các giới hạn tại vô cực và điểm gián đoạn",
                    "Xác định tiệm cận đứng, ngang, tiệm cận xiên của hàm phân thức hữu tỉ bằng chia đa thức",
                    "Tiệm cận xiên bằng giới hạn a = lim f(x)/x, b = lim [f(x) - ax] cho hàm chứa căn thức",
                    "Tìm tham số m để đồ thị hàm số có đúng k đường tiệm cận",
                    "Xác định toạ độ tâm đối xứng là giao điểm của 2 đường tiệm cận"
                ]
            },
            {
                "topic": "Nhận dạng đồ thị, Bảng biến thiên & Xét dấu hệ số",
                "subtopics": [
                    "Nhận dạng đồ thị hàm số bậc 3, hàm bậc 1/bậc 1, hàm bậc 2/bậc 1 từ hình vẽ cho trước",
                    "Xác định dấu của các hệ số a, b, c, d của hàm bậc 3 y = ax^3+bx^2+cx+d dựa vào đồ thị",
                    "Xác định dấu của các hệ số a, b, c, d của hàm phân thức y = (ax+b)/(cx+d) dựa vào tiệm cận và giao điểm trục toạ độ",
                    "Tâm đối xứng (Điểm uốn của hàm bậc 3, giao 2 tiệm cận của hàm phân thức) và trục đối xứng của đồ thị"
                ]
            },
            {
                "topic": "Tiếp tuyến của đồ thị hàm số",
                "subtopics": [
                    "Phương trình tiếp tuyến tại tiếp điểm M_0(x_0; y_0)",
                    "Phương trình tiếp tuyến có hệ số góc k cho trước (song song hoặc vuông góc với đường thẳng d)",
                    "Phương trình tiếp tuyến đi qua một điểm A(x_A; y_A) nằm ngoài đồ thị",
                    "Sự tiếp xúc của hai đường cong và bài toán tiếp tuyến chung"
                ]
            },
            {
                "topic": "Sự tương giao của đồ thị hàm số",
                "subtopics": [
                    "Tìm toạ độ giao điểm của hai đồ thị bằng phương trình hoành độ giao điểm",
                    "Biện luận số nghiệm của phương trình f(x) = m dựa vào đồ thị và bảng biến thiên",
                    "Tương giao hàm bậc 3 với đường thẳng, điều kiện có 3 nghiệm phân biệt lập thành cấp số cộng",
                    "Kỹ thuật Ghép trục và sơ đồ V giải phương trình hàm hợp f(u(x)) = m"
                ]
            },
            {
                "topic": "Ứng dụng đạo hàm giải bài toán thực tế",
                "subtopics": [
                    "Tối ưu hóa kinh tế: Doanh thu R(x), chi phí C(x), lợi nhuận P(x) = R(x) - C(x), chi phí trung bình",
                    "Tối ưu hóa hình học: Cắt tôn làm hộp thể tích max, chi phí vật liệu làm bồn chứa, vỏ lon hình trụ tối ưu",
                    "Bài toán quãng đường ống dẫn dầu ngầm dưới biển, góc nhìn biển quảng cáo cực đại Regiomontanus",
                    "Toán chuyển động vật lý: Vận tốc tức thời v(t) = s'(t), gia tốc tức thời a(t) = v'(t) = s''(t), tốc độ tăng trưởng sinh học"
                ]
            }
        ]
    },
    "c2": {
        "name": "Chương 2: Vectơ & Không gian",
        "topics": [
            {
                "topic": "Vectơ không gian & Các quy tắc tính",
                "subtopics": [
                    "Quy tắc hình hộp trong lăng trụ và hình lập phương",
                    "Hệ thức trọng tâm tứ diện, trung điểm đoạn thẳng trong không gian",
                    "Phân tích một vectơ theo bộ 3 vectơ không đồng phẳng trong hình chóp, tứ diện"
                ]
            },
            {
                "topic": "Sự đồng phẳng & Cặp VTCP",
                "subtopics": [
                    "Điều kiện 3 vectơ đồng phẳng c = m*a + n*b hoặc tích hỗn tạp [a, b].c = 0",
                    "Vectơ song song với mặt phẳng, cặp vectơ chỉ phương của mặt phẳng",
                    "Chứng minh 4 điểm đồng phẳng hoặc tạo thành tứ diện"
                ]
            },
            {
                "topic": "Tích vô hướng & Góc giữa hai vectơ",
                "subtopics": [
                    "Tính tích vô hướng và góc giữa 2 vectơ cạnh trong tứ diện đều, chóp cụt",
                    "Điều kiện vuông góc của 2 vectơ trong không gian u.v = 0",
                    "Ứng dụng tính công của lực F làm dịch chuyển vật thể W = F.s"
                ]
            },
            {
                "topic": "Hệ toạ độ Oxyz thuần túy & Tích có hướng",
                "subtopics": [
                    "Toạ độ điểm, vectơ, trọng tâm, diện tích tam giác S = 1/2|[AB, AC]|",
                    "Thể tích tứ diện V = 1/6|[AB, AC].AD| và thể tích hình hộp",
                    "Gắn hệ trục toạ độ Oxyz giải bài toán hình học không gian cổ điển"
                ]
            },
            {
                "topic": "Toán thực tế 3D tĩnh học & Vector",
                "subtopics": [
                    "Bài toán cân bằng lực 3 dây cáp treo vật nặng hoặc đèn chùm",
                    "Vận tốc máy bay khi chịu ảnh hưởng của vectơ gió cản và lực đẩy động cơ",
                    "Tính góc đón ánh nắng mặt trời của tấm pin năng lượng mặt trời"
                ]
            }
        ]
    },
    "c3": {
        "name": "Chương 3: Thống kê ghép nhóm",
        "topics": [
            {
                "topic": "Các số đo xu thế trung tâm ghép nhóm",
                "subtopics": [
                    "Tính số trung bình cộng của bảng phân bố tần số ghép nhóm",
                    "Tính trung vị Me theo công thức nội suy tuyến tính",
                    "Tính Mốt Mo của mẫu số liệu ghép nhóm và ý nghĩa thực tế",
                    "Tính Tứ phân vị Q1, Q3 bằng công thức nội suy"
                ]
            },
            {
                "topic": "Khoảng biến thiên & Khoảng tứ phân vị",
                "subtopics": [
                    "Tính khoảng biến thiên R = a_{k+1} - a_1 và nhược điểm nhạy cảm ngoại lai",
                    "Tính khoảng tứ phân vị Delta_Q = Q3 - Q1 và tính kháng ngoại lai",
                    "Phát hiện giá trị ngoại lai bất thường trong mẫu số liệu ghép nhóm"
                ]
            },
            {
                "topic": "Phương sai, Độ lệch chuẩn & Hệ số biến thiên",
                "subtopics": [
                    "Tính phương sai s^2 và độ lệch chuẩn s theo công thức rút gọn",
                    "Tính hệ số biến thiên CV = s / mean để so sánh độ phân tán khi số trung bình khác nhau",
                    "Bài toán so sánh mức độ rủi ro giữa hai danh mục đầu tư tài chính/chứng khoán",
                    "Tìm tần số ẩn x, y từ điều kiện số trung bình hoặc trung vị cho trước"
                ]
            }
        ]
    },
    "c4": {
        "name": "Chương 4: Nguyên hàm & Tích phân",
        "topics": [
            {
                "topic": "Nguyên hàm cơ bản & Mở rộng f(ax+b)",
                "subtopics": [
                    "Bảng nguyên hàm mở rộng phân thức 1/(ax+b), hàm mũ, lượng giác",
                    "Kỹ thuật biến đổi lượng giác tìm nguyên hàm của sin^2, cos^2, tan^2, tích lượng giác",
                    "Tìm nguyên hàm thỏa mãn điều kiện ban đầu F(x0) = y0"
                ]
            },
            {
                "topic": "Phương pháp Đổi biến số",
                "subtopics": [
                    "Đổi biến loại 1 vi phân nhanh f(u)u'dx với hàm căn thức, lượng giác, ln",
                    "Đổi biến loại 2 lượng giác hóa x = a*sin(t), x = a*tan(t)",
                    "Kỹ thuật che nghiệm Heaviside cho tích phân hàm phân thức hữu tỉ P(x)/Q(x)"
                ]
            },
            {
                "topic": "Phương pháp Tích phân từng phần",
                "subtopics": [
                    "Tích phân từng phần dạng đa thức nhân lượng giác, đa thức nhân mũ, đa thức nhân ln",
                    "Kỹ thuật múa cột (Diagonal Method) cho tích phân từng phần lặp bậc cao",
                    "Tích phân từng phần luân hồi (dạng e^x * sin(x))"
                ]
            },
            {
                "topic": "Ứng dụng hình học diện tích & thể tích",
                "subtopics": [
                    "Diện tích hình phẳng giới hạn bởi 2 đường cong f(x) và g(x)",
                    "Công thức tính nhanh diện tích Parabol Archimedes S = 2/3 * Đáy * Cao",
                    "Thể tích vật thể bất kỳ qua diện tích thiết diện S(x)",
                    "Thể tích tròn xoay quay quanh trục Ox và trục Oy"
                ]
            },
            {
                "topic": "Ứng dụng thực tế & Tích phân hàm ẩn 9+",
                "subtopics": [
                    "Chuyển động vật lý: Quãng đường s = int v(t)dt, vận tốc biến thiên v = int a(t)dt, công của lực kéo",
                    "Kinh tế học: Thặng dư người tiêu dùng CS và thặng dư nhà sản xuất PS",
                    "Phương trình vi phân hàm ẩn cấp 1: f'(x) + p(x)f(x) = q(x), f'(x)[f(x)]^n = g(x)"
                ]
            }
        ]
    },
    "c5": {
        "name": "Chương 5: Phương pháp Oxyz",
        "topics": [
            {
                "topic": "Mặt phẳng & Mặt cầu trong Oxyz",
                "subtopics": [
                    "Phương trình mặt phẳng đi qua điểm vuông góc đường thẳng, mặt phẳng đoạn chắn",
                    "Phương trình mặt phẳng trung trực, mặt phẳng tiếp xúc mặt cầu",
                    "Phương trình mặt cầu chính tắc và tổng quát, điều kiện xác định mặt cầu"
                ]
            },
            {
                "topic": "Phương trình Đường thẳng & Vị trí tương đối",
                "subtopics": [
                    "Phương trình tham số và chính tắc của đường thẳng",
                    "Xét 4 vị trí tương đối giữa 2 đường thẳng: trùng, song song, cắt nhau, chéo nhau",
                    "Vị trí tương đối giữa đường thẳng và mặt phẳng, tìm giao điểm",
                    "Mặt cầu cắt mặt phẳng theo đường tròn giao tuyến có bán kính r = sqrt(R^2 - d^2)"
                ]
            },
            {
                "topic": "Khoảng cách & Góc trong không gian",
                "subtopics": [
                    "Khoảng cách từ điểm đến mặt phẳng, từ điểm đến đường thẳng",
                    "Khoảng cách giữa hai đường thẳng chéo nhau bằng tích hỗn tạp",
                    "Góc giữa hai mặt phẳng, góc giữa hai đường thẳng, góc giữa đường thẳng và mặt phẳng"
                ]
            },
            {
                "topic": "Hình chiếu, Đối xứng & Tâm tỉ cự 9+",
                "subtopics": [
                    "Tìm hình chiếu vuông góc và điểm đối xứng qua mặt phẳng / đường thẳng",
                    "Cực trị hình học không gian bằng phương pháp Tâm tỉ cự (Barycentric)",
                    "Bài toán thực tế trạm radar kiểm soát không lưu quét máy bay, cáp treo núi"
                ]
            }
        ]
    },
    "c6": {
        "name": "Chương 6: Xác suất & Bayes",
        "topics": [
            {
                "topic": "Xác suất có điều kiện & Quy tắc nhân",
                "subtopics": [
                    "Bản chất xác suất có điều kiện P(A|B) = P(A cap B) / P(B) và thu hẹp không gian mẫu",
                    "Quy tắc nhân xác suất cho biến cố phụ thuộc và độc lập",
                    "Kiểm tra tính độc lập của hai biến cố P(A cap B) = P(A)P(B)"
                ]
            },
            {
                "topic": "Sơ đồ cây & Công thức xác suất toàn phần",
                "subtopics": [
                    "Dựng sơ đồ cây (Tree Diagram) 2-3 tầng giải bài toán xác suất nhiều bước",
                    "Công thức xác suất toàn phần P(A) = sum P(Bi)P(A|Bi) với hệ đầy đủ",
                    "Bài toán lấy bi/sản phẩm liên tiếp có hoàn lại và không hoàn lại"
                ]
            },
            {
                "topic": "Định lý Bayes & Suy luận nguyên nhân ngược",
                "subtopics": [
                    "Công thức Bayes tính xác suất hậu nghiệm P(Bk|A)",
                    "Bài toán y tế: Sàng lọc bệnh hiếm, độ nhạy, độ đặc hiệu, phân tích nghịch lý dương tính giả",
                    "Bài toán KCS: Kiểm tra chất lượng phế phẩm qua nhiều phân xưởng / dây chuyền máy móc",
                    "Bài toán lọc thư rác Spam Filter ứng dụng mô hình Naive Bayes"
                ]
            }
        ]
    }
}

# ==============================================================================
# HÀM TỰ ĐỘNG TÌM VÀ QUẢN LÝ MODEL HOẠT ĐỘNG (MULTI-MODEL POOL)
# ==============================================================================
MODEL_POOL = [
    ("v1beta", "gemini-3.5-flash"),
    ("v1beta", "gemini-3.5-flash-lite"),
    ("v1beta", "gemini-3.1-flash-lite"),
    ("v1beta", "gemini-3.7-flash"),
    ("v1beta", "gemini-3-flash-preview"),
    ("v1beta", "gemma-4-26b-a4b-it"),
    ("v1", "gemini-3.5-flash")
]

def find_working_model(api_key, start_index=0):
    for i in range(len(MODEL_POOL)):
        idx = (start_index + i) % len(MODEL_POOL)
        ver, mod = MODEL_POOL[idx]
        url = f"https://generativelanguage.googleapis.com/{ver}/models/{mod}:generateContent?key={api_key}"
        payload = {"contents": [{"parts": [{"text": "1+1="}]}]}
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )
        try:
            with urllib.request.urlopen(req, timeout=10) as res:
                return idx, ver, mod
        except Exception:
            continue
    return 0, MODEL_POOL[0][0], MODEL_POOL[0][1]

# ==============================================================================
# HÀM GỌI GEMINI REST API
# ==============================================================================
import re

def robust_json_loads(raw_text):
    raw_text = raw_text.strip()
    if raw_text.startswith("```json"):
        raw_text = raw_text[7:]
    if raw_text.startswith("```"):
        raw_text = raw_text[3:]
    if raw_text.endswith("```"):
        raw_text = raw_text[:-3]
    raw_text = raw_text.strip()

    try:
        return json.loads(raw_text, strict=False)
    except Exception:
        pass

    result = []
    in_string = False
    i = 0
    n = len(raw_text)
    while i < n:
        c = raw_text[i]
        if not in_string:
            if c == '"':
                in_string = True
            result.append(c)
            i += 1
        else:
            if c == '\\':
                if i + 1 < n:
                    next_c = raw_text[i + 1]
                    if next_c == '"':
                        result.append('\\"')
                        i += 2
                    elif next_c == '\\':
                        result.append('\\\\')
                        i += 2
                    elif next_c in ['n', 't', 'r', 'b', 'f']:
                        if i + 2 < n and raw_text[i + 2].isalpha():
                            # LaTeX command like \frac, \begin, \text, \right, \nearrow
                            result.append('\\\\')
                            i += 1
                        else:
                            result.append('\\' + next_c)
                            i += 2
                    elif next_c == 'u' and i + 5 < n and all(ch in '0123456789abcdefABCDEF' for ch in raw_text[i+2:i+6]):
                        result.append(raw_text[i:i+6])
                        i += 6
                    else:
                        result.append('\\\\')
                        i += 1
                else:
                    result.append('\\\\')
                    i += 1
            elif c == '"':
                in_string = False
                result.append(c)
                i += 1
            else:
                result.append(c)
                i += 1

    return json.loads(''.join(result), strict=False)

def call_gemini_api(api_key, api_ver, model_name, prompt):
    url = f"https://generativelanguage.googleapis.com/{api_ver}/models/{model_name}:generateContent?key={api_key}"
    
    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ],
        "generationConfig": {
            "temperature": 0.7,
            "responseMimeType": "application/json"
        }
    }
    
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    
    try:
        with urllib.request.urlopen(req, timeout=60) as response:
            res_body = response.read().decode("utf-8")
            res_json = json.loads(res_body)
            raw_text = res_json["candidates"][0]["content"]["parts"][0]["text"]
            return robust_json_loads(raw_text)
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8")
        if e.code == 429:
            raise Exception("Rate limit 429: Too Many Requests")
        if e.code == 503:
            raise Exception("Server Busy 503: Model experiencing temporary high demand")
        raise Exception(f"HTTP {e.code}: {err_msg}")
    except Exception as e:
        raise e

# ==============================================================================
# TẠO PROMPT CHUẨN JSON SCHEMA CHO AI
# ==============================================================================
def create_batch_prompt(chapter_id, chapter_name, topic, subtopic, batch_size=5):
    return f"""Bạn là một chuyên gia khảo thí và biên soạn đề thi Toán THPT Quốc gia theo chương trình GDPT 2018 (SGK Kết nối tri thức, Cánh Diều, Chân trời sáng tạo).

Hãy tạo chính xác {batch_size} câu hỏi bài tập flashcard TOÁN 12 ĐỘC ĐÁO, CHẤT LƯỢNG CAO, KHÔNG LẶP LẠI theo yêu cầu sau:
- Chương: {chapter_name} (Mã: {chapter_id})
- Chủ đề: {topic}
- Dạng toán cụ thể: {subtopic}
- Phân bổ độ khó đa dạng: gồm cả Nhận biết, Thông hiểu, Vận dụng, Vận dụng cao.
- Đề bài phải phong phú: có hàm đa thức, lượng giác, phân thức, hàm mũ, logarithmic, căn thức, hình học không gian Oxyz, toán thực tế...
- QUY TẮC HIỂN THỊ ĐỒ THỊ & BẢNG BIẾN THIÊN:
  + Nếu bài toán cần BẢNG BIẾN THIÊN (BBT): Hãy viết bằng mã KaTeX array chuẩn, ví dụ:
    $$\\begin{{array}}{{c|ccccccc}} x & -\\infty & & x_1 & & x_2 & & +\\infty \\\\ \\hline f'(x) & & + & 0 & - & 0 & + & \\\\ \\hline f(x) & -\\infty & \\nearrow & y_{{CĐ}} & \\searrow & y_{{CT}} & \\nearrow & +\\infty \\end{{array}}$$
  + Nếu bài toán cần DÁNG ĐIỆU ĐỒ THỊ: Hãy mô tả chi tiết các đặc trưng hình học (chiều các nhánh vô cực, toạ độ điểm cực trị, giao điểm trục Oy, Ox, tiệm cận, điểm uốn tâm đối xứng) hoặc nhúng mã SVG đơn giản.
- Tuyệt đối KHÔNG sinh câu hỏi mẫu rập khuôn chỉ thay đổi số lẻ. Hãy tạo ra các tình huống toán học thực tế và bài toán tư duy sâu.

Hãy trả về một mảng JSON (Array) gồm đúng {batch_size} objects với cấu trúc chính xác sau:
[
  {{
    "chapter_id": "{chapter_id}",
    "chapter_name": "{chapter_name}",
    "topic": "{topic}",
    "difficulty": "Nhận biết" | "Thông hiểu" | "Vận dụng" | "Vận dụng cao",
    "front_content": "Đề bài câu hỏi đầy đủ (viết công thức toán học bằng ký hiệu LaTeX $...$ hoặc $$...$$)",
    "back_type": "Tên dạng toán cụ thể & phương pháp",
    "back_strategy": "1. Bước 1: ...\\n2. Bước 2: ... (Hướng giải tư duy logic từng bước ngắn gọn, sắc bén)",
    "back_pitfalls": "⚠️ Những sai lầm học sinh dễ mắc phải hoặc cạm bẫy toán học cần tránh",
    "back_solution": "Lời giải chi tiết từng dòng, có biến đổi công thức LaTeX rõ ràng",
    "final_answer": "Đáp số cuối cùng ngắn gọn"
  }}
]"""

# ==============================================================================
# HÀM DATABASE VÀ TIẾN TRÌNH
# ==============================================================================
def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db(reset=False):
    conn = get_db()
    cursor = conn.cursor()
    if reset:
        cursor.execute("DROP TABLE IF EXISTS flashcards")
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS flashcards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chapter_id TEXT NOT NULL,
        chapter_name TEXT NOT NULL,
        topic TEXT NOT NULL,
        difficulty TEXT NOT NULL,
        front_content TEXT NOT NULL,
        back_type TEXT NOT NULL,
        back_strategy TEXT NOT NULL,
        back_pitfalls TEXT NOT NULL,
        back_solution TEXT NOT NULL,
        final_answer TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()

def get_current_count(chapter_id=None):
    conn = get_db()
    if chapter_id:
        count = conn.execute("SELECT COUNT(*) FROM flashcards WHERE chapter_id = ?", (chapter_id,)).fetchone()[0]
    else:
        count = conn.execute("SELECT COUNT(*) FROM flashcards").fetchone()[0]
    conn.close()
    return count

def save_batch_to_db(cards_batch):
    conn = get_db()
    cursor = conn.cursor()
    inserted = 0
    for c in cards_batch:
        if not c.get("front_content") or not c.get("back_solution"):
            continue
        cursor.execute("""
        INSERT INTO flashcards (
            chapter_id, chapter_name, topic, difficulty,
            front_content, back_type, back_strategy, back_pitfalls,
            back_solution, final_answer
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            c.get("chapter_id", "c1"),
            c.get("chapter_name", "Toán 12"),
            c.get("topic", "Tổng hợp"),
            c.get("difficulty", "Thông hiểu"),
            c.get("front_content", ""),
            c.get("back_type", ""),
            c.get("back_strategy", ""),
            c.get("back_pitfalls", ""),
            c.get("back_solution", ""),
            c.get("final_answer", "")
        ))
        inserted += 1
    conn.commit()
    conn.close()
    return inserted

def export_to_json_and_html():
    conn = get_db()
    rows = conn.execute("SELECT id, chapter_id, chapter_name, topic, difficulty, front_content, back_type, back_strategy, back_pitfalls, back_solution, final_answer FROM flashcards ORDER BY id ASC").fetchall()
    conn.close()

    export_data = []
    for r in rows:
        export_data.append({
            "id": r["id"],
            "chapter_id": r["chapter_id"],
            "chapter_name": r["chapter_name"],
            "topic": r["topic"],
            "difficulty": r["difficulty"],
            "front": r["front_content"],
            "back_type": r["back_type"],
            "back_strategy": r["back_strategy"],
            "back_pitfalls": r["back_pitfalls"],
            "back_solution": r["back_solution"],
            "final_answer": r["final_answer"]
        })

    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(export_data, f, ensure_ascii=False, indent=2)

    # Sync into index.html
    html_path = os.path.join(REV_DIR, "index.html")
    if os.path.exists(html_path):
        try:
            with open(html_path, "r", encoding="utf-8") as f:
                html = f.read()

            marker_start = "    // FLASHCARD SYSTEM WITH RICH DATABASE"
            marker_end = "    // QUIZ CHECK SYSTEM"
            pos_start = html.find(marker_start)
            pos_end = html.find(marker_end)

            if pos_start != -1 and pos_end != -1:
                new_js = f"""    // FLASHCARD SYSTEM WITH RICH DATABASE ({len(export_data)} QUESTIONS)
    const allFlashcards = {json.dumps(export_data, ensure_ascii=False)};
    let activeFlashcards = [...allFlashcards];
    let currentFcIndex = 0;

    function filterFlashcards() {{
      const chap = document.getElementById('fcChapterFilter').value;
      const diff = document.getElementById('fcDiffFilter').value;

      activeFlashcards = allFlashcards.filter(card => {{
        const matchChap = (chap === 'all' || card.chapter_id === chap);
        const matchDiff = (diff === 'all' || card.difficulty === diff);
        return matchChap && matchDiff;
      }});

      if (activeFlashcards.length === 0) {{
        activeFlashcards = [{{
          id: 0,
          chapter_name: "Không có kết quả",
          topic: "Trống",
          difficulty: "N/A",
          front: "Không tìm thấy flashcard nào phù hợp với bộ lọc hiện tại. Vui lòng chọn lại.",
          back_type: "Trống",
          back_strategy: "Chọn 'Tất cả các chương' hoặc 'Tất cả mức độ'.",
          back_pitfalls: "Không có",
          back_solution: "N/A",
          final_answer: "N/A"
        }}];
      }}

      currentFcIndex = 0;
      updateFlashcardUI();
    }}

    function updateFlashcardUI() {{
      const card = activeFlashcards[currentFcIndex];
      document.getElementById('fcCategoryBadge').innerText = card.chapter_name.split(':')[0] || "Toán 12";
      document.getElementById('fcTopicBadge').innerText = card.topic || "Tổng hợp";
      document.getElementById('fcDiffBadge').innerText = card.difficulty || "Thông hiểu";
      document.getElementById('fcQuestion').innerHTML = card.front;

      document.getElementById('fcBackType').innerText = card.back_type || "";
      document.getElementById('fcBackStrategy').innerHTML = card.back_strategy || "";
      document.getElementById('fcBackPitfalls').innerHTML = card.back_pitfalls || "";
      document.getElementById('fcBackSolution').innerHTML = (card.back_solution || "") + (card.final_answer ? ("<br><strong>Đáp số:</strong> " + card.final_answer) : "");

      document.getElementById('fcProgress').innerText = `Thẻ ${{currentFcIndex + 1}} / ${{activeFlashcards.length}}`;
      
      const fcEl = document.getElementById('flashcardCard');
      fcEl.classList.remove('flipped');
      setTimeout(renderAllFlashcardMath, 20);
    }}

    function flipCard() {{
      document.getElementById('flashcardCard').classList.toggle('flipped');
      setTimeout(renderAllFlashcardMath, 20);
    }}

    function nextCard() {{
      currentFcIndex = (currentFcIndex + 1) % activeFlashcards.length;
      updateFlashcardUI();
    }}

    function prevCard() {{
      currentFcIndex = (currentFcIndex - 1 + activeFlashcards.length) % activeFlashcards.length;
      updateFlashcardUI();
    }}

    function randomCard() {{
      currentFcIndex = Math.floor(Math.random() * activeFlashcards.length);
      updateFlashcardUI();
    }}"""
                html = html[:pos_start] + new_js + "\n\n" + html[pos_end:]
                with open(html_path, "w", encoding="utf-8") as f:
                    f.write(html)
        except Exception as e:
            print(f"Lưu ý đồng bộ HTML: {e}")

# ==============================================================================
# HÀM CHÍNH ĐIỀU PHỐI TIẾN TRÌNH GENERATOR
# ==============================================================================
def run_generator(api_key, target_count=1000, specific_chapter=None, reset=False):
    init_db(reset=reset)
    initial_count = get_current_count()

    print("=" * 80)
    print(f"🚀 KHỞI ĐỘNG HỆ THỐNG SINH BÀI TẬP FLASHCARD TOÁN 12 BẰNG GEMINI AI")
    print(f"🎯 Mục tiêu: {target_count} câu hỏi chất lượng cao")
    print("🔍 Đang tự động kiểm tra model hoạt động...")
    model_idx, api_ver, model_name = find_working_model(api_key)
    print(f"🤖 Model AI đang sử dụng: {model_name} (API: {api_ver})")
    print(f"📂 Hiện có trong Database: {initial_count} câu hỏi")
    print("=" * 80)

    if initial_count >= target_count and not reset:
        print(f"✅ Database đã có đủ {initial_count} câu hỏi (>= mục tiêu {target_count}).")
        export_to_json_and_html()
        return

    # Lập danh sách các chuyên đề cần sinh
    chapters_to_run = [specific_chapter] if specific_chapter else list(SYLLABUS.keys())

    all_tasks = []
    for c_id in chapters_to_run:
        c_info = SYLLABUS[c_id]
        for t_info in c_info["topics"]:
            for sub in t_info["subtopics"]:
                all_tasks.append({
                    "chapter_id": c_id,
                    "chapter_name": c_info["name"],
                    "topic": t_info["topic"],
                    "subtopic": sub
                })

    random.shuffle(all_tasks)

    current_total = get_current_count()
    task_idx = 0
    batch_size = 5

    while current_total < target_count:
        task = all_tasks[task_idx % len(all_tasks)]
        task_idx += 1

        c_id = task["chapter_id"]
        c_name = task["chapter_name"]
        top = task["topic"]
        sub = task["subtopic"]

        print(f"\n⚡ Đang sinh [{current_total}/{target_count}] | {c_name} | {top}...")
        print(f"   Dạng toán: {sub}")

        prompt = create_batch_prompt(c_id, c_name, top, sub, batch_size=batch_size)

        max_retries = 5
        success = False
        for attempt in range(max_retries):
            try:
                cards = call_gemini_api(api_key, api_ver, model_name, prompt)
                if isinstance(cards, list) and len(cards) > 0:
                    added = save_batch_to_db(cards)
                    current_total = get_current_count()
                    print(f"   ✅ Đã nạp thành công +{added} câu hỏi chất lượng cao! (Tổng: {current_total}/{target_count})")
                    export_to_json_and_html()
                    success = True
                    time.sleep(1.5)
                    break
                else:
                    print(f"   ⚠️ Kết quả trả về không hợp lệ, thử lại lần {attempt+1}...")
            except Exception as e:
                err_str = str(e)
                if "429" in err_str or "Rate limit" in err_str or "503" in err_str:
                    print(f"   ⏳ Model {model_name} đang nghẽn ({err_str[:40]}). Đang tự động đổi model...")
                    model_idx, api_ver, model_name = find_working_model(api_key, start_index=model_idx + 1)
                    print(f"   🔄 Đã chuyển sang model: {model_name} ({api_ver})")
                    time.sleep(2)
                else:
                    print(f"   ❌ Lỗi ({err_str}), thử lại sau 3s...")
                    time.sleep(3)

        if not success:
            print(f"   ⚠️ Bỏ qua dạng toán này sau {max_retries} lần thử.")

    print("\n" + "=" * 80)
    print(f"🎉 HOÀN THÀNH TOÀN DIỆN! Tổng số câu hỏi đạt {get_current_count()} câu.")
    print(f"📁 Database: {DB_PATH}")
    print(f"📁 Web Flashcard: {JSON_PATH}")
    print("=" * 80)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sinh kho câu hỏi Flashcard Toán 12 bằng Gemini AI")
    parser.add_argument("--api-key", help="Khóa Google Gemini API Key")
    parser.add_argument("--target", type=int, default=1000, help="Tổng số lượng câu hỏi mục tiêu (mặc định 1000)")
    parser.add_argument("--chapter", help="Chỉ sinh riêng 1 chương: c1, c2, c3, c4, c5, c6")
    parser.add_argument("--reset", action="store_true", help="Xóa sạch database cũ và tạo mới hoàn toàn")

    args = parser.parse_args()

    api_key = args.api_key or os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("\n🔑 CHƯA TÌM THẤY GEMINI API KEY!")
        print("Vui lòng nhập Gemini API Key của bạn bên dưới:")
        try:
            api_key = input("Nhập API Key: ").strip()
        except EOFError:
            api_key = ""

    if not api_key:
        print("\n❌ Lỗi: Không có API Key. Bạn có thể lấy miễn phí tại https://aistudio.google.com/app/apikey")
        sys.exit(1)

    run_generator(
        api_key=api_key,
        target_count=args.target,
        specific_chapter=args.chapter,
        reset=args.reset
    )
