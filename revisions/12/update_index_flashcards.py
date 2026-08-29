import json
import os

rev_dir = r"c:\Users\Admin\Code\Test\toan-12\revisions\12"
json_path = os.path.join(rev_dir, "data", "flashcards_data.json")

with open(json_path, "r", encoding="utf-8") as f:
    flashcards_list = json.load(f)

# Load index.html
with open(os.path.join(rev_dir, "index.html"), "r", encoding="utf-8") as f:
    html = f.read()

# Replace Flashcard JS data and logic
new_flashcard_js = f"""    // MATH RENDERING FOR FLASHCARD & QUIZ
    function renderAllFlashcardMath() {{
      const card = document.getElementById('flashcardCard');
      if (card && window.renderMathInElement) {{
        renderMathInElement(card, {{
          delimiters: [
            {{left: '$$', right: '$$', display: true}},
            {{left: '$', right: '$', display: false}}
          ],
          throwOnError: false
        }});
      }}
    }}

    function renderAllQuizMath() {{
      const qz = document.getElementById('quiz-view');
      if (qz && window.renderMathInElement) {{
        renderMathInElement(qz, {{
          delimiters: [
            {{left: '$$', right: '$$', display: true}},
            {{left: '$', right: '$', display: false}}
          ],
          throwOnError: false
        }});
      }}
    }}

    // FLASHCARD SYSTEM WITH RICH DATABASE (1143+ QUESTIONS)
    const allFlashcards = {json.dumps(flashcards_list, ensure_ascii=False)};
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

# Replace in index.html
start_fc_js = "    // MATH RENDERING FOR FLASHCARD & QUIZ"
if start_fc_js not in html:
    start_fc_js = "    // FLASHCARD SYSTEM"

end_fc_js = "    // QUIZ CHECK SYSTEM"

pos_start_js = html.find(start_fc_js)
pos_end_js = html.find(end_fc_js)

if pos_start_js != -1 and pos_end_js != -1:
    html = html[:pos_start_js] + new_flashcard_js + "\n\n" + html[pos_end_js:]

with open(os.path.join(rev_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)

print(f"Successfully embedded {len(flashcards_list)} flashcards into index.html with auto-math rendering!")
