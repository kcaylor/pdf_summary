#%%
import openai
import wget
import pathlib
import pdfplumber
import pypdf
import json
import os
import sys
from progress.bar import Bar

from dotenv import load_dotenv
load_dotenv() 

openai.organization = os.getenv('ORGANIZATION_ID', None)
openai.api_key = os.getenv('API_KEY', None)
engine = "text-davinci-003"

tldr_tag = "\n tl;dr:"
#%%

def get_paper(paper_url, filename="random_paper.pdf"):
    """
    Downloads a paper from it's arxiv page and returns
    the local path to that file.
    """
    downloaded_paper = wget.download(paper_url, filename)    
    downloaded_paper_filepath = pathlib.Path(downloaded_paper)

    return downloaded_paper_filepath

def get_paper_content(filename=None,use_pypdf=True):
    if filename and not use_pypdf:
        return pdfplumber.open(filename).pages
    elif filename and use_pypdf:
        pdfFileObj = open(filename, 'rb')
        pdfReader = pypdf.PdfReader(pdfFileObj)
        return pdfReader.pages
        
def summarize_page(page,tldr_tag=tldr_tag,
                   type='college professor',
                   max_tokens=100):
    prompt = "Summarize this for a {type}:\n".format(type=type)
    text = prompt + page.extract_text() + tldr_tag
    response = openai.Completion.create(engine="text-davinci-003",prompt=text,
            temperature=0.3,
            max_tokens=max_tokens,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=[tldr_tag]
        )
    return response['choices'][0]['text']

#%%
filename = 'test_file.pdf'
paper_content = get_paper_content(filename=filename)
#print(summarize_page(paper_content[3]))
summary = {i:summarize_page(page) for i,page in enumerate(paper_content)}

# %%

if __name__ == "__main__":
    args = sys.argv[1:]
    filename = args[0]
    paper_content = get_paper_content(filename=filename)
    bar = Bar('Processing', max=len(paper_content))
    summary = {}
    for i,page in enumerate(paper_content):
        summary[i] = summarize_page(page)
        bar.next()
    bar.finish()
    [print(f"Page {i}"+item) for i,item in enumerate(summary.values())]
    # print(json.dumps(summary))

