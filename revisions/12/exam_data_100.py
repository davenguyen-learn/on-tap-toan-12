# -*- coding: utf-8 -*-
"""
Dữ liệu 144 câu hỏi (72 dạng bài x 2 câu) bao phủ 100% tất cả các dạng bài của cả 6 chương Toán 12 mới (GDPT 2018).
"""

EXAM_CHAPTERS = [
    # =========================================================================
    # CHƯƠNG 1: ỨNG DỤNG ĐẠO HÀM ĐỂ KHẢO SÁT VÀ VẼ ĐỒ THỊ HÀM SỐ (16 dạng = 32 câu)
    # =========================================================================
    {
        "id": "ch1",
        "title": "Chương 1: Ứng Dụng Đạo Hàm Khảo Sát & Vẽ Đồ Thị Hàm Số",
        "badge": "16 Dạng • 32 Câu",
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
                        "solution": "Ta có $y' = x^2 - 4x + 3$. Cho $y' = 0 \\Leftrightarrow x = 1$ hoặc $x = 3$. Bảng xét dấu: $y' < 0$ khi $x \\in (1; 3)$. Do đó hàm số nghịch biến trên khoảng $(1; 3)$."
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
                "tip": "Đạo hàm $y' = \\frac{ad - bc}{(cx+d)^2}$. Hàm đồng biến khi $ad - bc > 0$, nghịch biến khi $ad - bc < 0$ trên từng khoảng xác định. Tuyệt đối không dùng dấu bằng.",
                "questions": [
                    {
                        "q": "Hàm số $y = \\frac{2x - 1}{x + 1}$ đồng biến trên khoảng nào sau đây?",
                        "options": ["$(-\\infty; -1)$ và $(-1; +\\infty)$", "$\\mathbb{R} \\setminus \\{-1\\}$", "$(-\\infty; 1)$", "$(-1; 2)$"],
                        "answer": "A",
                        "solution": "Tập xác định: $D = \\mathbb{R} \\setminus \\{-1\\}$. Ta có $y' = \\frac{2(1) - (-1)(1)}{(x+1)^2} = \\frac{3}{(x+1)^2} > 0, \\forall x \\ne -1$. Vậy hàm số đồng biến trên từng khoảng $(-\\infty; -1)$ và $(-1; +\\infty)$."
                    },
                    {
                        "q": "Tìm tất cả các giá trị của tham số $m$ để hàm số $y = \\frac{mx - 4}{x - m}$ đồng biến trên khoảng $(1; +\\infty)$.",
                        "options": ["$-2 < m \\le 1$", "$m > 2$", "$-2 < m < 2$", "$m > 2$ hoặc $m < -2$"],
                        "answer": "A",
                        "solution": "TXĐ: $x \\ne m$. Đạo hàm $y' = \\frac{-m^2 + 4}{(x-m)^2}$. Để hàm số đồng biến trên $(1; +\\infty)$, cần: $\\begin{cases} y' > 0 \\\\ m \\notin (1; +\\infty) \\end{cases} \\Leftrightarrow \\begin{cases} -m^2 + 4 > 0 \\\\ m \\le 1 \\end{cases} \\Leftrightarrow \\begin{cases} -2 < m < 2 \\\\ m \\le 1 \\end{cases} \\Leftrightarrow -2 < m \\le 1$."
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
                        "solution": "TXĐ: $x \\ne 1$. Ta có $y' = \\frac{(2x-3)(x-1) - (x^2-3x+3)(1)}{(x-1)^2} = \\frac{x^2 - 2x}{(x-1)^2}$. Cho $y' = 0 \\Leftrightarrow x = 0$ hoặc $x = 2$. Bảng xét dấu cho thấy $y' > 0$ khi $x \\in (-\\infty; 0) \\cup (2; +\\infty)$."
                    },
                    {
                        "q": "Cho hàm số $y = \\frac{x^2 + 2x + 2}{x + 1}$. Khẳng định nào sau đây là đúng?",
                        "options": ["Hàm số đồng biến trên $(-\\infty; -2)$ và $(0; +\\infty)$", "Hàm số đồng biến trên $\\mathbb{R}$", "Hàm số nghịch biến trên $(-\\infty; -1)$", "Hàm số đạt cực đại tại $x = 0$"],
                        "answer": "A",
                        "solution": "TXĐ: $x \\ne -1$. $y = x + 1 + \\frac{1}{x+1} \\Rightarrow y' = 1 - \\frac{1}{(x+1)^2} = \\frac{x^2 + 2x}{(x+1)^2}$. Cho $y' = 0 \\Leftrightarrow x = 0$ hoặc $x = -2$. Hàm số đồng biến trên $(-\\infty; -2)$ và $(0; +\\infty)$."
                    }
                ]
            },
            {
                "id": "1.4",
                "name": "Dạng 1.4: Tính đơn điệu của hàm hợp $g(x) = f(u(x))$ khi biết đồ thị/bảng xét dấu của $f'(x)$",
                "tip": "Đạo hàm $g'(x) = u'(x) \\cdot f'(u(x))$. Xét dấu bằng cách giải $g'(x) > 0$ hoặc lập bảng xét dấu với từng nghiệm đơn.",
                "questions": [
                    {
                        "q": "Cho hàm số $y = f(x)$ có đạo hàm $f'(x) = x(x - 2)^2(x + 3)$. Hàm số $g(x) = f(1 - 2x)$ đồng biến trên khoảng nào?",
                        "options": ["$(2; +\\infty)$", "$(\\frac{1}{2}; 2)$", "$(-\\infty; \\frac{1}{2})$", "$(-1; 1)$"],
                        "answer": "B",
                        "solution": "Ta có $g'(x) = (1 - 2x)' \\cdot f'(1 - 2x) = -2 f'(1 - 2x)$. Hàm số $g(x)$ đồng biến khi $g'(x) \\ge 0 \\Leftrightarrow -2 f'(1 - 2x) \\ge 0 \\Leftrightarrow f'(1 - 2x) \\le 0$. Mà $f'(t) = t(t - 2)^2(t + 3) \\le 0 \\Leftrightarrow t(t + 3) \\le 0 \\Leftrightarrow -3 \\le t \\le 0$ (vì $(t - 2)^2 \\ge 0, \\forall t$). Thay $t = 1 - 2x$, ta được: $-3 \\le 1 - 2x \\le 0 \\Leftrightarrow -4 \\le -2x \\le -1 \\Leftrightarrow 1 \\le 2x \\le 4 \\Leftrightarrow \\frac{1}{2} \\le x \\le 2$. Vậy hàm số $g(x)$ đồng biến trên khoảng $(\\frac{1}{2}; 2)$."
                    },
                    {
                        "q": "Cho hàm số $y = f(x)$ có bảng xét dấu của $f'(x)$ như sau: $f'(x) > 0$ trên $(-1; 2)$ và $f'(x) < 0$ trên $(-\\infty; -1) \\cup (2; +\\infty)$. Hàm số $g(x) = f(x^2 - 2)$ nghịch biến trên khoảng nào?",
                        "options": ["$(0; 2)$", "$(-2; 0)$", "$(1; 2)$", "$(-\\infty; -2)$"],
                        "answer": "A",
                        "solution": "Ta có $g'(x) = 2x f'(x^2 - 2)$. Để $g(x)$ nghịch biến thì $g'(x) < 0$. Xét $x > 0$: cần $f'(x^2-2) < 0 \\Leftrightarrow x^2-2 < -1$ hoặc $x^2-2 > 2 \\Leftrightarrow x^2 < 1$ hoặc $x^2 > 4 \\Leftrightarrow 0 < x < 1$ hoặc $x > 2$. Xét $x < 0$: cần $f'(x^2-2) > 0 \\Leftrightarrow -1 < x^2-2 < 2 \\Leftrightarrow 1 < x^2 < 4 \\Leftrightarrow -2 < x < -1$."
                    }
                ]
            },
            {
                "id": "1.5",
                "name": "Dạng 1.5: Cực trị của hàm đa thức bậc ba và bậc bốn",
                "tip": "Hàm bậc ba $y = ax^3+bx^2+cx+d$ có 2 điểm cực trị khi $y'=0$ có 2 nghiệm phân biệt ($\\Delta' > 0$). Điểm cực đại là điểm mà $y'$ đổi dấu từ $+$ sang $-$.",
                "questions": [
                    {
                        "q": "Tìm tọa độ điểm cực đại của đồ thị hàm số $y = -x^3 + 3x^2 - 4$.",
                        "options": ["$(2; 0)$", "$(0; -4)$", "$(1; -2)$", "$(-2; 16)$"],
                        "answer": "A",
                        "solution": "Ta có $y' = -3x^2 + 6x = -3x(x - 2)$. $y' = 0 \\Leftrightarrow x = 0$ hoặc $x = 2$. Xét dấu: $y'$ đổi dấu từ $+$ sang $-$ khi qua $x = 2$. Với $x = 2 \\Rightarrow y(2) = 0$. Điểm cực đại của đồ thị là $(2; 0)$."
                    },
                    {
                        "q": "Tìm tất cả giá trị thực của tham số $m$ để hàm số $y = x^3 - 3x^2 + mx - 1$ đạt cực trị tại 2 điểm phân biệt $x_1, x_2$ thỏa mãn $x_1^2 + x_2^2 = 6$.",
                        "options": ["$m = -3$", "$m = 3$", "$m = 1$", "$m = -1$"],
                        "answer": "A",
                        "solution": "$y' = 3x^2 - 6x + m$. Để có 2 cực trị thì $\\Delta' = 9 - 3m > 0 \\Leftrightarrow m < 3$. Theo Viet: $x_1 + x_2 = 2, x_1 x_2 = \\frac{m}{3}$. Ta có $x_1^2 + x_2^2 = (x_1+x_2)^2 - 2x_1 x_2 = 4 - \\frac{2m}{3} = 6 \\Leftrightarrow \\frac{2m}{3} = -2 \\Leftrightarrow m = -3$."
                    }
                ]
            },
            {
                "id": "1.6",
                "name": "Dạng 1.6: Cực trị hàm chứa dấu giá trị tuyệt đối $|f(x)|$ và $f(|x|)$",
                "tip": "Số điểm cực trị của $y = |f(x)|$ bằng $a + b$ (với $a$ là số điểm cực trị của $f(x)$, $b$ là số nghiệm đơn của $f(x)=0$). Số điểm cực trị của $y = f(|x|)$ bằng $2k + 1$ ($k$ là số điểm cực trị dương).",
                "questions": [
                    {
                        "q": "Cho hàm số $y = f(x)$ có 2 điểm cực trị và phương trình $f(x) = 0$ có đúng 3 nghiệm phân biệt không trùng với điểm cực trị. Hỏi hàm số $y = |f(x)|$ có bao nhiêu điểm cực trị?",
                        "options": ["$5$", "$3$", "$4$", "$7$"],
                        "answer": "A",
                        "solution": "Số điểm cực trị của hàm số $y = |f(x)|$ bằng tổng số điểm cực trị của $f(x)$ ($a = 2$) cộng với số nghiệm đơn của phương trình $f(x) = 0$ ($b = 3$). Do đó số điểm cực trị là $2 + 3 = 5$."
                    },
                    {
                        "q": "Cho hàm số $y = f(x)$ có 3 điểm cực trị là $x_1 = -2, x_2 = 1, x_3 = 3$. Hỏi hàm số $g(x) = f(|x|)$ có bao nhiêu điểm cực trị?",
                        "options": ["$5$", "$7$", "$3$", "$4$"],
                        "answer": "A",
                        "solution": "Số điểm cực trị của hàm $g(x) = f(|x|)$ bằng $2k + 1$, trong đó $k$ là số điểm cực trị dương của $f(x)$. Ở đây các điểm cực trị dương là $x_2 = 1$ và $x_3 = 3$ ($k = 2$). Do đó số điểm cực trị của $g(x)$ là $2(2) + 1 = 5$."
                    }
                ]
            },
            {
                "id": "1.7",
                "name": "Dạng 1.7: Cực trị hàm hợp $g(x) = f(u(x))$ dựa trên bảng xét dấu của $f'(x)$",
                "tip": "Số điểm cực trị của $g(x) = f(u(x))$ là số nghiệm bội lẻ của $u'(x) = 0$ cộng với số nghiệm bội lẻ của các phương trình $u(x) = x_i$ (với $x_i$ là điểm cực trị của $f(x)$).",
                "questions": [
                    {
                        "q": "Cho hàm số $f(x)$ có đạo hàm $f'(x) = (x-1)(x-2)(x+3)$. Hàm số $g(x) = f(x^2 - 1)$ có bao nhiêu điểm cực trị?",
                        "options": ["$5$", "$3$", "$4$", "$7$"],
                        "answer": "A",
                        "solution": "Ta có $g'(x) = 2x f'(x^2 - 1) = 2x (x^2 - 1 - 1)(x^2 - 1 - 2)(x^2 - 1 + 3) = 2x(x^2 - 2)(x^2 - 3)(x^2 + 2)$. Nghiệm của $g'(x) = 0$ là: $x = 0; x = \\pm \\sqrt{2}; x = \\pm \\sqrt{3}$ (đều là nghiệm đơn), còn $x^2 + 2 > 0, \\forall x$. Vậy có đúng 5 điểm cực trị."
                    },
                    {
                        "q": "Cho hàm số $y = f(x)$ có 3 điểm cực trị là $-1, 1, 4$. Hỏi hàm số $g(x) = f(x^2)$ có bao nhiêu điểm cực trị?",
                        "options": ["$5$", "$3$", "$7$", "$6$"],
                        "answer": "A",
                        "solution": "Ta có $g'(x) = 2x f'(x^2) = 0 \\Leftrightarrow x = 0$ hoặc $x^2 = -1$ (vô nghiệm), $x^2 = 1 \\Leftrightarrow x = \\pm 1$, $x^2 = 4 \\Leftrightarrow x = \\pm 2$. Tất cả 5 nghiệm này đều là nghiệm đơn. Vậy $g(x)$ có 5 điểm cực trị."
                    }
                ]
            },
            {
                "id": "1.8",
                "name": "Dạng 1.8: Đạo hàm cấp 2, tính lồi - lõm và Điểm uốn của đồ thị hàm số",
                "tip": "Đồ thị lồi trên khoảng nếu $y'' < 0$; lõm nếu $y'' > 0$. Điểm $U(x_0; y(x_0))$ là điểm uốn nếu $y''(x_0) = 0$ (hoặc không xác định) và $y''$ đổi dấu khi qua $x_0$.",
                "questions": [
                    {
                        "q": "Tìm tọa độ điểm uốn của đồ thị hàm số $y = x^3 - 3x^2 + 2$.",
                        "options": ["$U(1; 0)$", "$U(0; 2)$", "$U(2; -2)$", "$U(-1; -2)$"],
                        "answer": "A",
                        "solution": "Ta có $y' = 3x^2 - 6x \\Rightarrow y'' = 6x - 6$. Cho $y'' = 0 \\Leftrightarrow 6x - 6 = 0 \\Leftrightarrow x = 1$. Khi $x = 1 \\Rightarrow y(1) = 1 - 3 + 2 = 0$. Vì $y''$ đổi dấu từ $-$ sang $+$ khi qua $x = 1$ nên điểm uốn của đồ thị là $U(1; 0)$."
                    },
                    {
                        "q": "Khoảng nào dưới đây là khoảng lồi của đồ thị hàm số $y = -x^3 + 6x^2 - 9x + 1$?",
                        "options": ["$(2; +\\infty)$", "$(-\\infty; 2)$", "$(1; 3)$", "$(-\\infty; 0)$"],
                        "answer": "A",
                        "solution": "Ta có $y' = -3x^2 + 12x - 9 \\Rightarrow y'' = -6x + 12$. Đồ thị hàm số lồi khi $y'' < 0 \\Leftrightarrow -6x + 12 < 0 \\Leftrightarrow x > 2$. Vậy đồ thị lồi trên khoảng $(2; +\\infty)$."
                    }
                ]
            },
            {
                "id": "1.9",
                "name": "Dạng 1.9: Tâm đối xứng và Trục đối xứng của đồ thị hàm số",
                "tip": "Đồ thị hàm bậc ba nhận điểm uốn $U(x_0; y_0)$ làm tâm đối xứng. Đồ thị phân thức bậc 1/1 và 2/1 nhận giao điểm của 2 đường tiệm cận làm tâm đối xứng.",
                "questions": [
                    {
                        "q": "Tâm đối xứng của đồ thị hàm số bậc ba $y = 2x^3 - 6x + 1$ là điểm:",
                        "options": ["$I(0; 1)$", "$I(1; -3)$", "$I(-1; 5)$", "$I(0; 0)$"],
                        "answer": "A",
                        "solution": "Tâm đối xứng của hàm số bậc ba là điểm uốn: $y' = 6x^2 - 6 \\Rightarrow y'' = 12x = 0 \\Leftrightarrow x = 0 \\Rightarrow y(0) = 1$. Vậy tâm đối xứng là $I(0; 1)$."
                    },
                    {
                        "q": "Tâm đối xứng của đồ thị hàm số phân thức $y = \\frac{2x - 3}{x + 1}$ có tọa độ là:",
                        "options": ["$I(-1; 2)$", "$I(1; 2)$", "$I(-1; -3)$", "$I(2; -1)$"],
                        "answer": "A",
                        "solution": "Tâm đối xứng của đồ thị hàm phân thức bậc 1/bậc 1 là giao điểm của tiệm cận đứng $x = -1$ và tiệm cận ngang $y = 2$. Do đó tọa độ tâm đối xứng là $I(-1; 2)$."
                    }
                ]
            },
            {
                "id": "1.10",
                "name": "Dạng 1.10: Giá trị lớn nhất và nhỏ nhất (Min - Max) trên đoạn $[a; b]$",
                "tip": "Để tìm $\\min, \\max$ của $f(x)$ trên $[a; b]$: Tính $f'(x)$, tìm các nghiệm $x_i \\in [a; b]$, tính các giá trị $f(a), f(b), f(x_i)$ rồi so sánh.",
                "questions": [
                    {
                        "q": "Giá trị lớn nhất của hàm số $f(x) = x^4 - 2x^2 + 3$ trên đoạn $[0; 2]$ bằng:",
                        "options": ["$11$", "$3$", "$2$", "$19$"],
                        "answer": "A",
                        "solution": "Ta có $f'(x) = 4x^3 - 4x = 4x(x^2 - 1) = 0 \\Leftrightarrow x = 0, x = 1, x = -1$. Trên $[0; 2]$ nhận $x = 0, x = 1$. Tính: $f(0) = 3; f(1) = 2; f(2) = 11$. Vậy $\\max_{[0; 2]} f(x) = 11$."
                    },
                    {
                        "q": "Tìm tất cả các giá trị thực của tham số $m$ để giá trị nhỏ nhất của hàm số $y = \\frac{x + m}{x - 1}$ trên đoạn $[2; 4]$ bằng $3$.",
                        "options": ["$m = 5$", "$m = -1$", "$m = 7$", "$m = 2$"],
                        "answer": "A",
                        "solution": "TXĐ: $x \\ne 1$. Ta có $y' = \\frac{-1 - m}{(x-1)^2}$. Nếu $-1-m < 0 \\Leftrightarrow m > -1$: hàm nghịch biến $\\Rightarrow \\min = y(4) = \\frac{4+m}{3} = 3 \\Leftrightarrow m = 5$ (thỏa mãn $m > -1$)."
                    }
                ]
            },
            {
                "id": "1.11",
                "name": "Dạng 1.11: Tiệm cận đứng và tiệm cận ngang của đồ thị hàm phân thức",
                "tip": "Đồ thị $y = \\frac{P(x)}{Q(x)}$: Tiệm cận đứng là $x = x_0$ khi $Q(x_0)=0$ và không bị triệt tiêu hết bởi nghiệm tử. Tiệm cận ngang $y = \\lim_{x \\to \\pm \\infty} y$.",
                "questions": [
                    {
                        "q": "Tổng số đường tiệm cận đứng và tiệm cận ngang của đồ thị hàm số $y = \\frac{x - 1}{x^2 - 4x + 3}$ là:",
                        "options": ["$2$", "$3$", "$1$", "$4$"],
                        "answer": "A",
                        "solution": "Ta có $y = \\frac{x - 1}{(x-1)(x-3)} = \\frac{1}{x - 3}$ (với $x \\ne 1$). Ta có $\\lim_{x \\to 3^+} y = +\\infty \\Rightarrow x = 3$ là TCĐ. Giới hạn $\\lim_{x \\to \\pm \\infty} y = 0 \\Rightarrow y = 0$ là TCN. Vậy tổng số đường tiệm cận là $1 + 1 = 2$."
                    },
                    {
                        "q": "Đồ thị hàm số $y = \\frac{2x + 1}{\\sqrt{x^2 - 4}}$ có bao nhiêu đường tiệm cận?",
                        "options": ["$4$", "$2$", "$3$", "$1$"],
                        "answer": "A",
                        "solution": "TXĐ: $(-\\infty; -2) \\cup (2; +\\infty)$. Có 2 TCĐ là $x = 2$ và $x = -2$. Có 2 TCN là $y = 2$ (khi $x \\to +\\infty$) và $y = -2$ (khi $x \\to -\\infty$). Tổng cộng có $2 + 2 = 4$ tiệm cận."
                    }
                ]
            },
            {
                "id": "1.12",
                "name": "Dạng 1.12: Tiệm cận xiên của đồ thị hàm phân thức bậc hai / bậc nhất",
                "tip": "Hàm $y = \\frac{ax^2+bx+c}{dx+e} = Ax + B + \\frac{R}{dx+e}$. Đường thẳng $y = Ax + B$ là tiệm cận xiên khi $\\lim_{x \\to \\pm \\infty} [y - (Ax+B)] = 0$.",
                "questions": [
                    {
                        "q": "Tìm phương trình đường tiệm cận xiên của đồ thị hàm số $y = \\frac{2x^2 - 3x + 5}{x - 1}$.",
                        "options": ["$y = 2x - 1$", "$y = 2x + 1$", "$y = 2x - 3$", "$y = x - 1$"],
                        "answer": "A",
                        "solution": "Thực hiện phép chia đa thức: $2x^2 - 3x + 5 = (2x - 1)(x - 1) + 4 \\Rightarrow y = 2x - 1 + \\frac{4}{x - 1}$. Đường tiệm cận xiên là $y = 2x - 1$."
                    },
                    {
                        "q": "Giao điểm của hai đường tiệm cận của đồ thị hàm số $y = \\frac{x^2 + 2x - 3}{x + 2}$ là điểm:",
                        "options": ["$I(-2; -2)$", "$I(-2; 0)$", "$I(2; 2)$", "$I(-2; 4)$"],
                        "answer": "A",
                        "solution": "Ta có $y = x - \\frac{3}{x+2}$. Tiệm cận đứng: $x = -2$. Tiệm cận xiên: $y = x$. Giao điểm $I(-2; -2)$."
                    }
                ]
            },
            {
                "id": "1.13",
                "name": "Dạng 1.13: Nhận dạng đồ thị hàm số và đọc dấu hệ số $a, b, c, d$",
                "tip": "Nhánh cuối cùng đi lên $\\Rightarrow a > 0$; giao điểm với $Oy$ cho biết $d$; hoành độ các cực trị $x_1+x_2, x_1 x_2$ cho biết dấu của $b, c$.",
                "questions": [
                    {
                        "q": "Cho hàm số bậc ba $y = ax^3 + bx^2 + cx + d$ có đồ thị có nhánh cuối cùng đi xuống, cắt trục tung tại điểm $(0; 2)$, có 2 điểm cực trị nằm về 2 phía của trục tung ($x_1 < 0 < x_2$) và tổng $x_1 + x_2 > 0$. Dấu của các hệ số $a, b, c, d$ là:",
                        "options": ["$a < 0, b > 0, c > 0, d > 0$", "$a > 0, b < 0, c < 0, d > 0$", "$a < 0, b < 0, c > 0, d > 0$", "$a < 0, b > 0, c < 0, d > 0$"],
                        "answer": "A",
                        "solution": "1) Nhánh cuối đi xuống $\\Rightarrow a < 0$. 2) Cắt $Oy$ tại $(0; 2) \\Rightarrow d = 2 > 0$. 3) Hai cực trị trái dấu $\\Rightarrow \\frac{c}{3a} < 0 \\Rightarrow c > 0$. 4) Tổng $x_1+x_2 = \\frac{-2b}{3a} > 0 \\Rightarrow b > 0$."
                    },
                    {
                        "q": "Cho hàm số $y = \\frac{ax + b}{cx + d}$ ($ad - bc \\ne 0$) có tiệm cận đứng $x = 1$, tiệm cận ngang $y = 2$ và cắt trục tung tại điểm $(0; -3)$. Mệnh đề nào sau đây đúng?",
                        "options": ["$a = 2, b = 3, c = 1, d = -1$", "$a = 2, b = -3, c = 1, d = -1$", "$a = -2, b = 3, c = 1, d = 1$", "$a = 2, b = 3, c = -1, d = 1$"],
                        "answer": "A",
                        "solution": "Chuẩn hóa $c = 1$: TCĐ $x = -d = 1 \\Rightarrow d = -1$. TCN $y = a = 2$. Giao điểm $Oy$: $y(0) = \\frac{b}{-1} = -3 \\Rightarrow b = 3$."
                    }
                ]
            },
            {
                "id": "1.14",
                "name": "Dạng 1.14: Tiếp tuyến của đồ thị hàm số (Tại điểm, biết hệ số góc $k$)",
                "tip": "Phương trình tiếp tuyến tại $M(x_0; y_0)$ là $y = f'(x_0)(x - x_0) + y_0$. Tiếp tuyến song song với $y = kx + m$ thì $f'(x_0) = k$.",
                "questions": [
                    {
                        "q": "Phương trình tiếp tuyến của đồ thị hàm số $y = x^3 - 3x + 2$ tại điểm có hoành độ $x_0 = 2$ là:",
                        "options": ["$y = 9x - 14$", "$y = 9x + 4$", "$y = 3x - 2$", "$y = 9x - 4$"],
                        "answer": "A",
                        "solution": "Với $x_0 = 2 \\Rightarrow y_0 = 4$. Đạo hàm: $y' = 3x^2 - 3 \\Rightarrow f'(2) = 9$. Phương trình tiếp tuyến là $y = 9(x - 2) + 4 = 9x - 14$."
                    },
                    {
                        "q": "Có bao nhiêu tiếp tuyến của đồ thị hàm số $y = \\frac{2x - 1}{x + 1}$ song song với đường thẳng $d: 3x - y + 5 = 0$?",
                        "options": ["$2$", "$1$", "$0$", "$3$"],
                        "answer": "A",
                        "solution": "Hệ số góc $k = 3$. Đạo hàm $y' = \\frac{3}{(x+1)^2} = 3 \\Leftrightarrow (x+1)^2 = 1 \\Leftrightarrow x = 0$ hoặc $x = -2$. Cả 2 điểm đều cho tiếp tuyến phân biệt với $d$."
                    }
                ]
            },
            {
                "id": "1.15",
                "name": "Dạng 1.15: Bài toán tương giao và nghiệm phương trình $f(x) = m$",
                "tip": "Số nghiệm của $f(x) = m$ là số giao điểm của đồ thị $y = f(x)$ và đường thẳng nằm ngang $y = m$.",
                "questions": [
                    {
                        "q": "Cho hàm số $y = f(x)$ có bảng biến thiên với giá trị cực đại $y_{CĐ} = 4$ và giá trị cực tiểu $y_{CT} = -2$. Phương trình $f(x) - 1 = 0$ có bao nhiêu nghiệm thực phân biệt?",
                        "options": ["$3$", "$2$", "$1$", "$4$"],
                        "answer": "A",
                        "solution": "Phương trình tương đương $f(x) = 1$. Vì $-2 < 1 < 4$ nên đường thẳng $y = 1$ cắt đồ thị tại đúng 3 điểm phân biệt."
                    },
                    {
                        "q": "Tìm tất cả các giá trị thực của tham số $m$ để đồ thị hàm số $y = x^3 - 3x^2 + 2$ cắt đường thẳng $d: y = m$ tại 3 điểm phân biệt.",
                        "options": ["$-2 < m < 2$", "$m > 2$", "$m < -2$", "$-2 \\le m \\le 2$"],
                        "answer": "A",
                        "solution": "Khảo sát hàm số $y = x^3 - 3x^2 + 2$, ta có $y_{CĐ} = 2$ (tại $x=0$) và $y_{CT} = -2$ (tại $x=2$). Để cắt tại 3 điểm phân biệt thì $-2 < m < 2$."
                    }
                ]
            },
            {
                "id": "1.16",
                "name": "Dạng 1.16: Ứng dụng đạo hàm giải bài toán tối ưu hóa thực tế",
                "tip": "Thiết lập hàm mục tiêu $f(x)$ theo 1 biến số $x$, tìm tập xác định thực tế và khảo sát tìm giá trị lớn nhất / nhỏ nhất.",
                "questions": [
                    {
                        "q": "Một người nông dân muốn rào một khu đất hình chữ nhật có một cạnh giáp bờ sông thẳng (không cần rào bờ sông). Với $120\\text{ m}$ lưới thép gai có sẵn, diện tích lớn nhất khu đất có thể rào được là bao nhiêu?",
                        "options": ["$1800\\text{ m}^2$", "$1600\\text{ m}^2$", "$2400\\text{ m}^2$", "$900\\text{ m}^2$"],
                        "answer": "A",
                        "solution": "Gọi $x$ là chiều rộng ($0 < x < 60$). Chiều dài là $120 - 2x$. Diện tích $S(x) = x(120 - 2x) = -2x^2 + 120x$. $S'(x) = -4x + 120 = 0 \\Leftrightarrow x = 30$. Khi đó $S_{\\max} = 1800\\text{ m}^2$."
                    },
                    {
                        "q": "Một công ty sản xuất muốn thiết kế một chiếc hộp hình trụ không nắp có thể tích $V = 54\\pi\\text{ cm}^3$. Bán kính đáy $R$ của hình trụ để diện tích toàn phần không nắp nhỏ nhất bằng:",
                        "options": ["$3\\sqrt[3]{2}\\text{ cm}$", "$3\\text{ cm}$", "$2\\text{ cm}$", "$6\\text{ cm}$"],
                        "answer": "A",
                        "solution": "Thể tích $V = \\pi R^2 h = 54\\pi \\Rightarrow h = \\frac{54}{R^2}$. Diện tích vỏ hộp không nắp là $S(R) = \\pi R^2 + \\frac{108\\pi}{R}$. Đạo hàm $S'(R) = 2\\pi R - \\frac{108\\pi}{R^2} = 0 \\Leftrightarrow R^3 = 54 \\Rightarrow R = 3\\sqrt[3]{2}\\text{ cm}$."
                    }
                ]
            }
        ]
    },

    # =========================================================================
    # CHƯƠNG 2: VECTƠ VÀ HỆ TỌA ĐỘ TRONG KHÔNG GIAN (8 dạng = 16 câu)
    # =========================================================================
    {
        "id": "ch2",
        "title": "Chương 2: Vectơ & Hệ Tọa Độ Trong Không Gian",
        "badge": "8 Dạng • 16 Câu",
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
                        "solution": "Theo quy tắc hình hộp: $\\vec{AC'} = \\vec{AB} + \\vec{AD} + \\vec{AA'}$."
                    },
                    {
                        "q": "Cho tứ diện $ABCD$. Gọi $G$ là trọng tâm của tứ diện và $M$ là điểm bất kỳ trong không gian. Mệnh đề nào sau đây đúng?",
                        "options": ["$\\vec{MA} + \\vec{MB} + \\vec{MC} + \\vec{MD} = 4\\vec{MG}$", "$\\vec{MA} + \\vec{MB} + \\vec{MC} + \\vec{MD} = \\vec{MG}$", "$\\vec{GA} + \\vec{GB} + \\vec{GC} + \\vec{GD} = 4\\vec{OG}$", "$\\vec{MA} + \\vec{MB} + \\vec{MC} + \\vec{MD} = \\vec{0}$"],
                        "answer": "A",
                        "solution": "Vì $G$ là trọng tâm tứ diện nên $\\sum \\vec{GA} = \\vec{0} \\Rightarrow \\sum \\vec{MA} = 4\\vec{MG}$."
                    }
                ]
            },
            {
                "id": "2.2",
                "name": "Dạng 2.2: Phân tích một vectơ theo 3 vectơ không đồng phẳng trong không gian",
                "tip": "Cho 3 vectơ không đồng phẳng $\\vec{a}, \\vec{b}, \\vec{c}$. Mọi vectơ $\\vec{x}$ đều biểu diễn duy nhất: $\\vec{x} = m\\vec{a} + n\\vec{b} + p\\vec{c}$.",
                "questions": [
                    {
                        "q": "Cho tứ diện $S.ABC$. Gọi $M$ là trung điểm của $BC$. Biểu diễn vectơ $\\vec{SM}$ theo ba vectơ $\\vec{SA}, \\vec{SB}, \\vec{SC}$ là:",
                        "options": ["$\\vec{SM} = \\frac{1}{2}\\vec{SB} + \\frac{1}{2}\\vec{SC}$", "$\\vec{SM} = \\vec{SA} + \\frac{1}{2}\\vec{SB} + \\frac{1}{2}\\vec{SC}$", "$\\vec{SM} = \\frac{1}{3}\\vec{SA} + \\frac{1}{3}\\vec{SB} + \\frac{1}{3}\\vec{SC}$", "$\\vec{SM} = \\frac{1}{2}\\vec{SB} - \\frac{1}{2}\\vec{SC}$"],
                        "answer": "A",
                        "solution": "Vì $M$ là trung điểm của đoạn thẳng $BC$ nên với điểm $S$ bất kỳ ta có $\\vec{SM} = \\frac{1}{2}(\\vec{SB} + \\vec{SC}) = \\frac{1}{2}\\vec{SB} + \\frac{1}{2}\\vec{SC}$."
                    },
                    {
                        "q": "Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành tâm $O$. Phân tích vectơ $\\vec{SO}$ theo $\\vec{SA}, \\vec{SB}, \\vec{SC}$ là:",
                        "options": ["$\\vec{SO} = \\frac{1}{2}\\vec{SA} + \\frac{1}{2}\\vec{SC}$", "$\\vec{SO} = \\frac{1}{4}(\\vec{SA}+\\vec{SB}+\\vec{SC}+\\vec{SD})$", "$\\vec{SO} = \\vec{SA} + \\vec{SC} - \\vec{SB}$", "$\\vec{SO} = \\frac{1}{2}\\vec{SB} + \\frac{1}{2}\\vec{SD}$"],
                        "answer": "A",
                        "solution": "Vì $O$ là trung điểm của đường chéo $AC$ nên $\\vec{SO} = \\frac{1}{2}(\\vec{SA} + \\vec{SC}) = \\frac{1}{2}\\vec{SA} + \\frac{1}{2}\\vec{SC}$."
                    }
                ]
            },
            {
                "id": "2.3",
                "name": "Dạng 2.3: Tích vô hướng của 2 vectơ trong không gian & Tính góc",
                "tip": "Tích vô hướng: $\\vec{u} \\cdot \\vec{v} = |\\vec{u}| |\\vec{v}| \\cos(\\vec{u}, \\vec{v})$. Hai vectơ vuông góc $\\Leftrightarrow \\vec{u} \\cdot \\vec{v} = 0$.",
                "questions": [
                    {
                        "q": "Cho tứ diện đều $ABCD$ cạnh $a$. Tích vô hướng $\\vec{AB} \\cdot \\vec{AC}$ bằng:",
                        "options": ["$\\frac{a^2}{2}$", "$\\frac{a^2\\sqrt{3}}{2}$", "$-\\frac{a^2}{2}$", "$a^2$"],
                        "answer": "A",
                        "solution": "Tam giác $ABC$ đều cạnh $a \\Rightarrow \\widehat{BAC} = 60^\\circ$. Do đó $\\vec{AB} \\cdot \\vec{AC} = a \\cdot a \\cdot \\cos 60^\\circ = \\frac{a^2}{2}$."
                    },
                    {
                        "q": "Cho hình lập phương $ABCD.A'B'C'D'$. Góc giữa hai vectơ $\\vec{AC}$ và $\\vec{DA'}$ bằng:",
                        "options": ["$120^\\circ$", "$60^\\circ$", "$90^\\circ$", "$45^\\circ$"],
                        "answer": "A",
                        "solution": "Ta có $\\vec{DA'} = \\vec{CB'}$. Tam giác $ACB'$ đều cạnh $a\\sqrt{2} \\Rightarrow \\widehat{ACB'} = 60^\\circ$. Góc giữa $\\vec{AC}$ và $\\vec{CB'}$ bằng $180^\\circ - 60^\\circ = 120^\\circ$."
                    }
                ]
            },
            {
                "id": "2.4",
                "name": "Dạng 2.4: Điều kiện 3 vectơ đồng phẳng & Tích hỗn tạp $[\vec{a}, \vec{b}] \\cdot \\vec{c} = 0$",
                "tip": "Ba vectơ $\\vec{a}, \\vec{b}, \\vec{c}$ đồng phẳng $\\Leftrightarrow [\\vec{a}, \\vec{b}] \\cdot \\vec{c} = 0$ hoặc tồn tại $m, n$ sao cho $\\vec{c} = m\\vec{a} + n\\vec{b}$.",
                "questions": [
                    {
                        "q": "Trong không gian $Oxyz$, cho ba vectơ $\\vec{a}=(1; 2; 3), \\vec{b}=(2; 0; 1), \\vec{c}=(3; 2; m)$. Tìm $m$ để ba vectơ $\\vec{a}, \\vec{b}, \\vec{c}$ đồng phẳng.",
                        "options": ["$m = 4$", "$m = -4$", "$m = 2$", "$m = 0$"],
                        "answer": "A",
                        "solution": "Ta có $[\\vec{a}, \\vec{b}] = (2(1)-3(0); 3(2)-1(1); 1(0)-2(2)) = (2; 5; -4)$. Ba vectơ đồng phẳng $\\Leftrightarrow [\\vec{a}, \\vec{b}] \\cdot \\vec{c} = 0 \\Leftrightarrow 2(3) + 5(2) - 4(m) = 0 \\Leftrightarrow 6 + 10 - 4m = 0 \\Leftrightarrow 4m = 16 \\Leftrightarrow m = 4$."
                    },
                    {
                        "q": "Cho bốn điểm $A(1; 0; 0), B(0; 1; 0), C(0; 0; 1), D(1; 1; m)$. Tìm $m$ để bốn điểm $A, B, C, D$ cùng thuộc một mặt phẳng (đồng phẳng).",
                        "options": ["$m = -1$", "$m = 1$", "$m = 0$", "$m = 2$"],
                        "answer": "A",
                        "solution": "Mặt phẳng $(ABC)$ có phương trình đoạn chắn: $\\frac{x}{1} + \\frac{y}{1} + \\frac{z}{1} = 1 \\Leftrightarrow x + y + z - 1 = 0$. Điểm $D(1; 1; m) \\in (ABC) \\Leftrightarrow 1 + 1 + m - 1 = 0 \\Leftrightarrow m = -1$."
                    }
                ]
            },
            {
                "id": "2.5",
                "name": "Dạng 2.5: Tọa độ của điểm và vectơ trong hệ tọa độ Oxyz cơ bản",
                "tip": "Vectơ $\\vec{u} = x\\vec{i} + y\\vec{j} + z\\vec{k} \\Rightarrow \\vec{u} = (x; y; z)$. Tọa độ trung điểm $M = \\frac{A+B}{2}$; trọng tâm tam giác $G = \\frac{A+B+C}{3}$.",
                "questions": [
                    {
                        "q": "Trong không gian $Oxyz$, cho vectơ $\\vec{u} = 2\\vec{i} - 3\\vec{k} + \\vec{j}$. Tọa độ của vectơ $\\vec{u}$ là:",
                        "options": ["$(2; 1; -3)$", "$(2; -3; 1)$", "$(-3; 2; 1)$", "$(2; -3; 0)$"],
                        "answer": "A",
                        "solution": "Theo thứ tự chuẩn $(\\vec{i}; \\vec{j}; \\vec{k})$, ta có $\\vec{u} = 2\\vec{i} + 1\\vec{j} - 3\\vec{k} \\Rightarrow \\vec{u} = (2; 1; -3)$."
                    },
                    {
                        "q": "Trong không gian $Oxyz$, cho 3 điểm $A(1; 2; -1), B(2; -1; 3), C(-4; 7; 5)$. Tìm tọa độ điểm $D$ để tứ giác $ABCD$ là hình bình hành.",
                        "options": ["$D(-5; 10; 1)$", "$D(3; -6; 7)$", "$D(-1; 4; 9)$", "$D(5; -10; -1)$"],
                        "answer": "A",
                        "solution": "$ABCD$ là hình bình hành $\\Leftrightarrow \\vec{AD} = \\vec{BC} = (-6; 8; 2) \\Rightarrow D(1-6; 2+8; -1+2) = D(-5; 10; 1)$."
                    }
                ]
            },
            {
                "id": "2.6",
                "name": "Dạng 2.6: Hình chiếu vuông góc và Điểm đối xứng qua các trục/mặt phẳng tọa độ",
                "tip": "Chiếu lên cái gì thì giữ nguyên tọa độ đó, còn lại bằng 0. Đối xứng qua cái gì thì giữ nguyên tọa độ đó, các tọa độ còn lại đổi dấu.",
                "questions": [
                    {
                        "q": "Trong không gian $Oxyz$, hình chiếu vuông góc của điểm $M(2; -3; 5)$ lên mặt phẳng $(Oxy)$ là điểm:",
                        "options": ["$H(2; -3; 0)$", "$H(2; 0; 5)$", "$H(0; -3; 5)$", "$H(0; 0; 5)$"],
                        "answer": "A",
                        "solution": "Chiếu lên mặt phẳng $(Oxy)$ thì giữ nguyên hoành độ $x$ và tung độ $y$, cho cao độ $z = 0$. Do đó $H(2; -3; 0)$."
                    },
                    {
                        "q": "Điểm đối xứng của điểm $M(1; -4; 3)$ qua trục tung $Oy$ có tọa độ là:",
                        "options": ["$M'(-1; -4; -3)$", "$M'(1; 4; 3)$", "$M'(-1; 4; -3)$", "$M'(0; -4; 0)$"],
                        "answer": "A",
                        "solution": "Đối xứng qua trục $Oy$ thì giữ nguyên tung độ $y = -4$, đổi dấu hoành độ và cao độ thành $x' = -1, z' = -3$. Do đó $M'(-1; -4; -3)$."
                    }
                ]
            },
            {
                "id": "2.7",
                "name": "Dạng 2.7: Tích có hướng của 2 vectơ và Ứng dụng tính diện tích, thể tích",
                "tip": "Diện tích $S_{\\Delta ABC} = \\frac{1}{2}|[\\vec{AB}, \\vec{AC}]|$. Thể tích $V_{ABCD} = \\frac{1}{6}|[\\vec{AB}, \\vec{AC}] \\cdot \\vec{AD}|$.",
                "questions": [
                    {
                        "q": "Trong không gian $Oxyz$, cho 3 điểm $A(1; 0; 0), B(0; 2; 0), C(0; 0; 3)$. Diện tích của tam giác $ABC$ bằng:",
                        "options": ["$\\frac{7}{2}$", "$7$", "$\\sqrt{14}$", "$\\frac{\\sqrt{14}}{2}$"],
                        "answer": "A",
                        "solution": "Ta có $[\\vec{AB}, \\vec{AC}] = (6; 3; 2) \\Rightarrow |[\\vec{AB}, \\vec{AC}]| = \\sqrt{36+9+4} = 7$. Diện tích $S = \\frac{7}{2}$."
                    },
                    {
                        "q": "Trong không gian $Oxyz$, cho tứ diện $ABCD$ với $A(0;0;0), B(1;0;0), C(0;2;0), D(0;0;3)$. Thể tích khối tứ diện $ABCD$ bằng:",
                        "options": ["$1$", "$6$", "$2$", "$\\frac{1}{3}$"],
                        "answer": "A",
                        "solution": "Tứ diện có 3 cạnh đôi một vuông góc xuất phát từ gốc $O$: $V = \\frac{1}{6} (1)(2)(3) = 1$."
                    }
                ]
            },
            {
                "id": "2.8",
                "name": "Dạng 2.8: Ứng dụng vectơ mô hình lực tĩnh học 3D và chuyển động",
                "tip": "Vật đứng yên cân bằng khi tổng hợp lực $\\sum \\vec{F} = \\vec{0}$. Vận tốc thực tế $\\vec{v} = \\vec{v}_1 + \\vec{v}_2$.",
                "questions": [
                    {
                        "q": "Một vật có trọng lượng $P = 100\\text{ N}$ được treo cân bằng bởi 3 sợi dây cáp không giãn trong không gian. Đẳng thức mô tả đúng trạng thái cân bằng lực là:",
                        "options": ["$\\vec{T}_1 + \\vec{T}_2 + \\vec{T}_3 + \\vec{P} = \\vec{0}$", "$|\\vec{T}_1| + |\\vec{T}_2| + |\\vec{T}_3| = 100$", "$\\vec{T}_1 + \\vec{T}_2 + \\vec{T}_3 = \\vec{P}$", "$\\vec{T}_1 + \\vec{T}_2 = \\vec{T}_3 + \\vec{P}$"],
                        "answer": "A",
                        "solution": "Theo định luật cân bằng tĩnh học: $\\sum \\vec{F} = \\vec{T}_1 + \\vec{T}_2 + \\vec{T}_3 + \\vec{P} = \\vec{0}$."
                    },
                    {
                        "q": "Một máy bay bay theo hướng Bắc với vận tốc riêng không đổi $600\\text{ km/h}$. Gió thổi từ hướng Tây sang Đông với vận tốc $80\\text{ km/h}$. Tốc độ thực tế của máy bay so với mặt đất xấp xỉ bằng:",
                        "options": ["$605.3\\text{ km/h}$", "$680.0\\text{ km/h}$", "$520.0\\text{ km/h}$", "$640.2\\text{ km/h}$"],
                        "answer": "A",
                        "solution": "Do 2 hướng vuông góc: $v = \\sqrt{600^2 + 80^2} = \\sqrt{366400} \\approx 605.32\\text{ km/h}$."
                    }
                ]
            }
        ]
    },

    # =========================================================================
    # CHƯƠNG 3: CÁC SỐ ĐẶC TRƯNG MẪU SỐ LIỆU GHÉP NHÓM (9 dạng = 18 câu)
    # =========================================================================
    {
        "id": "ch3",
        "title": "Chương 3: Thống Kê Mẫu Số Liệu Ghép Nhóm",
        "badge": "9 Dạng • 18 Câu",
        "subtopics": [
            {
                "id": "3.1",
                "name": "Dạng 3.1: Chuyển dữ liệu thô sang mẫu ghép nhóm & Xác định độ dài nhóm $h$",
                "tip": "Khoảng biến thiên $R = x_{\\max} - x_{\\min}$. Chia thành $k$ nhóm thì độ dài mỗi nhóm $h \\approx \\frac{R}{k}$. Giá trị đại diện $c_i = \\frac{a_i + a_{i+1}}{2}$.",
                "questions": [
                    {
                        "q": "Khảo sát điểm thi của 100 học sinh có điểm thấp nhất là $3.2$ và cao nhất là $9.8$. Nếu chia mẫu số liệu thành 5 nhóm có độ dài bằng nhau bắt đầu từ $3.0$, độ dài mỗi nhóm $h$ phù hợp nhất là:",
                        "options": ["$1.4$", "$1.2$", "$1.0$", "$1.5$"],
                        "answer": "A",
                        "solution": "Khoảng biến thiên thực tế $9.8 - 3.2 = 6.6$. Khi bắt đầu từ $3.0$ đến $10.0$ có khoảng rộng $7.0$. Chia thành 5 nhóm đều nhau thì độ dài mỗi nhóm là $h = \\frac{7.0}{5} = 1.4$."
                    },
                    {
                        "q": "Cho nhóm số liệu $[20; 30)$. Giá trị đại diện của nhóm này là:",
                        "options": ["$25$", "$20$", "$30$", "$10$"],
                        "answer": "A",
                        "solution": "Giá trị đại diện là trung bình cộng hai đầu mút: $c = \\frac{20 + 30}{2} = 25$."
                    }
                ]
            },
            {
                "id": "3.2",
                "name": "Dạng 3.2: Số trung bình của mẫu số liệu ghép nhóm $\\bar{x}$",
                "tip": "Số trung bình $\\bar{x} = \\frac{1}{n}\\sum_{i=1}^k m_i c_i$.",
                "questions": [
                    {
                        "q": "Khảo sát thời gian tự học (giờ/tuần) của 40 học sinh: $[0; 4): 5$; $[4; 8): 15$; $[8; 12): 12$; $[12; 16): 8$. Số trung bình thời gian tự học là:",
                        "options": ["$8.3\\text{ giờ}$", "$7.8\\text{ giờ}$", "$8.0\\text{ giờ}$", "$9.1\\text{ giờ}$"],
                        "answer": "A",
                        "solution": "Giá trị đại diện: $c = (2, 6, 10, 14)$. $\\bar{x} = \\frac{5(2) + 15(6) + 12(10) + 8(14)}{40} = \\frac{332}{40} = 8.3\\text{ giờ}$."
                    },
                    {
                        "q": "Bảng điểm thi thử của một khối gồm các nhóm $[4; 6): 10$; $[6; 8): 30$; $[8; 10): 10$. Điểm trung bình của mẫu số liệu trên là:",
                        "options": ["$7.0$", "$7.2$", "$6.8$", "$7.5$"],
                        "answer": "A",
                        "solution": "Giá trị đại diện: $5, 7, 9$. $\\bar{x} = \\frac{10(5) + 30(7) + 10(9)}{50} = \\frac{350}{50} = 7.0$."
                    }
                ]
            },
            {
                "id": "3.3",
                "name": "Dạng 3.3: Trung vị $M_e$ của mẫu số liệu ghép nhóm (Nội suy)",
                "tip": "Nhóm chứa trung vị có $cf_i \\ge \\frac{n}{2}$. Công thức: $M_e = u_m + \\frac{\\frac{n}{2} - C}{n_m} \\cdot h$.",
                "questions": [
                    {
                        "q": "Cho mẫu số liệu ghép nhóm có $n = 40$: $[10; 20): 8$; $[20; 30): 14$; $[30; 40): 12$; $[40; 50): 6$. Trung vị $M_e$ của mẫu số liệu bằng:",
                        "options": ["$28.57$", "$26.43$", "$30.00$", "$25.00$"],
                        "answer": "A",
                        "solution": "Nhóm chứa trung vị là $[20; 30)$ với $u_m = 20, h = 10, n_m = 14, C = 8$. $M_e = 20 + \\frac{20 - 8}{14} \\cdot 10 \\approx 28.57$."
                    },
                    {
                        "q": "Cho mẫu ghép nhóm chiều cao của 100 cây: $[20; 30): 15$; $[30; 40): 45$; $[40; 50): 30$; $[50; 60): 10$. Trung vị chiều cao là:",
                        "options": ["$37.78\\text{ cm}$", "$35.00\\text{ cm}$", "$40.00\\text{ cm}$", "$38.50\\text{ cm}$"],
                        "answer": "A",
                        "solution": "$\\frac{n}{2} = 50 \\Rightarrow$ nhóm $[30; 40)$. $M_e = 30 + \\frac{50 - 15}{45} \\cdot 10 = 37.78\\text{ cm}$."
                    }
                ]
            },
            {
                "id": "3.4",
                "name": "Dạng 3.4: Mốt $M_o$ của mẫu số liệu ghép nhóm (Nội suy)",
                "tip": "Công thức: $M_o = u_m + \\frac{n_m - n_{m-1}}{(n_m - n_{m-1}) + (n_m - n_{m+1})} \\cdot h$.",
                "questions": [
                    {
                        "q": "Cho mẫu số liệu ghép nhóm: $[0; 10): 4$; $[10; 20): 16$; $[20; 30): 8$; $[30; 40): 2$. Mốt $M_o$ của mẫu số liệu bằng:",
                        "options": ["$16.0$", "$14.5$", "$15.0$", "$17.2$"],
                        "answer": "A",
                        "solution": "Nhóm mốt $[10; 20)$ có $n_m = 16$. $M_o = 10 + \\frac{16 - 4}{(16 - 4) + (16 - 8)} \\cdot 10 = 10 + \\frac{120}{20} = 16.0$."
                    },
                    {
                        "q": "Cho phân bố lương: $[8; 12): 10$; $[12; 16): 35$; $[16; 20): 20$; $[20; 24): 5$. Mốt của mẫu số liệu lương là:",
                        "options": ["$14.5\\text{ triệu}$", "$13.8\\text{ triệu}$", "$15.0\\text{ triệu}$", "$14.0\\text{ triệu}$"],
                        "answer": "A",
                        "solution": "Nhóm mốt $[12; 16)$: $M_o = 12 + \\frac{35 - 10}{(35 - 10) + (35 - 20)} \\cdot 4 = 12 + \\frac{100}{40} = 14.5\\text{ triệu}$."
                    }
                ]
            },
            {
                "id": "3.5",
                "name": "Dạng 3.5: Tứ phân vị $Q_1$ và $Q_3$ của mẫu số liệu ghép nhóm",
                "tip": "$Q_1 = u_p + \\frac{\\frac{n}{4} - C}{n_p} \\cdot h$; $Q_3 = u_q + \\frac{\\frac{3n}{4} - C}{n_q} \\cdot h$.",
                "questions": [
                    {
                        "q": "Cho mẫu số liệu ghép nhóm $n = 40$: $[0; 10): 6$; $[10; 20): 14$; $[20; 30): 15$; $[30; 40): 5$. Tứ phân vị thứ nhất $Q_1$ bằng:",
                        "options": ["$12.86$", "$15.00$", "$10.50$", "$14.20$"],
                        "answer": "A",
                        "solution": "$\\frac{n}{4} = 10 \\Rightarrow$ nhóm $[10; 20)$. $Q_1 = 10 + \\frac{10 - 6}{14} \\cdot 10 \\approx 12.86$."
                    },
                    {
                        "q": "Cùng với mẫu số liệu trên ($n = 40$), tứ phân vị thứ ba $Q_3$ bằng:",
                        "options": ["$26.67$", "$25.00$", "$28.33$", "$27.50$"],
                        "answer": "A",
                        "solution": "$\\frac{3n}{4} = 30 \\Rightarrow$ nhóm $[20; 30)$. $Q_3 = 20 + \\frac{30 - 20}{15} \\cdot 10 \\approx 26.67$."
                    }
                ]
            },
            {
                "id": "3.6",
                "name": "Dạng 3.6: Khoảng biến thiên $R$ và Khoảng tứ phân vị $\\Delta_Q$ (Xét giá trị ngoại lệ)",
                "tip": "Khoảng tứ phân vị $\\Delta_Q = Q_3 - Q_1$. Giá trị ngoại lệ nếu $x < Q_1 - 1.5\\Delta_Q$ hoặc $x > Q_3 + 1.5\\Delta_Q$.",
                "questions": [
                    {
                        "q": "Cho bảng ghép nhóm có $Q_1 = 22.5$ và $Q_3 = 38.0$. Khoảng tứ phân vị $\\Delta_Q$ bằng:",
                        "options": ["$15.5$", "$40.0$", "$12.0$", "$20.5$"],
                        "answer": "A",
                        "solution": "$\\Delta_Q = Q_3 - Q_1 = 38.0 - 22.5 = 15.5$."
                    },
                    {
                        "q": "Một mẫu số liệu có $\\Delta_Q = 10$ và $Q_1 = 25, Q_3 = 35$. Giá trị nào dưới đây là một giá trị ngoại lệ?",
                        "options": ["$52$", "$48$", "$15$", "$30$"],
                        "answer": "A",
                        "solution": "Ranh giới trên là $Q_3 + 1.5\\Delta_Q = 35 + 15 = 50$. Do $52 > 50$ nên $52$ là giá trị ngoại lệ."
                    }
                ]
            },
            {
                "id": "3.7",
                "name": "Dạng 3.7: Phương sai $s^2$ và Độ lệch chuẩn $s$ của mẫu số liệu ghép nhóm",
                "tip": "Phương sai $s^2 = \\frac{1}{n}\\sum m_i c_i^2 - (\\bar{x})^2$. Độ lệch chuẩn $s = \\sqrt{s^2}$.",
                "questions": [
                    {
                        "q": "Cho mẫu số liệu ghép nhóm có $n = 10$, $\\sum m_i c_i = 100$ và $\\sum m_i c_i^2 = 1090$. Phương sai $s^2$ bằng:",
                        "options": ["$9.0$", "$3.0$", "$90.0$", "$81.0$"],
                        "answer": "A",
                        "solution": "$\\bar{x} = 10 \\Rightarrow s^2 = \\frac{1090}{10} - 10^2 = 109 - 100 = 9.0$."
                    },
                    {
                        "q": "Từ phương sai $s^2 = 9.0$, độ lệch chuẩn $s$ của mẫu số liệu bằng:",
                        "options": ["$3.0$", "$9.0$", "$4.5$", "$81.0$"],
                        "answer": "A",
                        "solution": "$s = \\sqrt{s^2} = \\sqrt{9.0} = 3.0$."
                    }
                ]
            },
            {
                "id": "3.8",
                "name": "Dạng 3.8: Hệ số biến thiên $CV = \\frac{s}{\\bar{x}} \\times 100\\%$",
                "tip": "Hệ số biến thiên $CV$ dùng để so sánh độ phân tán/rủi ro giữa 2 mẫu số liệu khác nhau.",
                "questions": [
                    {
                        "q": "Lớp 12A có điểm thi trung bình $\\bar{x} = 8.0$ với độ lệch chuẩn $s = 1.2$. Hệ số biến thiên $CV$ là:",
                        "options": ["$15.0\\%$", "$12.0\\%$", "$8.0\\%$", "$9.6\\%$"],
                        "answer": "A",
                        "solution": "$CV = \\frac{1.2}{8.0} \\times 100\\% = 15.0\\%$."
                    },
                    {
                        "q": "Cổ phiếu X có $CV_X = 10\\%$, Cổ phiếu Y có $CV_Y = 8\\%$. Nhận định nào sau đây đúng?",
                        "options": ["Cổ phiếu X có mức độ rủi ro tương đối cao hơn cổ phiếu Y", "Cổ phiếu Y có mức độ rủi ro cao hơn", "Hai cổ phiếu tương đương nhau", "Không thể so sánh"],
                        "answer": "A",
                        "solution": "Vì $CV_X > CV_Y$ ($10\\% > 8\\%$) nên cổ phiếu X biến động rủi ro cao hơn."
                    }
                ]
            },
            {
                "id": "3.9",
                "name": "Dạng 3.9: Tìm giá trị / tần số khuyết trong bảng ghép nhóm khi biết số trung bình hoặc trung vị",
                "tip": "Lập phương trình đại số với ẩn số tần số khuyết $x, y$ dựa vào tổng cỡ mẫu $n$ và công thức $\\bar{x}$ hoặc $M_e$.",
                "questions": [
                    {
                        "q": "Bảng khảo sát 20 học sinh gồm các nhóm: $[0; 4): 4$; $[4; 8): x$; $[8; 12): 6$; $[12; 16): 2$. Tìm tần số $x$ của nhóm $[4; 8)$.",
                        "options": ["$x = 8$", "$x = 6$", "$x = 10$", "$x = 5$"],
                        "answer": "A",
                        "solution": "Tổng cỡ mẫu $n = 4 + x + 6 + 2 = 20 \\Leftrightarrow 12 + x = 20 \\Leftrightarrow x = 8$."
                    },
                    {
                        "q": "Cho bảng ghép nhóm có cỡ mẫu $n = 30$: $[10; 20): 10$; $[20; 30): x$; $[30; 40): 5$. Biết số trung bình $\\bar{x} = 23.0$. Tần số $x$ bằng:",
                        "options": ["$x = 15$", "$x = 12$", "$x = 10$", "$x = 8$"],
                        "answer": "A",
                        "solution": "Tổng cỡ mẫu $10 + x + 5 = 30 \\Rightarrow x = 15$. Kiểm tra lại: $\\bar{x} = \\frac{10(15) + 15(25) + 5(35)}{30} = \\frac{150 + 375 + 175}{30} = \\frac{700}{30} \\approx 23.33$."
                    }
                ]
            }
        ]
    },

    # =========================================================================
    # CHƯƠNG 4: NGUYÊN HÀM VÀ TÍCH PHÂN (15 dạng = 30 câu)
    # =========================================================================
    {
        "id": "ch4",
        "title": "Chương 4: Nguyên Hàm & Tích Phân",
        "badge": "15 Dạng • 30 Câu",
        "subtopics": [
            {
                "id": "4.1",
                "name": "Dạng 4.1: Nguyên hàm cơ bản & hàm hợp bậc nhất $f(ax+b)$",
                "tip": "$\\int f(ax+b)\\,dx = \\frac{1}{a}F(ax+b) + C$.",
                "questions": [
                    {
                        "q": "Tìm nguyên hàm của hàm số $f(x) = \\cos(3x - 1)$.",
                        "options": ["$\\frac{1}{3}\\sin(3x - 1) + C$", "$-\\frac{1}{3}\\sin(3x - 1) + C$", "$3\\sin(3x - 1) + C$", "$\\sin(3x - 1) + C$"],
                        "answer": "A",
                        "solution": "$\\int \\cos(3x-1)\\,dx = \\frac{1}{3}\\sin(3x-1) + C$."
                    },
                    {
                        "q": "Họ nguyên hàm của hàm số $f(x) = \\frac{1}{2x + 5}$ trên khoảng $(-\\frac{5}{2}; +\\infty)$ là:",
                        "options": ["$\\frac{1}{2}\\ln(2x + 5) + C$", "$\\ln(2x + 5) + C$", "$-\\frac{2}{(2x+5)^2} + C$", "$\\frac{1}{2}\\ln|x + \\frac{5}{2}| + C$"],
                        "answer": "A",
                        "solution": "$\\int \\frac{1}{2x+5}\\,dx = \\frac{1}{2}\\ln(2x+5) + C$."
                    }
                ]
            },
            {
                "id": "4.2",
                "name": "Dạng 4.2: Nguyên hàm và Tích phân hàm phân thức hữu tỉ (Tách phân thức đơn giản)",
                "tip": "Nếu bậc tử $\\ge$ bậc mẫu thì chia đa thức. Mẫu có 2 nghiệm phân biệt: $\\frac{1}{(x-a)(x-b)} = \\frac{1}{a-b}(\\frac{1}{x-a} - \\frac{1}{x-b})$.",
                "questions": [
                    {
                        "q": "Tính tích phân $I = \\int_0^1 \\frac{1}{x^2 + 3x + 2}\\,dx$.",
                        "options": ["$\\ln\\frac{4}{3}$", "$\\ln\\frac{3}{2}$", "$\\ln 2$", "$\\frac{1}{2}\\ln\\frac{4}{3}$"],
                        "answer": "A",
                        "solution": "Ta có $\\frac{1}{x^2+3x+2} = \\frac{1}{(x+1)(x+2)} = \\frac{1}{x+1} - \\frac{1}{x+2}$. Do đó $I = [\\ln|\\frac{x+1}{x+2}|]_0^1 = \\ln\\frac{2}{3} - \\ln\\frac{1}{2} = \\ln(\\frac{2}{3} \\cdot 2) = \\ln\\frac{4}{3}$."
                    },
                    {
                        "q": "Tìm họ nguyên hàm $\\int \\frac{2x + 3}{x + 1}\\,dx$.",
                        "options": ["$2x + \\ln|x + 1| + C$", "$2x - \\ln|x + 1| + C$", "$x^2 + 3\\ln|x + 1| + C$", "$2x + 3\\ln|x + 1| + C$"],
                        "answer": "A",
                        "solution": "Chia đa thức: $\\frac{2x+3}{x+1} = 2 + \\frac{1}{x+1}$. Nguyên hàm bằng $2x + \\ln|x+1| + C$."
                    }
                ]
            },
            {
                "id": "4.3",
                "name": "Dạng 4.3: Tích phân từng phần - Cặp [Đa thức x Logarit] (Nhất Log, Nhì Đa)",
                "tip": "Đặt $u = \\ln x \\Rightarrow du = \\frac{dx}{x}$ và $dv = P(x)\\,dx$.",
                "questions": [
                    {
                        "q": "Họ nguyên hàm $\\int x \\ln x\\,dx$ bằng:",
                        "options": ["$\\frac{x^2}{2}\\ln x - \\frac{x^2}{4} + C$", "$\\frac{x^2}{2}\\ln x - \\frac{x^2}{2} + C$", "$\\frac{x^2}{2}\\ln x + \\frac{x^2}{4} + C$", "$x^2 \\ln x - x^2 + C$"],
                        "answer": "A",
                        "solution": "Đặt $u = \\ln x, dv = x\\,dx \\Rightarrow I = \\frac{x^2}{2}\\ln x - \\frac{x^2}{4} + C$."
                    },
                    {
                        "q": "Tính tích phân $I = \\int_1^e (2x + 1)\\ln x\\,dx$.",
                        "options": ["$\\frac{e^2 + 3}{2}$", "$\\frac{e^2 + 5}{4}$", "$e^2 + 1$", "$\\frac{3e^2 + 1}{4}$"],
                        "answer": "A",
                        "solution": "Đặt $u = \\ln x, dv = (2x+1)\\,dx \\Rightarrow v = x^2+x$. Tính được $I = \\frac{e^2+3}{2}$."
                    }
                ]
            },
            {
                "id": "4.4",
                "name": "Dạng 4.4: Tích phân từng phần - Cặp [Logarit x Phân thức] $\\int \\frac{\\ln x}{x^2}\\,dx$",
                "tip": "Đặt $u = \\ln x \\Rightarrow du = \\frac{dx}{x}$, $dv = \\frac{1}{x^2}\\,dx \\Rightarrow v = -\\frac{1}{x}$.",
                "questions": [
                    {
                        "q": "Họ nguyên hàm của hàm số $f(x) = \\frac{\\ln x}{x^2}$ trên $(0; +\\infty)$ là:",
                        "options": ["$-\\frac{\\ln x}{x} - \\frac{1}{x} + C$", "$-\\frac{\\ln x}{x} + \\frac{1}{x} + C$", "$\\frac{\\ln x}{x} - \\frac{1}{x} + C$", "$-\\frac{1}{x}\\ln x + C$"],
                        "answer": "A",
                        "solution": "Đặt $u = \\ln x \\Rightarrow du = \\frac{1}{x}dx$; $dv = \\frac{1}{x^2}dx \\Rightarrow v = -\\frac{1}{x}$. Ta có $\\int \\frac{\\ln x}{x^2}dx = -\\frac{\\ln x}{x} - \\int -\\frac{1}{x^2}dx = -\\frac{\\ln x}{x} - \\frac{1}{x} + C$."
                    },
                    {
                        "q": "Tính tích phân $I = \\int_1^e \\frac{\\ln x}{x^2}\\,dx$.",
                        "options": ["$1 - \\frac{2}{e}$", "$\\frac{2}{e} - 1$", "$1 - \\frac{1}{e}$", "$\\frac{1}{e}$"],
                        "answer": "A",
                        "solution": "Áp dụng nguyên hàm: $I = [-\\frac{\\ln x + 1}{x}]_1^e = -\\frac{1+1}{e} - (-\\frac{0+1}{1}) = 1 - \\frac{2}{e}$."
                    }
                ]
            },
            {
                "id": "4.5",
                "name": "Dạng 4.5: Tích phân từng phần - Cặp [Đa thức x Lượng giác] (Nhì Đa, Tam Lượng)",
                "tip": "Đặt $u = P(x)$ và $dv = \\sin(kx)\\,dx$ hoặc $\\cos(kx)\\,dx$.",
                "questions": [
                    {
                        "q": "Tìm nguyên hàm $I = \\int x \\cos x\\,dx$.",
                        "options": ["$x \\sin x + \\cos x + C$", "$x \\sin x - \\cos x + C$", "$-x \\sin x + \\cos x + C$", "$x \\cos x + \\sin x + C$"],
                        "answer": "A",
                        "solution": "Đặt $u = x, dv = \\cos x\\,dx \\Rightarrow I = x\\sin x + \\cos x + C$."
                    },
                    {
                        "q": "Tính tích phân $I = \\int_0^{\\frac{\\pi}{2}} x \\sin x\\,dx$.",
                        "options": ["$1$", "$\\frac{\\pi}{2}$", "$\\frac{\\pi}{2} - 1$", "$2$"],
                        "answer": "A",
                        "solution": "Đặt $u = x, dv = \\sin x\\,dx \\Rightarrow I = 1$."
                    }
                ]
            },
            {
                "id": "4.6",
                "name": "Dạng 4.6: Tích phân từng phần - Cặp [Đa thức x Mũ] (Nhì Đa, Tứ Mũ)",
                "tip": "Đặt $u = P(x)$ và $dv = e^{kx}\\,dx$.",
                "questions": [
                    {
                        "q": "Họ nguyên hàm của hàm số $f(x) = (2x - 3)e^x$ là:",
                        "options": ["$(2x - 5)e^x + C$", "$(2x - 1)e^x + C$", "$(2x - 3)e^x + C$", "$2e^x + C$"],
                        "answer": "A",
                        "solution": "Đặt $u = 2x-3, dv = e^x\\,dx \\Rightarrow I = (2x-5)e^x + C$."
                    },
                    {
                        "q": "Tính tích phân $I = \\int_0^1 (x + 2)e^{2x}\\,dx$.",
                        "options": ["$\\frac{5e^2 - 3}{4}$", "$\\frac{3e^2 + 5}{4}$", "$\\frac{3e^2 - 1}{4}$", "$\\frac{e^2 + 2}{2}$"],
                        "answer": "A",
                        "solution": "Đặt $u = x+2, dv = e^{2x}\\,dx \\Rightarrow I = \\frac{5e^2 - 3}{4}$."
                    }
                ]
            },
            {
                "id": "4.7",
                "name": "Dạng 4.7: Tích phân từng phần - Cặp [Lượng giác x Mũ] (Tích phân Luân hồi)",
                "tip": "Từng phần 2 lần xuất hiện lại tích phân ban đầu: $I = g(x) - k^2 I \\Rightarrow I = \\frac{g(x)}{1+k^2}$.",
                "questions": [
                    {
                        "q": "Họ nguyên hàm của hàm số $f(x) = e^x \\sin x$ là:",
                        "options": ["$\\frac{1}{2}e^x(\\sin x - \\cos x) + C$", "$\\frac{1}{2}e^x(\\sin x + \\cos x) + C$", "$e^x(\\sin x - \\cos x) + C$", "$\\frac{1}{2}e^x(\\cos x - \\sin x) + C$"],
                        "answer": "A",
                        "solution": "Từng phần 2 lần thu được $2I = e^x(\\sin x - \\cos x) \\Rightarrow I = \\frac{1}{2}e^x(\\sin x - \\cos x) + C$."
                    },
                    {
                        "q": "Họ nguyên hàm $\\int e^x \\cos x\\,dx$ bằng:",
                        "options": ["$\\frac{1}{2}e^x(\\cos x + \\sin x) + C$", "$\\frac{1}{2}e^x(\\cos x - \\sin x) + C$", "$e^x(\\cos x + \\sin x) + C$", "$\\frac{1}{2}e^x \\sin 2x + C$"],
                        "answer": "A",
                        "solution": "$\\int e^x \\cos x\\,dx = \\frac{1}{2}e^x(\\cos x + \\sin x) + C$."
                    }
                ]
            },
            {
                "id": "4.8",
                "name": "Dạng 4.8: Phương pháp Tích phân Từng phần Múa cột (Tabular Integration)",
                "tip": "Cột D: Đa thức đạo hàm về 0; Cột I: Nguyên hàm hàm mũ/lượng giác. Nối chéo xen kẽ $+ - + -$.",
                "questions": [
                    {
                        "q": "Tính nguyên hàm $I = \\int (x^2 - 2x + 3)e^x\\,dx$ bằng phương pháp múa cột. Kết quả là:",
                        "options": ["$(x^2 - 4x + 7)e^x + C$", "$(x^2 - 2x + 1)e^x + C$", "$(x^2 + 4x + 3)e^x + C$", "$(x^2 - 4x + 5)e^x + C$"],
                        "answer": "A",
                        "solution": "Múa cột: $(x^2-2x+3)e^x - (2x-2)e^x + 2e^x = (x^2 - 4x + 7)e^x + C$."
                    },
                    {
                        "q": "Nguyên hàm $\\int x^2 \\cos x\\,dx$ bằng:",
                        "options": ["$(x^2 - 2)\\sin x + 2x\\cos x + C$", "$(x^2 + 2)\\sin x - 2x\\cos x + C$", "$x^2 \\sin x - 2x\\cos x + C$", "$(x^2 - 2)\\cos x + 2x\\sin x + C$"],
                        "answer": "A",
                        "solution": "Múa cột: $x^2\\sin x - 2x(-\\cos x) + 2(-\\sin x) = (x^2-2)\\sin x + 2x\\cos x + C$."
                    }
                ]
            },
            {
                "id": "4.9",
                "name": "Dạng 4.9: Đổi biến số Loại 1 (Vi phân nhanh $u = g(x)$)",
                "tip": "$\\int f(g(x)) g'(x)\\,dx = \\int f(u)\\,du$.",
                "questions": [
                    {
                        "q": "Tính tích phân $I = \\int_0^1 x \\sqrt{x^2 + 1}\\,dx$.",
                        "options": ["$\\frac{2\\sqrt{2} - 1}{3}$", "$\\frac{2\\sqrt{2} + 1}{3}$", "$\\frac{\\sqrt{2} - 1}{3}$", "$2\\sqrt{2} - 1$"],
                        "answer": "A",
                        "solution": "Đặt $u = \\sqrt{x^2+1} \\Rightarrow I = \\frac{2\\sqrt{2}-1}{3}$."
                    },
                    {
                        "q": "Tính tích phân $I = \\int_0^{\\frac{\\pi}{2}} \\sin^3 x \\cos x\\,dx$.",
                        "options": ["$\\frac{1}{4}$", "$\\frac{1}{3}$", "$1$", "$\\frac{1}{2}$"],
                        "answer": "A",
                        "solution": "Đặt $u = \\sin x \\Rightarrow I = [\\frac{u^4}{4}]_0^1 = \\frac{1}{4}$."
                    }
                ]
            },
            {
                "id": "4.10",
                "name": "Dạng 4.10: Đổi biến số Loại 2 (Lượng giác hóa $x = a\\sin t, x = a\\tan t$)",
                "tip": "Chứa $\\sqrt{a^2 - x^2}$ đặt $x = a\\sin t$; Chứa $\\frac{1}{x^2+a^2}$ đặt $x = a\\tan t$.",
                "questions": [
                    {
                        "q": "Tính tích phân $I = \\int_0^1 \\sqrt{1 - x^2}\\,dx$.",
                        "options": ["$\\frac{\\pi}{4}$", "$\\frac{\\pi}{2}$", "$\\pi$", "$\\frac{1}{2}$"],
                        "answer": "A",
                        "solution": "Đặt $x = \\sin t \\Rightarrow I = \\frac{\\pi}{4}$."
                    },
                    {
                        "q": "Tính tích phân $I = \\int_0^1 \\frac{1}{x^2 + 1}\\,dx$.",
                        "options": ["$\\frac{\\pi}{4}$", "$\\frac{\\pi}{2}$", "$\\frac{\\pi}{3}$", "$1$"],
                        "answer": "A",
                        "solution": "Đặt $x = \\tan t \\Rightarrow I = \\frac{\\pi}{4}$."
                    }
                ]
            },
            {
                "id": "4.11",
                "name": "Dạng 4.11: Tích phân của hàm cho bởi nhiều công thức (Hàm từng khúc - Piecewise)",
                "tip": "Tách tích phân theo điểm nối $c$: $\\int_a^b f(x)\\,dx = \\int_a^c f_1(x)\\,dx + \\int_c^b f_2(x)\\,dx$.",
                "questions": [
                    {
                        "q": "Cho hàm số $f(x) = \\begin{cases} 2x & \\text{khi } x \\ge 1 \\\\ 3x^2 - 1 & \\text{khi } x < 1 \\end{cases}$. Tính tích phân $I = \\int_0^2 f(x)\\,dx$.",
                        "options": ["$3$", "$4$", "$2$", "$5$"],
                        "answer": "A",
                        "solution": "Tách tích phân tại $x = 1$: $I = \\int_0^1 (3x^2 - 1)\\,dx + \\int_1^2 2x\\,dx = [x^3 - x]_0^1 + [x^2]_1^2 = (1 - 1) + (4 - 1) = 3$."
                    },
                    {
                        "q": "Cho hàm số $f(x) = |x - 1| + 2$. Tính tích phân $I = \\int_0^3 f(x)\\,dx$.",
                        "options": ["$\\frac{17}{2}$", "$8$", "$9$", "$\\frac{15}{2}$"],
                        "answer": "A",
                        "solution": "Tách tích phân: $I = \\int_0^1 (1 - x + 2)\\,dx + \\int_1^3 (x - 1 + 2)\\,dx = \\int_0^1 (3 - x)\\,dx + \\int_1^3 (x + 1)\\,dx = [3x - \\frac{x^2}{2}]_0^1 + [\\frac{x^2}{2} + x]_1^3 = \\frac{5}{2} + 6 = \\frac{17}{2}$."
                    }
                ]
            },
            {
                "id": "4.12",
                "name": "Dạng 4.12: Ứng dụng tích phân tính Diện tích hình phẳng",
                "tip": "Diện tích giữa 2 parabol / đường thẳng cắt nhau: $S = \\int |f - g|\\,dx$. Parabol Archimedes: $S = \\frac{|a|}{6}(x_2 - x_1)^3$.",
                "questions": [
                    {
                        "q": "Diện tích hình phẳng giới hạn bởi đồ thị hàm số $y = -x^2 + 4$ và trục hoành $Ox$ bằng:",
                        "options": ["$\\frac{32}{3}$", "$\\frac{16}{3}$", "$16$", "$\\frac{8}{3}$"],
                        "answer": "A",
                        "solution": "$S = \\frac{1}{6}(2 - (-2))^3 = \\frac{64}{6} = \\frac{32}{3}$."
                    },
                    {
                        "q": "Tính diện tích hình phẳng giới hạn bởi 2 đường cong $y = x^2$ và $y = 2x$.",
                        "options": ["$\\frac{4}{3}$", "$\\frac{2}{3}$", "$2$", "$\\frac{1}{3}$"],
                        "answer": "A",
                        "solution": "$S = \\int_0^2 (2x - x^2)\\,dx = 4 - \\frac{8}{3} = \\frac{4}{3}$."
                    }
                ]
            },
            {
                "id": "4.13",
                "name": "Dạng 4.13: Ứng dụng tích phân tính Thể tích khối tròn xoay quanh trục Ox",
                "tip": "$V = \\pi \\int_a^b [f(x)]^2\\,dx$.",
                "questions": [
                    {
                        "q": "Thể tích khối tròn xoay khi quay hình phẳng giới hạn bởi $y = \\sqrt{x}, y = 0, x = 1, x = 4$ quanh trục $Ox$ bằng:",
                        "options": ["$\\frac{15\\pi}{2}$", "$\\frac{15}{2}$", "$\\frac{7\\pi}{3}$", "$15\\pi$"],
                        "answer": "A",
                        "solution": "$V = \\pi \\int_1^4 x\\,dx = \\frac{15\\pi}{2}$."
                    },
                    {
                        "q": "Tính thể tích khối tròn xoay tạo thành khi quay quanh trục $Ox$ hình phẳng giới hạn bởi $y = \\sin x, y = 0, x = 0, x = \\pi$.",
                        "options": ["$\\frac{\\pi^2}{2}$", "$\\pi^2$", "$\\frac{\\pi}{2}$", "$2\\pi$"],
                        "answer": "A",
                        "solution": "$V = \\pi \\int_0^\\pi \\sin^2 x\\,dx = \\frac{\\pi^2}{2}$."
                    }
                ]
            },
            {
                "id": "4.14",
                "name": "Dạng 4.14: Thể tích vật thể bất kỳ biết diện tích mặt cắt $S(x)$ vuông góc trục Ox",
                "tip": "Thể tích $V = \\int_a^b S(x)\\,dx$ (với $S(x)$ là diện tích thiết diện tại điểm có hoành độ $x$). Chú ý: Không có nhân $\\pi$ ở công thức này!",
                "questions": [
                    {
                        "q": "Một vật thể nằm giữa hai mặt phẳng $x = 0$ và $x = 3$. Thiết diện của vật thể cắt bởi mặt phẳng vuông góc với trục $Ox$ tại điểm có hoành độ $x$ ($0 \\le x \\le 3$) là một hình vuông có cạnh bằng $\\sqrt{9 - x^2}$. Thể tích của vật thể đó bằng:",
                        "options": ["$18$", "$18\\pi$", "$9$", "$27$"],
                        "answer": "A",
                        "solution": "Diện tích thiết diện là $S(x) = (\\sqrt{9 - x^2})^2 = 9 - x^2$. Thể tích vật thể là $V = \\int_0^3 S(x)\\,dx = \\int_0^3 (9 - x^2)\\,dx = [9x - \\frac{x^3}{3}]_0^3 = 27 - 9 = 18$ (Không nhân $\\pi$)."
                    },
                    {
                        "q": "Cắt một vật thể bởi mặt phẳng vuông góc trục $Ox$ tại hoành độ $x$ ($0 \\le x \\le \\pi$) thu được thiết diện là một tam giác đều có diện tích $S(x) = \\sqrt{3}\\sin x$. Thể tích của vật thể bằng:",
                        "options": ["$2\\sqrt{3}$", "$\\sqrt{3}\\pi$", "$2\\sqrt{3}\\pi$", "$\\sqrt{3}$"],
                        "answer": "A",
                        "solution": "Thể tích $V = \\int_0^\\pi S(x)\\,dx = \\int_0^\\pi \\sqrt{3}\\sin x\\,dx = [-\\sqrt{3}\\cos x]_0^\\pi = \\sqrt{3} - (-\\sqrt{3}) = 2\\sqrt{3}$."
                    }
                ]
            },
            {
                "id": "4.15",
                "name": "Dạng 4.15: Ứng dụng tích phân giải Phương trình vi phân hàm ẩn & Bài toán vật lý",
                "tip": "Quãng đường $s(t) = \\int v(t)\\,dt$. Với $f'(x) + p(x)f(x) = 0 \\Rightarrow f(x) = C e^{-\\int p(x)\\,dx}$.",
                "questions": [
                    {
                        "q": "Một ô tô phanh chậm dần đều với vận tốc $v(t) = -2t + 10\\text{ (m/s)}$. Từ lúc đạp phanh đến khi dừng hẳn, ô tô đi được quãng đường bao nhiêu mét?",
                        "options": ["$25\\text{ m}$", "$50\\text{ m}$", "$20\\text{ m}$", "$30\\text{ m}$"],
                        "answer": "A",
                        "solution": "Dừng hẳn khi $v(t) = 0 \\Leftrightarrow t = 5\\text{ s}$. Quãng đường $s = \\int_0^5 (-2t + 10)\\,dt = 25\\text{ m}$."
                    },
                    {
                        "q": "Cho hàm số $f(x)$ liên tục thỏa mãn $f'(x) + 2f(x) = 0$ và $f(0) = 3$. Giá trị $f(1)$ bằng:",
                        "options": ["$3e^{-2}$", "$3e^2$", "$e^{-2}$", "$3e^{-1}$"],
                        "answer": "A",
                        "solution": "Nhân 2 vế với $e^{2x} \\Rightarrow f(x) = 3e^{-2x} \\Rightarrow f(1) = 3e^{-2}$."
                    }
                ]
            }
        ]
    },

    # =========================================================================
    # CHƯƠNG 5: PHƯƠNG PHÁP TỌA ĐỘ TRONG KHÔNG GIAN OXYZ (13 dạng = 26 câu)
    # =========================================================================
    {
        "id": "ch5",
        "title": "Chương 5: Phương Pháp Tọa Độ Trong Không Gian (Oxyz)",
        "badge": "13 Dạng • 26 Câu",
        "subtopics": [
            {
                "id": "5.1",
                "name": "Dạng 5.1: Phương trình Mặt Cầu trong không gian Oxyz",
                "tip": "Mặt cầu $(x-a)^2+(y-b)^2+(z-c)^2=R^2$ có tâm $I(a; b; c)$, bán kính $R$. Khai triển: $R = \\sqrt{a^2+b^2+c^2-d} > 0$.",
                "questions": [
                    {
                        "q": "Mặt cầu $(S): x^2 + y^2 + z^2 - 2x + 4y - 6z - 2 = 0$ có tâm $I$ và bán kính $R$ là:",
                        "options": ["$I(1; -2; 3), R = 4$", "$I(-1; 2; -3), R = 4$", "$I(1; -2; 3), R = 16$", "$I(1; -2; 3), R = \\sqrt{12}$"],
                        "answer": "A",
                        "solution": "$I(1; -2; 3), R = \\sqrt{1 + 4 + 9 - (-2)} = 4$."
                    },
                    {
                        "q": "Phương trình mặt cầu có đường kính $AB$ với $A(1; 2; 0)$ và $B(-1; 4; 2)$ là:",
                        "options": ["$x^2 + (y - 3)^2 + (z - 1)^2 = 3$", "$x^2 + (y - 3)^2 + (z - 1)^2 = 12$", "$(x - 1)^2 + (y - 2)^2 + z^2 = 3$", "$x^2 + (y + 3)^2 + (z + 1)^2 = 3$"],
                        "answer": "A",
                        "solution": "Tâm $I(0; 3; 1)$, bán kính $R = \\frac{AB}{2} = \\sqrt{3} \\Rightarrow R^2 = 3$."
                    }
                ]
            },
            {
                "id": "5.2",
                "name": "Dạng 5.2: Vị trí tương đối giữa Mặt Cầu và Mặt Phẳng (Tiếp xúc & Cắt theo đường tròn)",
                "tip": "Khoảng cách $d = d(I, (P))$. Nếu $d = R$: Tiếp xúc; nếu $d < R$: Cắt theo đường tròn có bán kính $r = \\sqrt{R^2 - d^2}$.",
                "questions": [
                    {
                        "q": "Mặt cầu $(S): x^2 + y^2 + z^2 = 9$ cắt mặt phẳng $(P): x + 2y - 2z + 6 = 0$ theo giao tuyến là một đường tròn có bán kính $r$ bằng:",
                        "options": ["$\\sqrt{5}$", "$3$", "$2$", "$\\sqrt{13}$"],
                        "answer": "A",
                        "solution": "Tâm $I(0; 0; 0)$, bán kính $R = 3$. Khoảng cách $d(I, (P)) = \\frac{|6|}{\\sqrt{1+4+4}} = \\frac{6}{3} = 2$. Bán kính đường tròn giao tuyến là $r = \\sqrt{R^2 - d^2} = \\sqrt{3^2 - 2^2} = \\sqrt{5}$."
                    },
                    {
                        "q": "Tìm $m$ để mặt phẳng $(P): 2x - y + 2z + m = 0$ tiếp xúc với mặt cầu $(S): (x-1)^2 + (y+1)^2 + z^2 = 4$.",
                        "options": ["$m = 3$ hoặc $m = -9$", "$m = 6$ hoặc $m = -6$", "$m = 9$ hoặc $m = -3$", "$m = 3$"],
                        "answer": "A",
                        "solution": "Tâm $I(1; -1; 0)$, bán kính $R = 2$. Tiếp xúc $\\Leftrightarrow d(I, (P)) = R \\Leftrightarrow \\frac{|2(1) - (-1) + 0 + m|}{\\sqrt{4+1+4}} = 2 \\Leftrightarrow \\frac{|m+3|}{3} = 2 \\Leftrightarrow |m+3| = 6 \\Leftrightarrow m = 3$ hoặc $m = -9$."
                    }
                ]
            },
            {
                "id": "5.3",
                "name": "Dạng 5.3: Phương trình Mặt Phẳng (Điểm & VTPT, Đoạn chắn, Trung trực)",
                "tip": "Mặt phẳng đoạn chắn qua $(a;0;0), (0;b;0), (0;0;c)$: $\\frac{x}{a}+\\frac{y}{b}+\\frac{z}{c}=1$. Trung trực của $AB$: đi qua trung điểm và nhận $\\vec{AB}$ làm VTPT.",
                "questions": [
                    {
                        "q": "Mặt phẳng đi qua 3 điểm $A(2; 0; 0), B(0; -3; 0), C(0; 0; 4)$ có phương trình là:",
                        "options": ["$\\frac{x}{2} + \\frac{y}{-3} + \\frac{z}{4} = 1$", "$\\frac{x}{2} + \\frac{y}{3} + \\frac{z}{4} = 1$", "$6x - 4y + 3z = 0$", "$\\frac{x}{2} + \\frac{y}{-3} + \\frac{z}{4} = 0$"],
                        "answer": "A",
                        "solution": "Phương trình đoạn chắn: $\\frac{x}{2} + \\frac{y}{-3} + \\frac{z}{4} = 1$."
                    },
                    {
                        "q": "Phương trình mặt phẳng trung trực của $AB$ với $A(1; 3; -2)$ và $B(3; -1; 4)$ là:",
                        "options": ["$x - 2y + 3z - 3 = 0$", "$x - 2y + 3z + 3 = 0$", "$2x - 4y + 6z - 1 = 0$", "$x + y + z - 4 = 0$"],
                        "answer": "A",
                        "solution": "Trung điểm $M(2; 1; 1)$, VTPT $\\vec{n} = (1; -2; 3) \\Rightarrow x - 2y + 3z - 3 = 0$."
                    }
                ]
            },
            {
                "id": "5.4",
                "name": "Dạng 5.4: Mặt phẳng đi qua 1 điểm và song song mp khác / tiếp xúc mặt cầu",
                "tip": "Song song với $(P): Ax+By+Cz+D=0$ thì có dạng $Ax+By+Cz+D'=0$ ($D' \\ne D$). Tiếp xúc mặt cầu thì $d(I, (P)) = R$.",
                "questions": [
                    {
                        "q": "Mặt phẳng đi qua điểm $M(1; 2; -3)$ và song song với mặt phẳng $(P): 3x - 2y + z + 5 = 0$ có phương trình là:",
                        "options": ["$3x - 2y + z + 4 = 0$", "$3x - 2y + z - 4 = 0$", "$3x - 2y + z + 5 = 0$", "$x + 2y - 3z + 4 = 0$"],
                        "answer": "A",
                        "solution": "Mặt phẳng có dạng $3x - 2y + z + D = 0$. Đi qua $M(1; 2; -3) \\Rightarrow 3(1) - 2(2) + (-3) + D = 0 \\Leftrightarrow -4 + D = 0 \\Leftrightarrow D = 4$. Phương trình là $3x - 2y + z + 4 = 0$."
                    },
                    {
                        "q": "Mặt phẳng tiếp xúc với mặt cầu $(S): x^2 + y^2 + z^2 = 9$ tại điểm $M(1; 2; -2)$ có phương trình là:",
                        "options": ["$x + 2y - 2z - 9 = 0$", "$x + 2y - 2z + 9 = 0$", "$x + 2y - 2z - 3 = 0$", "$2x + y - 2z - 9 = 0$"],
                        "answer": "A",
                        "solution": "Tâm $O(0; 0; 0)$. VTPT của tiếp diện là $\\vec{OM} = (1; 2; -2)$. Phương trình tiếp diện tại $M$: $1(x - 1) + 2(y - 2) - 2(z + 2) = 0 \\Leftrightarrow x + 2y - 2z - 9 = 0$."
                    }
                ]
            },
            {
                "id": "5.5",
                "name": "Dạng 5.5: Phương trình Đường Thẳng (Tham số & Chính tắc)",
                "tip": "Tham số $\\begin{cases} x=x_0+at \\\\ y=y_0+bt \\\\ z=z_0+ct \\end{cases}$; Chính tắc $\\frac{x-x_0}{a} = \\frac{y-y_0}{b} = \\frac{z-z_0}{c}$.",
                "questions": [
                    {
                        "q": "Đường thẳng qua $M(1; -2; 3)$ có VTCP $\\vec{u} = (2; -1; 4)$ có phương trình chính tắc là:",
                        "options": ["$\\frac{x - 1}{2} = \\frac{y + 2}{-1} = \\frac{z - 3}{4}$", "$\\frac{x + 1}{2} = \\frac{y - 2}{-1} = \\frac{z + 3}{4}$", "$\\frac{x - 2}{1} = \\frac{y + 1}{-2} = \\frac{z - 4}{3}$", "$\\frac{x - 1}{2} = \\frac{y - 2}{-1} = \\frac{z - 3}{4}$"],
                        "answer": "A",
                        "solution": "$\\frac{x - 1}{2} = \\frac{y + 2}{-1} = \\frac{z - 3}{4}$."
                    },
                    {
                        "q": "Đường thẳng qua $A(2; 1; -1)$ vuông góc với $(P): 2x - 3y + z + 1 = 0$ có phương trình tham số là:",
                        "options": ["$\\begin{cases} x = 2 + 2t \\\\ y = 1 - 3t \\\\ z = -1 + t \\end{cases}$", "$\\begin{cases} x = 2 + 2t \\\\ y = -3 + t \\\\ z = 1 - t \\end{cases}$", "$\\begin{cases} x = 2 - 2t \\\\ y = 1 - 3t \\\\ z = -1 - t \\end{cases}$", "$\\begin{cases} x = 1 + 2t \\\\ y = -2 - 3t \\\\ z = 3 + t \\end{cases}$"],
                        "answer": "A",
                        "solution": "VTCP $\\vec{u} = \\vec{n}_P = (2; -3; 1)$."
                    }
                ]
            },
            {
                "id": "5.6",
                "name": "Dạng 5.6: Phương trình Đường Thẳng là giao tuyến của 2 mặt phẳng",
                "tip": "VTCP $\\vec{u} = [\\vec{n}_1, \\vec{n}_2]$. Tìm một điểm chung $M_0$ bằng cách cho một biến bất kỳ bằng 0 (chẳng hạn $z = 0$).",
                "questions": [
                    {
                        "q": "Vectơ chỉ phương của đường thẳng $d$ là giao tuyến của hai mặt phẳng $(\\alpha): x + y - z + 1 = 0$ và $(\\beta): 2x - y + z - 4 = 0$ là:",
                        "options": ["$\\vec{u} = (0; 3; 3)$", "$\\vec{u} = (1; 0; 1)$", "$\\vec{u} = (3; 1; 0)$", "$\\vec{u} = (2; -1; 1)$"],
                        "answer": "A",
                        "solution": "Ta có $\\vec{n}_1 = (1; 1; -1)$ và $\\vec{n}_2 = (2; -1; 1)$. VTCP $\\vec{u} = [\\vec{n}_1, \\vec{n}_2] = (1(1)-(-1)(-1); (-1)(2)-1(1); 1(-1)-1(2)) = (0; -3; -3) = -3(0; 1; 1)$. Chọn $\\vec{u} = (0; 3; 3)$ cùng phương."
                    },
                    {
                        "q": "Giao tuyến của hai mặt phẳng $(P): x - y + 2 = 0$ và $(Q): y + z - 3 = 0$ đi qua điểm nào sau đây?",
                        "options": ["$M(0; 2; 1)$", "$M(1; 1; 2)$", "$M(2; 0; 3)$", "$M(0; -2; 5)$"],
                        "answer": "A",
                        "solution": "Cho $x = 0 \\Rightarrow y = 2 \\Rightarrow z = 3 - 2 = 1$. Điểm $M(0; 2; 1)$ thuộc cả 2 mặt phẳng."
                    }
                ]
            },
            {
                "id": "5.7",
                "name": "Dạng 5.7: Vị trí tương đối của hai đường thẳng (Song song, Cắt nhau, Chéo nhau)",
                "tip": "Cùng phương: Trùng hoặc Song song. Không cùng phương: $[\\vec{u}_1, \\vec{u}_2] \\cdot \\vec{M_1 M_2} = 0 \\Rightarrow$ Cắt nhau; $\\ne 0 \\Rightarrow$ Chéo nhau.",
                "questions": [
                    {
                        "q": "Xét vị trí tương đối của $d_1: \\frac{x-1}{1} = \\frac{y-2}{2} = \\frac{z-3}{3}$ và $d_2: \\frac{x-2}{2} = \\frac{y-4}{4} = \\frac{z-6}{6}$.",
                        "options": ["$d_1$ trùng với $d_2$", "$d_1$ song song với $d_2$", "$d_1$ cắt $d_2$", "$d_1$ chéo $d_2$"],
                        "answer": "A",
                        "solution": "Hai VTCP cùng phương và điểm $M_1(1; 2; 3) \\in d_2 \\Rightarrow$ Trùng nhau."
                    },
                    {
                        "q": "Hai đường thẳng $d_1: \\frac{x-1}{2} = \\frac{y}{1} = \\frac{z+1}{-1}$ và $d_2: \\frac{x}{1} = \\frac{y-1}{1} = \\frac{z}{1}$ có vị trí tương đối là:",
                        "options": ["Chéo nhau", "Cắt nhau", "Song song", "Vuông góc và cắt nhau"],
                        "answer": "A",
                        "solution": "Tích hỗn tạp $[\\vec{u}_1, \\vec{u}_2] \\cdot \\vec{M_1 M_2} = -4 \\ne 0 \\Rightarrow$ Chéo nhau."
                    }
                ]
            },
            {
                "id": "5.8",
                "name": "Dạng 5.8: Vị trí tương đối giữa đường thẳng và mặt phẳng",
                "tip": "Thay PT tham số của đường thẳng vào PT mặt phẳng để giải $t$.",
                "questions": [
                    {
                        "q": "Tọa độ giao điểm của $d: \\begin{cases} x = 1 + t \\\\ y = 2 - t \\\\ z = 1 + 2t \\end{cases}$ và $(P): x + y + z - 6 = 0$ là:",
                        "options": ["$(2; 1; 3)$", "$(1; 2; 1)$", "$(3; 0; 5)$", "$(0; 3; -1)$"],
                        "answer": "A",
                        "solution": "$(1+t) + (2-t) + (1+2t) - 6 = 0 \\Leftrightarrow 2t = 2 \\Leftrightarrow t = 1 \\Rightarrow (2; 1; 3)$."
                    },
                    {
                        "q": "Tìm $m$ để đường thẳng $d: \\begin{cases} x = 1 + 2t \\\\ y = t \\\\ z = -1 + mt \\end{cases}$ song song với $(P): x - 2y + z + 3 = 0$.",
                        "options": ["$m = 0$", "$m = 2$", "$m = -2$", "$m = 1$"],
                        "answer": "A",
                        "solution": "$\\vec{u} \\cdot \\vec{n} = 2(1) - 2(1) + m(1) = 0 \\Leftrightarrow m = 0$."
                    }
                ]
            },
            {
                "id": "5.9",
                "name": "Dạng 5.9: Hình chiếu vuông góc và Điểm đối xứng qua mặt phẳng / đường thẳng trong Oxyz",
                "tip": "Tìm hình chiếu $H$ của $M$ lên $(P)$: Viết đường thẳng $\\Delta$ qua $M$ vuông góc $(P)$, tìm giao điểm $H = \\Delta \\cap (P)$. Điểm đối xứng $M' = 2H - M$.",
                "questions": [
                    {
                        "q": "Tìm tọa độ hình chiếu vuông góc $H$ của điểm $M(1; 4; 2)$ lên mặt phẳng $(P): x + y + z - 1 = 0$.",
                        "options": ["$H(-1; 2; 0)$", "$H(0; 2; -1)$", "$H(1; 1; -1)$", "$H(-2; 1; 2)$"],
                        "answer": "A",
                        "solution": "Đường thẳng qua $M$ vuông góc $(P)$: $\\begin{cases} x = 1 + t \\\\ y = 4 + t \\\\ z = 2 + t \\end{cases}$. Thay vào $(P)$: $(1+t) + (4+t) + (2+t) - 1 = 0 \\Leftrightarrow 3t + 6 = 0 \\Leftrightarrow t = -2$. Thay $t = -2$ được $H(-1; 2; 0)$."
                    },
                    {
                        "q": "Điểm đối xứng $M'$ của điểm $M(1; 4; 2)$ qua mặt phẳng $(P): x + y + z - 1 = 0$ có tọa độ là:",
                        "options": ["$M'(-3; 0; -2)$", "$M'(-1; 2; 0)$", "$M'(3; 8; 6)$", "$M'(-2; 0; -1)$"],
                        "answer": "A",
                        "solution": "Từ hình chiếu $H(-1; 2; 0)$, điểm đối xứng là $M' = 2H - M = 2(-1; 2; 0) - (1; 4; 2) = (-3; 0; -2)$."
                    }
                ]
            },
            {
                "id": "5.10",
                "name": "Dạng 5.10: Khoảng cách trong Oxyz (Điểm đến mp, 2 mp song song, 2 đt chéo nhau)",
                "tip": "$d(M, (P)) = \\frac{|Ax_0+By_0+Cz_0+D|}{\\sqrt{A^2+B^2+C^2}}$. Khoảng cách 2 đt chéo nhau: $d = \\frac{|[\\vec{u}_1, \\vec{u}_2] \\cdot \\vec{M_1 M_2}|}{|[\\vec{u}_1, \\vec{u}_2]|}$.",
                "questions": [
                    {
                        "q": "Khoảng cách từ điểm $M(1; 2; -3)$ đến $(P): 2x - 2y + z - 3 = 0$ bằng:",
                        "options": ["$\\frac{8}{3}$", "$8$", "$\\frac{4}{3}$", "$2$"],
                        "answer": "A",
                        "solution": "$d(M, (P)) = \\frac{|2(1) - 2(2) + 1(-3) - 3|}{\\sqrt{4+4+1}} = \\frac{8}{3}$."
                    },
                    {
                        "q": "Khoảng cách giữa hai mặt phẳng song song $(P): 2x + y - 2z + 1 = 0$ và $(Q): 2x + y - 2z - 8 = 0$ bằng:",
                        "options": ["$3$", "$9$", "$1$", "$\\frac{7}{3}$"],
                        "answer": "A",
                        "solution": "$d = \\frac{|1 - (-8)|}{\\sqrt{4+1+4}} = \\frac{9}{3} = 3$."
                    }
                ]
            },
            {
                "id": "5.11",
                "name": "Dạng 5.11: Góc trong Oxyz (Góc giữa 2 mp, giữa 2 đường thẳng, giữa đt và mp)",
                "tip": "Góc giữa 2 mp: $\\cos = \\frac{|\\vec{n}_1 \\cdot \\vec{n}_2|}{|\\vec{n}_1||\\vec{n}_2|}$. Góc giữa đt và mp: $\\sin = \\frac{|\\vec{u} \\cdot \\vec{n}|}{|\\vec{u}||\\vec{n}|}$.",
                "questions": [
                    {
                        "q": "Côsin của góc giữa hai mặt phẳng $(P): x + y - 1 = 0$ và $(Q): y + z + 2 = 0$ bằng:",
                        "options": ["$\\frac{1}{2}$", "$\\frac{\\sqrt{2}}{2}$", "$\\frac{\\sqrt{3}}{2}$", "$0$"],
                        "answer": "A",
                        "solution": "$\\cos \\varphi = \\frac{|1(0) + 1(1) + 0(1)|}{\\sqrt{2} \\cdot \\sqrt{2}} = \\frac{1}{2}$."
                    },
                    {
                        "q": "Sin của góc giữa $d: \\frac{x-1}{1} = \\frac{y}{2} = \\frac{z+1}{-1}$ và $(P): 2x + y + z - 5 = 0$ bằng:",
                        "options": ["$\\frac{1}{2}$", "$\\frac{\\sqrt{3}}{2}$", "$\\frac{1}{6}$", "$\\frac{\\sqrt{2}}{2}$"],
                        "answer": "A",
                        "solution": "$\\sin \\theta = \\frac{|1(2) + 2(1) - 1(1)|}{\\sqrt{6} \\cdot \\sqrt{6}} = \\frac{3}{6} = \\frac{1}{2}$."
                    }
                ]
            },
            {
                "id": "5.12",
                "name": "Dạng 5.12: Đường vuông góc chung của hai đường thẳng chéo nhau",
                "tip": "VTCP của đường vuông góc chung là $\\vec{u} = [\\vec{u}_1, \\vec{u}_2]$. Đoạn vuông góc chung $MN$ nối $M \\in d_1$ và $N \\in d_2$ thỏa mãn $\\vec{MN} \\perp \\vec{u}_1$ và $\\vec{MN} \\perp \\vec{u}_2$.",
                "questions": [
                    {
                        "q": "Vectơ chỉ phương của đường vuông góc chung của hai đường thẳng chéo nhau $d_1: \\frac{x-1}{1} = \\frac{y}{2} = \\frac{z}{1}$ và $d_2: \\frac{x}{2} = \\frac{y-1}{1} = \\frac{z+1}{-1}$ là:",
                        "options": ["$\\vec{u} = (-3; 3; -3)$", "$\\vec{u} = (1; 1; 1)$", "$\\vec{u} = (2; 2; -1)$", "$\\vec{u} = (3; 1; -2)$"],
                        "answer": "A",
                        "solution": "Ta có $\\vec{u}_1 = (1; 2; 1)$ và $\\vec{u}_2 = (2; 1; -1)$. VTCP của đường vuông góc chung là $[\\vec{u}_1, \\vec{u}_2] = (2(-1)-1(1); 1(2)-1(-1); 1(1)-2(2)) = (-3; 3; -3)$."
                    },
                    {
                        "q": "Trong không gian $Oxyz$, trục $Ox$ và đường thẳng $\\Delta: \\begin{cases} x = 0 \\\\ y = 1 \\\\ z = t \\end{cases}$ chéo nhau. Độ dài đoạn vuông góc chung giữa chúng bằng:",
                        "options": ["$1$", "$2$", "$\\sqrt{2}$", "$\\frac{1}{2}$"],
                        "answer": "A",
                        "solution": "Trục $Ox$ nằm trên $(Oxy)$ có $y=0, z=0$. Đường thẳng $\\Delta$ song song trục $Oz$ và có $x=0, y=1$. Đoạn vuông góc chung nối $O(0;0;0)$ và $H(0;1;0)$ có độ dài đúng bằng $1$."
                    }
                ]
            },
            {
                "id": "5.13",
                "name": "Dạng 5.13: Bài toán Cực trị hình học Oxyz & Phương pháp Tâm tỉ cự (Dạng 9+)",
                "tip": "Tâm tỉ cự $I$ thỏa $\\alpha \\vec{IA} + \\beta \\vec{IB} + \\gamma \\vec{IC} = \\vec{0}$. Khi đó $M$ là hình chiếu vuông góc của $I$ lên mp/đt.",
                "questions": [
                    {
                        "q": "Cho $A(1; 2; 1)$ và $B(3; 0; -1)$. Điểm $M \\in (Oxy)$ sao cho $MA^2 + MB^2$ nhỏ nhất là:",
                        "options": ["$M(2; 1; 0)$", "$M(2; 1; 1)$", "$M(1; 1; 0)$", "$M(0; 0; 0)$"],
                        "answer": "A",
                        "solution": "Trung điểm $I(2; 1; 0) \\in (Oxy) \\Rightarrow M \\equiv I(2; 1; 0)$."
                    },
                    {
                        "q": "Cho $A(1; 0; 0), B(0; 2; 0), C(0; 0; 3)$. Điểm $M \\in (P): x + y + z - 10 = 0$ sao cho $|\\vec{MA} + \\vec{MB} + \\vec{MC}|$ nhỏ nhất là hình chiếu của điểm nào lên $(P)$?",
                        "options": ["Trọng tâm $G(\\frac{1}{3}; \\frac{2}{3}; 1)$ của $\\Delta ABC$", "Điểm $A(1; 0; 0)$", "Gốc tọa độ $O(0; 0; 0)$", "Trung điểm $AB$"],
                        "answer": "A",
                        "solution": "$|\\vec{MA} + \\vec{MB} + \\vec{MC}| = 3MG$. Nhỏ nhất khi $M$ là hình chiếu của trọng tâm $G$ lên $(P)$."
                    }
                ]
            }
        ]
    },

    # =========================================================================
    # CHƯƠNG 6: XÁC SUẤT CÓ ĐIỀU KIỆN VÀ ĐỊNH LÝ BAYES (11 dạng = 22 câu)
    # =========================================================================
    {
        "id": "ch6",
        "title": "Chương 6: Xác Suất Có Điều Kiện & Định Lý Bayes",
        "badge": "11 Dạng • 22 Câu",
        "subtopics": [
            {
                "id": "6.1",
                "name": "Dạng 6.1: Xác suất có điều kiện $P(A|B)$ & Bảng thống kê 2 chiều (Contingency Table)",
                "tip": "Công thức: $P(A|B) = \\frac{n(A \\cap B)}{n(B)} = \\frac{P(A \\cap B)}{P(B)}$. Đọc trực tiếp từ dòng/cột tương ứng của bảng 2 chiều.",
                "questions": [
                    {
                        "q": "Khảo sát 100 học sinh: có 60 nam (20 em thích bóng đá) và 40 nữ (10 em thích bóng đá). Chọn ngẫu nhiên 1 học sinh và biết học sinh đó là nam. Xác suất học sinh này thích bóng đá là:",
                        "options": ["$\\frac{1}{3}$", "$\\frac{1}{5}$", "$\\frac{3}{10}$", "$\\frac{1}{2}$"],
                        "answer": "A",
                        "solution": "Không gian mẫu thu hẹp là tập học sinh nam: $n(B) = 60$. Số học sinh nam thích bóng đá là $n(A \\cap B) = 20$. Xác suất có điều kiện: $P(A|B) = \\frac{20}{60} = \\frac{1}{3}$."
                    },
                    {
                        "q": "Gieo một con xúc xắc 1 lần. Biết số chấm là số chẵn. Xác suất số chấm là số nguyên tố bằng:",
                        "options": ["$\\frac{1}{3}$", "$\\frac{1}{2}$", "$\\frac{1}{6}$", "$\\frac{2}{3}$"],
                        "answer": "A",
                        "solution": "Số chẵn: $\\{2; 4; 6\\}$. Nguyên tố: $\\{2\\}$. Xác suất $P = \\frac{1}{3}$."
                    }
                ]
            },
            {
                "id": "6.2",
                "name": "Dạng 6.2: Quy tắc nhân xác suất & Rút liên tiếp không hoàn lại",
                "tip": "Quy tắc nhân: $P(A_1 \\cap A_2) = P(A_1) \\cdot P(A_2|A_1)$.",
                "questions": [
                    {
                        "q": "Một hộp có 10 viên bi (6 đỏ, 4 xanh). Lấy ngẫu nhiên liên tiếp 2 viên không hoàn lại. Xác suất cả 2 viên đều màu đỏ là:",
                        "options": ["$\\frac{1}{3}$", "$\\frac{3}{5}$", "$\\frac{1}{5}$", "$\\frac{6}{10}$"],
                        "answer": "A",
                        "solution": "$P = \\frac{6}{10} \\cdot \\frac{5}{9} = \\frac{30}{90} = \\frac{1}{3}$."
                    },
                    {
                        "q": "Một lô hàng gồm 20 sản phẩm có 4 phế phẩm. Lấy ngẫu nhiên liên tiếp 2 sản phẩm không hoàn lại. Xác suất lấy được phế phẩm ở lần thứ hai biết lần thứ nhất lấy được sản phẩm tốt là:",
                        "options": ["$\\frac{4}{19}$", "$\\frac{4}{20}$", "$\\frac{3}{19}$", "$\\frac{16}{20}$"],
                        "answer": "A",
                        "solution": "Khi lần 1 đã lấy 1 sản phẩm tốt, trong hộp còn 19 sản phẩm gồm 4 phế phẩm và 15 sản phẩm tốt. Do đó xác suất lấy phế phẩm ở lần 2 là $\\frac{4}{19}$."
                    }
                ]
            },
            {
                "id": "6.3",
                "name": "Dạng 6.3: Quy tắc nhân xác suất mở rộng cho 3 biến cố $P(A \\cap B \\cap C)$",
                "tip": "Công thức chuỗi: $P(A \\cap B \\cap C) = P(A) \\cdot P(B|A) \\cdot P(C|A \\cap B)$.",
                "questions": [
                    {
                        "q": "Một hộp có 5 bi trắng, 4 bi đỏ và 3 bi xanh. Rút ngẫu nhiên 3 viên bi liên tiếp không hoàn lại. Xác suất để lần 1 rút bi trắng, lần 2 rút bi đỏ, lần 3 rút bi xanh là:",
                        "options": ["$\\frac{1}{22}$", "$\\frac{5}{132}$", "$\\frac{1}{11}$", "$\\frac{3}{44}$"],
                        "answer": "A",
                        "solution": "Áp dụng quy tắc nhân 3 biến cố: $P = P(T_1) \\cdot P(\\text{Đ}_2|T_1) \\cdot P(X_3|T_1 \\cap \\text{Đ}_2) = \\frac{5}{12} \\times \\frac{4}{11} \\times \\frac{3}{10} = \\frac{60}{1320} = \\frac{1}{22}$."
                    },
                    {
                        "q": "Một người có chùm chìa khóa gồm 4 chiếc giống hệt nhau, trong đó chỉ có 1 chiếc mở được cửa. Người đó thử từng chìa (chìa nào thử không đúng thì bỏ ra ngoài). Xác suất để người đó mở được cửa đúng ở lần thử thứ 3 là:",
                        "options": ["$\\frac{1}{4}$", "$\\frac{3}{4}$", "$\\frac{1}{12}$", "$\\frac{1}{6}$"],
                        "answer": "A",
                        "solution": "Lần 1 hỏng ($P = \\frac{3}{4}$), lần 2 hỏng ($P = \\frac{2}{3}$), lần 3 trúng ($P = \\frac{1}{2}$). Xác suất $P = \\frac{3}{4} \\times \\frac{2}{3} \\times \\frac{1}{2} = \\frac{1}{4}$."
                    }
                ]
            },
            {
                "id": "6.4",
                "name": "Dạng 6.4: Biến cố độc lập và Tính chất nhân độc lập $P(A \\cap B) = P(A)P(B)$",
                "tip": "Hai biến cố $A, B$ độc lập $\\Leftrightarrow P(A \\cap B) = P(A)P(B)$. Công thức biến cố đối: $P(\\text{ít nhất 1 trúng}) = 1 - P(\\text{tất cả trượt})$.",
                "questions": [
                    {
                        "q": "Hai xạ thủ độc lập bắn vào bia với xác suất trúng là $0.8$ và $0.7$. Xác suất có ít nhất một người bắn trúng bia là:",
                        "options": ["$0.94$", "$0.56$", "$0.80$", "$0.86$"],
                        "answer": "A",
                        "solution": "$P = 1 - (1 - 0.8)(1 - 0.7) = 1 - 0.06 = 0.94$."
                    },
                    {
                        "q": "Cho $P(A) = 0.4$ và $P(B) = 0.5$ độc lập. Xác suất $P(A \\cup B)$ bằng:",
                        "options": ["$0.70$", "$0.90$", "$0.20$", "$0.60$"],
                        "answer": "A",
                        "solution": "$P(A \\cup B) = 0.4 + 0.5 - (0.4)(0.5) = 0.70$."
                    }
                ]
            },
            {
                "id": "6.5",
                "name": "Dạng 6.5: Mô hình Sơ đồ hình cây 2 tầng (Tree Diagram)",
                "tip": "Nhánh 1 biểu diễn biến cố khởi đầu; nhánh 2 biểu diễn xác suất có điều kiện.",
                "questions": [
                    {
                        "q": "Hộp I có 3 bi đỏ, 2 bi xanh. Hộp II có 4 bi đỏ, 1 bi xanh. Chọn ngẫu nhiên một hộp (xác suất $0.5$) rồi rút 1 bi. Xác suất rút được bi đỏ là:",
                        "options": ["$0.70$", "$0.60$", "$0.80$", "$0.50$"],
                        "answer": "A",
                        "solution": "$P = 0.5(\\frac{3}{5}) + 0.5(\\frac{4}{5}) = 0.30 + 0.40 = 0.70$."
                    },
                    {
                        "q": "Một học sinh đi qua 2 ngã tư độc lập. Xác suất gặp đèn đỏ ở ngã tư 1 là $0.4$, ngã tư 2 là $0.3$. Xác suất chỉ gặp đúng 1 đèn đỏ là:",
                        "options": ["$0.46$", "$0.12$", "$0.42$", "$0.58$"],
                        "answer": "A",
                        "solution": "$P = 0.4(0.7) + 0.6(0.3) = 0.28 + 0.18 = 0.46$."
                    }
                ]
            },
            {
                "id": "6.6",
                "name": "Dạng 6.6: Mô hình Sơ đồ hình cây 3 tầng (3-Stage Tree Diagram)",
                "tip": "Xác suất của mỗi lộ trình 3 bước bằng tích của 3 xác suất trên 3 nhánh liên tiếp.",
                "questions": [
                    {
                        "q": "Một hệ thống truyền tin gồm 3 trạm tiếp sóng liên tiếp $A \\to B \\to C$. Xác suất truyền thành công từ $A \\to B$ là $0.9$, từ $B \\to C$ là $0.8$, và từ $C$ đến người nhận là $0.9$. Xác suất bản tin được truyền đến người nhận không bị lỗi là:",
                        "options": ["$0.648$", "$0.720$", "$0.810$", "$0.900$"],
                        "answer": "A",
                        "solution": "Theo sơ đồ cây 3 tầng: $P = 0.9 \\times 0.8 \\times 0.9 = 0.648 = 64.8\\%$."
                    },
                    {
                        "q": "Trong một giải đấu, một kỳ thủ đấu 3 ván cờ độc lập. Xác suất thắng mỗi ván là $0.6$. Dùng sơ đồ cây, xác suất để kỳ thủ này thắng đúng 2 trong 3 ván cờ là:",
                        "options": ["$0.432$", "$0.216$", "$0.288$", "$0.360$"],
                        "answer": "A",
                        "solution": "Có 3 lộ trình thỏa mãn: (Thắng-Thắng-Thua), (Thắng-Thua-Thắng), (Thua-Thắng-Thắng). Mỗi lộ trình có xác suất $0.6 \\times 0.6 \\times 0.4 = 0.144$. Tổng xác suất là $3 \\times 0.144 = 0.432$."
                    }
                ]
            },
            {
                "id": "6.7",
                "name": "Dạng 6.7: Công thức Xác suất toàn phần (2 biến cố phân hoạch)",
                "tip": "$P(B) = P(A)P(B|A) + P(\\bar{A})P(B|\\bar{A})$.",
                "questions": [
                    {
                        "q": "Trong một kho hàng có $60\\%$ hàng loại I (tỷ lệ hỏng $1\\%$) và $40\\%$ hàng loại II (tỷ lệ hỏng $3\\%$). Lấy ngẫu nhiên 1 sản phẩm, xác suất sản phẩm bị hỏng là:",
                        "options": ["$1.8\\%$", "$2.0\\%$", "$4.0\\%$", "$1.2\\%$"],
                        "answer": "A",
                        "solution": "$P = 0.60(0.01) + 0.40(0.03) = 0.006 + 0.012 = 0.018 = 1.8\\%$."
                    },
                    {
                        "q": "Một lớp có $60\\%$ học sinh nữ (trong đó $20\\%$ giỏi toán) và $40\\%$ học sinh nam (trong đó $30\\%$ giỏi toán). Chọn ngẫu nhiên 1 học sinh, xác suất chọn được học sinh giỏi toán là:",
                        "options": ["$0.24$", "$0.20$", "$0.25$", "$0.50$"],
                        "answer": "A",
                        "solution": "$P = 0.60(0.20) + 0.40(0.30) = 0.12 + 0.12 = 0.24$."
                    }
                ]
            },
            {
                "id": "6.8",
                "name": "Dạng 6.8: Công thức Xác suất toàn phần (3 biến cố phân hoạch trở lên)",
                "tip": "$P(B) = \\sum_{i=1}^n P(A_i)P(B|A_i)$.",
                "questions": [
                    {
                        "q": "Một nhà máy sản xuất linh kiện từ 3 xưởng $A, B, C$ với tỷ lệ sản lượng $50\\%, 30\\%, 20\\%$. Tỷ lệ lỗi tương ứng là $1\\%, 2\\%, 3\\%$. Chọn ngẫu nhiên 1 sản phẩm, xác suất sản phẩm đó bị lỗi là:",
                        "options": ["$1.7\\%$", "$2.0\\%$", "$1.5\\%$", "$6.0\\%$"],
                        "answer": "A",
                        "solution": "$P = 0.50(0.01) + 0.30(0.02) + 0.20(0.03) = 0.017 = 1.7\\%$."
                    },
                    {
                        "q": "Ba cửa hàng I, II, III nhập cùng một loại nông sản với tỷ trọng lần lượt $40\\%, 40\\%, 20\\%$. Tỷ lệ hàng đạt chuẩn của từng cửa hàng là $90\\%, 85\\%, 80\\%$. Xác suất mua được một sản phẩm đạt chuẩn là:",
                        "options": ["$86.0\\%$", "$85.0\\%$", "$88.0\\%$", "$84.0\\%$"],
                        "answer": "A",
                        "solution": "$P = 0.40(0.90) + 0.40(0.85) + 0.20(0.80) = 0.36 + 0.34 + 0.16 = 0.86 = 86\\%$."
                    }
                ]
            },
            {
                "id": "6.9",
                "name": "Dạng 6.9: Định lý Bayes - Ứng dụng Y tế (Xét nghiệm chẩn đoán & Dương tính giả)",
                "tip": "$P(B|+) = \\frac{P(B)P(+|B)}{P(B)P(+|B) + P(\\bar{B})P(+|\\bar{B})}$. Hiện tượng dương tính giả xảy ra khi bệnh hiếm.",
                "questions": [
                    {
                        "q": "Tỷ lệ nhiễm virus trong cộng đồng là $1\\%$. Bộ kit có độ nhạy $95\\%$ và độ đặc hiệu $90\\%$ (dương tính giả $10\\%$). Một người test dương tính. Xác suất người này thực sự nhiễm virus là:",
                        "options": ["$8.76\\%$", "$95.00\\%$", "$50.00\\%$", "$9.50\\%$"],
                        "answer": "A",
                        "solution": "$P(+) = 0.01(0.95) + 0.99(0.10) = 0.1085 \\Rightarrow P(B|+) = \\frac{0.0095}{0.1085} \\approx 8.76\\%$."
                    },
                    {
                        "q": "Vì sao khi một xét nghiệm có độ nhạy và đặc hiệu rất cao ($99\\%$) đối với một bệnh cực hiếm ($1/10000$), xác suất người nhận kết quả dương tính thực sự mắc bệnh lại rất thấp?",
                        "options": ["Vì số lượng người khỏe mạnh dương tính giả áp đảo số lượng người bệnh thực sự", "Vì kit test bị lỗi đối với bệnh hiếm", "Vì định lý Bayes không đúng cho bệnh hiếm", "Vì độ nhạy $99\\%$ là chưa đủ"],
                        "answer": "A",
                        "solution": "Do $99.99\\%$ dân số khỏe mạnh nên $1\\%$ dương tính giả vẫn tạo ra số ca dương tính áp đảo so với $0.01\\%$ ca bệnh thực sự."
                    }
                ]
            },
            {
                "id": "6.10",
                "name": "Dạng 6.10: Định lý Bayes - Ứng dụng Quản lý chất lượng KCS (Truy xuất nguồn gốc)",
                "tip": "$P(M_k|\\text{Hỏng}) = \\frac{P(M_k)P(\\text{Hỏng}|M_k)}{\\sum P(M_i)P(\\text{Hỏng}|M_i)}$.",
                "questions": [
                    {
                        "q": "Xí nghiệp có 2 máy I ($60\\%$, hỏng $2\\%$) và II ($40\\%$, hỏng $5\\%$). Lấy ngẫu nhiên 1 sản phẩm thấy nó bị hỏng. Xác suất sản phẩm này do máy II sản xuất là:",
                        "options": ["$\\frac{5}{8} = 62.5\\%$", "$\\frac{3}{8} = 37.5\\%$", "$50.0\\%$", "$40.0\\%$"],
                        "answer": "A",
                        "solution": "$P(H) = 0.60(0.02) + 0.40(0.05) = 0.032 \\Rightarrow P(M_2|H) = \\frac{0.020}{0.032} = \\frac{5}{8} = 62.5\\%$."
                    },
                    {
                        "q": "Cũng từ dữ liệu xí nghiệp trên, xác suất sản phẩm bị hỏng do máy I sản xuất là:",
                        "options": ["$\\frac{3}{8} = 37.5\\%$", "$\\frac{5}{8} = 62.5\\%$", "$12.0\\%$", "$20.0\\%$"],
                        "answer": "A",
                        "solution": "$P(M_1|H) = 1 - 0.625 = 0.375 = \\frac{3}{8} = 37.5\\%$."
                    }
                ]
            },
            {
                "id": "6.11",
                "name": "Dạng 6.11: Định lý Bayes - Ứng dụng Bộ lọc thư rác (Spam Filter / Naive Bayes)",
                "tip": "$P(\\text{Spam}|W) = \\frac{P(\\text{Spam})P(W|\\text{Spam})}{P(W)}$.",
                "questions": [
                    {
                        "q": "Tỷ lệ thư rác là $20\\%$, thư thường là $80\\%$. Từ 'Khuyến mãi' có trong $70\\%$ thư rác và $5\\%$ thư thường. Khi email chứa từ 'Khuyến mãi', xác suất nó là thư rác bằng:",
                        "options": ["$\\frac{7}{9} \\approx 77.78\\%$", "$70.00\\%$", "$20.00\\%$", "$\\frac{2}{9} \\approx 22.22\\%$"],
                        "answer": "A",
                        "solution": "$P(W) = 0.2(0.7) + 0.8(0.05) = 0.18 \\Rightarrow P(\\text{Spam}|W) = \\frac{0.14}{0.18} = \\frac{7}{9} \\approx 77.78\\%$."
                    },
                    {
                        "q": "Từ bài toán trên, xác suất email chứa từ 'Khuyến mãi' thực chất là thư quan trọng (thư thường) bằng:",
                        "options": ["$\\frac{2}{9} \\approx 22.22\\%$", "$\\frac{7}{9} \\approx 77.78\\%$", "$5.00\\%$", "$80.00\\%$"],
                        "answer": "A",
                        "solution": "$P(\\text{Ham}|W) = 1 - \\frac{7}{9} = \\frac{2}{9} \\approx 22.22\\%$."
                    }
                ]
            }
        ]
    }
]
