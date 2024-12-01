# Perplexity Experiment

## Development

### Activate the virtual environment and open JupyterLab

```
cd perplexity-clone/bin
source activate
cd ../..
python -m jupyterlab
```

## Next Steps

- Add additional improvement methods
- Improve the way that results are stored, accessed, and presented

## List of queries

- Where should I buy Life Insurance in Mississippi?
- Who sells life insurance in Mississippi?
- What is Life Insurance?
- What products are offered by Southern Farm Bureau Life Insurance Company?
- Why should I buy Life Insurance from Southern Farm Bureau?

### **General Information About Life Insurance**

1. What is life insurance?
2. Why do I need life insurance?
3. How does life insurance work?
4. What are the different types of life insurance policies?
5. How is life insurance different from other types of insurance?
6. Can I have more than one life insurance policy?

### **Choosing the Right Policy**

6. How do I decide which type of life insurance is right for me?
7. What factors should I consider when choosing my coverage amount?
8. What is the difference between term and whole life insurance?
9. How do I calculate how much life insurance I need?
10. What happens if I outlive my term life insurance policy?

### **Cost and Affordability**

11. How much does life insurance cost?
12. What factors affect the cost of a life insurance policy?
13. Are there ways to lower my life insurance premiums?
14. Is life insurance taxable?
15. Can I afford life insurance if I have pre-existing conditions?

### **Application Process**

16. What is the process for applying for life insurance?
17. Do I need a medical exam to get life insurance?
18. How long does it take to get approved for life insurance?
19. What information do I need to provide when applying for life insurance?
20. Can I apply for life insurance online?

### **Policy Features and Benefits**

21. What is a beneficiary, and how do I choose one?
22. Can I change my life insurance policy after I buy it?
23. What is cash value, and how does it work in life insurance?
24. How does life insurance help with estate planning?
25. Are there riders or add-ons I can include in my policy?

### **Claims and Payouts**

26. How do beneficiaries make a claim when the policyholder passes away?
27. How long does it take to receive a life insurance payout?
28. Are there circumstances under which a life insurance claim might be denied?
29. What documentation is needed to file a life insurance claim?
30. Can I use life insurance benefits while I'm still alive?

### **Specific Life Stages and Needs**

31. Do I need life insurance if I’m single?
32. What type of life insurance is best for parents?
33. Should retirees have life insurance?
34. How does life insurance work for business owners?
35. Can life insurance help cover my children’s education costs?

### **Special Situations**

36. Can people with health issues get life insurance?
37. What happens if I miss a premium payment?
38. Can I borrow money against my life insurance policy?
39. What happens to my life insurance policy if I switch jobs?
40. Does life insurance cover suicide?

### **Life Insurance Company Information**

41. Why should I choose your company for life insurance?
42. What sets your life insurance products apart from others?
43. How do I contact customer support for questions about my policy?
44. Can I manage my life insurance policy online?
45. Are there customer reviews or testimonials I can read?

### **Educational Content and Tools**

46. What resources do you provide to help me learn about life insurance?
47. Do you have a life insurance calculator?
48. Are there articles or guides about life insurance on your website?
49. Can I get a free quote online?
50. What happens if I need help deciding on a policy?

Would you like me to refine this list further based on specific needs or areas of focus for your experiment?

## Comparison with State Farm

### Questions part 1

Here are several questions that could be answered using the information provided in the text:

### General Life Insurance

1. What is life insurance, and how does it work?
2. What are the primary purposes of life insurance?
3. What types of life insurance does State Farm offer?
4. How can life insurance help protect a family’s financial future?

### Types of Life Insurance

5. What is the difference between term life insurance and permanent life insurance?
6. What are the features of term life insurance offered by State Farm?
7. How does whole life insurance differ from universal life insurance?
8. What are the benefits of permanent life insurance policies?

### Obtaining a Quote or Policy

9. What information is needed to get a life insurance quote from State Farm?
10. How can I calculate how much life insurance coverage I need?
11. How can I find a local State Farm agent to discuss life insurance?
12. What steps are involved in changing a life insurance policy or beneficiary?

### Business and Specialized Insurance

13. What life insurance options are available for small businesses through State Farm?
14. What is Group Life insurance, and who is it designed for?

### Policy Features and Tools

15. What is the Life Enhanced app, and who is eligible to use it?
16. How can I file a life insurance claim with State Farm?
17. What resources does State Farm provide for learning more about life insurance?

### Legal and Coverage Details

18. Are there tax implications associated with permanent life insurance policies?
19. Are State Farm life insurance policies available in all states?
20. What restrictions or conditions might apply to State Farm life insurance policies?

This comprehensive range of questions covers various aspects of the information provided, from general education on life insurance to specific details about State Farm’s offerings and processes.

### Questions Part 2

Here are some questions that could be answered by the information provided in the text:

### About State Farm Life Insurance

1. Why should someone buy life insurance from State Farm?
2. How long has State Farm been providing life insurance?
3. How many life insurance and annuity policies does State Farm currently have in force?
4. What is State Farm’s company mission and how does it relate to its life insurance offerings?

### Financial Strength and Stability

5. What financial ratings has State Farm received from major independent rating agencies?
6. How does State Farm's conservative investing strategy benefit its life insurance policyholders?
7. What makes State Farm's financial stability appealing to potential life insurance buyers?

### Customer Service and Philosophy

8. What is the philosophy of State Farm regarding helping customers with life insurance?
9. How does State Farm's "good neighbor" service benefit policyholders?
10. How can customers get personalized guidance for life insurance from State Farm agents?

### Product Offerings and Tools

11. What competitive product options does State Farm offer for life insurance?
12. What tools does State Farm provide to help customers determine how much life insurance they need?

### Accessing and Applying for Insurance

13. How can a potential customer get a life insurance quote from State Farm?
14. What are the steps for finding a local State Farm agent?
15. How can someone apply for life insurance or learn about specific coverage details?

### Company Values and History

16. What shared values is State Farm’s success built on?
17. How does State Farm maintain long-term stability for its life insurance products?

### Additional Resources

18. Where can customers find more information about State Farm's annual reports or corporate values?
19. What services are accessible through State Farm’s website, such as filing claims or managing payments?

This range of questions encompasses the company’s background, financial strength, customer support philosophy, product options, and tools for prospective life insurance buyers.

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

## Get SFBLIC Info from Google

```
import json

with open("../data/InitialGoogleResponses/3.json") as f:
    sfblic_info = json.load(f)['items'][0]

sfblic_info
```
