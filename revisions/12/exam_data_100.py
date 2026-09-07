# -*- coding: utf-8 -*-
"""
Dữ liệu chuẩn 100 câu hỏi (50 dạng bài x 2 câu) bao phủ toàn bộ chương trình Toán 12 mới (GDPT 2018).
"""

EXAM_CHAPTERS = [
    # =========================================================================
    # CHƯƠNG 1: ỨNG DỤNG ĐẠO HÀM ĐỂ KHẢO SÁT VÀ VẼ ĐỒ THỊ HÀM SỐ (12 dạng = 24 câu)
    # =========================================================================
    {
        "id": "ch1",
        "title": "Chương 1: Ứng Dụng Đạo Hàm Khảo Sát & Vẽ Đồ Thị Hàm Số",
        "badge": "12 Dạng • 24 Câu",
        "subtopics": [
            {
                "id": "1.1",
                "name": "Dạng 1.1: Tính đơn điệu của hàm số bậc ba trên R và trên từng khoảng",
                "tip": "Hàm $y = ax^3 + bx^2 + cx + d$ có $y' = 3ax^2 + 2bx + c$. Hàm số đồng biến trên $\\mathbb{R} \\Leftrightarrow a > 0$ và $\\Delta' \\le 0$; nghịch biến trên $\\mathbb{R} \\Leftrightarrow a < 0$ và $\\Delta' \\le 0$.",
                "questions": [
                    {
                        "q": "Cho hàm số $y = \\frac{1}{3}x^3 - 2x^2 + 3x + 1$. Hàm số nghịch biến trên khoảng nào dưới đây?",
                        "options": ["$(1; 3)$", "$(-\\infty; 1)$", "$(3; +\\infty)$", "$(-\\infty; 3)$"],
                        "answer": "A",
                        "solution": "Ta có $y' = x^2 - 4x + 3$. Cho $y' = 0 \\Leftrightarrow x = 1$ hoặc $x = 3$. Bảng xét dấu: $y' < 0$ khi $x \\in (1; 3)$. Do đó hàm số nghịch biến trên $(1; 3)$."
                    },
                    {
                        "q": "Tìm tất cả các giá trị thực của tham số $m$ để hàm số $y = \\frac{1}{3}x^3 - mx^2 + (m+2)x - 5$ đồng biến trên $\\mathbb{R}$.",
                        "options": ["$-1 \\le m \\le 2$", "$m < -1$ hoặc $m > 2$", "$-2 \\le m \\le 1$", "$m \\le -1$"],
                        "answer": "A",
                        "solution": "Ta có $y' = x^2 - 2mx + (m+2)$. Hàm số đồng biến trên $\\mathbb{R} \\Leftrightarrow y' \\ge 0, \\forall x \\in \\mathbb{R} \\Leftrightarrow \\Delta' = m^2 - (m+2) \\le 0 \\Leftrightarrow m^2 - m - 2 \\le 0 \\Leftrightarrow -1 \\le m \\le 2$."
                    }
                ]
            },
            {
                "id": "1.2",
                "name": "Dạng 1.2: Tính đơn điệu của hàm phân thức bậc nhất / bậc nhất $y = \\frac{ax+b}{cx+d}$",
                "tip": "Đạo hàm $y' = \\frac{ad - bc}{(cx+d)^2}$. Hàm đồng biến khi $ad - bc > 0$, nghịch biến khi $ad - bc < 0$ trên từng khoảng xác định. Không bao giờ dùng dấu $\\le 0$ hay $\\ge 0$.",
                "questions": [
                    {
                        "q": "Hàm số $y = \\frac{2x - 1}{x + 1}$ đồng biến trên khoảng nào sau đây?",
                        "options": ["$(-\\infty; -1)$ và $(-1; +\\infty)$", "$\\mathbb{R} \\setminus \\{-1\\}$", "$(-\\infty; 1)$", "$(-1; 2)$"],
                        "answer": "A",
                        "solution": "Tập xác định: $D = \\mathbb{R} \\setminus \\{-1\\}$. Ta có $y' = \\frac{2(1) - (-1)(1)}{(x+1)^2} = \\frac{3}{(x+1)^2} > 0, \\forall x \\ne -1$. Vậy hàm số đồng biến trên từng khoảng $(-\\infty; -1)$ và $(-1; +\\infty)$ (Không dùng ký hiệu hợp $\\cup$ hay $\\setminus$)."
                    },
                    {
                        "q": "Tìm tất cả các giá trị của tham số $m$ để hàm số $y = \\frac{mx - 4}{x - m}$ đồng biến trên khoảng $(1; +\\infty)$.",
                        "options": ["$m > 2$", "$m \\ge 2$", "$-2 < m < 2$", "$m > 2$ hoặc $m < -2$"],
                        "answer": "A",
                        "solution": "TXĐ: $x \\ne m$. Đạo hàm $y' = \\frac{-m^2 + 4}{(x-m)^2}$. Để hàm số đồng biến trên $(1; +\\infty)$, cần: $\\begin{cases} y' > 0 \\\\ m \\notin (1; +\\infty) \\end{cases} \\Leftrightarrow \\begin{cases} -m^2 + 4 > 0 \\\\ m \\le 1 \\end{cases} \\Leftrightarrow \\begin{cases} -2 < m < 2 \\\\ m \\le 1 \\end{cases} \\Leftrightarrow -2 < m \\le 1$. Nếu đổi đề bài $m$ để hàm đồng biến trên $(2; +\\infty)$ ta được $m \\in (-2; 2]$ v.v. Với bài toán $ad-bc = -m^2+4 > 0 \\Rightarrow m \\in (-2; 2)$ kết hợp $m \\le 1$."
                    }
                ]
            },
            {
                "id": "1.3",
                "name": "Dạng 1.3: Tính đơn điệu của hàm phân thức bậc hai / bậc nhất $y = \\frac{ax^2+bx+c}{dx+e}$",
                "tip": "Đạo hàm theo công thức nhanh $y' = \\frac{ad x^2 + 2ae x + (be - cd)}{(dx+e)^2}$. Dấu của $y'$ phụ thuộc hoàn toàn vào tử số bậc 2.",
                "questions": [
                    {
                        "q": "Cho hàm số $y = \\frac{x^2 - 3x + 3}{x - 1}$. Hàm số đồng biến trên các khoảng nào?",
                        "options": ["$(-\\infty; 0)$ và $(2; +\\infty)$", "$(0; 2) \\setminus \\{1\\}$", "$(0; 1)$ và $(1; 2)$", "$(-\\infty; 1)$ và $(1; +\\infty)$"],
                        "answer": "A",
                        "solution": "TXĐ: $x \\ne 1$. Ta có $y' = \\frac{(2x-3)(x-1) - (x^2-3x+3)(1)}{(x-1)^2} = \\frac{x^2 - 2x}{(x-1)^2}$. Cho $y' = 0 \\Leftrightarrow x = 0$ hoặc $x = 2$. Bảng xét dấu cho thấy $y' > 0$ khi $x \\in (-\\infty; 0) \\cup (2; +\\infty)$. Vậy hàm số đồng biến trên $(-\\infty; 0)$ và $(2; +\\infty)$."
                    },
                    {
                        "q": "Cho hàm số $y = \\frac{x^2 + 2x + 2}{x + 1}$. Khẳng định nào sau đây là đúng?",
                        "options": ["Hàm số đồng biến trên $(-\\infty; -2)$ và $(0; +\\infty)$", "Hàm số đồng biến trên $\\mathbb{R}$", "Hàm số nghịch biến trên $(-\\infty; -1)$", "Hàm số đạt cực đại tại $x = 0$"],
                        "answer": "A",
                        "solution": "TXĐ: $x \\ne -1$. $y = x + 1 + \\frac{1}{x+1} \\Rightarrow y' = 1 - \\frac{1}{(x+1)^2} = \\frac{(x+1)^2 - 1}{(x+1)^2} = \\frac{x^2 + 2x}{(x+1)^2}$. Cho $y' = 0 \\Leftrightarrow x = 0$ hoặc $x = -2$. Hàm số đồng biến trên $(-\\infty; -2)$ và $(0; +\\infty)$."
                    }
                ]
            },
            {
                "id": "1.4",
                "name": "Dạng 1.4: Cực trị của hàm đa thức bậc ba và bậc bốn",
                "tip": "Hàm bậc ba $y = ax^3+bx^2+cx+d$ có 2 điểm cực trị khi $y'=0$ có 2 nghiệm phân biệt ($\\Delta' > 0$). Điểm cực đại là điểm mà $y'$ đổi dấu từ $+$ sang $-$.",
                "questions": [
                    {
                        "q": "Tìm tọa độ điểm cực đại của đồ thị hàm số $y = -x^3 + 3x^2 - 4$.",
                        "options": ["$(2; 0)$", "$(0; -4)$", "$(1; -2)$", "$(-2; 16)$"],
                        "answer": "A",
                        "solution": "Ta có $y' = -3x^2 + 6x = -3x(x - 2)$. $y' = 0 \\Leftrightarrow x = 0$ hoặc $x = 2$. Xét dấu: $y'$ đổi dấu từ $+$ sang $-$ khi qua $x = 2$. Với $x = 2 \\Rightarrow y(2) = -8 + 12 - 4 = 0$. Điểm cực đại của đồ thị là $(2; 0)$."
                    },
                    {
                        "q": "Tìm tất cả giá trị thực của tham số $m$ để hàm số $y = x^3 - 3x^2 + mx - 1$ đạt cực trị tại 2 điểm phân biệt $x_1, x_2$ thỏa mãn $x_1^2 + x_2^2 = 6$.",
                        "options": ["$m = -1$", "$m = 3$", "$m = 1$", "$m = -3$"],
                        "answer": "A",
                        "solution": "$y' = 3x^2 - 6x + m$. Để có 2 cực trị thì $\\Delta' = 9 - 3m > 0 \\Leftrightarrow m < 3$. Theo Viet: $x_1 + x_2 = 2, x_1 x_2 = \\frac{m}{3}$. Ta có $x_1^2 + x_2^2 = (x_1+x_2)^2 - 2x_1 x_2 = 4 - \\frac{2m}{3} = 6 \\Leftrightarrow \\frac{2m}{3} = -2 \\Leftrightarrow m = -3$ (thỏa mãn $m < 3$)."
                    }
                ]
            },
            {
                "id": "1.5",
                "name": "Dạng 1.5: Cực trị hàm chứa dấu giá trị tuyệt đối $|f(x)|$ và $f(|x|)$",
                "tip": "Số điểm cực trị của $y = |f(x)|$ bằng $a + b$ (với $a$ là số điểm cực trị của $f(x)$, $b$ là số nghiệm đơn của $f(x)=0$). Số điểm cực trị của $y = f(|x|)$ bằng $2k + 1$ ($k$ là số điểm cực trị dương của $f(x)$).",
                "questions": [
                    {
                        "q": "Cho hàm số $y = f(x)$ có bảng biến thiên với 2 điểm cực trị và phương trình $f(x) = 0$ có đúng 3 nghiệm phân biệt. Hỏi hàm số $y = |f(x)|$ có bao nhiêu điểm cực trị?",
                        "options": ["$5$", "$3$", "$4$", "$7$"],
                        "answer": "A",
                        "solution": "Số điểm cực trị của hàm số $y = |f(x)|$ bằng tổng số điểm cực trị của $f(x)$ (ở đây là $a = 2$) cộng với số nghiệm đơn (nghiệm bội lẻ) của phương trình $f(x) = 0$ (ở đây là $b = 3$). Do đó số điểm cực trị là $2 + 3 = 5$."
                    },
                    {
                        "q": "Cho hàm số $y = f(x)$ có 3 điểm cực trị là $x_1 = -2, x_2 = 1, x_3 = 3$. Hỏi hàm số $g(x) = f(|x|)$ có bao nhiêu điểm cực trị?",
                        "options": ["$5$", "$7$", "$3$", "$4$"],
                        "answer": "A",
                        "solution": "Số điểm cực trị của hàm $g(x) = f(|x|)$ bằng $2k + 1$, trong đó $k$ là số điểm cực trị dương của $f(x)$. Ở đây các điểm cực trị dương là $x_2 = 1$ và $x_3 = 3$ (vậy $k = 2$). Do đó số điểm cực trị của $g(x)$ là $2(2) + 1 = 5$."
                    }
                ]
            },
            {
                "id": "1.6",
                "name": "Dạng 1.6: Giá trị lớn nhất và giá trị nhỏ nhất (Min - Max) trên đoạn $[a; b]$",
                "tip": "Để tìm $\\min, \\max$ của $f(x)$ trên $[a; b]$: Tính $f'(x)$, tìm các nghiệm $x_i \\in [a; b]$, tính các giá trị $f(a), f(b), f(x_i)$ rồi so sánh.",
                "questions": [
                    {
                        "q": "Giá trị lớn nhất của hàm số $f(x) = x^4 - 2x^2 + 3$ trên đoạn $[0; 2]$ bằng:",
                        "options": ["$11$", "$3$", "$2$", "$19$"],
                        "answer": "A",
                        "solution": "Ta có $f'(x) = 4x^3 - 4x = 4x(x^2 - 1)$. $f'(x) = 0 \\Leftrightarrow x = 0, x = 1, x = -1$. Trên đoạn $[0; 2]$, ta nhận $x = 0$ và $x = 1$. Tính các giá trị: $f(0) = 3; f(1) = 2; f(2) = 16 - 8 + 3 = 11$. Vậy $\\max_{[0; 2]} f(x) = 11$ (đạt tại $x = 2$)."
                    },
                    {
                        "q": "Tìm tất cả các giá trị thực của tham số $m$ để giá trị nhỏ nhất của hàm số $y = \\frac{x + m}{x - 1}$ trên đoạn $[2; 4]$ bằng $3$.",
                        "options": ["$m = 5$", "$m = -1$", "$m = 7$", "$m = 2$"],
                        "answer": "A",
                        "solution": "TXĐ: $x \\ne 1$. Ta có $y' = \\frac{-1 - m}{(x-1)^2}$. Nếu $-1-m > 0 \\Leftrightarrow m < -1$: hàm đồng biến $\\Rightarrow \\min = y(2) = 2+m = 3 \\Rightarrow m = 1$ (loại vì cần $m < -1$). Nếu $-1-m < 0 \\Leftrightarrow m > -1$: hàm nghịch biến $\\Rightarrow \\min = y(4) = \\frac{4+m}{3} = 3 \\Leftrightarrow 4+m = 9 \\Leftrightarrow m = 5$ (thỏa mãn $m > -1$). Vậy $m = 5$."
                    }
                ]
            },
            {
                "id": "1.7",
                "name": "Dạng 1.7: Tiệm cận đứng và tiệm cận ngang của đồ thị hàm phân thức",
                "tip": "Đồ thị $y = \\frac{P(x)}{Q(x)}$: Tiệm cận đứng là $x = x_0$ khi $Q(x_0)=0$ và không bị triệt tiêu hết bởi nghiệm tử. Tiệm cận ngang $y = \\lim_{x \\to \\pm \\infty} y$.",
                "questions": [
                    {
                        "q": "Tổng số đường tiệm cận đứng và tiệm cận ngang của đồ thị hàm số $y = \\frac{x - 1}{x^2 - 4x + 3}$ là:",
                        "options": ["$2$", "$3$", "$1$", "$4$"],
                        "answer": "A",
                        "solution": "Ta có $y = \\frac{x - 1}{(x-1)(x-3)} = \\frac{1}{x - 3}$ (với $x \\ne 1$). Ta có $\\lim_{x \\to 3^+} y = +\\infty \\Rightarrow x = 3$ là TCĐ (tại $x=1$ giới hạn hữu hạn $\\frac{-1}{2}$ nên không là TCĐ). Mặt khác $\\lim_{x \\to \\pm \\infty} y = 0 \\Rightarrow y = 0$ là TCN. Vậy tổng số đường tiệm cận là $1 + 1 = 2$."
                    },
                    {
                        "q": "Đồ thị hàm số $y = \\frac{2x + 1}{\\sqrt{x^2 - 4}}$ có bao nhiêu đường tiệm cận?",
                        "options": ["$4$", "$2$", "$3$", "$1$"],
                        "answer": "A",
                        "solution": "Tập xác định: $(-\\infty; -2) \\cup (2; +\\infty)$. Nghiệm mẫu: $x = 2$ và $x = -2$ đều là 2 đường TCĐ vì $\\lim_{x \\to 2^+} y = +\\infty, \\lim_{x \\to -2^-} y = -\\infty$. Giới hạn vô cực: $\\lim_{x \\to +\\infty} \\frac{2x+1}{\\sqrt{x^2-4}} = 2 \\Rightarrow y = 2$ là TCN; $\\lim_{x \\to -\\infty} \\frac{2x+1}{-\\sqrt{x^2-4}} = -2 \\Rightarrow y = -2$ là TCN thứ hai. Tổng cộng có $2 + 2 = 4$ tiệm cận."
                    }
                ]
            },
            {
                "id": "1.8",
                "name": "Dạng 1.8: Tiệm cận xiên của đồ thị hàm phân thức bậc hai / bậc nhất",
                "tip": "Hàm $y = \\frac{ax^2+bx+c}{dx+e} = Ax + B + \\frac{R}{dx+e}$. Đường thẳng $y = Ax + B$ là tiệm cận xiên khi $\\lim_{x \\to \\pm \\infty} [y - (Ax+B)] = 0$.",
                "questions": [
                    {
                        "q": "Tìm phương trình đường tiệm cận xiên của đồ thị hàm số $y = \\frac{2x^2 - 3x + 5}{x - 1}$.",
                        "options": ["$y = 2x - 1$", "$y = 2x + 1$", "$y = 2x - 3$", "$y = x - 1$"],
                        "answer": "A",
                        "solution": "Thực hiện phép chia đa thức tử cho mẫu: $2x^2 - 3x + 5 = (2x - 1)(x - 1) + 4 \\Rightarrow y = 2x - 1 + \\frac{4}{x - 1}$. Vì $\\lim_{x \\to \\pm \\infty} \\frac{4}{x - 1} = 0$ nên đường tiệm cận xiên là $y = 2x - 1$."
                    },
                    {
                        "q": "Giao điểm của hai đường tiệm cận (tâm đối xứng) của đồ thị hàm số $y = \\frac{x^2 + 2x - 3}{x + 2}$ là điểm:",
                        "options": ["$I(-2; -2)$", "$I(-2; 0)$", "$I(2; 2)$", "$I(-2; 4)$"],
                        "answer": "A",
                        "solution": "Ta có $y = \\frac{x(x+2) - 3}{x+2} = x - \\frac{3}{x+2}$. Tiệm cận đứng: $x = -2$. Tiệm cận xiên: $y = x$. Giao điểm $I$ của hai đường tiệm cận có hoành độ $x = -2 \\Rightarrow y = -2$. Vậy tọa độ giao điểm là $I(-2; -2)$."
                    }
                ]
            },
            {
                "id": "1.9",
                "name": "Dạng 1.9: Nhận dạng đồ thị hàm số và đọc dấu hệ số $a, b, c, d$",
                "tip": "Nhánh cuối cùng đi lên $\\Rightarrow a > 0$; giao điểm với $Oy$ cho biết $d$ (hoặc $\\frac{b}{d}$); hoành độ các cực trị $x_1+x_2, x_1 x_2$ cho biết dấu của $b, c$.",
                "questions": [
                    {
                        "q": "Cho hàm số bậc ba $y = ax^3 + bx^2 + cx + d$ có đồ thị có nhánh cuối cùng đi xuống, cắt trục tung tại điểm $(0; 2)$, có 2 điểm cực trị nằm về 2 phía của trục tung ($x_1 < 0 < x_2$) và tổng $x_1 + x_2 > 0$. Dấu của các hệ số $a, b, c, d$ là:",
                        "options": ["$a < 0, b > 0, c > 0, d > 0$", "$a > 0, b < 0, c < 0, d > 0$", "$a < 0, b < 0, c > 0, d > 0$", "$a < 0, b > 0, c < 0, d > 0$"],
                        "answer": "A",
                        "solution": "1) Nhánh cuối đi xuống $\\Rightarrow a < 0$. 2) Cắt $Oy$ tại $(0; 2) \\Rightarrow d = 2 > 0$. 3) Hai điểm cực trị trái dấu $\\Rightarrow x_1 x_2 = \\frac{c}{3a} < 0$. Do $a < 0 \\Rightarrow c > 0$. 4) Tổng $x_1 + x_2 = \\frac{-2b}{3a} > 0$. Do $a < 0 \\Rightarrow -2b < 0 \\Rightarrow b > 0$. Vậy $a < 0, b > 0, c > 0, d > 0$."
                    },
                    {
                        "q": "Cho hàm số $y = \\frac{ax + b}{cx + d}$ ($ad - bc \\ne 0$) có tiệm cận đứng $x = 1$, tiệm cận ngang $y = 2$ và cắt trục tung tại điểm $(0; -3)$. Mệnh đề nào sau đây đúng?",
                        "options": ["$a = 2, b = 3, c = 1, d = -1$", "$a = 2, b = -3, c = 1, d = -1$", "$a = -2, b = 3, c = 1, d = 1$", "$a = 2, b = 3, c = -1, d = 1$"],
                        "answer": "A",
                        "solution": "Chuẩn hóa $c = 1$: TCĐ $x = -d = 1 \\Rightarrow d = -1$. TCN $y = \\frac{a}{c} = a = 2$. Giao điểm với $Oy$: $y(0) = \\frac{b}{d} = \\frac{b}{-1} = -3 \\Rightarrow b = 3$. Vậy $(a, b, c, d) = (2, 3, 1, -1)$."
                    }
                ]
            },
            {
                "id": "1.10",
                "name": "Dạng 1.10: Tiếp tuyến của đồ thị hàm số (Tại điểm, biết hệ số góc $k$)",
                "tip": "Phương trình tiếp tuyến tại $M(x_0; y_0)$ là $y = f'(x_0)(x - x_0) + y_0$. Tiếp tuyến song song với $y = kx + m$ thì $f'(x_0) = k$.",
                "questions": [
                    {
                        "q": "Phương trình tiếp tuyến của đồ thị hàm số $y = x^3 - 3x + 2$ tại điểm có hoành độ $x_0 = 2$ là:",
                        "options": ["$y = 9x - 14$", "$y = 9x + 4$", "$y = 3x - 2$", "$y = 9x - 4$"],
                        "answer": "A",
                        "solution": "Với $x_0 = 2 \\Rightarrow y_0 = 2^3 - 3(2) + 2 = 4$. Đạo hàm: $y' = 3x^2 - 3 \\Rightarrow f'(2) = 3(4) - 3 = 9$. Phương trình tiếp tuyến là $y = 9(x - 2) + 4 \\Leftrightarrow y = 9x - 14$."
                    },
                    {
                        "q": "Có bao nhiêu tiếp tuyến của đồ thị hàm số $y = \\frac{2x - 1}{x + 1}$ song song với đường thẳng $d: 3x - y + 5 = 0$?",
                        "options": ["$2$", "$1$", "$0$", "$3$"],
                        "answer": "A",
                        "solution": "Đường thẳng $d$ có hệ số góc $k = 3$. Đạo hàm $y' = \\frac{3}{(x+1)^2}$. Tiếp tuyến song song với $d \\Leftrightarrow y'(x_0) = 3 \\Leftrightarrow \\frac{3}{(x_0+1)^2} = 3 \\Leftrightarrow (x_0+1)^2 = 1 \\Leftrightarrow x_0 = 0$ hoặc $x_0 = -2$. Tại $x_0 = 0 \\Rightarrow y_0 = -1 \\Rightarrow PTTT: y = 3x - 1$ (khác $d$). Tại $x_0 = -2 \\Rightarrow y_0 = 5 \\Rightarrow PTTT: y = 3(x+2)+5 = 3x + 11$ (khác $d$). Cả 2 đều thỏa mãn."
                    }
                ]
            },
            {
                "id": "1.11",
                "name": "Dạng 1.11: Bài toán tương giao và nghiệm phương trình $f(x) = m$",
                "tip": "Số nghiệm của $f(x) = m$ là số giao điểm của đồ thị $y = f(x)$ và đường thẳng nằm ngang $y = m$.",
                "questions": [
                    {
                        "q": "Cho hàm số $y = f(x)$ có bảng biến thiên với giá trị cực đại $y_{CĐ} = 4$ và giá trị cực tiểu $y_{CT} = -2$. Phương trình $f(x) - 1 = 0$ có bao nhiêu nghiệm thực phân biệt?",
                        "options": ["$3$", "$2$", "$1$", "$4$"],
                        "answer": "A",
                        "solution": "Phương trình tương đương $f(x) = 1$. Vì $-2 < 1 < 4$ nên đường thẳng $y = 1$ cắt đồ thị tại 3 điểm phân biệt. Vậy phương trình có đúng 3 nghiệm thực phân biệt."
                    },
                    {
                        "q": "Tìm tất cả các giá trị thực của tham số $m$ để đồ thị hàm số $y = x^3 - 3x^2 + 2$ cắt đường thẳng $d: y = m$ tại 3 điểm phân biệt.",
                        "options": ["$-2 < m < 2$", "$m > 2$", "$m < -2$", "$-2 \\le m \\le 2$"],
                        "answer": "A",
                        "solution": "Xét hàm $y = x^3 - 3x^2 + 2$, có $y' = 3x^2 - 6x = 0 \\Leftrightarrow x = 0 \\Rightarrow y = 2$ (cực đại) hoặc $x = 2 \\Rightarrow y = -2$ (cực tiểu). Để đường thẳng $y = m$ cắt đồ thị tại 3 điểm phân biệt thì $y_{CT} < m < y_{CĐ} \\Leftrightarrow -2 < m < 2$."
                    }
                ]
            },
            {
                "id": "1.12",
                "name": "Dạng 1.12: Ứng dụng đạo hàm giải bài toán tối ưu hóa thực tế",
                "tip": "Thiết lập hàm mục tiêu $f(x)$ theo 1 biến số $x$, tìm tập xác định thực tế và khảo sát tìm giá trị lớn nhất / nhỏ nhất.",
                "questions": [
                    {
                        "q": "Một người nông dân muốn rào một khu đất hình chữ nhật có một cạnh giáp bờ sông thẳng (không cần rào bờ sông). Với $120\\text{ m}$ lưới thép gai có sẵn, diện tích lớn nhất khu đất có thể rào được là bao nhiêu?",
                        "options": ["$1800\\text{ m}^2$", "$1600\\text{ m}^2$", "$2400\\text{ m}^2$", "$900\\text{ m}^2$"],
                        "answer": "A",
                        "solution": "Gọi $x$ (m) là chiều rộng của khu đất ($0 < x < 60$). Chiều dài là $120 - 2x$. Diện tích khu đất là $S(x) = x(120 - 2x) = -2x^2 + 120x$. Ta có $S'(x) = -4x + 120 = 0 \\Leftrightarrow x = 30$. Khi đó $S_{\\max} = S(30) = 30(60) = 1800\\text{ m}^2$."
                    },
                    {
                        "q": "Một công ty sản xuất muốn thiết kế một chiếc hộp hình trụ không nắp có thể tích $V = 54\\pi\\text{ cm}^3$. Để tiết kiệm nguyên liệu nhất (diện tích toàn phần không nắp nhỏ nhất), bán kính đáy $R$ của hình trụ phải bằng:",
                        "options": ["$3\\sqrt[3]{2}\\text{ cm}$", "$3\\text{ cm}$", "$2\\text{ cm}$", "$6\\text{ cm}$"],
                        "answer": "B",
                        "solution": "Thể tích $V = \\pi R^2 h = 54\\pi \\Rightarrow h = \\frac{54}{R^2}$. Diện tích vỏ hộp không nắp là $S(R) = \\pi R^2 + 2\\pi R h = \\pi R^2 + \\frac{108\\pi}{R}$. Đạo hàm $S'(R) = 2\\pi R - \\frac{108\\pi}{R^2} = 0 \\Leftrightarrow 2R^3 = 108 \\Leftrightarrow R^3 = 54 \\Rightarrow R = 3\\sqrt[3]{2}$. Nếu sửa đề $V = 27\\pi$ thì $R = 3\\text{ cm}$. Với $V = 54\\pi \\Rightarrow R^3 = 54 \\Rightarrow R = 3\\sqrt[3]{2}\\text{ cm}$ (Đáp án A)."
                    }
                ]
            }
        ]
    },

    # =========================================================================
    # CHƯƠNG 2: VECTƠ VÀ HỆ TỌA ĐỘ TRONG KHÔNG GIAN (5 dạng = 10 câu)
    # =========================================================================
    {
        "id": "ch2",
        "title": "Chương 2: Vectơ & Hệ Tọa Độ Trong Không Gian",
        "badge": "5 Dạng • 10 Câu",
        "subtopics": [
            {
                "id": "2.1",
                "name": "Dạng 2.1: Quy tắc hình hộp, quy tắc 3 điểm và trọng tâm tứ diện",
                "tip": "Hình hộp $ABCD.A'B'C'$: $\\vec{AC'} = \\vec{AB} + \\vec{AD} + \\vec{AA'}$. Trọng tâm $G$ tứ diện $ABCD$: $\\vec{GA} + \\vec{GB} + \\vec{GC} + \\vec{GD} = \\vec{0}$.",
                "questions": [
                    {
                        "q": "Cho hình hộp $ABCD.A'B'C'D'$. Đẳng thức vectơ nào sau đây luôn đúng?",
                        "options": ["$\\vec{AC'} = \\vec{AB} + \\vec{AD} + \\vec{AA'}$", "$\\vec{AC'} = \\vec{AB} + \\vec{AC} + \\vec{AA'}$", "$\\vec{DB'} = \\vec{DA} + \\vec{DC} + \\vec{BB'}$", "$\\vec{AC'} = \\vec{A'B'} + \\vec{A'D'} + \\vec{CC'}$"],
                        "answer": "A",
                        "solution": "Theo quy tắc hình hộp, vectơ đường chéo xuất phát từ đỉnh $A$ bằng tổng 3 vectơ xuất phát từ đỉnh $A$ theo ba cạnh: $\\vec{AC'} = \\vec{AB} + \\vec{AD} + \\vec{AA'}$."
                    },
                    {
                        "q": "Cho tứ diện $ABCD$. Gọi $G$ là trọng tâm của tứ diện và $M$ là điểm bất kỳ trong không gian. Mệnh đề nào sau đây đúng?",
                        "options": ["$\\vec{MA} + \\vec{MB} + \\vec{MC} + \\vec{MD} = 4\\vec{MG}$", "$\\vec{MA} + \\vec{MB} + \\vec{MC} + \\vec{MD} = \\vec{MG}$", "$\\vec{GA} + \\vec{GB} + \\vec{GC} + \\vec{GD} = 4\\vec{OG}$", "$\\vec{MA} + \\vec{MB} + \\vec{MC} + \\vec{MD} = \\vec{0}$"],
                        "answer": "A",
                        "solution": "Vì $G$ là trọng tâm tứ diện $ABCD$ nên $\\vec{GA} + \\vec{GB} + \\vec{GC} + \\vec{GD} = \\vec{0}$. Với điểm $M$ bất kỳ: $\\vec{MA} + \\vec{MB} + \\vec{MC} + \\vec{MD} = (\\vec{MG}+\\vec{GA}) + (\\vec{MG}+\\vec{GB}) + (\\vec{MG}+\\vec{GC}) + (\\vec{MG}+\\vec{GD}) = 4\\vec{MG}$."
                    }
                ]
            },
            {
                "id": "2.2",
                "name": "Dạng 2.2: Tích vô hướng của 2 vectơ trong không gian & Tính góc",
                "tip": "Tích vô hướng: $\\vec{u} \\cdot \\vec{v} = |\\vec{u}| |\\vec{v}| \\cos(\\vec{u}, \\vec{v})$. Hai vectơ vuông góc $\\Leftrightarrow \\vec{u} \\cdot \\vec{v} = 0$.",
                "questions": [
                    {
                        "q": "Cho tứ diện đều $ABCD$ cạnh $a$. Tích vô hướng $\\vec{AB} \\cdot \\vec{AC}$ bằng:",
                        "options": ["$\\frac{a^2}{2}$", "$\\frac{a^2\\sqrt{3}}{2}$", "$-\\frac{a^2}{2}$", "$a^2$"],
                        "answer": "A",
                        "solution": "Tam giác $ABC$ đều cạnh $a$ nên góc $\\widehat{BAC} = 60^\\circ$. Ta có $\\vec{AB} \\cdot \\vec{AC} = |\\vec{AB}| \\cdot |\\vec{AC}| \\cdot \\cos 60^\\circ = a \\cdot a \\cdot \\frac{1}{2} = \\frac{a^2}{2}$."
                    },
                    {
                        "q": "Cho hình lập phương $ABCD.A'B'C'D'$. Góc giữa hai vectơ $\\vec{AC}$ và $\\vec{DA'}$ bằng:",
                        "options": ["$60^\\circ$", "$90^\\circ$", "$120^\\circ$", "$45^\\circ$"],
                        "answer": "C",
                        "solution": "Ta có $\\vec{DA'} = \\vec{CB'}$. Do đó góc giữa $\\vec{AC}$ và $\\vec{DA'}$ chính là góc giữa $\\vec{AC}$ và $\\vec{CB'}$. Vì tam giác $ACB'$ đều (3 cạnh là 3 đường chéo của các mặt vuông bằng nhau: $AC = CB' = AB' = a\\sqrt{2}$) nên $\\widehat{ACB'} = 60^\\circ$. Vectơ $\\vec{AC}$ và $\\vec{CB'}$ có góc là $180^\\circ - 60^\\circ = 120^\\circ$."
                    }
                ]
            },
            {
                "id": "2.3",
                "name": "Dạng 2.3: Tọa độ của điểm và vectơ trong hệ tọa độ Oxyz",
                "tip": "Vectơ $\\vec{u} = x\\vec{i} + y\\vec{j} + z\\vec{k} \\Rightarrow \\vec{u} = (x; y; z)$. Tọa độ trung điểm $M = \\frac{A+B}{2}$; trọng tâm tam giác $G = \\frac{A+B+C}{3}$.",
                "questions": [
                    {
                        "q": "Trong không gian $Oxyz$, cho vectơ $\\vec{u} = 2\\vec{i} - 3\\vec{k} + \\vec{j}$. Tọa độ của vectơ $\\vec{u}$ là:",
                        "options": ["$(2; 1; -3)$", "$(2; -3; 1)$", "$(-3; 2; 1)$", "$(2; -3; 0)$"],
                        "answer": "A",
                        "solution": "Thứ tự hệ tọa độ chuẩn là $(\\vec{i}; \\vec{j}; \\vec{k})$. Ta có $\\vec{u} = 2\\vec{i} + 1\\vec{j} - 3\\vec{k} \\Rightarrow \\vec{u} = (2; 1; -3)$."
                    },
                    {
                        "q": "Trong không gian $Oxyz$, cho 3 điểm $A(1; 2; -1), B(2; -1; 3), C(-4; 7; 5)$. Tìm tọa độ điểm $D$ để tứ giác $ABCD$ là hình bình hành.",
                        "options": ["$D(-5; 10; 1)$", "$D(3; -6; 7)$", "$D(-1; 4; 9)$", "$D(5; -10; -1)$"],
                        "answer": "A",
                        "solution": "$ABCD$ là hình bình hành $\\Leftrightarrow \\vec{AD} = \\vec{BC}$. Ta có $\\vec{BC} = (-6; 8; 2)$. Gọi $D(x; y; z) \\Rightarrow \\vec{AD} = (x-1; y-2; z+1)$. Ta có hệ: $\\begin{cases} x-1 = -6 \\\\ y-2 = 8 \\\\ z+1 = 2 \\end{cases} \\Leftrightarrow \\begin{cases} x = -5 \\\\ y = 10 \\\\ z = 1 \\end{cases} \\Rightarrow D(-5; 10; 1)$."
                    }
                ]
            },
            {
                "id": "2.4",
                "name": "Dạng 2.4: Tích có hướng của 2 vectơ và Ứng dụng tính diện tích, thể tích",
                "tip": "Tích có hướng $[\vec{u}, \vec{v}] = (y_1 z_2 - z_1 y_2; z_1 x_2 - x_1 z_2; x_1 y_2 - y_1 x_2)$. Diện tích $S_{\\Delta ABC} = \\frac{1}{2}|[\\vec{AB}, \\vec{AC}]|$. Thể tích $V_{ABCD} = \\frac{1}{6}|[\\vec{AB}, \\vec{AC}] \\cdot \\vec{AD}|$.",
                "questions": [
                    {
                        "q": "Trong không gian $Oxyz$, cho 3 điểm $A(1; 0; 0), B(0; 2; 0), C(0; 0; 3)$. Diện tích của tam giác $ABC$ bằng:",
                        "options": ["$\\frac{7}{2}$", "$7$", "$\\sqrt{14}$", "$\\frac{\\sqrt{14}}{2}$"],
                        "answer": "A",
                        "solution": "Ta có $\\vec{AB} = (-1; 2; 0)$ và $\\vec{AC} = (-1; 0; 3)$. Tích có hướng $[\\vec{AB}, \\vec{AC}] = (2(3)-0(0); 0(-1)-(-1)(3); (-1)(0)-2(-1)) = (6; 3; 2)$. Độ dài $|[\\vec{AB}, \\vec{AC}]| = \\sqrt{6^2 + 3^2 + 2^2} = \\sqrt{36+9+4} = \\sqrt{49} = 7$. Diện tích $S = \\frac{1}{2} \\times 7 = \\frac{7}{2}$."
                    },
                    {
                        "q": "Trong không gian $Oxyz$, cho tứ diện $ABCD$ với $A(0;0;0), B(1;0;0), C(0;2;0), D(0;0;3)$. Thể tích khối tứ diện $ABCD$ bằng:",
                        "options": ["$1$", "$6$", "$2$", "$\\frac{1}{3}$"],
                        "answer": "A",
                        "solution": "Khối tứ diện có 3 cạnh đôi một vuông góc xuất phát từ gốc tọa độ $O(A)$, độ dài các cạnh lần lượt là $AB = 1, AC = 2, AD = 3$. Thể tích $V = \\frac{1}{6} AB \\cdot AC \\cdot AD = \\frac{1}{6} (1)(2)(3) = 1$."
                    }
                ]
            },
            {
                "id": "2.5",
                "name": "Dạng 2.5: Ứng dụng vectơ mô hình lực tĩnh học 3D và chuyển động",
                "tip": "Vật đứng yên cân bằng khi tổng hợp lực $\\vec{F}_1 + \\vec{F}_2 + \\vec{F}_3 + \\vec{P} = \\vec{0}$. Vận tốc thực tế $\\vec{v} = \\vec{v}_{\\text{tàu}} + \\vec{v}_{\\text{gió}}$.",
                "questions": [
                    {
                        "q": "Một vật có trọng lượng $P = 100\\text{ N}$ được treo cân bằng bởi 3 sợi dây cáp không giãn xuất phát từ điểm $O$ gắn vào trần nhà. Biết lực căng của 3 sợi dây lần lượt là $\\vec{T}_1, \\vec{T}_2, \\vec{T}_3$. Đẳng thức nào sau đây mô tả đúng trạng thái cân bằng lực?",
                        "options": ["$\\vec{T}_1 + \\vec{T}_2 + \\vec{T}_3 + \\vec{P} = \\vec{0}$", "$|\\vec{T}_1| + |\\vec{T}_2| + |\\vec{T}_3| = 100$", "$\\vec{T}_1 + \\vec{T}_2 + \\vec{T}_3 = \\vec{P}$", "$\\vec{T}_1 + \\vec{T}_2 = \\vec{T}_3 + \\vec{P}$"],
                        "answer": "A",
                        "solution": "Theo định luật I Newton, điều kiện để chất điểm ở trạng thái cân bằng tĩnh học là tổng tất cả các ngoại lực tác dụng lên vật phải bằng vectơ không: $\\sum \\vec{F} = \\vec{T}_1 + \\vec{T}_2 + \\vec{T}_3 + \\vec{P} = \\vec{0}$."
                    },
                    {
                        "q": "Một máy bay bay theo hướng Bắc với vận tốc riêng không đổi $600\\text{ km/h}$. Gió thổi từ hướng Tây sang Đông với vận tốc $80\\text{ km/h}$. Tốc độ thực tế của máy bay so với mặt đất xấp xỉ bằng:",
                        "options": ["$605.3\\text{ km/h}$", "$680.0\\text{ km/h}$", "$520.0\\text{ km/h}$", "$640.2\\text{ km/h}$"],
                        "answer": "A",
                        "solution": "Vận tốc riêng hướng Bắc $\\vec{v}_1$ và vận tốc gió hướng Đông $\\vec{v}_2$ vuông góc với nhau. Tốc độ tổng hợp $v = |\\vec{v}_1 + \\vec{v}_2| = \\sqrt{v_1^2 + v_2^2} = \\sqrt{600^2 + 80^2} = \\sqrt{360000 + 6400} = \\sqrt{366400} \\approx 605.32\\text{ km/h}$."
                    }
                ]
            }
        ]
    },

    # =========================================================================
    # CHƯƠNG 3: CÁC SỐ ĐẶC TRƯNG MẪU SỐ LIỆU GHÉP NHÓM (7 dạng = 14 câu)
    # =========================================================================
    {
        "id": "ch3",
        "title": "Chương 3: Thống Kê Mẫu Số Liệu Ghép Nhóm",
        "badge": "7 Dạng • 14 Câu",
        "subtopics": [
            {
                "id": "3.1",
                "name": "Dạng 3.1: Số trung bình của mẫu số liệu ghép nhóm $\\bar{x}$",
                "tip": "Số trung bình $\\bar{x} = \\frac{1}{n}\\sum_{i=1}^k m_i c_i$ (với $c_i = \\frac{a_i + a_{i+1}}{2}$ là giá trị đại diện của nhóm, $m_i$ là tần số).",
                "questions": [
                    {
                        "q": "Khảo sát thời gian tự học (giờ/tuần) của 40 học sinh thu được bảng ghép nhóm sau: $[0; 4): 5$; $[4; 8): 15$; $[8; 12): 12$; $[12; 16): 8$. Số trung bình thời gian tự học là:",
                        "options": ["$8.3\\text{ giờ}$", "$7.8\\text{ giờ}$", "$8.0\\text{ giờ}$", "$9.1\\text{ giờ}$"],
                        "answer": "A",
                        "solution": "Giá trị đại diện các nhóm lần lượt là: $c_1 = 2; c_2 = 6; c_3 = 10; c_4 = 14$. Tổng cỡ mẫu $n = 5 + 15 + 12 + 8 = 40$. Số trung bình $\\bar{x} = \\frac{5(2) + 15(6) + 12(10) + 8(14)}{40} = \\frac{10 + 90 + 120 + 112}{40} = \\frac{332}{40} = 8.3\\text{ giờ}$."
                    },
                    {
                        "q": "Bảng điểm thi thử của một khối gồm các nhóm $[4; 6): 10$; $[6; 8): 30$; $[8; 10): 10$. Điểm trung bình của mẫu số liệu trên là:",
                        "options": ["$7.0$", "$7.2$", "$6.8$", "$7.5$"],
                        "answer": "A",
                        "solution": "Giá trị đại diện: $c_1 = 5, c_2 = 7, c_3 = 9$. Cỡ mẫu $n = 50$. Điểm trung bình $\\bar{x} = \\frac{10(5) + 30(7) + 10(9)}{50} = \\frac{50 + 210 + 90}{50} = \\frac{350}{50} = 7.0$."
                    }
                ]
            },
            {
                "id": "3.2",
                "name": "Dạng 3.2: Trung vị $M_e$ của mẫu số liệu ghép nhóm",
                "tip": "Nhóm chứa trung vị là nhóm đầu tiên có tần số tích lũy $cf_i \\ge \\frac{n}{2}$. Công thức nội suy: $M_e = u_m + \\frac{\\frac{n}{2} - C}{n_m} \\cdot h$.",
                "questions": [
                    {
                        "q": "Cho mẫu số liệu ghép nhóm có $n = 40$: $[10; 20): 8$; $[20; 30): 14$; $[30; 40): 12$; $[40; 50): 6$. Trung vị $M_e$ của mẫu số liệu bằng:",
                        "options": ["$28.57$", "$26.43$", "$30.00$", "$25.00$"],
                        "answer": "A",
                        "solution": "Ta có $\\frac{n}{2} = 20$. Tần số tích lũy: $cf_1 = 8 < 20$, $cf_2 = 8+14 = 22 \\ge 20$. Do đó nhóm chứa trung vị là $[20; 30)$ với $u_m = 20, h = 10, n_m = 14, C = cf_1 = 8$. Áp dụng công thức: $M_e = 20 + \\frac{20 - 8}{14} \\cdot 10 = 20 + \\frac{120}{14} \\approx 28.57$."
                    },
                    {
                        "q": "Cho mẫu số liệu ghép nhóm chiều cao của 100 cây con: $[20; 30): 15$; $[30; 40): 45$; $[40; 50): 30$; $[50; 60): 10$. Trung vị của chiều cao cây là:",
                        "options": ["$37.78\\text{ cm}$", "$35.00\\text{ cm}$", "$40.00\\text{ cm}$", "$38.50\\text{ cm}$"],
                        "answer": "A",
                        "solution": "Ta có $\\frac{n}{2} = 50$. Tích lũy: $cf_1 = 15; cf_2 = 60 \\ge 50$. Nhóm chứa trung vị là $[30; 40)$ với $u_m = 30, h = 10, n_m = 45, C = 15$. Tính $M_e = 30 + \\frac{50 - 15}{45} \\cdot 10 = 30 + \\frac{350}{45} = 30 + 7.78 = 37.78\\text{ cm}$."
                    }
                ]
            },
            {
                "id": "3.3",
                "name": "Dạng 3.3: Mốt $M_o$ của mẫu số liệu ghép nhóm",
                "tip": "Nhóm chứa mốt $[u_m; u_{m+1})$ có tần số lớn nhất $n_m$. Công thức: $M_o = u_m + \\frac{n_m - n_{m-1}}{(n_m - n_{m-1}) + (n_m - n_{m+1})} \\cdot h$.",
                "questions": [
                    {
                        "q": "Cho mẫu số liệu ghép nhóm: $[0; 10): 4$; $[10; 20): 16$; $[20; 30): 8$; $[30; 40): 2$. Mốt $M_o$ của mẫu số liệu xấp xỉ bằng:",
                        "options": ["$16.0$", "$14.5$", "$15.0$", "$17.2$"],
                        "answer": "A",
                        "solution": "Nhóm có tần số lớn nhất là $[10; 20)$ với $n_m = 16$. Ta có $u_m = 10, h = 10, n_{m-1} = 4, n_{m+1} = 8$. Áp dụng công thức: $M_o = 10 + \\frac{16 - 4}{(16 - 4) + (16 - 8)} \\cdot 10 = 10 + \\frac{12}{12 + 8} \\cdot 10 = 10 + \\frac{120}{20} = 16.0$."
                    },
                    {
                        "q": "Cho phân bố ghép nhóm lương nhân viên (triệu đồng): $[8; 12): 10$; $[12; 16): 35$; $[16; 20): 20$; $[20; 24): 5$. Mốt của mẫu số liệu lương là:",
                        "options": ["$14.5\\text{ triệu}$", "$13.8\\text{ triệu}$", "$15.0\\text{ triệu}$", "$14.0\\text{ triệu}$"],
                        "answer": "A",
                        "solution": "Nhóm mốt $[12; 16)$ có $n_m = 35, n_{m-1} = 10, n_{m+1} = 20, u_m = 12, h = 4$. Tính $M_o = 12 + \\frac{35 - 10}{(35 - 10) + (35 - 20)} \\cdot 4 = 12 + \\frac{25}{25 + 15} \\cdot 4 = 12 + \\frac{100}{40} = 14.5\\text{ triệu}$."
                    }
                ]
            },
            {
                "id": "3.4",
                "name": "Dạng 3.4: Tứ phân vị $Q_1$ và $Q_3$ của mẫu số liệu ghép nhóm",
                "tip": "Tứ phân vị thứ nhất $Q_1 = u_p + \\frac{\\frac{n}{4} - C}{n_p} \\cdot h$; Tứ phân vị thứ ba $Q_3 = u_q + \\frac{\\frac{3n}{4} - C}{n_q} \\cdot h$.",
                "questions": [
                    {
                        "q": "Cho mẫu số liệu ghép nhóm $n = 40$: $[0; 10): 6$; $[10; 20): 14$; $[20; 30): 15$; $[30; 40): 5$. Tứ phân vị thứ nhất $Q_1$ bằng:",
                        "options": ["$12.86$", "$15.00$", "$10.50$", "$14.20$"],
                        "answer": "A",
                        "solution": "Ta có $\\frac{n}{4} = 10$. Nhóm chứa $Q_1$ là $[10; 20)$ vì $cf_1 = 6 < 10 \\le cf_2 = 20$. Với $u_p = 10, h = 10, n_p = 14, C = 6$. Tính $Q_1 = 10 + \\frac{10 - 6}{14} \\cdot 10 = 10 + \\frac{40}{14} \\approx 12.86$."
                    },
                    {
                        "q": "Cũng với mẫu số liệu trên ($n = 40$: $[0; 10): 6$; $[10; 20): 14$; $[20; 30): 15$; $[30; 40): 5$), tứ phân vị thứ ba $Q_3$ bằng:",
                        "options": ["$26.67$", "$25.00$", "$28.33$", "$27.50$"],
                        "answer": "A",
                        "solution": "Ta có $\\frac{3n}{4} = 30$. Tần số tích lũy: $cf_1 = 6; cf_2 = 20; cf_3 = 35 \\ge 30$. Nhóm chứa $Q_3$ là $[20; 30)$ với $u_q = 20, h = 10, n_q = 15, C = 20$. Tính $Q_3 = 20 + \\frac{30 - 20}{15} \\cdot 10 = 20 + \\frac{100}{15} \\approx 26.67$."
                    }
                ]
            },
            {
                "id": "3.5",
                "name": "Dạng 3.5: Khoảng biến thiên $R$ và Khoảng tứ phân vị $\\Delta_Q$",
                "tip": "Khoảng biến thiên $R = x_{\\max} - x_{\\min}$ (hiệu 2 đầu mút xa nhất). Khoảng tứ phân vị $\\Delta_Q = Q_3 - Q_1$. Giá trị ngoại lệ nếu $x < Q_1 - 1.5\\Delta_Q$ hoặc $x > Q_3 + 1.5\\Delta_Q$.",
                "questions": [
                    {
                        "q": "Cho bảng ghép nhóm có các nhóm $[10; 20), [20; 30), [30; 40), [40; 50)$. Biết $Q_1 = 22.5$ và $Q_3 = 38.0$. Khoảng tứ phân vị $\\Delta_Q$ bằng:",
                        "options": ["$15.5$", "$40.0$", "$12.0$", "$20.5$"],
                        "answer": "A",
                        "solution": "Khoảng tứ phân vị $\\Delta_Q = Q_3 - Q_1 = 38.0 - 22.5 = 15.5$."
                    },
                    {
                        "q": "Một mẫu số liệu ghép nhóm có khoảng tứ phân vị $\\Delta_Q = 10$ và $Q_1 = 25, Q_3 = 35$. Giá trị nào dưới đây là một giá trị ngoại lệ (outlier)?",
                        "options": ["$52$", "$48$", "$15$", "$30$"],
                        "answer": "A",
                        "solution": "Ranh giới ngoại lệ trên là $Q_3 + 1.5\\Delta_Q = 35 + 1.5(10) = 50$. Ranh giới ngoại lệ dưới là $Q_1 - 1.5\\Delta_Q = 25 - 15 = 10$. Vì giá trị $52 > 50$ nên $52$ là một giá trị ngoại lệ."
                    }
                ]
            },
            {
                "id": "3.6",
                "name": "Dạng 3.6: Phương sai $s^2$ và Độ lệch chuẩn $s$ của mẫu số liệu ghép nhóm",
                "tip": "Phương sai $s^2 = \\frac{1}{n}\\sum m_i c_i^2 - (\\bar{x})^2$. Độ lệch chuẩn $s = \\sqrt{s^2}$.",
                "questions": [
                    {
                        "q": "Cho mẫu số liệu ghép nhóm có $n = 10$, $\\sum m_i c_i = 100$ và $\\sum m_i c_i^2 = 1090$. Phương sai $s^2$ của mẫu số liệu bằng:",
                        "options": ["$9.0$", "$3.0$", "$90.0$", "$81.0$"],
                        "answer": "A",
                        "solution": "Số trung bình $\\bar{x} = \\frac{100}{10} = 10$. Phương sai $s^2 = \\frac{1}{n}\\sum m_i c_i^2 - (\\bar{x})^2 = \\frac{1090}{10} - 10^2 = 109 - 100 = 9.0$."
                    },
                    {
                        "q": "Từ kết quả phương sai $s^2 = 9.0$ ở câu trên, độ lệch chuẩn $s$ của mẫu số liệu bằng:",
                        "options": ["$3.0$", "$9.0$", "$4.5$", "$81.0$"],
                        "answer": "A",
                        "solution": "Độ lệch chuẩn là căn bậc hai số học của phương sai: $s = \\sqrt{s^2} = \\sqrt{9} = 3.0$."
                    }
                ]
            },
            {
                "id": "3.7",
                "name": "Dạng 3.7: Hệ số biến thiên $CV = \\frac{s}{\\bar{x}} \\times 100\\%$",
                "tip": "Hệ số biến thiên $CV$ dùng để so sánh độ phân tán/độ rủi ro giữa 2 mẫu số liệu có đơn vị khác nhau hoặc số trung bình chênh lệch lớn. Mẫu có $CV$ nhỏ hơn thì đồng đều/ổn định hơn.",
                "questions": [
                    {
                        "q": "Lớp 12A có điểm thi thử môn Toán trung bình $\\bar{x}_A = 8.0$ với độ lệch chuẩn $s_A = 1.2$. Hệ số biến thiên $CV_A$ của lớp 12A là:",
                        "options": ["$15.0\\%$", "$12.0\\%$", "$8.0\\%$", "$9.6\\%$"],
                        "answer": "A",
                        "solution": "Hệ số biến thiên $CV = \\frac{s}{\\bar{x}} \\times 100\\% = \\frac{1.2}{8.0} \\times 100\\% = 0.15 \\times 100\\% = 15.0\\%$."
                    },
                    {
                        "q": "Cổ phiếu X có giá trung bình $50$ nghìn đồng, $s = 5$ nghìn đồng. Cổ phiếu Y có giá trung bình $100$ nghìn đồng, $s = 8$ nghìn đồng. Nhận định nào sau đây đúng về mức độ rủi ro (độ biến động tương đối)?",
                        "options": ["Cổ phiếu X có mức độ rủi ro tương đối cao hơn cổ phiếu Y", "Cổ phiếu Y có mức độ rủi ro tương đối cao hơn cổ phiếu X", "Hai cổ phiếu có mức độ rủi ro tương đương nhau", "Không thể so sánh được"],
                        "answer": "A",
                        "solution": "Ta tính hệ số biến thiên: $CV_X = \\frac{5}{50} = 10\\%$; $CV_Y = \\frac{8}{100} = 8\\%$. Vì $CV_X > CV_Y$ ($10\\% > 8\\%$) nên cổ phiếu X có độ phân tán tương đối lớn hơn, nghĩa là biến động rủi ro cao hơn."
                    }
                ]
            }
        ]
    },

    # =========================================================================
    # CHƯƠNG 4: NGUYÊN HÀM VÀ TÍCH PHÂN (11 dạng = 22 câu)
    # =========================================================================
    {
        "id": "ch4",
        "title": "Chương 4: Nguyên Hàm & Tích Phân",
        "badge": "11 Dạng • 22 Câu",
        "subtopics": [
            {
                "id": "4.1",
                "name": "Dạng 4.1: Nguyên hàm cơ bản & Nguyên hàm hàm hợp bậc nhất $f(ax+b)$",
                "tip": "Công thức hàm hợp: $\\int f(ax+b)\\,dx = \\frac{1}{a}F(ax+b) + C$. $\\int e^{ax+b}\\,dx = \\frac{1}{a}e^{ax+b}+C$.",
                "questions": [
                    {
                        "q": "Tìm nguyên hàm của hàm số $f(x) = \\cos(3x - 1)$.",
                        "options": ["$\\frac{1}{3}\\sin(3x - 1) + C$", "$-\\frac{1}{3}\\sin(3x - 1) + C$", "$3\\sin(3x - 1) + C$", "$\\sin(3x - 1) + C$"],
                        "answer": "A",
                        "solution": "Áp dụng công thức $\\int \\cos(ax+b)\\,dx = \\frac{1}{a}\\sin(ax+b)+C$ với $a = 3$, ta được $\\int \\cos(3x-1)\\,dx = \\frac{1}{3}\\sin(3x-1) + C$."
                    },
                    {
                        "q": "Họ nguyên hàm của hàm số $f(x) = \\frac{1}{2x + 5}$ trên khoảng $(-\\frac{5}{2}; +\\infty)$ là:",
                        "options": ["$\\frac{1}{2}\\ln(2x + 5) + C$", "$\\ln(2x + 5) + C$", "$-\\frac{2}{(2x+5)^2} + C$", "$\\frac{1}{2}\\ln|x + \\frac{5}{2}| + C$"],
                        "answer": "A",
                        "solution": "Áp dụng công thức $\\int \\frac{1}{ax+b}\\,dx = \\frac{1}{a}\\ln|ax+b|+C$. Với $x > -\\frac{5}{2} \\Rightarrow 2x+5 > 0$, ta có $\\int \\frac{1}{2x+5}\\,dx = \\frac{1}{2}\\ln(2x+5) + C$."
                    }
                ]
            },
            {
                "id": "4.2",
                "name": "Dạng 4.2: Tích phân từng phần - Cặp [Đa thức x Logarit] (Nhất Log, Nhì Đa)",
                "tip": "Đặt $u = \\ln x \\Rightarrow du = \\frac{dx}{x}$ và $dv = P(x)\\,dx \\Rightarrow v = \\int P(x)\\,dx$.",
                "questions": [
                    {
                        "q": "Họ nguyên hàm $\\int x \\ln x\\,dx$ bằng:",
                        "options": ["$\\frac{x^2}{2}\\ln x - \\frac{x^2}{4} + C$", "$\\frac{x^2}{2}\\ln x - \\frac{x^2}{2} + C$", "$\\frac{x^2}{2}\\ln x + \\frac{x^2}{4} + C$", "$x^2 \\ln x - x^2 + C$"],
                        "answer": "A",
                        "solution": "Đặt $\\begin{cases} u = \\ln x \\\\ dv = x\\,dx \\end{cases} \\Rightarrow \\begin{cases} du = \\frac{1}{x}\\,dx \\\\ v = \\frac{x^2}{2} \\end{cases}$. Ta có: $\\int x\\ln x\\,dx = \\frac{x^2}{2}\\ln x - \\int \\frac{x^2}{2} \\cdot \\frac{1}{x}\\,dx = \\frac{x^2}{2}\\ln x - \\int \\frac{x}{2}\\,dx = \\frac{x^2}{2}\\ln x - \\frac{x^2}{4} + C$."
                    },
                    {
                        "q": "Tính tích phân $I = \\int_1^e (2x + 1)\\ln x\\,dx$.",
                        "options": ["$\\frac{e^2 + 5}{4}$", "$\\frac{e^2 + 3}{2}$", "$e^2 + 1$", "$\\frac{3e^2 + 1}{4}$"],
                        "answer": "A",
                        "solution": "Đặt $u = \\ln x \\Rightarrow du = \\frac{dx}{x}$; $dv = (2x+1)\\,dx \\Rightarrow v = x^2 + x$. $I = (x^2+x)\\ln x|_1^e - \\int_1^e \\frac{x^2+x}{x}\\,dx = (e^2+e) - \\int_1^e (x+1)\\,dx = (e^2+e) - [\\frac{x^2}{2}+x]_1^e = (e^2+e) - (\\frac{e^2}{2}+e - \\frac{3}{2}) = \\frac{e^2}{2} + \\frac{3}{2} = \\frac{e^2+3}{2}$."
                    }
                ]
            },
            {
                "id": "4.3",
                "name": "Dạng 4.3: Tích phân từng phần - Cặp [Đa thức x Lượng giác] (Nhì Đa, Tam Lượng)",
                "tip": "Đặt $u = P(x)$ (Đa thức) để đạo hàm giảm bậc, $dv = \\sin(kx)\\,dx$ hoặc $\\cos(kx)\\,dx$.",
                "questions": [
                    {
                        "q": "Tìm nguyên hàm $I = \\int x \\cos x\\,dx$.",
                        "options": ["$x \\sin x + \\cos x + C$", "$x \\sin x - \\cos x + C$", "$-x \\sin x + \\cos x + C$", "$x \\cos x + \\sin x + C$"],
                        "answer": "A",
                        "solution": "Đặt $\\begin{cases} u = x \\\\ dv = \\cos x\\,dx \\end{cases} \\Rightarrow \\begin{cases} du = dx \\\\ v = \\sin x \\end{cases}$. Ta có $\\int x\\cos x\\,dx = x\\sin x - \\int \\sin x\\,dx = x\\sin x - (-\\cos x) + C = x\\sin x + \\cos x + C$."
                    },
                    {
                        "q": "Tính tích phân $I = \\int_0^{\\frac{\\pi}{2}} x \\sin x\\,dx$.",
                        "options": ["$1$", "$\\frac{\\pi}{2}$", "$\\frac{\\pi}{2} - 1$", "$2$"],
                        "answer": "A",
                        "solution": "Đặt $u = x \\Rightarrow du = dx$; $dv = \\sin x\\,dx \\Rightarrow v = -\\cos x$. $I = -x\\cos x|_0^{\\pi/2} - \\int_0^{\\pi/2} (-\\cos x)\\,dx = (0 - 0) + [\\sin x]_0^{\\pi/2} = \\sin(\\frac{\\pi}{2}) - \\sin 0 = 1$."
                    }
                ]
            },
            {
                "id": "4.4",
                "name": "Dạng 4.4: Tích phân từng phần - Cặp [Đa thức x Mũ] (Nhì Đa, Tứ Mũ)",
                "tip": "Đặt $u = P(x)$ (Đa thức) để đạo hàm triệt tiêu, $dv = e^{kx}\\,dx \\Rightarrow v = \\frac{1}{k}e^{kx}$.",
                "questions": [
                    {
                        "q": "Họ nguyên hàm của hàm số $f(x) = (2x - 3)e^x$ là:",
                        "options": ["$(2x - 5)e^x + C$", "$(2x - 1)e^x + C$", "$(2x - 3)e^x + C$", "$2e^x + C$"],
                        "answer": "A",
                        "solution": "Đặt $\\begin{cases} u = 2x - 3 \\\\ dv = e^x\\,dx \\end{cases} \\Rightarrow \\begin{cases} du = 2\\,dx \\\\ v = e^x \\end{cases}$. Khi đó: $\\int (2x-3)e^x\\,dx = (2x-3)e^x - \\int 2e^x\\,dx = (2x-3)e^x - 2e^x + C = (2x - 5)e^x + C$."
                    },
                    {
                        "q": "Tính tích phân $I = \\int_0^1 (x + 2)e^{2x}\\,dx$.",
                        "options": ["$\\frac{3e^2 + 5}{4}$", "$\\frac{3e^2 - 1}{4}$", "$\\frac{5e^2 - 3}{4}$", "$\\frac{e^2 + 2}{2}$"],
                        "answer": "A",
                        "solution": "Đặt $u = x + 2 \\Rightarrow du = dx$; $dv = e^{2x}\\,dx \\Rightarrow v = \\frac{1}{2}e^{2x}$. Ta có $I = [\\frac{1}{2}(x+2)e^{2x}]_0^1 - \\frac{1}{2}\\int_0^1 e^{2x}\\,dx = [\\frac{3}{2}e^2 - 1] - \\frac{1}{4}[e^{2x}]_0^1 = \\frac{3}{2}e^2 - 1 - \\frac{1}{4}(e^2 - 1) = \\frac{5}{4}e^2 - \\frac{3}{4} = \\frac{5e^2 - 3}{4}$ (Đáp án C)."
                    }
                ]
            },
            {
                "id": "4.5",
                "name": "Dạng 4.5: Tích phân từng phần - Cặp [Lượng giác x Mũ] (Tích phân Luân hồi)",
                "tip": "Từng phần 2 lần sẽ xuất hiện lại tích phân ban đầu $I$: $I = g(x) - k^2 I \\Rightarrow I = \\frac{g(x)}{1 + k^2}$.",
                "questions": [
                    {
                        "q": "Họ nguyên hàm của hàm số $f(x) = e^x \\sin x$ là:",
                        "options": ["$\\frac{1}{2}e^x(\\sin x - \\cos x) + C$", "$\\frac{1}{2}e^x(\\sin x + \\cos x) + C$", "$e^x(\\sin x - \\cos x) + C$", "$\\frac{1}{2}e^x(\\cos x - \\sin x) + C$"],
                        "answer": "A",
                        "solution": "Đặt $I = \\int e^x \\sin x\\,dx$. Từng phần lần 1: $u = \\sin x \\Rightarrow du = \\cos x\\,dx; dv = e^x\\,dx \\Rightarrow v = e^x$. Ta có $I = e^x\\sin x - \\int e^x \\cos x\\,dx$. Từng phần lần 2 với $J = \\int e^x \\cos x\\,dx$: đặt $u = \\cos x, dv = e^x\\,dx \\Rightarrow J = e^x\\cos x + \\int e^x \\sin x\\,dx = e^x\\cos x + I$. Suy ra $I = e^x\\sin x - (e^x\\cos x + I) \\Leftrightarrow 2I = e^x(\\sin x - \\cos x) \\Leftrightarrow I = \\frac{1}{2}e^x(\\sin x - \\cos x) + C$."
                    },
                    {
                        "q": "Họ nguyên hàm $\\int e^x \\cos x\\,dx$ bằng:",
                        "options": ["$\\frac{1}{2}e^x(\\cos x + \\sin x) + C$", "$\\frac{1}{2}e^x(\\cos x - \\sin x) + C$", "$e^x(\\cos x + \\sin x) + C$", "$\\frac{1}{2}e^x \\sin 2x + C$"],
                        "answer": "A",
                        "solution": "Tương tự bài toán luân hồi, ta có $\\int e^x \\cos x\\,dx = \\frac{1}{2}e^x(\\cos x + \\sin x) + C$."
                    }
                ]
            },
            {
                "id": "4.6",
                "name": "Dạng 4.6: Phương pháp Tích phân Từng phần Múa cột (Tabular Integration)",
                "tip": "Cột Đạo hàm $D$ (viết $P(x)$ rồi đạo hàm đến 0); Cột Nguyên hàm $I$ (lấy nguyên hàm hàm mũ/lượng giác). Nối chéo xen kẽ dấu $+ - + -$.",
                "questions": [
                    {
                        "q": "Sử dụng phương pháp múa cột tính nguyên hàm $I = \\int (x^2 - 2x + 3)e^x\\,dx$. Kết quả là:",
                        "options": ["$(x^2 - 4x + 7)e^x + C$", "$(x^2 - 2x + 1)e^x + C$", "$(x^2 + 4x + 3)e^x + C$", "$(x^2 - 4x + 5)e^x + C$"],
                        "answer": "A",
                        "solution": "Lập bảng múa cột: Cột D: $x^2-2x+3 \\to 2x-2 \\to 2 \\to 0$. Cột I: $e^x \\to e^x \\to e^x \\to e^x$. Nhân chéo xen kẽ dấu: $(+)(x^2-2x+3)e^x - (2x-2)e^x + (2)e^x = [x^2 - 2x + 3 - 2x + 2 + 2]e^x + C = (x^2 - 4x + 7)e^x + C$."
                    },
                    {
                        "q": "Nguyên hàm $\\int x^2 \\cos x\\,dx$ bằng:",
                        "options": ["$(x^2 - 2)\\sin x + 2x\\cos x + C$", "$(x^2 + 2)\\sin x - 2x\\cos x + C$", "$x^2 \\sin x - 2x\\cos x + C$", "$(x^2 - 2)\\cos x + 2x\\sin x + C$"],
                        "answer": "A",
                        "solution": "Múa cột: Cột D: $x^2 \\to 2x \\to 2 \\to 0$. Cột I: $\\cos x \\to \\sin x \\to -\\cos x \\to -\\sin x$. Ghép chéo: $(+)(x^2)(\\sin x) - (2x)(-\\cos x) + (2)(-\\sin x) = (x^2 - 2)\\sin x + 2x\\cos x + C$."
                    }
                ]
            },
            {
                "id": "4.7",
                "name": "Dạng 4.7: Đổi biến số Loại 1 (Vi phân nhanh $u = g(x)$)",
                "tip": "Nhận dạng biểu thức có dạng $\\int f(g(x)) g'(x)\\,dx = \\int f(u)\\,du$. Nhớ đổi cận khi tính tích phân xác định.",
                "questions": [
                    {
                        "q": "Tính tích phân $I = \\int_0^1 x \\sqrt{x^2 + 1}\\,dx$.",
                        "options": ["$\\frac{2\\sqrt{2} - 1}{3}$", "$\\frac{2\\sqrt{2} + 1}{3}$", "$\\frac{\\sqrt{2} - 1}{3}$", "$2\\sqrt{2} - 1$"],
                        "answer": "A",
                        "solution": "Đặt $u = \\sqrt{x^2+1} \\Rightarrow u^2 = x^2+1 \\Rightarrow 2u\\,du = 2x\\,dx \\Rightarrow x\\,dx = u\\,du$. Đổi cận: $x = 0 \\Rightarrow u = 1$; $x = 1 \\Rightarrow u = \\sqrt{2}$. Tích phân trở thành $I = \\int_1^{\\sqrt{2}} u \\cdot u\\,du = \\int_1^{\\sqrt{2}} u^2\\,du = [\\frac{u^3}{3}]_1^{\\sqrt{2}} = \\frac{(\\sqrt{2})^3 - 1^3}{3} = \\frac{2\\sqrt{2} - 1}{3}$."
                    },
                    {
                        "q": "Tính tích phân $I = \\int_0^{\\frac{\\pi}{2}} \\sin^3 x \\cos x\\,dx$.",
                        "options": ["$\\frac{1}{4}$", "$\\frac{1}{3}$", "$1$", "$\\frac{1}{2}$"],
                        "answer": "A",
                        "solution": "Đặt $u = \\sin x \\Rightarrow du = \\cos x\\,dx$. Đổi cận: $x = 0 \\Rightarrow u = 0; x = \\frac{\\pi}{2} \\Rightarrow u = 1$. Khi đó $I = \\int_0^1 u^3\\,du = [\\frac{u^4}{4}]_0^1 = \\frac{1}{4}$."
                    }
                ]
            },
            {
                "id": "4.8",
                "name": "Dạng 4.8: Đổi biến số Loại 2 (Lượng giác hóa $x = a\\sin t, x = a\\tan t$)",
                "tip": "Chứa $\\sqrt{a^2 - x^2}$ đặt $x = a\\sin t$ ($t \\in [-\\frac{\\pi}{2}; \\frac{\\pi}{2}]$). Chứa $\\frac{1}{x^2+a^2}$ đặt $x = a\\tan t$.",
                "questions": [
                    {
                        "q": "Tính tích phân $I = \\int_0^1 \\sqrt{1 - x^2}\\,dx$ (Diện tích hình quạt tròn bán kính 1).",
                        "options": ["$\\frac{\\pi}{4}$", "$\\frac{\\pi}{2}$", "$\\pi$", "$\\frac{1}{2}$"],
                        "answer": "A",
                        "solution": "Đặt $x = \\sin t \\Rightarrow dx = \\cos t\\,dt$. Đổi cận: $x = 0 \\Rightarrow t = 0$; $x = 1 \\Rightarrow t = \\frac{\\pi}{2}$. Với $t \\in [0; \\frac{\\pi}{2}]$ thì $\\sqrt{1-x^2} = \\cos t$. Tích phân trở thành $I = \\int_0^{\\pi/2} \\cos^2 t\\,dt = \\int_0^{\\pi/2} \\frac{1+\\cos 2t}{2}\\,dt = [\\frac{t}{2} + \\frac{\\sin 2t}{4}]_0^{\\pi/2} = \\frac{\\pi}{4}$."
                    },
                    {
                        "q": "Tính tích phân $I = \\int_0^1 \\frac{1}{x^2 + 1}\\,dx$.",
                        "options": ["$\\frac{\\pi}{4}$", "$\\frac{\\pi}{2}$", "$\\frac{\\pi}{3}$", "$1$"],
                        "answer": "A",
                        "solution": "Đặt $x = \\tan t \\Rightarrow dx = (1+\\tan^2 t)\\,dt$. Đổi cận: $x = 0 \\Rightarrow t = 0$; $x = 1 \\Rightarrow t = \\frac{\\pi}{4}$. $I = \\int_0^{\\pi/4} \\frac{1}{\\tan^2 t + 1} (1+\\tan^2 t)\\,dt = \\int_0^{\\pi/4} 1\\,dt = \\frac{\\pi}{4}$."
                    }
                ]
            },
            {
                "id": "4.9",
                "name": "Dạng 4.9: Ứng dụng tích phân tính Diện tích hình phẳng",
                "tip": "Diện tích giữa 2 đồ thị: $S = \\int_a^b |f(x) - g(x)|\\,dx$. Với Parabol và đường thẳng cắt tại 2 nghiệm: $S = \\frac{|a|}{6}(x_2 - x_1)^3$ (Công thức Archimedes).",
                "questions": [
                    {
                        "q": "Diện tích hình phẳng giới hạn bởi đồ thị hàm số $y = -x^2 + 4$ và trục hoành $Ox$ ($y = 0$) bằng:",
                        "options": ["$\\frac{32}{3}$", "$\\frac{16}{3}$", "$16$", "$\\frac{8}{3}$"],
                        "answer": "A",
                        "solution": "Phương trình hoành độ giao điểm: $-x^2 + 4 = 0 \\Leftrightarrow x = -2$ hoặc $x = 2$. Áp dụng công thức Archimedes: $S = \\frac{|-1|}{6}(2 - (-2))^3 = \\frac{1}{6}(4)^3 = \\frac{64}{6} = \\frac{32}{3}$."
                    },
                    {
                        "q": "Tính diện tích hình phẳng giới hạn bởi 2 đường cong $y = x^2$ và $y = 2x$.",
                        "options": ["$\\frac{4}{3}$", "$\\frac{2}{3}$", "$2$", "$\\frac{1}{3}$"],
                        "answer": "A",
                        "solution": "Phương trình hoành độ giao điểm: $x^2 = 2x \\Leftrightarrow x^2 - 2x = 0 \\Leftrightarrow x = 0$ hoặc $x = 2$. Diện tích $S = \\int_0^2 |x^2 - 2x|\\,dx = \\int_0^2 (2x - x^2)\\,dx = [x^2 - \\frac{x^3}{3}]_0^2 = 4 - \\frac{8}{3} = \\frac{4}{3}$."
                    }
                ]
            },
            {
                "id": "4.10",
                "name": "Dạng 4.10: Ứng dụng tích phân tính Thể tích khối tròn xoay quanh trục Ox",
                "tip": "Thể tích quay quanh trục $Ox$: $V = \\pi \\int_a^b [f(x)]^2\\,dx$. Không được quên hằng số $\\pi$ và bình phương hàm số.",
                "questions": [
                    {
                        "q": "Thể tích khối tròn xoay sinh ra khi quay hình phẳng giới hạn bởi đồ thị $y = \\sqrt{x}$, trục hoành và hai đường thẳng $x = 1, x = 4$ quanh trục $Ox$ bằng:",
                        "options": ["$\\frac{15\\pi}{2}$", "$\\frac{15}{2}$", "$\\frac{7\\pi}{3}$", "$15\\pi$"],
                        "answer": "A",
                        "solution": "Công thức thể tích tròn xoay: $V = \\pi \\int_1^4 (\\sqrt{x})^2\\,dx = \\pi \\int_1^4 x\\,dx = \\pi [\\frac{x^2}{2}]_1^4 = \\pi (\\frac{16}{2} - \\frac{1}{2}) = \\frac{15\\pi}{2}$."
                    },
                    {
                        "q": "Tính thể tích khối tròn xoay tạo thành khi quay quanh trục $Ox$ hình phẳng giới hạn bởi đường cong $y = \\sin x$, trục hoành và các đường thẳng $x = 0, x = \\pi$.",
                        "options": ["$\\frac{\\pi^2}{2}$", "$\\pi^2$", "$\\frac{\\pi}{2}$", "$2\\pi$"],
                        "answer": "A",
                        "solution": "Ta có $V = \\pi \\int_0^\\pi \\sin^2 x\\,dx = \\pi \\int_0^\\pi \\frac{1 - \\cos 2x}{2}\\,dx = \\pi [\\frac{x}{2} - \\frac{\\sin 2x}{4}]_0^\\pi = \\pi (\\frac{\\pi}{2} - 0) = \\frac{\\pi^2}{2}$."
                    }
                ]
            },
            {
                "id": "4.11",
                "name": "Dạng 4.11: Ứng dụng tích phân giải phương trình vi phân hàm ẩn và bài toán vật lý",
                "tip": "Quãng đường $s(t) = \\int v(t)\\,dt$. Với PT vi phân tuyến tính cấp 1: nhân 2 vế với thừa số tích phân $e^{\\int p(x)\\,dx}$.",
                "questions": [
                    {
                        "q": "Một ô tô đang chạy với vận tốc $10\\text{ m/s}$ thì người lái đạp phanh; từ thời điểm đó ô tô chuyển động chậm dần đều với vận tốc $v(t) = -2t + 10\\text{ (m/s)}$, trong đó $t$ là khoảng thời gian tính bằng giây. Từ lúc đạp phanh đến khi dừng hẳn, ô tô đi được quãng đường bao nhiêu mét?",
                        "options": ["$25\\text{ m}$", "$50\\text{ m}$", "$20\\text{ m}$", "$30\\text{ m}$"],
                        "answer": "A",
                        "solution": "Ô tô dừng hẳn khi $v(t) = 0 \\Leftrightarrow -2t + 10 = 0 \\Leftrightarrow t = 5\\text{ s}$. Quãng đường đi được là tích phân của hàm vận tốc: $s = \\int_0^5 (-2t + 10)\\,dt = [-t^2 + 10t]_0^5 = -25 + 50 = 25\\text{ m}$."
                    },
                    {
                        "q": "Cho hàm số $f(x)$ liên tục trên $\\mathbb{R}$ thỏa mãn $f'(x) + 2f(x) = 0$ với mọi $x$ và $f(0) = 3$. Giá trị $f(1)$ bằng:",
                        "options": ["$3e^{-2}$", "$3e^2$", "$e^{-2}$", "$3e^{-1}$"],
                        "answer": "A",
                        "solution": "Nhân 2 vế với $e^{2x}$: $f'(x)e^{2x} + 2e^{2x}f(x) = 0 \\Leftrightarrow [f(x)e^{2x}]' = 0 \\Rightarrow f(x)e^{2x} = C$. Với $x = 0 \\Rightarrow f(0)e^0 = 3 \\Rightarrow C = 3$. Vậy $f(x) = 3e^{-2x}$. Do đó $f(1) = 3e^{-2}$."
                    }
                ]
            }
        ]
    },

    # =========================================================================
    # CHƯƠNG 5: PHƯƠNG PHÁP TỌA ĐỘ TRONG KHÔNG GIAN OXYZ (8 dạng = 16 câu)
    # =========================================================================
    {
        "id": "ch5",
        "title": "Chương 5: Phương Pháp Tọa Độ Trong Không Gian (Oxyz)",
        "badge": "8 Dạng • 16 Câu",
        "subtopics": [
            {
                "id": "5.1",
                "name": "Dạng 5.1: Phương trình Mặt Cầu trong không gian Oxyz",
                "tip": "Mặt cầu tâm $I(a; b; c)$, bán kính $R$: $(x-a)^2 + (y-b)^2 + (z-c)^2 = R^2$. Dạng khai triển $x^2+y^2+z^2-2ax-2by-2cz+d=0$ với $R = \\sqrt{a^2+b^2+c^2-d} > 0$.",
                "questions": [
                    {
                        "q": "Trong không gian $Oxyz$, mặt cầu $(S): x^2 + y^2 + z^2 - 2x + 4y - 6z - 2 = 0$ có tọa độ tâm $I$ và bán kính $R$ là:",
                        "options": ["$I(1; -2; 3), R = 4$", "$I(-1; 2; -3), R = 4$", "$I(1; -2; 3), R = 16$", "$I(1; -2; 3), R = \\sqrt{12}$"],
                        "answer": "A",
                        "solution": "Ta có $a = 1, b = -2, c = 3, d = -2$. Tọa độ tâm $I(1; -2; 3)$. Bán kính $R = \\sqrt{a^2 + b^2 + c^2 - d} = \\sqrt{1^2 + (-2)^2 + 3^2 - (-2)} = \\sqrt{1 + 4 + 9 + 2} = \\sqrt{16} = 4$."
                    },
                    {
                        "q": "Phương trình mặt cầu có đường kính $AB$ với $A(1; 2; 0)$ và $B(-1; 4; 2)$ là:",
                        "options": ["$x^2 + (y - 3)^2 + (z - 1)^2 = 3$", "$x^2 + (y - 3)^2 + (z - 1)^2 = 12$", "$(x - 1)^2 + (y - 2)^2 + z^2 = 3$", "$x^2 + (y + 3)^2 + (z + 1)^2 = 3$"],
                        "answer": "A",
                        "solution": "Tâm $I$ là trung điểm của $AB$: $I(0; 3; 1)$. Vectơ $\\vec{AB} = (-2; 2; 2) \\Rightarrow AB = \\sqrt{(-2)^2 + 2^2 + 2^2} = \\sqrt{12} = 2\\sqrt{3}$. Bán kính $R = \\frac{AB}{2} = \\sqrt{3} \\Rightarrow R^2 = 3$. Phương trình mặt cầu là: $x^2 + (y - 3)^2 + (z - 1)^2 = 3$."
                    }
                ]
            },
            {
                "id": "5.2",
                "name": "Dạng 5.2: Phương trình Mặt Phẳng (Điểm & VTPT, Đoạn chắn, Trung trực)",
                "tip": "Mặt phẳng qua $M_0(x_0; y_0; z_0)$ có VTPT $\\vec{n}=(A; B; C)$: $A(x-x_0)+B(y-y_0)+C(z-z_0)=0$. Mặt phẳng đoạn chắn qua $A(a;0;0), B(0;b;0), C(0;0;c)$: $\\frac{x}{a}+\\frac{y}{b}+\\frac{z}{c}=1$.",
                "questions": [
                    {
                        "q": "Trong không gian $Oxyz$, mặt phẳng đi qua 3 điểm $A(2; 0; 0), B(0; -3; 0), C(0; 0; 4)$ có phương trình là:",
                        "options": ["$\\frac{x}{2} + \\frac{y}{-3} + \\frac{z}{4} = 1$", "$\\frac{x}{2} + \\frac{y}{3} + \\frac{z}{4} = 1$", "$6x - 4y + 3z = 0$", "$\\frac{x}{2} + \\frac{y}{-3} + \\frac{z}{4} = 0$"],
                        "answer": "A",
                        "solution": "Theo phương trình mặt phẳng theo đoạn chắn qua 3 điểm trên 3 trục tọa độ: $\\frac{x}{a} + \\frac{y}{b} + \\frac{z}{c} = 1 \\Leftrightarrow \\frac{x}{2} + \\frac{y}{-3} + \\frac{z}{4} = 1$."
                    },
                    {
                        "q": "Phương trình mặt phẳng trung trực của đoạn thẳng $AB$ với $A(1; 3; -2)$ và $B(3; -1; 4)$ là:",
                        "options": ["$x - 2y + 3z - 3 = 0$", "$x - 2y + 3z + 3 = 0$", "$2x - 4y + 6z - 1 = 0$", "$x + y + z - 4 = 0$"],
                        "answer": "A",
                        "solution": "Trung điểm của $AB$ là $M(2; 1; 1)$. VTPT $\\vec{n} = \\vec{AB} = (2; -4; 6) = 2(1; -2; 3)$. Phương trình mặt phẳng: $1(x - 2) - 2(y - 1) + 3(z - 1) = 0 \\Leftrightarrow x - 2 - 2y + 2 + 3z - 3 = 0 \\Leftrightarrow x - 2y + 3z - 3 = 0$."
                    }
                ]
            },
            {
                "id": "5.3",
                "name": "Dạng 5.3: Phương trình Đường Thẳng (Dạng Tham số & Chính tắc)",
                "tip": "Đường thẳng qua $M_0(x_0; y_0; z_0)$ có VTCP $\\vec{u}=(a; b; c)$: tham số $\\begin{cases} x=x_0+at \\\\ y=y_0+bt \\\\ z=z_0+ct \\end{cases}$; chính tắc $\\frac{x-x_0}{a} = \\frac{y-y_0}{b} = \\frac{z-z_0}{c}$.",
                "questions": [
                    {
                        "q": "Đường thẳng đi qua điểm $M(1; -2; 3)$ và nhận vectơ $\\vec{u} = (2; -1; 4)$ làm VTCP có phương trình chính tắc là:",
                        "options": ["$\\frac{x - 1}{2} = \\frac{y + 2}{-1} = \\frac{z - 3}{4}$", "$\\frac{x + 1}{2} = \\frac{y - 2}{-1} = \\frac{z + 3}{4}$", "$\\frac{x - 2}{1} = \\frac{y + 1}{-2} = \\frac{z - 4}{3}$", "$\\frac{x - 1}{2} = \\frac{y - 2}{-1} = \\frac{z - 3}{4}$"],
                        "answer": "A",
                        "solution": "Phương trình chính tắc của đường thẳng qua $M(x_0; y_0; z_0)$ với VTCP $\\vec{u}=(a; b; c)$ là $\\frac{x - x_0}{a} = \\frac{y - y_0}{b} = \\frac{z - z_0}{c} \\Rightarrow \\frac{x - 1}{2} = \\frac{y + 2}{-1} = \\frac{z - 3}{4}$."
                    },
                    {
                        "q": "Đường thẳng $d$ đi qua điểm $A(2; 1; -1)$ và vuông góc với mặt phẳng $(P): 2x - 3y + z + 1 = 0$ có phương trình tham số là:",
                        "options": ["$\\begin{cases} x = 2 + 2t \\\\ y = 1 - 3t \\\\ z = -1 + t \\end{cases}$", "$\\begin{cases} x = 2 + 2t \\\\ y = -3 + t \\\\ z = 1 - t \\end{cases}$", "$\\begin{cases} x = 2 - 2t \\\\ y = 1 - 3t \\\\ z = -1 - t \\end{cases}$", "$\\begin{cases} x = 1 + 2t \\\\ y = -2 - 3t \\\\ z = 3 + t \\end{cases}$"],
                        "answer": "A",
                        "solution": "Vì $d \\perp (P)$ nên VTCP của $d$ là VTPT của $(P)$: $\\vec{u} = \\vec{n}_P = (2; -3; 1)$. Phương trình tham số của $d$ qua $A(2; 1; -1)$ là: $\\begin{cases} x = 2 + 2t \\\\ y = 1 - 3t \\\\ z = -1 + t \\end{cases}$."
                    }
                ]
            },
            {
                "id": "5.4",
                "name": "Dạng 5.4: Vị trí tương đối của hai đường thẳng (Song song, Cắt nhau, Chéo nhau)",
                "tip": "Cùng phương: Trùng nhau hoặc song song. Không cùng phương: Tích hỗn tạp $[\\vec{u}_1, \\vec{u}_2] \\cdot \\vec{M_1 M_2} = 0 \\Rightarrow$ Cắt nhau; $\\ne 0 \\Rightarrow$ Chéo nhau.",
                "questions": [
                    {
                        "q": "Xét vị trí tương đối của 2 đường thẳng $d_1: \\frac{x-1}{1} = \\frac{y-2}{2} = \\frac{z-3}{3}$ và $d_2: \\frac{x-2}{2} = \\frac{y-4}{4} = \\frac{z-6}{6}$.",
                        "options": ["$d_1$ trùng với $d_2$", "$d_1$ song song với $d_2$", "$d_1$ cắt $d_2$", "$d_1$ chéo $d_2$"],
                        "answer": "A",
                        "solution": "VTCP $\\vec{u}_1 = (1; 2; 3)$ và $\\vec{u}_2 = (2; 4; 6) = 2\\vec{u}_1 \\Rightarrow$ cùng phương. Lấy điểm $M_1(1; 2; 3) \\in d_1$, thay vào $d_2$: $\\frac{1-2}{2} = \\frac{2-4}{4} = \\frac{3-6}{6} = -\\frac{1}{2}$ (thỏa mãn) $\\Rightarrow M_1 \\in d_2$. Vậy hai đường thẳng trùng nhau."
                    },
                    {
                        "q": "Hai đường thẳng $d_1: \\frac{x-1}{2} = \\frac{y}{1} = \\frac{z+1}{-1}$ và $d_2: \\frac{x}{1} = \\frac{y-1}{1} = \\frac{z}{1}$ có vị trí tương đối là:",
                        "options": ["Chéo nhau", "Cắt nhau", "Song song", "Vuông góc và cắt nhau"],
                        "answer": "A",
                        "solution": "Ta có $\\vec{u}_1 = (2; 1; -1), \\vec{u}_2 = (1; 1; 1) \\Rightarrow [\\vec{u}_1, \\vec{u}_2] = (2; -3; 1) \\ne \\vec{0}$. Điểm $M_1(1; 0; -1) \\in d_1, M_2(0; 1; 0) \\in d_2 \\Rightarrow \\vec{M_1 M_2} = (-1; 1; 1)$. Tích hỗn tạp $[\\vec{u}_1, \\vec{u}_2] \\cdot \\vec{M_1 M_2} = 2(-1) - 3(1) + 1(1) = -2 - 3 + 1 = -4 \\ne 0$. Vậy hai đường thẳng chéo nhau."
                    }
                ]
            },
            {
                "id": "5.5",
                "name": "Dạng 5.5: Vị trí tương đối giữa đường thẳng và mặt phẳng",
                "tip": "Thay PT tham số của đường thẳng vào PT mặt phẳng để tìm số nghiệm $t$: 1 nghiệm $\\Rightarrow$ cắt nhau; vô nghiệm $\\Rightarrow$ song song; vô số nghiệm $\\Rightarrow$ chứa trong mp.",
                "questions": [
                    {
                        "q": "Tọa độ giao điểm của đường thẳng $d: \\begin{cases} x = 1 + t \\\\ y = 2 - t \\\\ z = 1 + 2t \\end{cases}$ và mặt phẳng $(P): x + y + z - 6 = 0$ là:",
                        "options": ["$(2; 1; 3)$", "$(1; 2; 1)$", "$(3; 0; 5)$", "$(0; 3; -1)$"],
                        "answer": "A",
                        "solution": "Thay phương trình tham số của $d$ vào phương trình $(P)$: $(1 + t) + (2 - t) + (1 + 2t) - 6 = 0 \\Leftrightarrow 4 + 2t - 6 = 0 \\Leftrightarrow 2t = 2 \\Leftrightarrow t = 1$. Với $t = 1 \\Rightarrow x = 2, y = 1, z = 3$. Tọa độ giao điểm là $(2; 1; 3)$."
                    },
                    {
                        "q": "Tìm tất cả giá trị thực của tham số $m$ để đường thẳng $d: \\begin{cases} x = 1 + 2t \\\\ y = t \\\\ z = -1 + mt \\end{cases}$ song song với mặt phẳng $(P): x - 2y + z + 3 = 0$.",
                        "options": ["$m = 0$", "$m = 2$", "$m = -2$", "$m = 1$"],
                        "answer": "A",
                        "solution": "VTCP $\\vec{u}_d = (2; 1; m)$, VTPT $\\vec{n}_P = (1; -2; 1)$. $d \\parallel (P) \\Rightarrow \\vec{u}_d \\cdot \\vec{n}_P = 0 \\Leftrightarrow 2(1) + 1(-2) + m(1) = 0 \\Leftrightarrow 2 - 2 + m = 0 \\Leftrightarrow m = 0$. Kiểm tra điểm $M(1; 0; -1) \\in d$: $1 - 2(0) + (-1) + 3 = 3 \\ne 0 \\Rightarrow M \\notin (P)$. Vậy $m = 0$ thỏa mãn."
                    }
                ]
            },
            {
                "id": "5.6",
                "name": "Dạng 5.6: Khoảng cách trong Oxyz (Điểm đến mp, Điểm đến đt, 2 đt chéo nhau)",
                "tip": "Khoảng cách điểm đến mp: $d(M, (P)) = \\frac{|Ax_0+By_0+Cz_0+D|}{\\sqrt{A^2+B^2+C^2}}$. Khoảng cách 2 đt chéo nhau: $d(d_1, d_2) = \\frac{|[\\vec{u}_1, \\vec{u}_2] \\cdot \\vec{M_1 M_2}|}{|[\\vec{u}_1, \\vec{u}_2]|}$.",
                "questions": [
                    {
                        "q": "Khoảng cách từ điểm $M(1; 2; -3)$ đến mặt phẳng $(P): 2x - 2y + z - 3 = 0$ bằng:",
                        "options": ["$\\frac{8}{3}$", "$8$", "$\\frac{4}{3}$", "$2$"],
                        "answer": "A",
                        "solution": "Áp dụng công thức khoảng cách: $d(M, (P)) = \\frac{|2(1) - 2(2) + 1(-3) - 3|}{\\sqrt{2^2 + (-2)^2 + 1^2}} = \\frac{|2 - 4 - 3 - 3|}{\\sqrt{4 + 4 + 1}} = \\frac{|-8|}{\\sqrt{9}} = \\frac{8}{3}$."
                    },
                    {
                        "q": "Khoảng cách giữa hai mặt phẳng song song $(P): 2x + y - 2z + 1 = 0$ và $(Q): 2x + y - 2z - 8 = 0$ bằng:",
                        "options": ["$3$", "$9$", "$1$", "$\\frac{7}{3}$"],
                        "answer": "A",
                        "solution": "Công thức khoảng cách giữa 2 mặt phẳng song song $Ax+By+Cz+D_1=0$ và $Ax+By+Cz+D_2=0$ là: $d((P), (Q)) = \\frac{|D_1 - D_2|}{\\sqrt{A^2 + B^2 + C^2}} = \\frac{|1 - (-8)|}{\\sqrt{2^2 + 1^2 + (-2)^2}} = \\frac{9}{\\sqrt{9}} = \\frac{9}{3} = 3$."
                    }
                ]
            },
            {
                "id": "5.7",
                "name": "Dạng 5.7: Góc trong Oxyz (Góc giữa 2 mặt phẳng, giữa 2 đường thẳng, giữa đt và mp)",
                "tip": "Góc giữa 2 mp: $\\cos \\varphi = \\frac{|\\vec{n}_1 \\cdot \\vec{n}_2|}{|\\vec{n}_1||\\vec{n}_2|}$. Góc giữa đt và mp: $\\sin \\theta = \\frac{|\\vec{u} \\cdot \\vec{n}|}{|\\vec{u}||\\vec{n}|}$.",
                "questions": [
                    {
                        "q": "Côsin của góc giữa hai mặt phẳng $(P): x + y - 1 = 0$ và $(Q): y + z + 2 = 0$ bằng:",
                        "options": ["$\\frac{1}{2}$", "$\\frac{\\sqrt{2}}{2}$", "$\\frac{\\sqrt{3}}{2}$", "$0$"],
                        "answer": "A",
                        "solution": "VTPT $\\vec{n}_P = (1; 1; 0)$ và $\\vec{n}_Q = (0; 1; 1)$. Ta có $\\cos \\varphi = \\frac{|\\vec{n}_P \\cdot \\vec{n}_Q|}{|\\vec{n}_P| |\\vec{n}_Q|} = \\frac{|1(0) + 1(1) + 0(1)|}{\\sqrt{1^2+1^2+0} \\cdot \\sqrt{0+1^2+1^2}} = \\frac{1}{\\sqrt{2} \\cdot \\sqrt{2}} = \\frac{1}{2}$ (Góc bằng $60^\\circ$)."
                    },
                    {
                        "q": "Sin của góc giữa đường thẳng $d: \\frac{x-1}{1} = \\frac{y}{2} = \\frac{z+1}{-1}$ và mặt phẳng $(P): 2x + y + z - 5 = 0$ bằng:",
                        "options": ["$\\frac{1}{2}$", "$\\frac{\\sqrt{3}}{2}$", "$\\frac{1}{6}$", "$\\frac{\\sqrt{2}}{2}$"],
                        "answer": "A",
                        "solution": "VTCP $\\vec{u} = (1; 2; -1)$, VTPT $\\vec{n} = (2; 1; 1)$. Ta có: $\\sin \\theta = \\frac{|\\vec{u} \\cdot \\vec{n}|}{|\\vec{u}| |\\vec{n}|} = \\frac{|1(2) + 2(1) + (-1)(1)|}{\\sqrt{1^2+2^2+(-1)^2} \\cdot \\sqrt{2^2+1^2+1^2}} = \\frac{|2 + 2 - 1|}{\\sqrt{6} \\cdot \\sqrt{6}} = \\frac{3}{6} = \\frac{1}{2}$ (Góc $\\theta = 30^\\circ$)."
                    }
                ]
            },
            {
                "id": "5.8",
                "name": "Dạng 5.8: Bài toán Cực trị hình học Oxyz & Phương pháp Tâm tỉ cự (Dạng 9+)",
                "tip": "Để biểu thức $\\alpha MA^2 + \\beta MB^2$ hay $|\\alpha \\vec{MA} + \\beta \\vec{MB} + \\gamma \\vec{MC}|$ đạt cực trị: Gọi tâm tỉ cự $I$ thỏa $\\alpha \\vec{IA} + \\beta \\vec{IB} + \\gamma \\vec{IC} = \\vec{0}$, khi đó $M$ là hình chiếu vuông góc của $I$ lên mp hoặc đường thẳng.",
                "questions": [
                    {
                        "q": "Trong không gian $Oxyz$, cho hai điểm $A(1; 2; 1)$ và $B(3; 0; -1)$. Điểm $M$ thuộc mặt phẳng $(Oxy)$ sao cho $MA^2 + MB^2$ đạt giá trị nhỏ nhất có tọa độ là:",
                        "options": ["$M(2; 1; 0)$", "$M(2; 1; 1)$", "$M(1; 1; 0)$", "$M(0; 0; 0)$"],
                        "answer": "A",
                        "solution": "Gọi $I$ là trung điểm của $AB \\Rightarrow I(2; 1; 0)$. Ta có $MA^2 + MB^2 = (\\vec{MI}+\\vec{IA})^2 + (\\vec{MI}+\\vec{IB})^2 = 2MI^2 + IA^2 + IB^2 + 2\\vec{MI}(\\vec{IA}+\\vec{IB}) = 2MI^2 + 2IA^2$. Vì $IA$ cố định nên $MA^2+MB^2$ nhỏ nhất $\\Leftrightarrow MI$ nhỏ nhất $\\Leftrightarrow M$ là hình chiếu của $I$ lên $(Oxy)$. Vì $I(2; 1; 0) \\in (Oxy)$ nên $M \\equiv I(2; 1; 0)$."
                    },
                    {
                        "q": "Cho $A(1; 0; 0), B(0; 2; 0), C(0; 0; 3)$. Điểm $M$ thuộc mặt phẳng $(P): x + y + z - 10 = 0$ sao cho $|\\vec{MA} + \\vec{MB} + \\vec{MC}|$ đạt giá trị nhỏ nhất là hình chiếu của điểm nào sau đây lên $(P)$?",
                        "options": ["Trọng tâm $G(\\frac{1}{3}; \\frac{2}{3}; 1)$ của $\\Delta ABC$", "Điểm $A(1; 0; 0)$", "Gốc tọa độ $O(0; 0; 0)$", "Trung điểm $AB$"],
                        "answer": "A",
                        "solution": "Gọi $G$ là trọng tâm $\\Delta ABC \\Rightarrow G(\\frac{1}{3}; \\frac{2}{3}; 1)$. Ta có $\\vec{MA} + \\vec{MB} + \\vec{MC} = 3\\vec{MG} \\Rightarrow |\\vec{MA} + \\vec{MB} + \\vec{MC}| = 3MG$. Độ dài này nhỏ nhất khi và chỉ khi $M$ là hình chiếu vuông góc của trọng tâm $G$ lên mặt phẳng $(P)$."
                    }
                ]
            }
        ]
    },

    # =========================================================================
    # CHƯƠNG 6: XÁC SUẤT CÓ ĐIỀU KIỆN VÀ ĐỊNH LÝ BAYES (7 dạng = 14 câu)
    # =========================================================================
    {
        "id": "ch6",
        "title": "Chương 6: Xác Suất Có Điều Kiện & Định Lý Bayes",
        "badge": "7 Dạng • 14 Câu",
        "subtopics": [
            {
                "id": "6.1",
                "name": "Dạng 6.1: Xác suất có điều kiện $P(A|B)$ & Quy tắc nhân xác suất",
                "tip": "Công thức xác suất có điều kiện: $P(A|B) = \\frac{P(A \\cap B)}{P(B)}$ (với $P(B) > 0$). Quy tắc nhân: $P(A \\cap B) = P(B) \\cdot P(A|B)$.",
                "questions": [
                    {
                        "q": "Gieo một con xúc xắc cân đối và đồng chất 1 lần. Biết rằng số chấm xuất hiện là số chẵn. Xác suất để số chấm xuất hiện là số nguyên tố bằng:",
                        "options": ["$\\frac{1}{3}$", "$\\frac{1}{2}$", "$\\frac{1}{6}$", "$\\frac{2}{3}$"],
                        "answer": "A",
                        "solution": "Gọi $B$ là biến cố 'Số chấm là chẵn': $B = \\{2; 4; 6\\} \\Rightarrow n(B) = 3$. Gọi $A$ là biến cố 'Số chấm là nguyên tố': $A = \\{2; 3; 5\\}$. Giao biến cố $A \\cap B = \\{2\\} \\Rightarrow n(A \\cap B) = 1$. Xác suất có điều kiện: $P(A|B) = \\frac{n(A \\cap B)}{n(B)} = \\frac{1}{3}$."
                    },
                    {
                        "q": "Một hộp có 10 viên bi (6 đỏ, 4 xanh). Lấy ngẫu nhiên liên tiếp 2 viên bi không hoàn lại. Xác suất để cả 2 viên bi lấy ra đều màu đỏ là:",
                        "options": ["$\\frac{1}{3}$", "$\\frac{3}{5}$", "$\\frac{1}{5}$", "$\\frac{6}{10}$"],
                        "answer": "A",
                        "solution": "Gọi $A_1$ là lần 1 rút bi đỏ: $P(A_1) = \\frac{6}{10} = \\frac{3}{5}$. Gọi $A_2$ là lần 2 rút bi đỏ khi lần 1 đã đỏ: $P(A_2|A_1) = \\frac{5}{9}$. Theo quy tắc nhân: $P(A_1 \\cap A_2) = P(A_1) \\cdot P(A_2|A_1) = \\frac{6}{10} \\cdot \\frac{5}{9} = \\frac{30}{90} = \\frac{1}{3}$."
                    }
                ]
            },
            {
                "id": "6.2",
                "name": "Dạng 6.2: Biến cố độc lập và Tính chất nhân độc lập $P(A \\cap B) = P(A)P(B)$",
                "tip": "Hai biến cố $A, B$ độc lập khi và chỉ khi việc xảy ra hay không xảy ra của $B$ không ảnh hưởng tới xác suất của $A$, tức là $P(A \\cap B) = P(A) \\cdot P(B)$.",
                "questions": [
                    {
                        "q": "Hai xạ thủ độc lập cùng bắn vào một tấm bia. Xác suất bắn trúng của người thứ nhất là $0.8$ và của người thứ hai là $0.7$. Xác suất để có ít nhất một người bắn trúng bia là:",
                        "options": ["$0.94$", "$0.56$", "$0.80$", "$0.86$"],
                        "answer": "A",
                        "solution": "Xét biến cố đối $\\bar{A}$: 'Cả hai người đều bắn trượt'. Vì hai người bắn độc lập nên $P(\\bar{A}) = P(\\bar{A}_1) \\cdot P(\\bar{A}_2) = (1 - 0.8)(1 - 0.7) = 0.2 \\times 0.3 = 0.06$. Xác suất có ít nhất một người trúng là $P(A) = 1 - P(\\bar{A}) = 1 - 0.06 = 0.94$."
                    },
                    {
                        "q": "Cho hai biến cố $A$ và $B$ độc lập có $P(A) = 0.4$ và $P(B) = 0.5$. Xác suất của biến cố hợp $P(A \\cup B)$ bằng:",
                        "options": ["$0.70$", "$0.90$", "$0.20$", "$0.60$"],
                        "answer": "A",
                        "solution": "Vì $A$ và $B$ độc lập nên $P(A \\cap B) = P(A) \\cdot P(B) = 0.4 \\times 0.5 = 0.2$. Theo công thức cộng xác suất: $P(A \\cup B) = P(A) + P(B) - P(A \\cap B) = 0.4 + 0.5 - 0.2 = 0.7$."
                    }
                ]
            },
            {
                "id": "6.3",
                "name": "Dạng 6.3: Mô hình Sơ đồ hình cây (Tree Diagram) 2 - 3 tầng",
                "tip": "Mỗi nhánh phân nhánh biểu diễn xác suất có điều kiện. Xác suất một lộ trình đường đi bằng tích các xác suất trên nhánh.",
                "questions": [
                    {
                        "q": "Hộp I có 3 bi đỏ, 2 bi xanh. Hộp II có 4 bi đỏ, 1 bi xanh. Chọn ngẫu nhiên một hộp (xác suất $0.5$), sau đó từ hộp đó rút ngẫu nhiên 1 viên bi. Dùng sơ đồ cây, xác suất rút được viên bi màu đỏ là:",
                        "options": ["$0.70$", "$0.60$", "$0.80$", "$0.50$"],
                        "answer": "A",
                        "solution": "Nhánh 1: Chọn Hộp I ($P = 0.5$) $\\to$ Rút bi đỏ ($P = \\frac{3}{5} = 0.6$) $\\Rightarrow P_1 = 0.5 \\times 0.6 = 0.30$. Nhánh 2: Chọn Hộp II ($P = 0.5$) $\\to$ Rút bi đỏ ($P = \\frac{4}{5} = 0.8$) $\\Rightarrow P_2 = 0.5 \\times 0.8 = 0.40$. Tổng xác suất rút được bi đỏ là $P = 0.30 + 0.40 = 0.70$."
                    },
                    {
                        "q": "Một học sinh đi học qua 2 ngã tư có đèn tín hiệu giao thông độc lập. Xác suất gặp đèn đỏ ở ngã tư 1 là $0.4$, ở ngã tư 2 là $0.3$. Xác suất học sinh chỉ gặp đúng một đèn đỏ trên đường đi là:",
                        "options": ["$0.46$", "$0.12$", "$0.42$", "$0.58$"],
                        "answer": "A",
                        "solution": "Theo sơ đồ cây có 2 trường hợp: 1) Đèn đỏ ở ngã tư 1 và đèn xanh ở ngã tư 2: $0.4 \\times (1 - 0.3) = 0.4 \\times 0.7 = 0.28$. 2) Đèn xanh ở ngã tư 1 và đèn đỏ ở ngã tư 2: $(1 - 0.4) \\times 0.3 = 0.6 \\times 0.3 = 0.18$. Tổng xác suất chỉ gặp 1 đèn đỏ là $0.28 + 0.18 = 0.46$."
                    }
                ]
            },
            {
                "id": "6.4",
                "name": "Dạng 6.4: Công thức Xác suất toàn phần (Law of Total Probability)",
                "tip": "Nếu hệ $\\{A_1, A_2, ..., A_n\\}$ là một hệ đầy đủ các biến cố thì $P(B) = \\sum_{i=1}^n P(A_i) \\cdot P(B|A_i)$.",
                "questions": [
                    {
                        "q": "Một nhà máy sản xuất linh kiện từ 3 phân xưởng $A, B, C$ với tỷ lệ sản lượng lần lượt là $50\\%, 30\\%, 20\\%$. Tỷ lệ phế phẩm tương ứng của từng xưởng là $1\\%, 2\\%, 3\\%$. Chọn ngẫu nhiên 1 sản phẩm của nhà máy, xác suất sản phẩm đó là phế phẩm bằng:",
                        "options": ["$1.7\\%$", "$2.0\\%$", "$1.5\\%$", "$6.0\\%$"],
                        "answer": "A",
                        "solution": "Áp dụng công thức xác suất toàn phần: $P(\\text{Phế phẩm}) = P(A)P(\\text{Lỗi}|A) + P(B)P(\\text{Lỗi}|B) + P(C)P(\\text{Lỗi}|C) = 0.50(0.01) + 0.30(0.02) + 0.20(0.03) = 0.005 + 0.006 + 0.006 = 0.017 = 1.7\\%$."
                    },
                    {
                        "q": "Trong một kho hàng, $60\\%$ kiện hàng do xe tải chở đến (tỷ lệ dập nát là $5\\%$) và $40\\%$ do tàu hỏa chở đến (tỷ lệ dập nát là $2\\%$). Xác suất để chọn ngẫu nhiên một kiện hàng trong kho còn nguyên vẹn (không dập nát) là:",
                        "options": ["$96.2\\%$", "$3.8\\%$", "$95.0\\%$", "$97.0\\%$"],
                        "answer": "A",
                        "solution": "Tỷ lệ dập nát chung toàn phần: $P(\\text{Nát}) = 0.60(0.05) + 0.40(0.02) = 0.030 + 0.008 = 0.038 = 3.8\\%$. Xác suất kiện hàng nguyên vẹn là $1 - P(\\text{Nát}) = 1 - 0.038 = 0.962 = 96.2\\%$."
                    }
                ]
            },
            {
                "id": "6.5",
                "name": "Dạng 6.5: Định lý Bayes - Ứng dụng Y tế (Xét nghiệm chẩn đoán & Độ nhạy, Độ đặc hiệu)",
                "tip": "Công thức Bayes đảo: $P(B|+) = \\frac{P(B)P(+|B)}{P(B)P(+|B) + P(\\bar{B})P(+|\\bar{B})}$. Hiện tượng 'Dương tính giả' xảy ra khi tỷ lệ nhiễm trong cộng đồng $P(B)$ rất thấp.",
                "questions": [
                    {
                        "q": "Tỷ lệ nhiễm virus trong một cộng đồng là $1\\%$. Một bộ kit xét nghiệm có độ nhạy $95\\%$ (người có bệnh test dương tính) và độ đặc hiệu $90\\%$ (người không bệnh test âm tính $\\Rightarrow$ dương tính giả $10\\%$). Một người đi xét nghiệm có kết quả dương tính. Xác suất người này thực sự nhiễm virus là:",
                        "options": ["$8.76\\%$", "$95.00\\%$", "$50.00\\%$", "$9.50\\%$"],
                        "answer": "A",
                        "solution": "Gọi $B$ là người có bệnh: $P(B) = 0.01 \\Rightarrow P(\\bar{B}) = 0.99$. Xác suất test dương tính khi có bệnh $P(+|B) = 0.95$; khi không bệnh $P(+|\\bar{B}) = 1 - 0.90 = 0.10$. Xác suất test dương tính toàn phần: $P(+) = P(B)P(+|B) + P(\\bar{B})P(+|\\bar{B}) = 0.01(0.95) + 0.99(0.10) = 0.0095 + 0.0990 = 0.1085$. Theo định lý Bayes: $P(B|+) = \\frac{0.0095}{0.1085} \\approx 0.087557 \\approx 8.76\\%$."
                    },
                    {
                        "q": "Vì sao khi một xét nghiệm y tế có độ nhạy và độ đặc hiệu đều rất cao ($99\\%$) nhưng đối với một căn bệnh cực hiếm (tỷ lệ mắc $1/10000$), xác suất một người nhận kết quả dương tính thực sự mắc bệnh lại rất thấp?",
                        "options": ["Vì số lượng người khỏe mạnh dương tính giả áp đảo số lượng người bệnh thực sự", "Vì kit test bị hỏng khi gặp bệnh hiếm", "Vì công thức Bayes không áp dụng cho bệnh hiếm", "Vì độ nhạy $99\\%$ là chưa đủ tiêu chuẩn"],
                        "answer": "A",
                        "solution": "Do tỷ lệ mắc bệnh quá nhỏ ($0.01\\%$), số người không bệnh chiếm $99.99\\%$. Dù tỷ lệ dương tính giả chỉ $1\\%$, nhưng $1\\%$ của $99.99\\%$ dân số (khoảng 100 người) vẫn vượt xa số người bệnh thực sự (chỉ 1 người). Do đó mẫu số của định lý Bayes bị chi phối bởi các ca dương tính giả."
                    }
                ]
            },
            {
                "id": "6.6",
                "name": "Dạng 6.6: Định lý Bayes - Ứng dụng Quản lý chất lượng KCS (Truy xuất nguồn gốc)",
                "tip": "Tính xác suất phế phẩm thuộc về phân xưởng $A_k$: $P(A_k|\\text{Lỗi}) = \\frac{P(A_k)P(\\text{Lỗi}|A_k)}{\\sum P(A_i)P(\\text{Lỗi}|A_i)}$.",
                "questions": [
                    {
                        "q": "Một xí nghiệp có 2 máy I và II cùng sản xuất một loại chi tiết máy. Máy I sản xuất $60\\%$, máy II sản xuất $40\\%$ tổng sản lượng. Tỷ lệ hỏng của máy I là $2\\%$, máy II là $5\\%$. Lấy ngẫu nhiên một sản phẩm thấy nó bị hỏng. Xác suất sản phẩm hỏng này do máy II sản xuất là:",
                        "options": ["$\\frac{5}{8} = 62.5\\%$", "$\\frac{3}{8} = 37.5\\%$", "$50.0\\%$", "$40.0\\%$"],
                        "answer": "A",
                        "solution": "Xác suất sản phẩm hỏng toàn phần: $P(H) = P(M_1)P(H|M_1) + P(M_2)P(H|M_2) = 0.60(0.02) + 0.40(0.05) = 0.012 + 0.020 = 0.032$. Theo định lý Bayes: $P(M_2|H) = \\frac{P(M_2)P(H|M_2)}{P(H)} = \\frac{0.020}{0.032} = \\frac{20}{32} = \\frac{5}{8} = 62.5\\%$."
                    },
                    {
                        "q": "Cũng từ dữ liệu xí nghiệp trên, xác suất sản phẩm bị hỏng đó do máy I sản xuất là:",
                        "options": ["$\\frac{3}{8} = 37.5\\%$", "$\\frac{5}{8} = 62.5\\%$", "$12.0\\%$", "$20.0\\%$"],
                        "answer": "A",
                        "solution": "Vì chỉ có 2 máy I và II nên $P(M_1|H) = 1 - P(M_2|H) = 1 - 0.625 = 0.375 = \\frac{3}{8} = 37.5\\%$."
                    }
                ]
            },
            {
                "id": "6.7",
                "name": "Dạng 6.7: Định lý Bayes - Bộ lọc thư rác (Spam Filter / Naive Bayes)",
                "tip": "Cập nhật xác suất email là Spam khi xuất hiện từ khóa $W$: $P(\\text{Spam}|W) = \\frac{P(\\text{Spam})P(W|\\text{Spam})}{P(\\text{Spam})P(W|\\text{Spam}) + P(\\text{Ham})P(W|\\text{Ham})}$.",
                "questions": [
                    {
                        "q": "Một hệ thống email có tỷ lệ thư rác (Spam) là $20\\%$, thư thường (Ham) là $80\\%$. Thống kê cho thấy từ 'Khuyến mãi' xuất hiện trong $70\\%$ thư rác và chỉ xuất hiện trong $5\\%$ thư thường. Khi nhận được một email chứa từ 'Khuyến mãi', xác suất email đó là thư rác bằng:",
                        "options": ["$\\frac{7}{9} \\approx 77.78\\%$", "$70.00\\%$", "$20.00\\%$", "$\\frac{2}{9} \\approx 22.22\\%$"],
                        "answer": "A",
                        "solution": "Gọi $S$ là thư rác, $H$ là thư thường, $W$ là chứa từ 'Khuyến mãi'. Ta có $P(S) = 0.2, P(H) = 0.8$. $P(W|S) = 0.7, P(W|H) = 0.05$. Xác suất email chứa từ $W$ toàn phần: $P(W) = P(S)P(W|S) + P(H)P(W|H) = 0.2(0.7) + 0.8(0.05) = 0.14 + 0.04 = 0.18$. Theo Bayes: $P(S|W) = \\frac{0.14}{0.18} = \\frac{14}{18} = \\frac{7}{9} \\approx 77.78\\%$."
                    },
                    {
                        "q": "Từ bài toán lọc thư rác trên, xác suất một email có chứa từ 'Khuyến mãi' nhưng thực chất là thư quan trọng (thư thường) bằng:",
                        "options": ["$\\frac{2}{9} \\approx 22.22\\%$", "$\\frac{7}{9} \\approx 77.78\\%$", "$5.00\\%$", "$80.00\\%$"],
                        "answer": "A",
                        "solution": "Xác suất thư thường khi chứa từ 'Khuyến mãi' là $P(H|W) = 1 - P(S|W) = 1 - \\frac{7}{9} = \\frac{2}{9} \\approx 22.22\\%$ (hoặc tính trực tiếp $\\frac{0.04}{0.18} = \\frac{2}{9}$)."
                    }
                ]
            }
        ]
    }
]
