def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    # Your code here
    return [i for i in tokens if i not in stopwords]
    pass