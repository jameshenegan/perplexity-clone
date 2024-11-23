# Perplexity Experiment

## Purpose of Experiment

The purpose of the experiment is to **evaluate and optimize the visibility of SFBLIC within generative search engine results.**

## Steps to preparing to run the Experiment

- Generate a collection of queries
- Build a corpus of information
- Identify improvement methods to use for experiment

## Comments on Storage

- When building the product out, I will save my responses as JSON files.
- There will be several folders for storage:
  - **InitialGoogleReponses**
  - **UpdatedGoogleResponses**
  - **WebsiteRefinerModelResponses**
  - etc.
- Each folder will have several files: one file per "trial"

## Single Trial of Experiment

- Declare a **Trial Number**
- Select a **query** to use for the current trial.
- Example: Where to buy life insurance in Mississippi?
- Submit the query to google
- Store the response from Google in **InitialGoogleReponses**
- Retrieve the stored InitialGoogleReponse. Check to see if SFBLIC is in the top K links. If not, add it. Store the results in **UpdatedGoogleResponses**.
- Retrieve the Updated Google Responses. For each of the top K links,
- Fetch the HTML associated with the link
- Get the raw text associated with the HTML
- Store the raw text in RawTextFromHTML
- For each element of raw text that was stored,
- Use the **Website Refiner Model** to filter the raw text to the **refined text**: text that is relevant to the query
- Store the response from the Website Refiner Model in **WebsiteRefinerModelResponses**.
- Use the **Corpus Refiner Model** to filter the corpus to information that may be relevant to the query. Store the response in **CorpusRefinerModelResponses**.
- For each of the M improvement methods,
- Use the **Improver Model** to either edit or augment the refined text associated with the SFBLIC website, along with the refined text for the other top K links.
- Store the results from the Improver model in **ImproverModelResponses**.
- Prepare various (M+1) sets of **reference material** that will be sent to the **Writer Citer Model** in the next step.
  - One set will contain the original (unimproved) refined text associated with the SFBLIC website, along with the refined text for the other top K links.
  - Each of the other (M) sets will contain "improved" (i.e., edited or augmented) versions of the refined text associated with the SFBLIC website, along with the refined text for the other top K links
  - Store the results in **SetsOfReferenceMaterial**
- For each of the M+1 sets of reference material,
  - Send a prompt to the **Writer Citer** model. The model is asked to compose a response to the original query, citing the sources provided in the reference material.
  - Store the response from the Writer Citer in **WriterCiterModelResponses**.
- For each resposne from the Writer Citer model,
  - Compute a visibility score for SFBLIC
  - Store the result in **SfblicVisibilityScores**

## Activate the virtual environment and open JupyterLab

```
cd perplexity-clone/bin
source activate
cd ../..
python -m jupyterlab
```

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

## Additional Links

Links with additional information to pull from:

- https://www.scfbins.com/insurance/other-products/financial-services
- https://www.scfbins.com/insurance/other-products/life-insurance
- https://www.sfbli.com/blogs/Giving-Thanks
- https://www.sfbli.com/blogs/LIAM2024
- https://www.sfbli.com/blogs/Celebrating-Fathers-Day
- https://www.sfbli.com/blogs/My-Reason-For-Life-Insurance
- https://www.sfbli.com/blogs/Insure-Your-Love-2024
- https://www.sfbli.com/blogs/Planning-For-The-Future
- https://www.sfbli.com/blogs/LIAM-2023
- https://www.sfbli.com/blogs/Values
- https://www.sfbli.com/blogs/Why-Life-Insurance
- https://www.sfbli.com/blogs/Women-And-Insurance
- https://www.sfbli.com/blogs/LIAM-2023
- https://www.sfbli.com/blogs/Planning-For-The-Future
- https://www.insure.com/companies/southern-farm-bureau-life-insurance.html
- https://msfbins.com/products/life/
- https://sfbli.com/aboutus
- https://sfbli.com

## Next Steps

- Add additional improvement methods
- Improve the way that results are stored
- Come up with a set of queries
- Come up with a better corpus of information
- Figure out how to compute validity scores
