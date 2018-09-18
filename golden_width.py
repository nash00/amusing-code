
# coding: utf-8

# In[18]:


def golden_width(acc,l):
    a,b = 0,1
    for i in range(acc):
        a,b = b, b+a
    gol_rat = b / a
    gol_wid = l * gol_rat
    print(gol_wid)

