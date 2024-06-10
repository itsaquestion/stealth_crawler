
from readability import Document
from markdownify import markdownify as md

def remove_last_line_if_starts_with_hash(text):
    """ 如果最后一行以#开头，则去除该行
    :param text:
    :return: text
    """
    lines = text.splitlines()  # 将文本按行分割成列表
    if lines and lines[-1].startswith('#'):  # 检查最后一行是否以#开头
        lines = lines[:-1]  # 去除最后一行
    return '\n'.join(lines)  # 将剩余行合并成字符串

def get_short_title(html):
    doc = Document(html)
    # summary = doc.summary()
    title = doc.short_title()
    return title

def parse(page_html):
    doc = Document(page_html)
    # summary = doc.summary()
    title = doc.short_title()
    summary = doc.summary()
    
    markdown = html_to_md(summary, title)
    
    return {'title':title, 'html':summary, 'md':markdown}
    

def html_to_md(summary, title):
    """ 将html转换为markdown
    :param html:
    :return: markdown
    """
    markdown = md(summary).strip()
    
    if not markdown.startswith('# '):
        markdown = "# " + title + '\n\n' + markdown
    
    return remove_last_line_if_starts_with_hash(markdown).strip()