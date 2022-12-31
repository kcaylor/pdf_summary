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

#%%

def get_paper_content(filename=None,use_pypdf=True):
    """ Create pdf object from file

    Parameters
    ----------
    filename : string, optional
        filename for pdf, by default None
    use_pypdf : bool, optional
        choose which pdf library to use, by default True

    Returns
    -------
    list
        list of page objects, one per page in pdf

    """    
    if filename and not use_pypdf:
        return pdfplumber.open(filename).pages
    elif filename and use_pypdf:
        pdfFileObj = open(filename, 'rb')
        pdfReader = pypdf.PdfReader(pdfFileObj)
        return pdfReader.pages
        
def summarize_page(page,
                   stop_tag='###---###',
                   type='college professor',
                   max_tokens=100):
    """Summarizes pdf page using openai

    Parameters
    ----------
    page : page object
        single page of a pdf
    stop_tag : string, optional
        stop string for model, by default '###---###'
    type : str, optional
        reading level of summary output, by default 'college professor'
    max_tokens : int, optional
        maximum number of words in summary, by default 100

    Returns
    -------
    string
        Summary text from model
    """    
    prompt = "Summarize this for a {type}:\n".format(type=type)
    text = prompt + page.extract_text() + stop_tag
    response = openai.Completion.create(engine="text-davinci-003",prompt=text,
            temperature=0.3,
            max_tokens=max_tokens,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=[stop_tag]
        )
    return response['choices'][0]['text']

# %%

if __name__ == "__main__":
    """
    Checks if the code is the main module and reassigns the command line arguments to variables.
    Gets the paper content from the specified filename.
    Creates a progress bar to track the progress of the summaries.
    Loops over the paper content and sumsarizes each page, saving the result in a dictionary.
    Prints each summary in the dictionary. 
    """
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

