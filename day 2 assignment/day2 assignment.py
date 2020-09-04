#!/usr/bin/env python
# coding: utf-8

# # list and its default functions

# In[ ]:


lst =["laptop","keyboard","mouse"]


# In[7]:


lst


# In[8]:


lst.append("mobile")                #append function


# In[16]:


lst


# In[17]:


lst.clear()                        #clear


# In[18]:


lst


# In[30]:


lst =["laptop","keyboard","mouse","mobile"]


# In[32]:


x=lst.copy()


# In[33]:


x


# In[36]:


a=lst.count("mouse")                           #count
a


# In[39]:


num=[1,2,21,3,7,6]
num


# In[40]:


lst.extend(num)                              #extend


# In[42]:


lst


# In[44]:


lst.index(21)                                #index


# In[48]:


lst.insert(3,"speakers")                     #insert
lst


# In[49]:


lst.pop(4)
lst                                          #pop


# In[51]:


lst.remove("mouse")
lst


# In[52]:


lst.reverse()
lst


# In[54]:


num.sort()
num


# In[56]:


lst1=["car","bat","google","apple"]
lst1


# In[60]:


lst1.sort()
lst1


# # Dictionary and its functions

# In[62]:


dit={"Brand":"OnePlus",                                          #Dictionary 
      "model":"8pro",
      "price":54999
    }
dit


# In[64]:


dit.clear()                                                      #clear
dit


# In[65]:


dit={"Brand":"OnePlus",                                          #Dictionary 
      "model":"8pro",
      "price":54999
    }
dit


# In[66]:


a = dit.copy()
a                                               #copy


# In[69]:


a=('key1','key2','key3')                        #fromkeys
b=0
x=dit.fromkeys(a,b)
x


# In[71]:


s=dit.get("Brand")                                   #get
s


# In[72]:


p=dit.items()                                          #items
p


# In[73]:


a=dit.keys()                                             #keys
a


# In[79]:


dit.pop("model")                                           #pop
dit


# In[87]:


dit.popitem()                                               #popitem
dit


# In[93]:


dit.setdefault("model","7T")                                #setdefault
dit


# In[94]:


dit.update({"color":"black"})                                #update
dit


# In[95]:


dit.values()                                                 #values
dit


# # #sets and its default functions

# In[119]:


st = {"python","letsupgrade",5,7,6,2}                   #sets
st


# In[102]:


st.add("sai")                                        #add
st


# In[100]:


st.clear()                                          #clear
st


# In[103]:


a=st.copy()                                          #copy
a


# In[120]:


st1={"python","letsupgrade","amar",7}                 # difference
x=st.difference(st1)
x


# In[111]:


st.difference_update(st1)                           #difference_update
st


# In[116]:


st.discard("sai")                                      #discard
st


# In[123]:


st = {"python","letsupgrade","sai",7,6,}               #intersection
st1={"python","letsupgrade","yash",7}
c=st.intersection(st1)
c


# In[128]:


st.intersection_update(st1)                            #intersection_update
st


# In[1]:


st = {"python","letsupgrade","sai"}                       #isdisjoint
st1={"JS","ABC","yash"}
d=st.isdisjoint(st1)
d


# In[133]:


st = {"python","letsupgrade","sai",7,6,}                #issubset
st1={"python","letsupgrade","yash",7}
e=st.issubset(st1)
e


# In[135]:


st = {"python","letsupgrade","sai",7,6,}                 #issuperset
st1={"python","letsupgrade",7}
f=st.issuperset(st1)
f


# In[136]:


st.pop()                                                   #pop
st


# In[137]:


st.remove("sai")                                           #remove
st


# In[139]:


st = {"python","letsupgrade","sai",7,6,}                    #symmetric_difference
st1={"python","letsupgrade","yash",7}
z=st.symmetric_difference(st1)
z


# In[140]:


st.symmetric_difference_update(st1)                          #symmetric_difference_update
st


# In[141]:


st = {"python","letsupgrade","sai",7,6,}                       #union
st1={"python","letsupgrade","yash",7}
y=st.union(st1)
y


# In[142]:


st = {"python","letsupgrade","sai",7,6,}                         #update
st1={"python","letsupgrade","yash",7}
st.update(st1)
st


