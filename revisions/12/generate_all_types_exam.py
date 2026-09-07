# -*- coding: utf-8 -*-
"""
Script to generate the comprehensive 100-question Math 12 Exam covering ALL subtopics (2 questions per type).
Outputs a standalone, print-ready HTML page with KaTeX support, PDF export, filter by chapter,
and toggleable solutions.
"""

import os
import json

HTML_HEADER = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Đề Kiểm Tra Tổng Hợp Tất Cả Dạng Bài Toán 12 (100 Câu - Xuất PDF)</title>
    
    <!-- KaTeX CSS & JS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;1,300&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <style>
        :root {
            --primary: #1e40af;
            --primary-dark: #1e3a8a;
            --primary-light: #eff6ff;
            --accent: #dc2626;
            --text-main: #1f2937;
            --text-muted: #4b5563;
            --border-color: #cbd5e1;
            --bg-page: #f8fafc;
            --card-bg: #ffffff;
            --success: #15803d;
            --success-bg: #f0fdf4;
            --tip-bg: #fefce8;
            --tip-border: #facc15;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Times New Roman', Times, serif;
            color: var(--text-main);
            background-color: var(--bg-page);
            line-height: 1.6;
            font-size: 14pt;
        }

        /* SCREEN TOOLBAR */
        .no-print-bar {
            position: sticky;
            top: 0;
            z-index: 9999;
            background: #ffffff;
            border-bottom: 2px solid #e2e8f0;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
            padding: 0.75rem 1.5rem;
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
            font-family: 'Plus Jakarta Sans', sans-serif;
        }

        .bar-left {
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        .bar-title {
            font-size: 1.1rem;
            font-weight: 700;
            color: #1e293b;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .badge-total {
            background: #dbeafe;
            color: #1d4ed8;
            padding: 0.2rem 0.6rem;
            border-radius: 9999px;
            font-size: 0.85rem;
            font-weight: 600;
        }

        .bar-actions {
            display: flex;
            align-items: center;
            gap: 0.6rem;
            flex-wrap: wrap;
        }

        .btn {
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            padding: 0.55rem 1rem;
            font-size: 0.9rem;
            font-weight: 600;
            border-radius: 8px;
            border: 1px solid transparent;
            cursor: pointer;
            transition: all 0.2s ease;
            text-decoration: none;
            font-family: inherit;
        }

        .btn-primary {
            background: #2563eb;
            color: #ffffff;
        }
        .btn-primary:hover {
            background: #1d4ed8;
            box-shadow: 0 2px 6px rgba(37, 99, 235, 0.3);
        }

        .btn-outline {
            background: #ffffff;
            color: #334155;
            border-color: #cbd5e1;
        }
        .btn-outline:hover {
            background: #f1f5f9;
            border-color: #94a3b8;
        }

        .btn-success {
            background: #16a34a;
            color: #ffffff;
        }
        .btn-success:hover {
            background: #15803d;
        }

        .filter-select {
            padding: 0.5rem 0.8rem;
            border-radius: 8px;
            border: 1px solid #cbd5e1;
            font-size: 0.9rem;
            font-family: inherit;
            background: #fff;
            color: #334155;
            cursor: pointer;
            font-weight: 500;
        }

        /* MAIN EXAM CONTAINER */
        .exam-container {
            max-width: 210mm;
            margin: 20px auto;
            background: #ffffff;
            padding: 20mm 20mm;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            border-radius: 4px;
        }

        /* EXAM OFFICIAL HEADER */
        .exam-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            border-bottom: 2px solid #000000;
            padding-bottom: 12px;
            margin-bottom: 16px;
        }

        .header-left {
            text-align: center;
            width: 45%;
        }

        .header-right {
            text-align: center;
            width: 50%;
        }

        .header-sub {
            font-size: 11pt;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .header-title-org {
            font-size: 12pt;
            font-weight: bold;
            text-transform: uppercase;
        }

        .header-main-title {
            font-size: 13pt;
            font-weight: bold;
            margin-top: 4px;
            color: #000;
        }

        .header-desc {
            font-size: 11pt;
            font-style: italic;
        }

        .exam-code {
            display: inline-block;
            border: 1.5px solid #000;
            padding: 2px 10px;
            font-weight: bold;
            margin-top: 4px;
            font-size: 11pt;
        }

        /* STUDENT INFO BOX */
        .student-info-box {
            border: 1px dashed #64748b;
            padding: 8px 14px;
            margin-bottom: 20px;
            font-size: 11pt;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: #fafafa;
        }

        .info-field {
            display: flex;
            gap: 6px;
        }
        .info-dots {
            border-bottom: 1px dotted #333;
            min-width: 140px;
            display: inline-block;
        }

        /* CHAPTER DIVIDER */
        .chapter-section {
            margin-top: 24px;
            margin-bottom: 16px;
        }

        .chapter-heading {
            background: #1e3a8a;
            color: #ffffff;
            padding: 6px 14px;
            font-size: 13pt;
            font-weight: bold;
            text-transform: uppercase;
            border-radius: 4px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            page-break-after: avoid;
            break-after: avoid;
        }

        .chapter-badge {
            background: #f59e0b;
            color: #000;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 9pt;
            font-weight: bold;
        }

        /* SUBTOPIC DẠNG BÀI */
        .subtopic-card {
            border: 1px solid #e2e8f0;
            border-left: 4px solid #2563eb;
            background: #ffffff;
            border-radius: 4px;
            margin: 16px 0;
            padding: 12px 16px;
            page-break-inside: avoid;
            break-inside: avoid;
        }

        .subtopic-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid #cbd5e1;
            padding-bottom: 6px;
            margin-bottom: 10px;
        }

        .subtopic-title {
            font-size: 12pt;
            font-weight: bold;
            color: #1e40af;
        }

        .subtopic-tip {
            background: var(--tip-bg);
            border-left: 3px solid var(--tip-border);
            padding: 6px 10px;
            font-size: 10.5pt;
            margin-bottom: 12px;
            border-radius: 2px;
            color: #854d0e;
            font-style: italic;
        }

        /* QUESTION ITEM */
        .question-item {
            margin-bottom: 14px;
            padding-bottom: 10px;
            page-break-inside: avoid;
            break-inside: avoid;
        }

        .question-item:not(:last-child) {
            border-bottom: 1px dashed #e2e8f0;
        }

        .question-text {
            font-size: 12pt;
            line-height: 1.5;
            margin-bottom: 8px;
            text-align: justify;
        }

        .q-number {
            font-weight: bold;
            color: #b91c1c;
        }

        /* OPTIONS GRID */
        .options-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 6px 14px;
            margin: 8px 0 10px 0;
            font-size: 11.5pt;
        }

        .options-grid.two-cols {
            grid-template-columns: repeat(2, 1fr);
        }

        .options-grid.one-col {
            grid-template-columns: 1fr;
        }

        .opt-label {
            font-weight: bold;
            margin-right: 4px;
        }

        .opt-correct {
            font-weight: bold;
            color: #15803d;
        }

        /* SOLUTION ACCORDION */
        .solution-box {
            background: #f8fafc;
            border: 1px solid #cbd5e1;
            border-radius: 4px;
            padding: 8px 12px;
            margin-top: 8px;
            font-size: 11pt;
            line-height: 1.5;
            display: none; /* Toggleable */
        }

        .solution-box.show {
            display: block;
        }

        .solution-header {
            font-weight: bold;
            color: #15803d;
            margin-bottom: 4px;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .solution-content {
            color: #334155;
            text-align: justify;
        }

        /* ANSWER KEY TABLE */
        .answer-key-section {
            margin-top: 30px;
            page-break-before: always;
            break-before: always;
        }

        .answer-key-title {
            text-align: center;
            font-size: 14pt;
            font-weight: bold;
            text-transform: uppercase;
            margin-bottom: 12px;
            color: #1e3a8a;
        }

        .answer-grid-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 10.5pt;
            text-align: center;
        }

        .answer-grid-table th, .answer-grid-table td {
            border: 1px solid #000000;
            padding: 4px 2px;
        }

        .answer-grid-table th {
            background: #f1f5f9;
            font-weight: bold;
        }

        .ans-bold {
            font-weight: bold;
            color: #b91c1c;
        }

        /* PRINT STYLES */
        @media print {
            body {
                background: #ffffff !important;
                font-size: 11pt !important;
                color: #000000 !important;
            }

            .no-print-bar {
                display: none !important;
            }

            .exam-container {
                max-width: 100% !important;
                margin: 0 !important;
                padding: 0 !important;
                box-shadow: none !important;
                border: none !important;
            }

            .subtopic-card {
                border: 1px solid #94a3b8 !important;
                border-left: 3px solid #000 !important;
                box-shadow: none !important;
                margin: 10px 0 !important;
                padding: 8px 10px !important;
            }

            .chapter-heading {
                background: #f1f5f9 !important;
                color: #000000 !important;
                border: 1.5px solid #000000 !important;
                font-size: 11.5pt !important;
                padding: 4px 8px !important;
            }

            .chapter-badge {
                border: 1px solid #000 !important;
                background: #ffffff !important;
                color: #000 !important;
            }

            .subtopic-title {
                color: #000000 !important;
                font-size: 11pt !important;
            }

            .subtopic-tip {
                display: none; /* Hide tip on student exam print to save space, unless in solution mode */
            }

            .solution-box {
                border: 1px dashed #64748b !important;
                background: #ffffff !important;
                font-size: 10pt !important;
                padding: 6px 8px !important;
            }

            .solution-box:not(.show) {
                display: none !important;
            }

            .q-number {
                color: #000000 !important;
            }

            .opt-correct {
                color: #000000 !important;
            }

            @page {
                size: A4;
                margin: 15mm 15mm 15mm 15mm;
            }
        }
    </style>
