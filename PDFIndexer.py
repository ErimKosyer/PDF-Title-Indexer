import sys
import pdfplumber
import re

#  put desired PDF file as first arg
file_input = sys.argv[1]
pdf_file = pdfplumber.open(file_input)

file_object = open(f"INDEX-FOR-{file_input}.csv",
                   "w")

#  This can be changed to have
file_object.write("Topic, Page Number\n")
for pages in pdf_file.pages:
    words_on_page = pages.extract_words(keep_blank_chars=True,
                                        extra_attrs=[
                                            "fontname", "size"])
    for word in words_on_page:
        if re.match(".{6}[+]Erie,Bold",
                    word['fontname']):
            subheading_word = word['text']
            if not re.match("\s+", subheading_word):
                page_footer_list = list((words_on_page[-2]['text']).split(" "))
                # print(page_footer_list)
                if page_footer_list[0] == "TSFX":  # check start of TSFX
                    page_number = page_footer_list[40]
                    file_object.write(f"{subheading_word}, {page_number}")
                else:
                    file_object.write(f"{subheading_word}, NO NUMBER")
                file_object.write('\n')

file_object.close()

# pages.page_number-first_page_number


print('Indexing is complete!\n')
