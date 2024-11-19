# Perplexity Clone

```
cd perplexity-clone/bin
source activate
cd ../..
python -m jupyterlab
```

1. User submits query.
2. Intelligent LLM "refiner" refines the query.
3. Refined query gets submitted to Google.
4. The URL's to the top 5 links are collected.
5. Does SFBLIC come up in the top 5 links? If not, replace the 5th link with SFBLIC.
6. Each link is fetched and cleaned with Beautiful soup's get_text()
7. Semi-intellignt LLM "trimmer" trims the cleaned results so that they contain information relevant to query.
8. Intelligent LLM "writer-citer" is asked to write a response that will answer the refined query using only the cleaned results, providing citations to the results in a certain manner.
9. Visibility metrics are computed.
10. Intelligent LLM "marketer" is asked to re-write or add content to the SFBLIC page according to certain directions.
11. Visibility metrics are computed.
12.

## Requirements

```
pip install openai
pip install requests
pip install python-dotenv
pip install beautifulsoup4
pip install google-api-python-client
pip install jupyterlab
python -m ipykernel install --user --name=perplexity-clone
```
