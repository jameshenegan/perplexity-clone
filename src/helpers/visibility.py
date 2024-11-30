import re
import nltk
import math
import itertools

def count_meaningful_words(words):
    """
    Count the number of words with more than 2 characters in a list of words.
    """
    return len([word for word in words if len(word) > 2])

def parse_citations_from_text(text):
    """
    Parse the text to extract structured citation data, including tokenized words, sentences, and citation IDs.
    """
    def extract_citation_ids(sentence):
        """
        Extract numerical citation IDs from a sentence.
        Citation format: [1], [2], etc.
        """
        citation_pattern = r'\[[^\w\s]*\d+[^\w\s]*\]'
        return [int(re.findall(r'\d+', citation)[0]) for citation in re.findall(citation_pattern, sentence)]

    # Split text into paragraphs
    paragraphs = re.split(r'\n\n', text)

    # Tokenize paragraphs into sentences, and tokenize sentences into words
    structured_data = [
        [(nltk.word_tokenize(sentence), sentence, extract_citation_ids(sentence)) for sentence in nltk.sent_tokenize(paragraph)]
        for paragraph in paragraphs
    ]
    return structured_data

def compute_citation_scores(citation_data, num_citations=5, normalize=True):
    """
    Compute relevance scores for each citation based on word count, position in text, and number of citations per sentence.
    """
    # Flatten the nested list of sentences
    flattened_sentences = list(itertools.chain(*citation_data))
    citation_scores = [0 for _ in range(num_citations)]

    for sentence_index, sentence_data in enumerate(flattened_sentences):
        words, _, citations = sentence_data
        if not citations:
            continue  # Skip sentences without citations

        # Calculate the number of meaningful words in the sentence
        word_count = count_meaningful_words(words)
        # Apply a position-based weight (exponential decay)
        position_weight = math.exp(-1 * sentence_index / (len(flattened_sentences) - 1)) if len(flattened_sentences) > 1 else 1
        # Distribute the sentence score equally among its citations
        sentence_score = word_count * position_weight / len(citations)

        # Accumulate scores for each citation
        for citation_id in citations:
            try:
                citation_scores[citation_id - 1] += sentence_score
            except IndexError:
                print(f'Warning: Citation ID out of range: {citation_id}')

    # Normalize the scores if required
    if normalize and sum(citation_scores) != 0:
        citation_scores = [score / sum(citation_scores) for score in citation_scores]
    elif normalize:
        citation_scores = [1 / num_citations for _ in range(num_citations)]

    return citation_scores