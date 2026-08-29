# SỔ TAY CÔNG THỨC TOÀN DIỆN TOÁN 12 (CHƯƠNG TRÌNH MỚI 2018 - 2025+)
> **Tra cứu siêu tốc – Toàn bộ Định lý, Công thức Giải nhanh & Tuyệt chiêu Casio 6 Chương**

---

## 1. ĐẠO HÀM & ỨNG DỤNG KHẢO SÁT HÀM SỐ
* **Tính đơn điệu:**
  * Hàm số $f(x)$ đồng biến trên $K \iff f'(x) \ge 0, \forall x \in K$ (bằng 0 tại hữu hạn điểm).
  * Hàm phân thức bậc nhất $y = \frac{ax+b}{cx+d} \implies y' = \frac{ad-bc}{(cx+d)^2}$ (luôn $> 0$ hoặc $< 0$, **tuyệt đối không có dấu $=$**).
* **Cực trị hàm số:**
  * Qua nghiệm bội lẻ ($x-a, (x-a)^3$): $f'(x)$ **đổi dấu** $\to$ sinh cực trị.
  * Qua nghiệm bội chẵn ($(x-a)^2, (x-a)^4$): $f'(x)$ **không đổi dấu** $\to$ không tạo cực trị.
  * Đạo hàm cấp 2: $f'(x_0) = 0, f''(x_0) < 0 \implies$ Cực đại; $f'(x_0) = 0, f''(x_0) > 0 \implies$ Cực tiểu.
  * Phân thức bậc 2 / bậc 1: $y = \frac{ax^2+bx+c}{dx+e} \implies$ Phương trình đường thẳng qua 2 cực trị là $y = \frac{(ax^2+bx+c)'}{(dx+e)'} = \frac{2ax+b}{d}$.
  * Số cực trị của hàm trị tuyệt đối $y = |f(x)|$: Số cực trị $= m + n$ ($m$ là số cực trị của $f(x)$, $n$ là số nghiệm đơn của $f(x) = 0$).
* **Tiệm cận:**
  * Tiệm cận đứng: $\lim_{x \to x_0^\pm} f(x) = \pm\infty \implies x = x_0$.
  * Tiệm cận ngang: $\lim_{x \to \pm\infty} f(x) = y_0 \implies y = y_0$.
  * Tiệm cận xiên: $y = ax + b$ với $a = \lim_{x \to \pm\infty} \frac{f(x)}{x}, b = \lim_{x \to \pm\infty} [f(x) - ax]$.
  * Phân thức $y = \frac{ax^2+bx+c}{dx+e} = \frac{a}{d}x + \frac{bd-ae}{d^2} + \frac{R}{dx+e} \implies$ TCX: $y = \frac{a}{d}x + \frac{bd-ae}{d^2}$.
* **Tâm đối xứng của đồ thị:** Giao điểm $I(x_0; y_0)$ của 2 đường tiệm cận.

---