</head>
<body>

    <!-- SCREEN CONTROLS TOOLBAR -->
    <div class="no-print-bar">
        <div class="bar-left">
            <a href="index.html" class="btn btn-outline" title="Quay lại ứng dụng chính">
                <i class="fa-solid fa-arrow-left"></i> Trang chủ
            </a>
            <div class="bar-title">
                <i class="fa-solid fa-file-pdf" style="color: #dc2626;"></i>
                Đề Kiểm Tra Tổng Hợp Toàn Diện Toán 12
                <span class="badge-total">144 Câu (72 Dạng &times; 2 Câu)</span>
            </div>
        </div>

        <div class="bar-actions">
            <!-- Filter by Chapter -->
            <select id="chapterFilter" class="filter-select" onchange="filterChapter(this.value)">
                <option value="all">📚 Tất cả 6 Chương (144 câu)</option>
                <option value="ch1">Chương 1: Khảo sát hàm số (32 câu)</option>
                <option value="ch2">Chương 2: Vectơ không gian (16 câu)</option>
                <option value="ch3">Chương 3: Thống kê ghép nhóm (18 câu)</option>
                <option value="ch4">Chương 4: Nguyên hàm & Tích phân (30 câu)</option>
                <option value="ch5">Chương 5: Hình học Oxyz (26 câu)</option>
                <option value="ch6">Chương 6: Xác suất & Bayes (22 câu)</option>
            </select>

            <!-- Toggle Solutions -->
            <button id="toggleSolBtn" class="btn btn-outline" onclick="toggleAllSolutions()">
                <i class="fa-solid fa-eye"></i> Hiện Lời giải chi tiết
            </button>

            <!-- Print / Export PDF -->
            <button class="btn btn-primary" onclick="window.print()">
                <i class="fa-solid fa-print"></i> In / Xuất PDF (A4)
            </button>
        </div>
    </div>

    <!-- MAIN EXAM PAPER CONTAINER -->
    <div class="exam-container">
        
        <!-- EXAM FORMAL HEADER -->
        <div class="exam-header">
            <div class="header-left">
                <div class="header-sub">BỘ GIÁO DỤC VÀ ĐÀO TẠO</div>
                <div class="header-title-org">TRƯỜNG THPT CHUYÊN ÔN TẬP</div>
                <div style="font-size: 10pt; margin-top: 2px;">NGÂN HÀNG ĐỀ ĐÁNH GIÁ NĂNG LỰC TOÀN DIỆN</div>
            </div>
            <div class="header-right">
                <div class="header-main-title">ĐỀ KIỂM TRA TOÀN BỘ 72 DẠNG TOÁN 12</div>
                <div class="header-desc">Chuẩn CT GDPT 2018 (KNTT, Cánh Diều, Chân Trời Sáng Tạo)</div>
                <div class="header-desc">Quy mô: 144 Câu Phân Loại (Mỗi dạng 2 câu chuẩn hóa)</div>
                <div class="exam-code">MÃ ĐỀ THI: 102</div>
            </div>
        </div>

        <!-- STUDENT INFO BOX -->
        <div class="student-info-box">
            <div class="info-field">
                <strong>Họ và tên thí sinh:</strong>
                <span class="info-dots" style="min-width: 220px;"></span>
            </div>
            <div class="info-field">
                <strong>Số báo danh:</strong>
                <span class="info-dots" style="min-width: 100px;"></span>
            </div>
            <div class="info-field">
                <strong>Phòng thi:</strong>
                <span class="info-dots" style="min-width: 60px;"></span>
            </div>
        </div>

        <!-- EXAM INSTRUCTIONS -->
        <div style="font-size: 10.5pt; font-style: italic; margin-bottom: 14px; text-align: justify; border-left: 2.5px solid #64748b; padding-left: 8px;">
            * Đề thi gồm 144 câu trắc nghiệm bao phủ toàn diện 100% tất cả 72 dạng toán cốt lõi của 6 chương Toán 12 (mỗi dạng đúng 2 câu tiêu biểu). Thí sinh chọn một phương án đúng duy nhất cho mỗi câu.
        </div>

        <!-- QUESTIONS CONTENT PLACEHOLDER -->
        <div id="examQuestionsList">
