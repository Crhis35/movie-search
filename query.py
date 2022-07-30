def search_prefix(keywords):
    #  Multi-field Search
    if not keywords:
        return None
    keywords = keywords.split(' ')
    if len(keywords) > 1:
        prefix = keywords[-1]
        phrase = ' '.join(keywords[:-1])
        query = {
            'query': {
                'bool': {
                    'must': [
                        {
                            'prefix': {
                                'search_index': prefix
                            }
                        },
                        {
                            'match': {
                                'search_index': {
                                    'query': phrase,
                                    'minimum_should_match': '100%'
                                }
                            }
                        }
                    ]
                }
            }
        }
    else:
        keywords = ' '.join(keywords)
        query = {
            'query': {
                'prefix': {
                    'search_index': keywords
                }
            }
        }
    return query


def search_phrase(prefix):
    return {
        'query': {
            'match_phrase_prefix': {
                'title': prefix
            }
        }
    }


def search_prefix_match(keywords):
    if not keywords:
        return None
    keywords = keywords.split(' ')
    if len(keywords) > 1:
        prefix = keywords[-1]
        phrase = ' '.join(keywords[:-1])
        query = {
            'query': {
                'bool': {
                    'must': [
                        {
                            'prefix': {
                                'title': prefix
                            }
                        },
                        {
                            'match': {
                                'title': {
                                    'query': phrase,
                                    'minimum_should_match': '100%'
                                }
                            }
                        }
                    ]
                }
            }
        }
    else:
        keywords = ' '.join(keywords)
        query = {
            'query': {
                'prefix': {
                    'title': keywords
                }
            }
        }
    return query
