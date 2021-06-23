def bdphonenumbersearch(text):
    import re
    phonerexx=re.compile(r'''(
        (\+\d{2})?                     # area code
        (01)                           # first 2 digits
        (\d{3})                        # next 3 digits
        (\s|-)?                        # separator
        (\d{6})                        # last 6 digits
        (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
         )''', re.VERBOSE)
    return phonerexx.findall(text)
print(bdphonenumbersearch('my phone number is 01745406936'))