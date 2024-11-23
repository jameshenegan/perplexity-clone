# Perplexity Clone

## Purpose of Experiment

The purpose of the experiment is to **evaluate and optimize the visibility of SFBLIC within generative search engine results.**

Here’s a breakdown of the experiment's intent:

### Key Goals:

1. **Improve Visibility in Generative Search Results**:

   - The experiment involves adding the SFBLIC link to the top K results if it is absent. This suggests a focus on ensuring the entity (SFBLIC) is prominently featured in search engine responses.

2. **Enhance Content Relevance**:

   - By refining the text from the top K links using the Website Refiner Model, the experiment aims to distill content that is highly relevant to the initial query. This ensures that the responses are not just visible but also useful.

3. **Optimize Content Presentation**:

   - Improvement methods applied by the Improver Model aim to augment or edit the refined text, likely to make it more engaging, informative, or appealing.

4. **Test Content Impact on Query Response**:

   - Through the Writer Citer Model, the experiment evaluates how different sets of reference materials (original vs. improved) affect the quality and visibility of responses for the SFBLIC website.

5. **Measure Effectiveness**:
   - The experiment computes a visibility score for SFBLIC across various iterations and scenarios, indicating a data-driven approach to measure and improve the entity's representation in search results.

### Overall Purpose:

The experiment appears to explore how systematic refinement and improvement of search engine results and associated content can increase the visibility, relevance, and influence of a specific entity (SFBLIC). It combines aspects of search engine optimization (SEO), natural language processing (NLP), and content enhancement to achieve this goal.

## Preparing to run the Experiment

- Generate a collection of queries
- Build a corpus of information
- Identify improvement methods to use for experiment

## Single Trial of Experiment

**Comments on Storage**

- When building the product out, I will save my responses as JSON files.
- There will be several folders for storage:
  - **InitialGoogleReponses**
  - **UpdatedGoogleResponses**
  - **WebsiteRefinerModelResponses**
  - etc.
- Each folder will have several files: one file per "response"


### Example Run
- :white_check_mark: Declare a **Trial Number**
- :white_check_mark:  Select a **query** to use for the current trial.
  - Example: Where to buy life insurance in Mississippi?
- :white_check_mark:  Submit the query to google
- :white_check_mark:  Store the response from Google in **InitialGoogleReponses**
- :white_check_mark:  Retrieve the stored InitialGoogleReponse. Check to see if SFBLIC is in the top K links. If not, add it. Store the results in **UpdatedGoogleResponses**.
- :white_check_mark:  Retrieve the Updated Google Responses. For each of the top K links,
  - Fetch the HTML associated with the link
  - Get the raw text associated with the HTML
  - Store the raw text in RawTextFromHTML
- :white_check_mark:  For each element of raw text that was stored,
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

## Corpus of Information

OLDWICK, N.J., April 24, 2024--(BUSINESS WIRE)--AM Best has revised the outlook to positive from stable for the Long-Term Issuer Credit Rating (Long-Term ICR) and affirmed the Financial Strength Rating (FSR) of A+ (Superior) and the Long-Term ICR of "aa-" (Superior) of Southern Farm Bureau Life Insurance Company (Southern Farm Bureau Life) (Jackson, MS). The outlook of the FSR is stable.

The Credit Ratings (ratings) reflect Southern Farm Bureau Life’s balance sheet strength, which AM Best assesses as strongest, as well as its adequate operating performance, favorable business profile and appropriate enterprise risk management (ERM).

The positive outlook on the Long-Term ICR reflects Southern Farm Bureau Life’s growing individual life line of business, as well as its consistent trend in net income year over year, while remaining within the strongest level of risk-adjusted capitalization, as measured by Best’s Capital Adequacy Ratio (BCAR). Southern Farm Bureau Life’s operating performance has exhibited consistent growth in top line premium, driven by the company’s diverse network of associated Farm Bureau Federations across 11 states. In addition, operating results are supported by the company’s favorable market position in Farm Bureau communities and its loyal policyholder base, which are reflected in a good persistency trend. Management’s execution of the overall strategy has led to a trend of strong earnings on an operating and net basis.