"""

HTML_FOOTER = """
        </div> <!-- End of examQuestionsList -->

        <!-- ANSWER KEY SECTION (IN TRANG CUỐI) -->
        <div class="answer-key-section" id="answerKeySection">
            <div class="answer-key-title">BẢNG ĐÁP ÁN 100 CÂU TRẮC NGHIỆM</div>
            <table class="answer-grid-table" id="answerGridTable">
                <!-- JS will populate rows -->
            </table>
        </div>

    </div> <!-- End exam-container -->

    <script>
        let solutionsVisible = false;

        function toggleAllSolutions() {
            solutionsVisible = !solutionsVisible;
            const boxes = document.querySelectorAll('.solution-box');
            boxes.forEach(b => {
                if (solutionsVisible) {
                    b.classList.add('show');
                } else {
                    b.classList.remove('show');
                }
            });

            const btn = document.getElementById('toggleSolBtn');
            if (solutionsVisible) {
                btn.innerHTML = '<i class="fa-solid fa-eye-slash"></i> Ẩn Lời giải chi tiết';
                btn.classList.add('btn-success');
                btn.classList.remove('btn-outline');
            } else {
                btn.innerHTML = '<i class="fa-solid fa-eye"></i> Hiện Lời giải chi tiết';
                btn.classList.add('btn-outline');
                btn.classList.remove('btn-success');
            }
        }

        function filterChapter(ch) {
            const sections = document.querySelectorAll('.chapter-section');
            sections.forEach(sec => {
                if (ch === 'all' || sec.dataset.chapter === ch) {
                    sec.style.display = 'block';
                } else {
                    sec.style.display = 'none';
                }
            });
        }

        // Render KaTeX after DOM loaded
        document.addEventListener("DOMContentLoaded", function() {
            if (typeof renderMathInElement === 'function') {
                renderMathInElement(document.body, {
                    delimiters: [
                        {left: "$$", right: "$$", display: true},
                        {left: "$", right: "$", display: false},
                        {left: "\\\\(", right: "\\\\)", display: false},
                        {left: "\\\\[", right: "\\\\]", display: true}
                    ],
                    throwOnError: false
                });
            }

            // Populate Answer Table
            renderAnswerTable();
        });

        function renderAnswerTable() {
            const table = document.getElementById('answerGridTable');
            if (!table) return;

            // Extract all answers from DOM
            const qItems = document.querySelectorAll('.question-item');
            let answers = [];
            qItems.forEach((q, idx) => {
                const correctOpt = q.dataset.correct || '?';
                answers.push({ num: idx + 1, ans: correctOpt });
            });

            // Render into a 5-column or 10-column table
            // 10 columns of (Câu, ĐA) -> each table row has 5 pairs of (Câu, ĐA)
            let html = '<thead><tr>';
            for (let i = 0; i < 5; i++) {
                html += '<th>Câu</th><th>ĐA</th>';
            }
            html += '</tr></thead><tbody>';

            const numRows = Math.ceil(answers.length / 5);
            for (let r = 0; r < numRows; r++) {
                html += '<tr>';
                for (let c = 0; c < 5; c++) {
                    const idx = r + c * numRows;
                    if (idx < answers.length) {
                        html += `<td><strong>${answers[idx].num}</strong></td><td class="ans-bold">${answers[idx].ans}</td>`;
                    } else {
                        html += '<td></td><td></td>';
                    }
                }
                html += '</tr>';
            }
            html += '</tbody>';
            table.innerHTML = html;
        }
    </script>
</body>
</html>
"""

print("Writing template setup done.")
