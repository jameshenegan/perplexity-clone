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
- The LLM summarizes the information from those sites.
- This summary is returned to the user.  

One of the main selling points behind generative engines is as follows: by summarizing information retrieved from sites relevant to the user's query, the LLM will be less likely to [hallucinate](https://www.ibm.com/topics/ai-hallucinations) when composing a response.

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
