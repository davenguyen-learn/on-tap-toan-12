# -*- coding: utf-8 -*-
"""
Script to build the final 'de_kiem_tra_toan_12_all_types.html' from 'exam_data_100.py'.
"""

import os
from exam_data_100 import EXAM_CHAPTERS

def build_exam_html():
    from generate_all_types_exam import HTML_HEADER, HTML_FOOTER

    html_content = HTML_HEADER
    
    question_counter = 1
    total_subtopics = 0

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
            total_subtopics += 1
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
                <div class="question-item" data-correct="{ans}">
                    <div class="question-text">
                        <span class="q-number">Câu {question_counter}:</span> {q_text}
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
