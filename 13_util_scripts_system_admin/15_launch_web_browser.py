
import webbrowser

# open a webbrowser
webbrowser.open('http://www.python.org')

# Open the page in a new browser window
webbrowser.open_new('http://www.python.org')

# Open the page in a new browser tab
webbrowser.open_new_tab('http://www.python.org')

# specify which browser
c = webbrowser.get('firefox')
c.open('http://www.python.org')

c.open_new_tab('http://docs.python.org')