## 2. VECTƠ VÀ HỆ TOẠ ĐỘ TRONG KHÔNG GIAN
* **Quy tắc hình hộp:** $\vec{AC'} = \vec{AB} + \vec{AD} + \vec{AA'}$.
* **Tích vô hướng:** $\vec{a} \cdot \vec{b} = x_1 x_2 + y_1 y_2 + z_1 z_2 = |\vec{a}| |\vec{b}| \cos(\vec{a}, \vec{b})$.
* **Tích có hướng:** $[\vec{a}, \vec{b}] = (y_1 z_2 - y_2 z_1; \; z_1 x_2 - z_2 x_1; \; x_1 y_2 - x_2 y_1)$.
* **Điều kiện đồng phẳng:** $\vec{a}, \vec{b}, \vec{c}$ đồng phẳng $\iff [\vec{a}, \vec{b}] \cdot \vec{c} = 0$.
* **Diện tích & Thể tích:**
  * Diện tích tam giác: $S_{\triangle ABC} = \frac{1}{2} |[\vec{AB}, \vec{AC}]|$.
  * Diện tích hình bình hành: $S_{ABCD} = |[\vec{AB}, \vec{AD}]|$.
  * Thể tích tứ diện: $V_{ABCD} = \frac{1}{6} |[\vec{AB}, \vec{AC}] \cdot \vec{AD}|$.
  * Thể tích hình hộp: $V = |[\vec{AB}, \vec{AD}] \cdot \vec{AA'}|$.

---

## 3. CÁC SỐ ĐẶC TRƯNG ĐO ĐỘ PHÂN TÁN CHO MẪU GHÉP NHÓM
* **Khoảng biến thiên:** $R = a_{k+1} - a_1$.
* **Tứ phân vị $Q_p$ ($p \in \{1, 2, 3\}$):**
  $$Q_p = a_m + \frac{\frac{p \cdot n}{4} - C}{n_m} \cdot (a_{m+1} - a_m)$$
  *(Với nhóm $[a_m; a_{m+1})$ là nhóm đầu tiên có $cf \ge \frac{p \cdot n}{4}$, và $C$ là tổng tần số các nhóm đứng trước).*
* **Khoảng tứ phân vị:** $\Delta_Q = Q_3 - Q_1$ (đo 50% số liệu trung tâm, miễn nhiễm với giá trị ngoại lai).
* **Phương sai & Độ lệch chuẩn:**
  $$s^2 = \frac{1}{n} \left(\sum_{i=1}^k n_i c_i^2\right) - \bar{x}^2, \qquad s = \sqrt{s^2}$$
* **Hệ số biến thiên:** $CV = \frac{s}{\bar{x}}$.

---

## 4. NGUYÊN HÀM VÀ TÍCH PHÂN
* **Bảng nguyên hàm then chốt:**
  * $\int x^\alpha \, dx = \frac{x^{\alpha+1}}{\alpha+1} + C \text{ } (\alpha \ne -1)$.
  * $\int \frac{1}{ax+b} \, dx = \frac{1}{a} \ln|ax+b| + C$.
  * $\int \frac{1}{x^2 - a^2} \, dx = \frac{1}{2a} \ln\left|\frac{x-a}{x+a}\right| + C$.
  * $\int e^{ax+b} \, dx = \frac{1}{a} e^{ax+b} + C$.
  * $\int a^{mx+n} \, dx = \frac{1}{m \ln a} a^{mx+n} + C$.
  * $\int \cos(ax+b) \, dx = \frac{1}{a} \sin(ax+b) + C$.
  * $\int \sin(ax+b) \, dx = -\frac{1}{a} \cos(ax+b) + C$.
* **Tích phân từng phần múa cột:** $\int u \, dv = uv - \int v \, du$ (Thứ tự ưu tiên $u$: Log $\to$ Đa $\to$ Lượng $\to$ Mũ).
* **Phương trình vi phân hàm ẩn:**
  * $f'(x) + p(x)f(x) = q(x) \implies [f(x) \cdot e^{\int p(x)dx}]' = q(x) \cdot e^{\int p(x)dx}$.
  * $f'(x) \cdot [f(x)]^n = g(x) \implies \frac{[f(x)]^{n+1}}{n+1} = \int g(x)dx + C$.
* **Ứng dụng hình học:**
  * Diện tích hình phẳng: $S = \int_a^b |f(x) - g(x)| \, dx$.
  * Thể tích vật thể thiết diện $S(x)$: $V = \int_a^b S(x) \, dx$.
  * Thể tích tròn xoay quanh $Ox$: $V = \pi \int_a^b f^2(x) \, dx$.
  * Parabol Archimedes: $S = \frac{2}{3} \cdot \text{Đáy} \cdot \text{Cao}$.
  * Diện tích Elip: $S = \pi a b$.
* **Ứng dụng Vật lý:** $s = \int_{t_1}^{t_2} v(t) \, dt, \quad v = \int_{t_1}^{t_2} a(t) \, dt, \quad W = \int_{x_1}^{x_2} F(x) \, dx$.

---

## 5. PHƯƠNG PHÁP TOẠ ĐỘ TRONG KHÔNG GIAN (OXYZ)
* **Khoảng cách từ $M(x_0; y_0; z_0)$ đến $(P): Ax+By+Cz+D=0$:**
  $$d(M, (P)) = \frac{|Ax_0 + By_0 + Cz_0 + D|}{\sqrt{A^2 + B^2 + C^2}}$$
* **Khoảng cách từ $M$ đến $d$ (qua $A$, VCP $\vec{u}$):**
  $$d(M, d) = \frac{|[\vec{AM}, \vec{u}]|}{|\vec{u}|}$$
* **Khoảng cách giữa hai đường chéo nhau $d_1(A, \vec{u}_1)$ và $d_2(B, \vec{u}_2)$:**
  $$d(d_1, d_2) = \frac{|[\vec{u}_1, \vec{u}_2] \cdot \vec{AB}|}{|[\vec{u}_1, \vec{u}_2]|}$$
* **Góc giữa đường thẳng và mặt phẳng:**
  $$\sin(d, (P)) = \frac{|\vec{u} \cdot \vec{n}|}{|\vec{u}| \cdot |\vec{n}|}$$
* **Mặt cầu cắt mặt phẳng:** $r = \sqrt{R^2 - d^2}$ (với $d = d(I, (P)) < R$).
* **Tâm tỉ cự:** $\sum k_i \vec{IA_i} = \vec{0} \implies \sum k_i MA_i^2 = (\sum k_i) MI^2 + \sum k_i IA_i^2$.

---

## 6. XÁC SUẤT CÓ ĐIỀU KIỆN & CÔNG THỨC BAYES
* **Xác suất có điều kiện:** $P(A|B) = \frac{P(A \cap B)}{P(B)}$ ($P(B) > 0$).
* **Quy tắc nhân:** $P(A \cap B) = P(B) \cdot P(A|B) = P(A) \cdot P(B|A)$.
* **Độc lập:** $A, B$ độc lập $\iff P(A \cap B) = P(A) \cdot P(B)$.
* **Công thức xác suất toàn phần:** Với hệ đầy đủ $\{B_1, \dots, B_n\}$:
  $$P(A) = \sum_{i=1}^n P(B_i) \cdot P(A|B_i)$$
* **Công thức Bayes:**
  $$P(B_k|A) = \frac{P(B_k) \cdot P(A|B_k)}{\sum_{i=1}^n P(B_i) \cdot P(A|B_i)}$$
* **Xét nghiệm lặp 2 lần độc lập:**
  $$P(B \mid +_1 \cap +_2) = \frac{P(B) \cdot [P(+ \mid B)]^2}{P(B) \cdot [P(+ \mid B)]^2 + P(\overline{B}) \cdot [P(+ \mid \overline{B})]^2}$$