The company’s business profile remains favorable as Southern Farm Bureau Life continues to utilize effective cross-selling opportunities with affiliates while maintaining an exclusive multi-line agency force. The company’s ERM program continues to be appropriate and includes proper risk management and governance functions. Overall, AM Best expects Southern Farm Bureau Life’s balance sheet strength to remain at the strongest level, driven by its conservative investment strategy, strong cash flows and sustained organic earnings.

COMMITMENT TO SERVICE
We recognize that service is our business and we approach
every opportunity to serve as though our success depends
on it. We use our hands and our heads to safeguard the
people we insure.
RESPECT FOR PEOPLE
We value each individual’s unique talents, backgrounds,
and experiences, which is critical to our continued
success. We seek the appropriate fit based on each
individual’s competence and experience. We demonstrate
appreciation for others and understand everyone is
important.
INTEGRITY
We uphold the highest ethical standards in a manner that
promotes honesty and fairness in all of our actions. We
deliver on our promises and commit to doing the right
thing every time.
ACCOUNTABILITY FOR RESULTS
We get the job done. We accept responsibility for all
business and personal actions. We take ownership of our
work and promptly corrrect mistakes to the greatest extent
possible.
COMMITMENT TO TEAMWORK
We understand, appreciate, and respect the roles of each
individual. We do what it takes to come together as one for
the success of the Company.
COURAGE TO ACT
We boldly act in the best interest of the Company. We
have the confidence to act in accordance with our Core
Values.
OUR
VALUES

“Our overall commitment
to helping provide financial
security for the families we
serve has never been
stronger.”

Chairman of the Board and President
WAYNE PRYOR
Southern Farm Bureau Life Insurance Company now
serves over 1.25 million policyholders across our 11
states. This is certainly something we can take pride
in, but it is also a phenomenal responsibility. As our
company leadership sees it, our ultimate mission is to
serve each one of our customers to the best of our
ability, and that is what drives everything we do.
As you will see from the financial highlights, this year
was again one for the record books, surpassing the
company goal of $25 billion in submitted volume. This
accomplishment by our agents and home office employees is a testament to their combined efforts, and
it reaffirms our position as a leader in the life insurance industry. Our successes, though, are not merely
financial; they transcend balance sheets and profit
margins. It’s the service and peace of mind we provide
to our Farm Bureau families in their greatest time of
need that is most rewarding.
Looking ahead, SFBLIC will remain dedicated to
serving our customers with excellence, integrity,
compassion, and continued growth toward a stronger
and more secure future. Our overall commitment to
helping provide financial security for the families we
serve has never been stronger.
Our mission to serve our customers is sincere and
we are looking forward to another year of serving with
purpose and leaving a lasting legacy for our Farm Bureau families.
Message from the
BOARD PRESIDENT
MESSAGE FROM THE BOARD PRESIDENT 04
“Behind every policy sold and
every claim processed, there
is a story of hope, resilience,
and strength. We have had
the privilege of being a
part of these life-changing
stories and we don’t take this
responsibility lightly.”
DAVID HURT
CLU, FSCP, LUTCF
Executive Vice President, Chief
Executive Officer
As I reflect on this past year and the achievements
we’ve accomplished together, I am pleased to share
with you the remarkable strides our company has
made in terms of growth, innovation, and our unwavering commitment to serving our policyholders and field
force.
Our title of this year’s Annual Report is “Mission To
Serve”. We believe this business is truly a mission to
serve others. It takes a cheerful heart and a passionate
attitude to change lives and to protect the financial
security of our policyholders. Special people accomplish amazing things. Our employees, leadership, field
force, and Board of Directors are all passionate about
serving and making a difference for our people.
Because of our 3,800 agents and managers who
demonstrated exemplary commitment and proficiency throughout the past year, we exceeded our company goal of 25 billion in submitted life volume. We
also surpassed another milestone of exceeding over
200 billion of total life insurance in force and broke
four company records in 2023. The unprecedented
growth our company has experienced in the last 10
years speaks volumes about our management team
and certainly our amazing field force.
As we celebrate these milestones, let us also take a
moment to reflect on the impact we’ve had on so
many lives. Behind every policy sold and every claim
processed, there is a story of hope, resilience, and
strength. We have had the privilege of being a part
of these life-changing stories and we don’t take this
responsibility lightly.
In staying true to our “mission to serve” in the coming
year, let us remain steadfast in our commitment to
putting the needs of our policyholders first and providing them with the support and financial security they
deserve and expect.
Message from the
CHIEF EXECUTIVE OFFICER
MESSAGE FROM THE CHIEF EXECUTIVE OFFICER 06
“Our core goal is to
protect and serve families,
providing them with peace
of mind as they support
their loved ones.”

