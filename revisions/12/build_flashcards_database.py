import sqlite3
import json
import os

db_path = r"c:\Users\Admin\Code\Test\toan-12\revisions\12\data\math12_flashcards.db"
json_path = r"c:\Users\Admin\Code\Test\toan-12\revisions\12\data\flashcards_data.json"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS flashcards")

cursor.execute("""
CREATE TABLE flashcards (
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

# Load and populate 40+ rich cards
cards = [
    # --- CHƯƠNG 1 ---
    {
        "chapter_id": "c1",
        "chapter_name": "Chương 1: Khảo sát hàm số",
        "topic": "Tính đơn điệu bậc 3",
        "difficulty": "Vận dụng",
        "front_content": "Tìm tất cả các giá trị thực của $m$ để hàm số $y = \\frac{1}{3}x^3 - mx^2 + (m^2 - m + 1)x + 2025$ đồng biến trên $\\mathbb{R}$.",
        "back_type": "Tìm tham số $m$ để tam thức bậc 2 không đổi dấu",
        "back_strategy": "1. Tính $y' = x^2 - 2mx + (m^2 - m + 1)$.\n2. Đồng biến trên $\\mathbb{R} \\iff y' \\ge 0, \\forall x \\in \\mathbb{R} \\iff \\Delta' \\le 0$.\n3. Giải bất phương trình $\\Delta' \\le 0$.",
        "back_pitfalls": "⚠️ Nhớ lấy dấu bằng ở $\\Delta' \\le 0$ đối với hàm đa thức.",
        "back_solution": "$y' = x^2 - 2mx + m^2 - m + 1 \\ge 0, \\forall x \\iff \\Delta' = m^2 - (m^2 - m + 1) = m - 1 \\le 0 \\iff m \\le 1$.",
        "final_answer": "$m \\le 1$"
    },
    {
        "chapter_id": "c1",
        "chapter_name": "Chương 1: Khảo sát hàm số",
        "topic": "Đơn điệu phân thức",
        "difficulty": "Vận dụng cao",
        "front_content": "Tìm $m$ để hàm số $y = \\frac{mx + 4}{x + m}$ nghịch biến trên khoảng $(1; +\\infty)$.",
        "back_type": "Hàm bậc nhất/bậc nhất đơn điệu trên khoảng",
        "back_strategy": "1. $y' = \\frac{m^2 - 4}{(x + m)^2}$.\n2. Điều kiện nghịch biến: $y' < 0$ và $-m \\notin (1; +\\infty) \\iff -m \\le 1 \\iff m \\ge -1$.\n3. Giải hệ điều kiện.",
        "back_pitfalls": "⚠️ Tuyệt đối KHÔNG CÓ DẤU BẰNG ở đạo hàm hàm bậc nhất/bậc nhất ($y' < 0$). Và đừng quên điều kiện điểm gián đoạn $-m \\le 1$.",
        "back_solution": "$\\begin{cases} m^2 - 4 < 0 \\\\ -m \\le 1 \\end{cases} \\iff \\begin{cases} -2 < m < 2 \\\\ m \\ge -1 \\end{cases} \\iff -1 \\le m < 2$.",
        "final_answer": "$-1 \\le m < 2$"
    },
    {
        "chapter_id": "c1",
        "chapter_name": "Chương 1: Khảo sát hàm số",
        "topic": "Đường thẳng qua 2 cực trị",
        "difficulty": "Thông hiểu",
        "front_content": "Viết phương trình đường thẳng đi qua 2 điểm cực trị của $y = \\frac{x^2 - 3x + 6}{x - 1}$.",
        "back_type": "Đường thẳng qua 2 cực trị của hàm phân thức bậc 2/bậc 1",
        "back_strategy": "Dùng công thức đạo hàm tử chia đạo hàm mẫu: $y = \\frac{u'(x)}{v'(x)} = \\frac{2x - 3}{1} = 2x - 3$.",
        "back_pitfalls": "⚠️ Không cần giải phương trình tìm toạ độ từng điểm cực trị.",
        "back_solution": "$y = \\frac{(x^2 - 3x + 6)'}{(x - 1)'} = \\frac{2x - 3}{1} = 2x - 3$.",
        "final_answer": "$y = 2x - 3$"
    },
    {
        "chapter_id": "c1",
        "chapter_name": "Chương 1: Khảo sát hàm số",
        "topic": "Cực trị trị tuyệt đối",
        "difficulty": "Vận dụng cao",
        "front_content": "Tìm số điểm cực trị của hàm số $g(x) = |x^3 - 3x^2 + 1|$.",
        "back_type": "Số điểm cực trị của $y = |f(x)|$",
        "back_strategy": "Số cực trị $= m + n$, với $m$ là số cực trị của $f(x)$ và $n$ là số nghiệm đơn của $f(x) = 0$.",
        "back_pitfalls": "⚠️ Chỉ đếm nghiệm đơn (cắt trục $Ox$), bỏ qua nghiệm kép (tiếp xúc).",
        "back_solution": "$f(x) = x^3 - 3x^2 + 1$ có $m = 2$ cực trị ($x = 0, x = 2$).\n$f(0) = 1 > 0, f(2) = -3 < 0 \\implies f(x)=0$ có $n = 3$ nghiệm đơn.\nSố cực trị $= 2 + 3 = 5$.",
        "final_answer": "$5$ điểm cực trị"
    },
    {
        "chapter_id": "c1",
        "chapter_name": "Chương 1: Khảo sát hàm số",
        "topic": "Tiệm cận xiên",
        "difficulty": "Thông hiểu",
        "front_content": "Tìm phương trình tiệm cận xiên của đồ thị hàm số $y = \\frac{2x^2 - 5x + 7}{x - 2}$.",
        "back_type": "Xác định tiệm cận xiên bằng chia đa thức",
        "back_strategy": "Chia tử cho mẫu: $\\frac{2x^2 - 5x + 7}{x - 2} = 2x - 1 + \\frac{5}{x - 2}$.\nPhần thương $y = 2x - 1$ là tiệm cận xiên.",
        "back_pitfalls": "⚠️ Tiệm cận xiên có dạng $y = ax + b$ với $a \\ne 0$.",
        "back_solution": "$y = 2x - 1 + \\frac{5}{x - 2} \\implies \\lim_{x \\to \\pm\\infty} [y - (2x - 1)] = 0 \\implies y = 2x - 1$.",
        "final_answer": "$y = 2x - 1$"
    },
    {
        "chapter_id": "c1",
        "chapter_name": "Chương 1: Khảo sát hàm số",
        "topic": "Tối ưu hóa kinh tế",
        "difficulty": "Vận dụng",
        "front_content": "Hàm tổng chi phí sản xuất là $C(x) = x^2 + 40x + 1600$, giá bán mỗi sản phẩm là $p(x) = 200 - x$. Tìm sản lượng $x$ để lợi nhuận tối đa.",
        "back_type": "Tối ưu hóa hàm lợi nhuận $P(x) = R(x) - C(x)$",
        "back_strategy": "1. Doanh thu: $R(x) = x(200 - x) = -x^2 + 200x$.\n2. Lợi nhuận: $P(x) = R(x) - C(x) = -2x^2 + 160x - 1600$.\n3. Cho $P'(x) = 0$ tìm $x$.",
        "back_pitfalls": "⚠️ Phân biệt rõ giữa hàm doanh thu $R(x) = x \\cdot p(x)$ và hàm lợi nhuận $P(x) = R(x) - C(x)$.",
        "back_solution": "$P'(x) = -4x + 160 = 0 \\iff x = 40$. $P''(x) = -4 < 0 \\implies x = 40$ cho lợi nhuận tối đa.",
        "final_answer": "$x = 40$ sản phẩm"
    },
    {
        "chapter_id": "c1",
        "chapter_name": "Chương 1: Khảo sát hàm số",
        "topic": "Tối ưu hóa vật liệu",
        "difficulty": "Vận dụng",
        "front_content": "Sản xuất lon nước ngọt hình trụ có thể tích $V_0$ cố định. Tìm tỉ số giữa chiều cao $h$ và bán kính $r$ để tốn ít kim loại nhất (diện tích toàn phần nhỏ nhất).",
        "back_type": "Bài toán cực trị hình học không gian bằng BĐT Cauchy",
        "back_strategy": "1. $V_0 = \\pi r^2 h \\implies h = \\frac{V_0}{\\pi r^2}$.\n2. $S_{tp} = 2\\pi r^2 + 2\\pi r h = 2\\pi r^2 + \\frac{V_0}{r} + \\frac{V_0}{r}$.\n3. Áp dụng Cauchy 3 số: $2\\pi r^2 = \\frac{V_0}{r} \\iff h = 2r$.",
        "back_pitfalls": "⚠️ Lon nước ngọt có 2 nắp (diện tích toàn phần $2\\pi r^2 + 2\\pi rh$), khác với cốc/hộp không nắp (chỉ có 1 đáy $\\pi r^2$).",
        "back_solution": "Dấu bằng Cauchy xảy ra khi $2\\pi r^2 = \\frac{V_0}{r} \\iff 2\\pi r^3 = \\pi r^2 h \\iff h = 2r$.",
        "final_answer": "$\\frac{h}{r} = 2$ (Chiều cao bằng đường kính đáy)"
    },
    {
        "chapter_id": "c1",
        "chapter_name": "Chương 1: Khảo sát hàm số",
        "topic": "Quang học Regiomontanus",
        "difficulty": "Vận dụng cao",
        "front_content": "Bảng quảng cáo cao $h$ gắn trên tường, mép dưới cách tầm mắt khoảng $b$, mép trên cách tầm mắt khoảng $a$. Người quan sát đứng cách tường khoảng $x$ bằng bao nhiêu thì góc nhìn lớn nhất?",
        "back_type": "Bài toán cực đại góc nhìn Regiomontanus",
        "back_strategy": "1. $\\tan \\theta = \\tan(\\alpha - \\beta) = \\frac{\\tan \\alpha - \\tan \\beta}{1 + \\tan \\alpha \\tan \\beta} = \\frac{\\frac{a}{x} - \\frac{b}{x}}{1 + \\frac{ab}{x^2}} = \\frac{a - b}{x + \\frac{ab}{x}}$.\n2. Góc lớn nhất $\\iff$ Mẫu nhỏ nhất $\\iff x = \\sqrt{ab}$.",
        "back_pitfalls": "⚠️ $a$ và $b$ là khoảng cách tính từ tầm mắt người quan sát, không phải từ mặt đất.",
        "back_solution": "Theo BĐT Cauchy: $x + \\frac{ab}{x} \\ge 2\\sqrt{ab}$. Dấu bằng $\\iff x = \\frac{ab}{x} \\iff x = \\sqrt{ab}$.",
        "final_answer": "$x = \\sqrt{ab}$"
    },

    # --- CHƯƠNG 2 ---
    {
        "chapter_id": "c2",
        "chapter_name": "Chương 2: Vectơ & Không gian",
        "topic": "Quy tắc hình hộp",
        "difficulty": "Nhận biết",
        "front_content": "Cho hình hộp $ABCD.A'B'C'D'$. Biểu diễn $\\vec{AC'}$ theo $\\vec{AB}, \\vec{AD}, \\vec{AA'}$.",
        "back_type": "Quy tắc hình hộp",
        "back_strategy": "$\\vec{AC'} = \\vec{AB} + \\vec{AD} + \\vec{AA'}$.",
        "back_pitfalls": "⚠️ Cả 3 vectơ phải cùng gốc $A$.",
        "back_solution": "$\\vec{AB} + \\vec{AD} = \\vec{AC}$ và $\\vec{AC} + \\vec{AA'} = \\vec{AC'}$.",
        "final_answer": "$\\vec{AC'} = \\vec{AB} + \\vec{AD} + \\vec{AA'}$"
    },
    {
        "chapter_id": "c2",
        "chapter_name": "Chương 2: Vectơ & Không gian",
        "topic": "Trọng tâm tứ diện",
        "difficulty": "Thông hiểu",
        "front_content": "Cho tứ diện $ABCD$ có trọng tâm $G$. Đẳng thức nào đúng với điểm $O$ bất kỳ?",
        "back_type": "Hệ thức trọng tâm tứ diện",
        "back_strategy": "$\\vec{OA} + \\vec{OB} + \\vec{OC} + \\vec{OD} = 4\\vec{OG}$.",
        "back_pitfalls": "⚠️ Hệ số của tứ diện là 4, không phải 3 như tam giác.",
        "back_solution": "Vì $\\vec{GA} + \\vec{GB} + \\vec{GC} + \\vec{GD} = \\vec{0} \\implies \\vec{OA} + \\vec{OB} + \\vec{OC} + \\vec{OD} = 4\\vec{OG}$.",
        "final_answer": "$\\vec{OA} + \\vec{OB} + \\vec{OC} + \\vec{OD} = 4\\vec{OG}$"
    },
    {
        "chapter_id": "c2",
        "chapter_name": "Chương 2: Vectơ & Không gian",
        "topic": "Tích có hướng",
        "difficulty": "Thông hiểu",
        "front_content": "Cho $\\vec{a} = (1; 2; -1), \\vec{b} = (3; 0; 2)$. Tính $[\\vec{a}, \\vec{b}]$.",
        "back_type": "Tính toạ độ tích có hướng",
        "back_strategy": "$[\\vec{a}, \\vec{b}] = (y_1 z_2 - y_2 z_1; z_1 x_2 - z_2 x_1; x_1 y_2 - x_2 y_1)$.",
        "back_pitfalls": "⚠️ Chú ý dấu ở toạ độ thứ hai: $(-1)(3) - 2(1) = -5$.",
        "back_solution": "$[\\vec{a}, \\vec{b}] = (4 - 0; -3 - 2; 0 - 6) = (4; -5; -6)$.",
        "final_answer": "$(4; -5; -6)$"
    },
    {
        "chapter_id": "c2",
        "chapter_name": "Chương 2: Vectơ & Không gian",
        "topic": "Thể tích tứ diện",
        "difficulty": "Vận dụng",
        "front_content": "Cho tứ diện $ABCD$ có $A(1;0;0), B(0;2;0), C(0;0;3), D(2;2;2)$. Tính thể tích tứ diện $ABCD$.",
        "back_type": "Thể tích tứ diện bằng tích hỗn tạp",
        "back_strategy": "$V = \\frac{1}{6} |[\\vec{AB}, \\vec{AC}] \\cdot \\vec{AD}|$.",
        "back_pitfalls": "⚠️ Hệ số là $\\frac{1}{6}$, không phải $\\frac{1}{3}$.",
        "back_solution": "$\\vec{AB} = (-1;2;0), \\vec{AC} = (-1;0;3) \\implies [\\vec{AB}, \\vec{AC}] = (6; 3; 2)$.\n$\\vec{AD} = (1; 2; 2) \\implies (6)(1) + (3)(2) + (2)(2) = 16 \\implies V = \\frac{16}{6} = \\frac{8}{3}$.",
        "final_answer": "$V = \\frac{8}{3}$"
    },
    {
        "chapter_id": "c2",
        "chapter_name": "Chương 2: Vectơ & Không gian",
        "topic": "Cân bằng lực 3D",
        "difficulty": "Vận dụng cao",
        "front_content": "Treo đèn chùm nặng $120\\text{ N}$ bằng 3 dây cáp đối xứng gắn vào trần nhà tại $A(1; \\sqrt{3}; 0), B(1; -\\sqrt{3}; 0), C(-2; 0; 0)$ với điểm buộc $S(0; 0; -2)$. Tính lực căng mỗi dây.",
        "back_type": "Bài toán cân bằng lực tĩnh học trong không gian",
        "back_strategy": "1. Chiều dài mỗi dây: $L = \\sqrt{1 + 3 + 4} = 2\\sqrt{2}\\text{ m}$.\n2. Chiếu lên trục $Oz$: $3 \\cdot \\left(T \\cdot \\frac{2}{2\\sqrt{2}}\\right) = 120 \\implies \\frac{3T}{\\sqrt{2}} = 120 \\implies T = 40\\sqrt{2}\\text{ N}$.",
        "back_pitfalls": "⚠️ Nhớ nhân hệ số 3 do có 3 sợi dây cáp cùng chịu tải trọng lực $P$.",
        "back_solution": "$3 \\cdot \\frac{T}{\\sqrt{2}} = 120 \\implies T = 40\\sqrt{2} \\approx 56.57\\text{ N}$.",
        "final_answer": "$40\\sqrt{2}\\text{ N} \\approx 56.57\\text{ N}$"
    },

    # --- CHƯƠNG 3 ---
    {
        "chapter_id": "c3",
        "chapter_name": "Chương 3: Thống kê ghép nhóm",
        "topic": "Tứ phân vị Q1",
        "difficulty": "Thông hiểu",
        "front_content": "Viết công thức nội suy tuyến tính tính Tứ phân vị thứ nhất $Q_1$ của mẫu số liệu ghép nhóm.",
        "back_type": "Công thức nội suy $Q_1$",
        "back_strategy": "$Q_1 = u_p + \\frac{\\frac{n}{4} - cf_{p-1}}{n_p} \\cdot (u_{p+1} - u_p)$ với nhóm $p$ là nhóm đầu tiên có $cf_p \\ge \\frac{n}{4}$.",
        "back_pitfalls": "⚠️ $cf_{p-1}$ là tần số tích lũy của nhóm trước nhóm $p$.",
        "back_solution": "$Q_1 = u_p + \\frac{\\frac{n}{4} - cf_{p-1}}{n_p} \\cdot (u_{p+1} - u_p)$.",
        "final_answer": "$$Q_1 = u_p + \\frac{\\frac{n}{4} - cf_{p-1}}{n_p} \\cdot (u_{p+1} - u_p)$$"
    },
    {
        "chapter_id": "c3",
        "chapter_name": "Chương 3: Thống kê ghép nhóm",
        "topic": "Khoảng tứ phân vị",
        "difficulty": "Thông hiểu",
        "front_content": "Khoảng tứ phân vị $\\Delta_Q$ được định nghĩa như thế nào và có ưu điểm gì so với khoảng biến thiên $R$?",
        "back_type": "Độ phân tán và tính kháng ngoại lai",
        "back_strategy": "$\\Delta_Q = Q_3 - Q_1$, đo độ phân tán của $50\\%$ số liệu trung tâm và không bị ảnh hưởng bởi giá trị ngoại lai.",
        "back_pitfalls": "⚠️ Khoảng biến thiên $R = x_{max} - x_{min}$ rất nhạy cảm với các điểm đột biến ở 2 đầu mút.",
        "back_solution": "$\\Delta_Q = Q_3 - Q_1$, có tính kháng ngoại lai vượt trội so với $R$.",
        "final_answer": "$\\Delta_Q = Q_3 - Q_1$, tính kháng ngoại lai cao"
    },
    {
        "chapter_id": "c3",
        "chapter_name": "Chương 3: Thống kê ghép nhóm",
        "topic": "Hệ số biến thiên",
        "difficulty": "Vận dụng",
        "front_content": "Khi nào cần sử dụng Hệ số biến thiên $CV = \\frac{s}{\\bar{x}}$ thay vì Độ lệch chuẩn $s$ để so sánh độ phân tán?",
        "back_type": "Ứng dụng hệ số biến thiên $CV$",
        "back_strategy": "Khi hai mẫu số liệu có đơn vị đo khác nhau hoặc có giá trị trung bình $\\bar{x}$ chênh lệch nhau đáng kể.",
        "back_pitfalls": "⚠️ Nếu hai mẫu có cùng số trung bình thì so sánh trực tiếp độ lệch chuẩn $s$ là đủ.",
        "back_solution": "Sử dụng $CV = \\frac{s}{\\bar{x}}$ để đo mức độ phân tán tương đối độc lập với quy mô của số trung bình.",
        "final_answer": "Khi hai mẫu có số trung bình khác nhau"
    },

    # --- CHƯƠNG 4 ---
    {
        "chapter_id": "c4",
        "chapter_name": "Chương 4: Nguyên hàm & Tích phân",
        "topic": "Đổi biến loại 1",
        "difficulty": "Thông hiểu",
        "front_content": "Tính tích phân $I = \\int_1^e \\frac{\\ln x}{x} \\, dx$.",
        "back_type": "Đổi biến vi phân nhanh $\\int u du$",
        "back_strategy": "Đặt $t = \\ln x \\implies dt = \\frac{dx}{x}$. Cận: $x=1 \\to t=0, x=e \\to t=1$. Khi đó $I = \\int_0^1 t dt = \\frac{1}{2}$.",
        "back_pitfalls": "⚠️ Nhớ đổi cận khi đổi biến số.",
        "back_solution": "$I = \\left[\\frac{\\ln^2 x}{2}\\right]_1^e = \\frac{1^2}{2} - 0 = \\frac{1}{2}$.",
        "final_answer": "$I = \\frac{1}{2}$"
    },
    {
        "chapter_id": "c4",
        "chapter_name": "Chương 4: Nguyên hàm & Tích phân",
        "topic": "Từng phần múa cột",
        "difficulty": "Thông hiểu",
        "front_content": "Tính $I = \\int_0^1 (2x + 1)e^x \\, dx$.",
        "back_type": "Tích phân từng phần đa thức nhân hàm mũ",
        "back_strategy": "Múa cột: $D: 2x+1 \\to 2 \\to 0$; $I: e^x \\to e^x \\to e^x$. $I = [(2x - 1)e^x]_0^1 = e + 1$.",
        "back_pitfalls": "⚠️ Nhớ đan dấu $+ - +$.",
        "back_solution": "$I = [(2x+1)e^x - 2e^x]_0^1 = [(2x-1)e^x]_0^1 = e - (-1) = e + 1$.",
        "final_answer": "$e + 1$"
    },
    {
        "chapter_id": "c4",
        "chapter_name": "Chương 4: Nguyên hàm & Tích phân",
        "topic": "Diện tích Parabol",
        "difficulty": "Thông hiểu",
        "front_content": "Tính diện tích hình phẳng giới hạn bởi $y = -x^2 + 4x$ và trục hoành $Ox$.",
        "back_type": "Diện tích Parabol Archimedes",
        "back_strategy": "Nghiệm $x = 0, x = 4$. Đáy $= 4$, Chiều cao đỉnh $= 4$. $S = \\frac{2}{3} \\cdot 4 \\cdot 4 = \\frac{32}{3}$.",
        "back_pitfalls": "⚠️ Hoặc tính tích phân $\\int_0^4 (-x^2 + 4x)dx = [-\\frac{x^3}{3} + 2x^2]_0^4 = \\frac{32}{3}$.",
        "back_solution": "$S = \\int_0^4 (-x^2 + 4x) dx = \\frac{32}{3}$.",
        "final_answer": "$S = \\frac{32}{3}$"
    },
    {
        "chapter_id": "c4",
        "chapter_name": "Chương 4: Nguyên hàm & Tích phân",
        "topic": "Hàm ẩn vi phân",
        "difficulty": "Vận dụng cao",
        "front_content": "Cho $f(x) > 0, \\forall x \\in [0; 1]$ thỏa mãn $f'(x) + 2x f(x) = 0$ và $f(0) = 1$. Tính $f(1)$.",
        "back_type": "Phương trình vi phân cấp 1",
        "back_strategy": "$\\frac{f'(x)}{f(x)} = -2x \\implies \\ln f(x) = -x^2 + C \\implies f(x) = e^{-x^2}$. $f(1) = e^{-1}$.",
        "back_pitfalls": "⚠️ Chia cho $f(x)$ được vì $f(x) > 0$.",
        "back_solution": "$\\ln f(x) = -x^2 \\implies f(x) = e^{-x^2} \\implies f(1) = \\frac{1}{e}$.",
        "final_answer": "$f(1) = \\frac{1}{e} = e^{-1}$"
    },

    # --- CHƯƠNG 5 ---
    {
        "chapter_id": "c5",
        "chapter_name": "Chương 5: Phương pháp Oxyz",
        "topic": "Mặt phẳng đoạn chắn",
        "difficulty": "Nhận biết",
        "front_content": "Viết phương trình mặt phẳng đi qua $A(2;0;0), B(0;-3;0), C(0;0;4)$.",
        "back_type": "Phương trình mặt phẳng theo đoạn chắn",
        "back_strategy": "$\\frac{x}{a} + \\frac{y}{b} + \\frac{z}{c} = 1 \\implies \\frac{x}{2} + \\frac{y}{-3} + \\frac{z}{4} = 1$.",
        "back_pitfalls": "⚠️ Chú ý dấu âm ở $y$-intercept: $\\frac{y}{-3}$.",
        "back_solution": "$\\frac{x}{2} - \\frac{y}{3} + \\frac{z}{4} = 1 \\iff 6x - 4y + 3z - 12 = 0$.",
        "final_answer": "$\\frac{x}{2} - \\frac{y}{3} + \\frac{z}{4} = 1$"
    },
    {
        "chapter_id": "c5",
        "chapter_name": "Chương 5: Phương pháp Oxyz",
        "topic": "Vị trí 2 đường thẳng",
        "difficulty": "Thông hiểu",
        "front_content": "Hai đường thẳng $d_1(A, \\vec{u}_1)$ và $d_2(B, \\vec{u}_2)$ chéo nhau khi nào?",
        "back_type": "Điều kiện hai đường thẳng chéo nhau",
        "back_strategy": "$[\\vec{u}_1, \\vec{u}_2] \\cdot \\vec{AB} \\ne 0$ (tích hỗn tạp khác 0, tức 3 vectơ không đồng phẳng).",
        "back_pitfalls": "⚠️ Nếu $[\vec{u}_1, \vec{u}_2] \cdot \vec{AB} = 0$ và $[\vec{u}_1, \vec{u}_2] \ne \vec{0}$ thì 2 đường thẳng CẮT NHAU.",
        "back_solution": "$d_1$ và $d_2$ chéo nhau $\\iff [\\vec{u}_1, \\vec{u}_2] \\cdot \\vec{AB} \\ne 0$.",
        "final_answer": "$[\\vec{u}_1, \\vec{u}_2] \\cdot \\vec{AB} \\ne 0$"
    },
    {
        "chapter_id": "c5",
        "chapter_name": "Chương 5: Phương pháp Oxyz",
        "topic": "Khoảng cách 2 đường chéo",
        "difficulty": "Thông hiểu",
        "front_content": "Viết công thức khoảng cách giữa 2 đường thẳng chéo nhau $d_1(A, \\vec{u}_1)$ và $d_2(B, \\vec{u}_2)$.",
        "back_type": "Khoảng cách giữa hai đường thẳng chéo nhau",
        "back_strategy": "$d(d_1, d_2) = \\frac{|[\\vec{u}_1, \\vec{u}_2] \\cdot \\vec{AB}|}{|[\\vec{u}_1, \\vec{u}_2]|}$.",
        "back_pitfalls": "⚠️ Tử số là độ lớn vô hướng, mẫu số là độ dài vectơ.",
        "back_solution": "$d(d_1, d_2) = \\frac{|[\\vec{u}_1, \\vec{u}_2] \\cdot \\vec{AB}|}{|[\\vec{u}_1, \\vec{u}_2]|}$.",
        "final_answer": "$$d(d_1, d_2) = \\frac{|[\\vec{u}_1, \\vec{u}_2] \\cdot \\vec{AB}|}{|[\\vec{u}_1, \\vec{u}_2]|}$$"
    },
    {
        "chapter_id": "c5",
        "chapter_name": "Chương 5: Phương pháp Oxyz",
        "topic": "Tâm tỉ cự cực trị",
        "difficulty": "Vận dụng cao",
        "front_content": "Tìm $M \\in (P): x+y+z-6=0$ để $MA^2 + MB^2$ đạt GTNN với $A(1;2;1), B(-1;0;3)$.",
        "back_type": "Cực trị tổng bình phương bằng tâm tỉ cự",
        "back_strategy": "1. Trung điểm $I(0; 1; 2)$ của $AB$.\n2. $MA^2 + MB^2 = 2MI^2 + \\frac{AB^2}{2} \\implies$ GTNN khi $M$ là hình chiếu của $I$ lên $(P)$.\n3. Tìm hình chiếu $M(1; 2; 3)$.",
        "back_pitfalls": "⚠️ Luôn quy về $MI^2$ thông qua điểm tâm tỉ cự $I$.",
        "back_solution": "Đường thẳng qua $I(0;1;2)$ vuông góc $(P)$: $x=t, y=1+t, z=2+t$. Thế vào $(P): 3t - 3 = 0 \\implies t=1 \\implies M(1; 2; 3)$.",
        "final_answer": "$M(1; 2; 3)$"
    },

    # --- CHƯƠNG 6 ---
    {
        "chapter_id": "c6",
        "chapter_name": "Chương 6: Xác suất & Bayes",
        "topic": "Xác suất có điều kiện",
        "difficulty": "Nhận biết",
        "front_content": "Viết công thức định nghĩa xác suất có điều kiện $P(A|B)$ và công thức nhân xác suất.",
        "back_type": "Định nghĩa xác suất có điều kiện",
        "back_strategy": "$P(A|B) = \\frac{P(A \\cap B)}{P(B)}$ và $P(A \\cap B) = P(B)P(A|B)$.",
        "back_pitfalls": "⚠️ Điều kiện $P(B) > 0$.",
        "back_solution": "$P(A|B) = \\frac{P(A \\cap B)}{P(B)}$.",
        "final_answer": "$$P(A|B) = \\frac{P(A \\cap B)}{P(B)}$$"
    },
    {
        "chapter_id": "c6",
        "chapter_name": "Chương 6: Xác suất & Bayes",
        "topic": "Định lý Bayes",
        "difficulty": "Thông hiểu",
        "front_content": "Viết công thức định lý Bayes cho hệ đầy đủ $\\{B_1, \\dots, B_n\\}$.",
        "back_type": "Công thức Bayes",
        "back_strategy": "$P(B_k|A) = \\frac{P(B_k)P(A|B_k)}{\\sum_{i=1}^n P(B_i)P(A|B_i)}$.",
        "back_pitfalls": "⚠️ Hệ $\{B_i\}$ phải là hệ đầy đủ.",
        "back_solution": "$P(B_k|A) = \\frac{P(B_k)P(A|B_k)}{\\sum_{i=1}^n P(B_i)P(A|B_i)}$.",
        "final_answer": "$$P(B_k|A) = \\frac{P(B_k)P(A|B_k)}{\\sum_{i=1}^n P(B_i)P(A|B_i)}$$"
    },
    {
        "chapter_id": "c6",
        "chapter_name": "Chương 6: Xác suất & Bayes",
        "topic": "Xét nghiệm y tế Bayes",
        "difficulty": "Vận dụng cao",
        "front_content": "Tỷ lệ bệnh $0.1\\%$. Test nhạy $99\\%$, dương tính giả $2\\%$. Một người test DƯƠNG TÍNH, tính xác suất thực sự mắc bệnh.",
        "back_type": "Nghịch lý dương tính giả trong y tế",
        "back_strategy": "Bayes: $P(B|+) = \\frac{0.001(0.99)}{0.001(0.99) + 0.999(0.02)} = \\frac{0.00099}{0.02097} \\approx 4.72\\%$.",
        "back_pitfalls": "⚠️ Đừng nhầm lẫn giữa độ nhạy của test ($99\\%$) và xác suất có bệnh khi test dương tính ($4.72\\%$).",
        "back_solution": "$P(B|+) = \\frac{0.00099}{0.00099 + 0.01998} = \\frac{99}{2097} \\approx 4.72\\%$.",
        "final_answer": "$\\approx 4.72\\%$"
    }
]

for c in cards:
    cursor.execute("""
    INSERT INTO flashcards (
        chapter_id, chapter_name, topic, difficulty,
        front_content, back_type, back_strategy, back_pitfalls,
        back_solution, final_answer
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        c["chapter_id"], c["chapter_name"], c["topic"], c["difficulty"],
        c["front_content"], c["back_type"], c["back_strategy"], c["back_pitfalls"],
        c["back_solution"], c["final_answer"]
    ))

conn.commit()

# Export to JSON
cursor.execute("SELECT id, chapter_id, chapter_name, topic, difficulty, front_content, back_type, back_strategy, back_pitfalls, back_solution, final_answer FROM flashcards")
rows = cursor.fetchall()
export_data = []
for r in rows:
    export_data.append({
        "id": r[0],
        "chapter_id": r[1],
        "chapter_name": r[2],
        "topic": r[3],
        "difficulty": r[4],
        "front": r[5],
        "back_type": r[6],
        "back_strategy": r[7],
        "back_pitfalls": r[8],
        "back_solution": r[9],
        "final_answer": r[10]
    })

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(export_data, f, ensure_ascii=False, indent=2)

print(f"Populated {len(cards)} rich flashcards into SQLite database and exported JSON successfully!")
conn.close()
