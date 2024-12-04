# Experiment involving a Perplexity Clone

## Introduction

The purpose of this repository is to record some ideas related to an experiment involving [Generative Engine Optimization (GEO)](https://arxiv.org/abs/2311.09735).

Large companies such as Microsoft and Google have been in the process of rolling out generative engines since 2023 with products such as [Bing Generative Search](https://blogs.bing.com/search/July-2024/generativesearch) and [Google AI Search Labs](https://blog.google/products/search/generative-ai-search/). Meanwhile, newer companies such as [Perplexity AI](https://en.wikipedia.org/wiki/Perplexity_AI) have been speciliazing in the development of generative engines.  Hence, we may use the term **Perplexity Clone** to refer to a generic, generative engine.

The purpose of the experiment is to see how different sets of **reference material** influence the **visibility metrics** of websites that get cited by a generative engine. In particular, we focus on improving the visibility metrics related to a particular website we have selected (SFBLIC).

### What do generative engines do?

At a high level, a generative engine is composed of 

- a **traditional search engine** that searches the web and
- a **large language model** (LLM).

A simplified version of the process is as follows:

- A user submits a query.
- The traditional search engine retrieves links to sites that contain information to answer the query.
- The LLM summarizes the information from those sites, attempting to provide an answer to the query.
- This summary is returned to the user.

For example, if the user submits a query such as "Where should I buy life insurance in Mississippi?", then the following information might be gathered from the web:

```json
[
            {
                "link": "https://www.mid.ms.gov/mississippi-insurance-department/consumers/life-insurance-and-annuities/",
                "information": "To buy life insurance in Mississippi, it is advisable to consult with a life insurance agent or company. They can help you review your insurance needs and inform you about available policies. The Mississippi Insurance Department suggests that you consider the following steps:\n\n1. **Determine Your Needs**: Assess how much coverage you need and what you can afford to pay.\n2. **Seek Guidance**: An agent can provide insight into different types of policies and help you find one that best fits your requirements.\n3. **Policy Comparison**: Once you have decided which type of life insurance you need, compare similar policies from different companies to find the best value for your money.\n\nFor more detailed information, you can visit the official website of the Mississippi Insurance Department and access resources for consumers regarding life insurance."
            },
            {
                "link": "https://www.mid.ms.gov/",
                "information": "The best place to buy life insurance in Mississippi would be through the Mississippi Insurance Department's resources. They offer guidance on \"Life Insurance and Annuities,\" where consumers can find information on purchasing the right coverage and amount, as well as detecting deceptive sales practices. Additionally, the Mississippi Insurance Department provides a life insurance policy locator service to assist consumers in locating life insurance policies of deceased family members. For personalized assistance, you can request help by calling their Consumer Help Line at 800-562-2957 or 601-359-2453 for the Jackson area."
            },
            {
                "link": "https://www.dfa.ms.gov/minnesota-life-insurance",
                "information": "You should consider buying life insurance from Minnesota Life Insurance Company, which is an affiliate of Securian Financial. The State of Mississippi offers group term life insurance coverage for active full-time employees through this provider. For more information, you can call Minnesota Life at (888) 658-0193."
            },
]
```

The LLM then might use this information to compose the following response:
```
When considering purchasing life insurance in Mississippi, the recommended approach
is to consult with a life insurance agent or company to help assess your insurance needs
and explore available policies [1]. The Mississippi Insurance Department is a valuable
resource, offering guidance on obtaining the appropriate coverage, comparing policies
from different providers, and avoiding deceptive sales practices [2]. They also provide
a life insurance policy locator service for consumers looking to find policies of deceased
family members [2]. For personalized assistance, you may contact their Consumer Help Line [2].
Additionally, group term life insurance coverage is available for active full-time employees
through the Minnesota Life Insurance Company, affiliated with Securian Financial [3].
```

### What do generative engines offer?

A user may prefer to use a generative engine over traditional web search if (i) they have a specific question that may be answered by information that is available on the web (potentially scattered across multiple sites) and (ii) would prefer to receive a single answer to that question, instead of having to visit multiple sites to piece together the answer themselves.

One of the main selling points behind generative engines is that they attempt to address the problem of [hallucinations](https://www.ibm.com/topics/ai-hallucinations). By summarizing information retrieved from sites relevant to the user's query, the LLM will be less likely to when composing a response.

In spirit, generative engines are somewhat related to [Retrieval-augmented Generation (RAG)](https://en.wikipedia.org/wiki/Retrieval-augmented_generation).   The main difference has to do with the set of documents that are searched.  While generative engines search the web, a RAG system will search a set of pre-defined documents.

## Code 

This repository is still in the early stages of development, but the notebooks are a good place to get started if you want to see what we're doing with our experiment.

- [Perplexity Clone](notebooks/perplexity-clone.ipynb): This notebook provides some code that walks through the basics of what a generative engine does.
- [Single Trial of Experiment](notebooks/run-through-single-trial-of-experiment.ipynb): This notebook walks through a single **trial** of our proposed experiment.

## Next Steps

- **Establish a set of queries**.  Currently, tthe notebook that runs through a single trial of the experiment uses a single query.  We want to have a set of different queries.  This will help us perform multiple trials of the experiment.  Our queries should be questions that could hopefully be answered by the particular website that we have selected (SFBLIC).
- **Add additional improvement methods**.  Right now, the notebook that runs through a single trial of the experiment uses a basic **improvement method**.  We can add additional improvement methods (e.g., 'use more authoritative language', 'write with clear language', etc.)
- **Improve the way that results are stored, accessed, and presented**.  Ultimately, we will be looking for concrete suggestions to make to our particular website.  These suggestions are currently tucked away in a [JSON file](data/ImproverModelResponses/1.json).  Eventually, we will want to make it easier to view these suggestions.

## Current Limitations

- Due to the [black box](https://en.wikipedia.org/wiki/Black_box) nature of commercially available generative engines, we have had to make certain assumptions about how they actually work behind the scenes.  We may be making some incorrect assumptions.
- Due to a scarcity of resources, the generative engine that we are using in the experiment is less sophisticated than the ones seen in the wild.
