import pdfplumber as plb
import sys
import re

# 检查是否提供了文件路径参数
if len(sys.argv) != 2:
    print("Usage: python wc.py <file_path>")
    sys.exit(1)

file_path = sys.argv[1]

pdf_words = 0
count = 0
with plb.open(file_path) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        words = re.findall(r'\b[A-Za-z]+\b', text)  # Regex to extract English words
        print("page " + str(count + 1) + ": " + str(len(words)))
        count += 1
        pdf_words += len(words)
    
    # for page in pdf.pages:
    #    print('Page' + str(page.page_number) + ': ', end="")
    #    pg = page.extract_text()
    #    del_f = [' ', '\n', '\s', '!', '.', '(', ')', ';', '-', '/', ':', '，', '。', '、', '；', '《', '》', '“', '”', '：', '（', '）']
    #    for j in del_f:
    #        pg = pg.translate({ord(i): '' for i in j})
    #    print(len(pg))
    #    pdf_words += len(pg)

print(' ')
print('Word Count in Total: ', pdf_words)
