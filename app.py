import streamlit as st

st.title("Title -> Hello World, This is Earth")
st.header("Header -> Hello World, This is Earth")
st.subheader("SubHeader -> Hello World, This is Earth")
st.text('Text -> Hello World, This is Earth')


st.markdown(' # Hi')
st.markdown('## Hi')
st.markdown('### Hi')
st.markdown('#### Hi')
st.markdown('##### Hi')
st.markdown('###### Hi')


st.success("Hey Data is Submitted! ")
st.info("Hey this is the Informtion")
st.warning("Warning")
st.error("You have a data Error")

# Now if we want to display a specific error that came, like if we divide 
# a number by zero then we get ZeroDivision Error in Python

exp=ZeroDivisionError("Division not Possible with 0")
st.exception(exp)

# or we can do

st.exception(ZeroDivisionError("Already Told we can't divide a number by 0"))


# If we want to know anything about any function then we can take the 
# help of help function and help function will take us to the main documentation

st.help(ZeroDivisionError)

# See the output both are displayed in different ways
st.write("range(1,10)")
st.write(range(1,10))
st.write('1+2+3')
st.write(1+2+3)

st.code('x=10 \n'
        'for i in range(x): \n'
            '\t print(i)')

st.checkbox('Male')
st.checkbox("Female")
# st.checkbox("Female") # note we can't add same name for two check boxes
# st.checkbox("female") # Note it is case sensitive so female and Female are two different thing

if(st.checkbox("Adult")):
    st.write("You are an Adult")


st.radio('Select  :',('Check',"Uncheck"))

st.radio('' ,('Check',"Uncheck"))

st.radio('New hai' ,['Check',"Uncheck"])


radioButton=st.radio('Please Select your Gender :',('Male',"Female",'Others'))

if(radioButton=='Male'):
    st.write('You are a Male')

elif(radioButton=='Female'):
    st.write("You are a Female")

else:
    st.write("You are Others")

st.subheader("Select Box")

st.selectbox('New Data Science :',('Data Analysis','Data visualization',
                               'Tablue','Data Scientist',
                               "Machine Learning",'NLP','Computer Vision',
                               'Image Procesing'))

selectBox=st.selectbox('Data Science :',['Data Analysis','Data visualization',
                               'Tablue','Data Scientist',
                               "Machine Learning",'NLP','Computer Vision',
                               'Image Procesing'])

st.write(selectBox)

st.write("You have Selected  :",selectBox)


st.subheader("Multi Select Box")

multiselbox1=st.multiselect('Naya Data Science :',['Data Analysis','Data visualization',
                               'Tablue','Data Scientist',
                               "Machine Learning",'NLP','Computer Vision',
                               'Image Procesing'])

st.write('You have Selected  -',len(multiselbox1),'courses')

multiselbox=st.multiselect('Data Science :',['Data Analysis','Data visualization',
                               'Tablue','Data Scientist',
                               "Machine Learning",'NLP','Computer Vision',
                               'Image Procesing'])

st.write('You have Selected  :',multiselbox)

st.write('You have Selected  :',multiselbox)

st.subheader("Button")

st.button("Button")

if(st.button('Click me')):
    st.write("Thanks for clicking")

st.subheader("Slider")

st.slider("Select a level",1,10,step=1)

volume=st.slider("Select volume level",0,100,step=1)
st.write('Your volume is -',volume)


st.subheader("Taking User Text Input")

st.text_input("Name : ")

name=st.text_input("Enter Your Name : ")
if(name):
    st.write('Hi,',name)


username=st.text_input("Enter Username : ")
if(username):
    st.write('Hi,',username)
Password=st.text_input("Enter Password : ",type='password')


# If I want to write whole pragraph, then in that case we use text area

st.subheader("Text Area")

st.text_area("Write 100 words")

textArea=st.text_area("Write about yourself")
st.write(textArea)

st.subheader("Input Number")
age=st.number_input("Select your age",18,110)  # here 18 to 110 is the limit

st.subheader("Input Date")
st.date_input("Select the date")

st.subheader("Input Time")
st.time_input("Enter the time")



