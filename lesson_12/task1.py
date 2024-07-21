from bs4 import BeautifulSoup
import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        text = soup.get_text(separator=' ').strip()

    with open(result_file, 'w', encoding='utf-8') as result:
        for line in text.split('\n'):
            cleaned_line = line.strip()
            if cleaned_line:
                result.write(cleaned_line + '\n')


delete_html_tags("draft.html", "cleaned.txt")
