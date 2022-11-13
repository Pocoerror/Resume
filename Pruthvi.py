import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

####################
# Header 

st.write('''
<h1 style="color:;font-size:50px;font-weight:bold;">PRUTHVIRAJ CHOKAKE</h1>

##### *Resume* 
''', unsafe_allow_html=True)

image = Image.open('images/pro.png')
st.image(image, width=300)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Graduated in Computer Science 
- Skills - Web development , Data Analysis , Web Scrapping
- Phone  - 9665545749
- E-mail -  chokake.pruthvi@gmail.com
''')

#####################
# Navigation

st.markdown("""  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">""", unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #6053b8;">
  <a class="navbar-brand" href="https://github.com/Pruthvi2121/" target="_blank">Pruthviraj</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#certification">Certification</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#hobbies">Hobbies</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**Bachelors of Science** (Computer Science), *Shivaji University*, Kolhapur',
'2021-2023')
st.markdown('''
- CGPA: `9.0`
- Graduated with First Class Honors.
''')

txt('**HSC 12th** (Science), *New Model English Medium School and Jr Collage*, Kolhapur',
'2020-2021')
st.markdown('''
- Percentage: `67 %`
- Graduated with First Class Honors.
''')
txt('**SSC 10th** , *Sou Ambubai Patil English Medium School - Military Pattern*',
'2017-2018')
st.markdown('''
- Percentage: `81.20 %`
- Graduated with First Class Honors.
''')

#####################
st.markdown('''
## Work Experience
''')


txt('**Final Year Project**',
'')


txt('***-  Restaurant Management System***',
'`Web app`')
st.markdown('''
- Not yet completed 
''')

txt('**Personal Project**',
'')
txt('***1)-  Stock Market Analysis***',
'`Web app`')
st.markdown('''
It is group of project helps predecting and determine trend in market and much more for traders    
Sub-Projects\

- page 1 Market Pressure  *------------- give you current market pressure (upward / downward)*
- page 2 stock market live chart *------ give live market chart*
- page 3 Round number strategy  *------- Filter stock according to live market strategy*   .
- page 4 . . . . up comming 
   .
''')

txt('***2)-  Trading view alert to telegram channel***',
'`program`')
st.markdown('''
- *give live alert from trading view to  telegram channel. In free plan*

''')

txt('***3)-  weather forecast***',
'`program`')
st.markdown('''
- *give live weather details in console*

''')

txt('***4)-  battery charging notifier***',
'`program`')
st.markdown('''
- *give notification when charging exceed 90% and prevent overcharging*

''')
txt('***5)-  auto vocab notifier***',
'`program`')
st.markdown('''
- *give vocabulary notification in interval of time*

''')
txt('***6)- job portal***',
'`web app`')
st.markdown('''
- *web job portal bulid in django*

''')




#####################


#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `Java`, `Linux`')
txt3('Data processing/analysis', ' `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `plotly`')
txt3('Web development', ' `Javascript`, `Django`, `HTML`, `CSS`, `Streamlit` ')
txt3('Model deployment', '`streamlit`')

#####################
st.markdown('''
## Social Media
''')

txt2('GitHub', 'https://github.com/Pruthvi2121/')
txt2('Leetcode', 'https://leetcode.com/Pruthvi2121/')
txt2('Hackerank', 'https://www.hackerrank.com/chokake_pruthvi?hr_r=1')
txt2('Streamlit', '123')
txt2('Replit', 'https://replit.com/@Pruthviraj2121')
txt2('Youtube', 'https://www.youtube.com/channel/UCziDxmJ-DGS_HAxn4J4br9g')
txt2('LinkedIn', 'https://www.linkedin.com/in/pruthviraj-chokake-82a594231/')


#####################

# st.markdown('''
# ## Certification
# ''')
st.header('Certification')

with st.expander("Python"):
  st.image("certificate/html.jpg")
  
with st.expander("JavaScript"):
  st.image("certificate/html.jpg")

with st.expander("React"):
  st.image("certificate/html.jpg")

with st.expander("CSS"):
  st.image("certificate/CSS.jpg")

with st.expander("Java"):
  st.image("certificate/html.jpg")

with st.expander("Django"):
  st.image("certificate/html.jpg")


st.header('Hobbies')
st.markdown('''
- Coding
- Football
- Swimming
- Travelling
- Video Games
- Riding bike


''')
