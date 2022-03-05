#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app = Flask(__name__)


# In[3]:


from flask import render_template,request
from textblob import TextBlob
get_ipython().system('pip install Textblob')

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text")
        r = TextBlob(text).sentiment
        return(render_template("index.html", results=r))
    else:
        return(render_template("index.html", results="2"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:





# In[ ]:




