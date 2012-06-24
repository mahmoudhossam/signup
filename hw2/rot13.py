import cgi

def rot13(s):
   s = s.encode('rot13')
   return cgi.escape(s, quote=True)
