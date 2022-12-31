# pdf_summary

This code summarizes a PDF file. 

The code requires an API key from openai, which is stored in an `.env` file

The model uses the `"text-davinci-003"` engine, but a different engine can be used. 

Default is to return summaries suitable for a college professor, but this can be altered by changing the `type` parameter in the call to `summarize_page`.

When run from the command line, the code will output a summary of the PDF file, with each page summarized on its own line.

