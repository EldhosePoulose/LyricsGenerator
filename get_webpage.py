def get_webpage(term):
    # For Example: term= "Imagine Dragons Believer"
    url= "https://genius.com/" + term.replace(" ", "-") + "-lyrics"
    print(url)
    return url