import pip

def install(package):
    pip.main(['install', package])

# Example
if __name__ == '__main__':
    install('wordcloud')
    install('hazm')
    install('matplotlib')
    install('arabic-reshaper')
    install('python-bidi')