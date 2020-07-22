myapplication/
    spam.py
    bar.py
    grok.py
    __main__.py

# can run like "python3 myapplication" and __main__.py will be called

# can also call your code this way if its in a zip file:
bash % ls
spam.py bar.py grok.py __main__.py
bash % zip -r myapp.zip *.py
bash % python3 myapp.zip
In [ ]:
#!/usr/bin/env python3 /usr/local/bin/myapp.zip