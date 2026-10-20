# -*- coding: utf-8 -*-
"""
Script to build the final 'de_kiem_tra_toan_12_all_types.html' from 'exam_data_100.py'.
"""

import os
from exam_data_100 import EXAM_CHAPTERS

def build_exam_html():
    from generate_all_types_exam import HTML_HEADER, HTML_FOOTER

    total_questions = sum(len(sub["questions"]) for ch in EXAM_CHAPTERS for sub in ch["subtopics"])
    total_subtopics = sum(len(ch["subtopics"]) for ch in EXAM_CHAPTERS)

    filter_options = [f'<option value="all">📚 Tất cả {len(EXAM_CHAPTERS)} Chương ({total_questions} câu - {total_subtopics} dạng)</option>']
    for ch in EXAM_CHAPTERS:
        ch_q_count = sum(len(sub["questions"]) for sub in ch["subtopics"])
        ch_sub_count = len(ch["subtopics"])
        filter_options.append(f'<option value="{ch["id"]}">{ch["title"]} ({ch_q_count} câu - {ch_sub_count} dạng)</option>')

    chapter_filter_options_html = "\n                ".join(filter_options)
    badge_total_html = f"{total_questions} Câu ({total_subtopics} Dạng bài)"
    exam_instructions_html = f"* Đề thi gồm {total_questions} câu trắc nghiệm bao phủ toàn diện 100% tất cả {total_subtopics} dạng toán cốt lõi của {len(EXAM_CHAPTERS)} chương Toán 12 mới (GDPT 2018). Thí sinh chọn một phương án đúng duy nhất cho mỗi câu."

    html_content = HTML_HEADER.replace("{{BADGE_TOTAL}}", badge_total_html)
    html_content = html_content.replace("{{CHAPTER_FILTER_OPTIONS}}", chapter_filter_options_html)
    html_content = html_content.replace("{{EXAM_INSTRUCTIONS}}", exam_instructions_html)
    
    question_counter = 1

    for ch in EXAM_CHAPTERS:
        ch_id = ch["id"]
        ch_title = ch["title"]
        ch_badge = ch["badge"]

        html_content += f"""
        <div class="chapter-section" data-chapter="{ch_id}">
            <div class="chapter-heading">
                <span><i class="fa-solid fa-graduation-cap"></i> {ch_title}</span>
                <span class="chapter-badge">{ch_badge}</span>
            </div>
        """

        for sub in ch["subtopics"]:
            sub_id = sub["id"]
            sub_name = sub["name"]
            sub_tip = sub["tip"]

            html_content += f"""
            <div class="subtopic-card">
                <div class="subtopic-header">
                    <div class="subtopic-title">{sub_name}</div>
                </div>
                <div class="subtopic-tip">
                    <i class="fa-regular fa-lightbulb"></i> <strong>Phương pháp & Công thức cốt lõi:</strong> {sub_tip}
                </div>
            """

            for q_data in sub["questions"]:
                q_text = q_data["q"]
                options = q_data["options"]
                ans = q_data["answer"]
                solution = q_data["solution"]
                is_trap = q_data.get("is_trap", False)
                trap_note = q_data.get("trap_note", "")
                trap_cls = " is-trap" if is_trap else ""
                trap_badge_html = '<span class="trap-badge"><i class="fa-solid fa-triangle-exclamation"></i> CÂU HỎI BẪY / ĐÁNH LỪA</span> ' if is_trap else ''
                trap_warning_html = f'<div class="trap-warning-box"><i class="fa-solid fa-triangle-exclamation"></i> <strong>Cạm bẫy học sinh hay mắc:</strong> {trap_note}</div>' if trap_note else ''

                # Check options length to choose grid layout (2 cols or 4 cols)
                max_opt_len = max(len(opt) for opt in options)
                grid_class = "options-grid"
                if max_opt_len > 45:
                    grid_class += " one-col"
                elif max_opt_len > 22:
                    grid_class += " two-cols"

                opt_labels = ["A", "B", "C", "D"]
                opts_html = ""
                for idx, opt in enumerate(options):
                    lbl = opt_labels[idx]
                    is_correct = (lbl == ans)
                    correct_cls = " opt-correct" if is_correct else ""
                    opts_html += f"""
                    <div class="option-choice{correct_cls}">
                        <span class="opt-label"><strong>{lbl}.</strong></span> {opt}
                    </div>
                    """

                html_content += f"""
                <div class="question-item{trap_cls}" data-correct="{ans}">
                    <div class="question-text">
                        <span class="q-number">Câu {question_counter}:</span> {trap_badge_html}{q_text}
                    </div>
                    <div class="{grid_class}">
                        {opts_html}
                    </div>
                    <div class="solution-box">
                        <div class="solution-header">
                            <i class="fa-solid fa-check-circle"></i> Đáp án đúng: <strong>{ans}</strong> • Lời giải chi tiết:
                        </div>
                        <div class="solution-content">
                            {solution}
                            {trap_warning_html}
                        </div>
                    </div>
                </div>
                """
                question_counter += 1

            html_content += """
            </div> <!-- End subtopic-card -->
            """

        html_content += """
        </div> <!-- End chapter-section -->
        """

    html_content += HTML_FOOTER

    output_path = os.path.join(os.path.dirname(__file__), "de_kiem_tra_toan_12_all_types.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Generated successfully: {output_path}")
    print(f"Summary: {len(EXAM_CHAPTERS)} Chapters, {total_subtopics} Subtopics, {question_counter - 1} Questions.")

if __name__ == "__main__":
    build_exam_html()