# # #Tuple and its default function
# 

# In[144]:


tup =("python","letsupgrade","sai","python")                       #tuple
tup


# In[145]:


tup.count("python")


# In[148]:


tup.index("letsupgrade")


# # #Strings and its methods
# 

# In[151]:


string="letsupgrade"
string


# In[154]:


string="hello, welcome to Letsupgrade"
s=string.capitalize()
s


# In[155]:


string.casefold()


# In[156]:


string="Letsupgrade"
a=string.center(10)
a


# In[159]:


string="hello, welcome to Letsupgrade,its sai from Letsupgrade"
b=string.count("Letsupgrade")
b


# In[164]:


string="hello!, welcome to Letsupgrade / its sai from Letsupgrade"
x=string.encode()
x


# In[165]:


string="hello, welcome to Letsupgrade,its sai from Letsupgrade"
x=string.endswith("from")
x


# In[169]:


string="h\te\tllo"
s=string.expandtabs(2)
s


# In[170]:


string="hello, welcome to Letsupgrade,its sai from Letsupgrade"
x=string.find("Letsupgrade")
x


# In[173]:


string="hey guyz I'am{fname}"
print(string.format(fname=" sai"))


# In[175]:


point={'x':4,'y':6}
print('{x},{y}'.format_map(point))


# In[176]:


string="hey guyz I'am saikiran"
print(string.index("guyz"))


# In[192]:


str="sai20"
print(str.isalnum())


# In[193]:


str="letsupgrade"
print(str.isalpha())


# In[199]:


a = "0.25"
print(a.isdecimal())


# In[202]:


s = "5045"
print(s.isdigit())


# In[206]:


s="097"
print(s.isascii())


# In[213]:


p="Letsupgrade"
print(p.isidentifier())


# In[215]:


a="Hello guyz"
print(a.islower())


# In[216]:


n="6448"
print(n.isnumeric())


# In[217]:


d="hello! guyz"
print(d.isprintable())


# In[218]:


u=" "
print(u.isspace())


# In[219]:


a="32683264"
print(a.istitle())


# In[221]:


m="HI"
print(m.isupper())


# In[229]:


a="sai","kiran"
s=" ".join(a)
print(s)


# In[234]:


r="letsupgrade"
e=r.ljust(10)
print(r, "community")


# In[235]:


s="Hello Guyz"
print(s.lower())


# In[236]:


h="good morning"
x=h.lstrip()
print("hello! guyz",x,"welcome to letsupgrade")


# In[241]:


str="hello guys"
x=str.maketrans("s", "z")
print(str.translate(x))


# In[243]:


str="Hello guyz welcome to letsupgrade"
print(str.partition("welcome"))


# In[250]:


txt="welcome to letsupgade"
x=txt.replace("letsupgade", "India")

print(x)


# In[251]:


txt="sai, kiran"
x=txt.rfind("kiran")
print(x)


# In[253]:


txt="sai kiran"
x=txt.rindex("kiran")
print(x)


# In[256]:


txt="saikiran"
x=txt.rjust(30)
print(x,"from letsupgrade")


# In[257]:


str="saikiran from letsupgrade"
x=str.rpartition("from")
x


# In[263]:


txt= "letsupgrade, python, batch7"
x=txt.rsplit(", ")
x


# In[266]:


txt=" good morning          "
x=txt.rstrip()
print("Hello",x,"to all")


# In[267]:


txt="saikiran from letsupgrade"
x=txt.split()
x


# In[268]:


txt="hello guyz \nits saikiran from letsupgrade"
x=txt.splitlines()
x


# In[269]:


txt="hello its saikiran from letsupgrade"
x=txt.startswith("hello")
x


# In[270]:


txt=" good morning          "
x=txt.strip()
print("Hello",x,"to all")


# In[271]:


txt="hello its saikiran from letsupgrade"
x=txt.swapcase()
x


# In[272]:


txt="hello welcome to letsupgrade"
x=txt.title()
x


# In[274]:


txt="hello word"
x=txt.upper()
x


# In[276]:


txt = "50"
x=txt.zfill(5)
print(x)


# In[ ]:




