import streamlit as st


st.markdown('# Stereo Rectification')
st.markdown('''
Once we calibrate both cameras, we need to makes the image planes of both these cameras coplanar. This will make the computation very easy.

It will help the stereo matching algorithm and hence reduces the search space of the same point in both images to just 1 line.
''')


st.image('images/320px-Epipolar_geometry.svg.png')
st.image('images/Screenshot from 2024-04-22 15-53-15.png')

cols = st.columns(2)

with cols[0]:
    st.markdown('## Left Camera')
    st.image("images/imageL1.png")


with cols[1]:
    st.markdown('## Right Camera')
    st.image("images/imageR1.png")




with cols[0]:
    st.markdown('## Stereo Rectified Left')
    st.image("images/rectifiedL1.png")


with cols[1]:
    st.markdown('## Stereo Rectified Right')
    st.image("images/rectifiedR1.png")

st.image('images/concatenated stereo rectified images gray_screenshot_22.04.2024.png')


st.markdown('## Evaluation Metrics')
st.markdown('### Visual Inspection')
st.markdown('Verify if the rectified images appear aligned and have parallel epipolar lines.')