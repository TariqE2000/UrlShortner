import pyshorteners 
def shortenUrl (longUrl: str):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(longUrl)