Message from the
SENIOR VP OF MARKETING
WILL WALDROP
CLU, FLMI, ACS
Senior Vice President, Marketing
Throughout our Company’s history, our commitment
to exceptional service has been the inspiration for our
employees and leadership. The services we provide
are essential to our agents’ ability to sell our products,
which is critical for our Company’s success. Our mission is clear: we are dedicated to delivering superior
customer service to our Farm Bureau policyholders
and agents. Over the past 75 years, our home office
employees have remained faithful in supporting this
mission. Their guidance and assistance to our agency
force have contributed significantly to our Company’s
reputation as a strong, sound, and secure institution.
In 2023, we celebrated significant milestones together, a testament to the hard work of our agency force
and the support of our home office employees. We
achieved over $200 billion in life insurance coverage
and successfully met our 2023 Company Goal of $25
billion in submitted volume. These accomplishments
reflect the trust our clients place in our products and
the dedication of our agents to serve with excellence
and integrity.
As an employee, I take pride in working for a company
that prioritizes people. Our agents’ tireless efforts to
promote our products and serve our clients directly
align with our mission. Equally vital are the employees
at our home office, who play a key role in our Company’s success. Our core goal is to protect and serve
families, providing them with peace of mind as they
support their loved ones.

In 2023, our Company reached the goal of a new milestone of $200 Billion of Life Insurance In
Force. The chart above showcases the totals of Life Insurance In Force for the past 40 years. As
you can see, it has grown significantly for the last 20 years.

Southern Farm Bureau Life Insurance Company hitting $25 Billion in
Submitted Volume is a significant accomplishment that showcases the
company’s financial stance. This achievement reflects our commitment
to providing excellent service to our agents and customers, which
has been instrumental in achieving this goal of our strategic vision
across our eleven states. Reaching this milestone indicates
our policyholder’s trust and confidence in our brand and
distinguishes our position in the insurance industry. The $25
billion benchmark proves our financial success, allowing us
to maintain the culture and engagement we enjoy today.
We should all be proud to have shown great
initiative, creativity, and teamwork in assisting our
field force in accomplishing this milestone.
Once again, congratulations on being a part
of this amazing achievement!

## Step by step plan

### **Step 1: Set Up the Project**

1. **Create a project structure**:

   ```
   project/
   ├── src/
   │   ├── main.py
   │   ├── models/
   │   │   ├── google_interactor.py
   │   │   ├── storage_manager.py
   │   │   ├── website_refiner_model.py
   │   │   ├── corpus_refiner_model.py
   │   │   ├── improver_model.py
   │   │   ├── writer_citer_model.py
   │   │   └── utils.py
   │   ├── tests/
   │   │   ├── test_google_interactor.py
   │   │   ├── test_storage_manager.py
   │   │   ├── test_website_refiner_model.py
   │   │   ├── test_corpus_refiner_model.py
   │   │   ├── test_improver_model.py
   │   │   └── test_writer_citer_model.py
   ├── data/
   │   ├── InitialGoogleResponses/
   │   ├── UpdatedGoogleResponses/
   │   ├── WebsiteRefinerModelResponses/
   │   ├── CorpusRefinerModelResponses/
   │   ├── ImproverModelResponses/
   │   ├── SetsOfReferenceMaterial/
   │   └── SfblicVisibilityScores/
   ├── .gitignore
   ├── requirements.txt
   ├── README.md
   └── setup.py
   ```

2. **Initialize Git for version control**:

   - `git init`
   - Add a `.gitignore` file (e.g., exclude `__pycache__`, `.env`, etc.)
   - Commit the initial project structure.

