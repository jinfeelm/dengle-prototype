import os
import glob

html_files = glob.glob('*.html')

old_footer = "<strong>(주)KNS에듀</strong> | 대표: 신동원 | 사업자등록번호: 123-45-67890 | 대치동 학원가로 123 KNS빌딩"
new_footer = "<strong>주식회사 케이엔에스북스</strong> | 대표이사 김치삼 | 사업자번호 777-81-03746<br>서울특별시 강남구 역삼로78길 21, 칼텍빌딩 3층(대치동) | e-mail: denglemaster@gmail.com"

# The user wants exact strings from the image:
# 주식회사 케이엔에스북스
# 서울특별시 강남구 역삼로78길 21, 칼텍빌딩 3층(대치동)
# 대표이사 김치삼
# 사업자번호 777-81-03746
# denglemaster@gmail.com
new_footer_html = """<strong>주식회사 케이엔에스북스</strong><br>
서울특별시 강남구 역삼로78길 21, 칼텍빌딩 3층(대치동)<br>
대표이사 김치삼 | 사업자번호 777-81-03746 | denglemaster@gmail.com"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update Footer
    if old_footer in content:
        content = content.replace(old_footer, new_footer_html)

    # Update global GNB navigation text
    content = content.replace(">나의 강의실</a>", ">MY 학습진단</a>")
    content = content.replace("> 나의 강의실</a>", "> MY 학습진단</a>")
    content = content.replace(">나의 강의실 </a>", ">MY 학습진단 </a>")

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Processed {len(html_files)} files.")