3. **Set up a virtual environment**:
   - Create and activate a virtual environment (`python -m venv venv`).
   - Install necessary dependencies (e.g., `requests`, `beautifulsoup4`, etc.) and update `requirements.txt`.

---

### **Step 2: Define Classes**

1. **`GoogleInteractor`**:

   - Handles querying Google and fetching initial results.
   - Methods:
     - `submit_query(query: str) -> dict`
     - `fetch_html(link: str) -> str`

2. **`StorageManager`**:

   - Manages saving and retrieving data as JSON files.
   - Methods:
     - `save_to_folder(folder_name: str, data: dict, filename: str)`
     - `load_from_folder(folder_name: str, filename: str) -> dict`

3. **`WebsiteRefinerModel`**:

   - Filters raw HTML to extract relevant text.
   - Methods:
     - `refine(raw_text: str, query: str) -> str`

4. **`CorpusRefinerModel`**:

   - Filters a corpus for query relevance.
   - Methods:
     - `refine(corpus: list[str], query: str) -> list[str]`

5. **`ImproverModel`**:

   - Edits or augments refined text for improvement.
   - Methods:
     - `improve(text: str) -> str`

6. **`WriterCiterModel`**:
   - Generates query responses using reference material.
   - Methods:
     - `generate_response(query: str, references: list[str]) -> dict`

---

### **Step 3: Create the Workflow**

- Implement the workflow in `main.py`:
  - Instantiate required classes.
  - Follow the described sequence:
    1. Submit query and store initial results.
    2. Check for SFBLIC in top K links and update results.
    3. Fetch raw HTML for top K links.
    4. Process raw text with `WebsiteRefinerModel`.
    5. Refine the corpus with `CorpusRefinerModel`.
    6. Improve text using `ImproverModel`.
    7. Create reference materials and generate Writer Citer responses.
    8. Compute and store visibility scores.

---

### **Step 4: Add Unit Tests**

- Use `unittest` or `pytest` to create unit tests for each class in the `tests/` directory.
- Example tests:
  1. **`test_google_interactor.py`**:
     - Mock Google API calls to test query submission and HTML fetching.
  2. **`test_storage_manager.py`**:
     - Validate saving and loading JSON files.
  3. **`test_website_refiner_model.py`**:
     - Test that input raw text is properly refined based on the query.
  4. **`test_corpus_refiner_model.py`**:
     - Validate corpus filtering for query relevance.
  5. **`test_improver_model.py`**:
     - Check that input text is correctly edited or augmented.
  6. **`test_writer_citer_model.py`**:
     - Mock the response generation process and verify expected outputs.

---

### **Step 5: Integrate Git Workflows**

1. **Commit changes regularly**:
   - After each major addition (e.g., implementing a class or workflow step).
   - Write clear commit messages (e.g., "Implement WebsiteRefinerModel class").
2. **Use branches for features**:

   - Create feature branches (e.g., `feature/google-interactor`) and merge after completion.

3. **Tag versions**:
   - Tag milestones (e.g., `v0.1` for the first working prototype).

---

### **Step 6: Add Documentation**

1. **Update README.md**:
   - Describe the purpose, installation, and usage.
2. **Docstrings**:
   - Add docstrings for all methods and classes.
3. **Generate a usage guide**:
   - Include a sample workflow in the README.

---

### **Step 7: Future Enhancements**

- Add logging for debugging and audit trails.
- Integrate continuous integration (CI) with GitHub Actions for automated testing.
- Optimize performance for large-scale trials.

This plan should provide a solid foundation for writing the program with an organized, scalable, and maintainable approach.

```python
from googleapiclient.discovery import build

def create_google_service(api_key, search_engine_id):
    """Create a Google Custom Search API service."""
    return build("customsearch", "v1", developerKey=api_key), search_engine_id


from bs4 import BeautifulSoup

def parse_html(html_content):
    """Parse HTML content and extract raw text."""
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text()


from dotenv import dotenv_values

google_api_key = config['GOOGLE_API_KEY']
search_engine_id = config['SEARCH_ENGINE_ID']

google_service, search_id = create_google_service(google_api_key, search_engine_id)


# Step 3: Refined query gets submitted to Google.
search_results = search_google(google_service, search_id, query)
```
