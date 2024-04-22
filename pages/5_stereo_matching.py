import streamlit as st

st.markdown('# Stereo Matching')

st.markdown('We aim to find correspondences between pixels in a pair of stereo images')
st.markdown('The goal is to establish pixel-level correspondences, often referred to as disparity, between the images')
st.markdown('Once we find disparity, extracting depth is a straight forward process')
st.latex(r'''
    \text{disparity} = \frac{fB}{d}
''')


st.markdown('## Disparity')
cols = st.columns(2)
with cols[0]:
    st.image("images/disparity map_screenshot_22.04.2024.png")
with cols[1]:
    st.image("images/disparity map visual_screenshot_22.04.2024.png")


st.markdown('## Depth')
cols = st.columns(2)
with cols[0]:
    st.image("images/depth map_screenshot_22.04.2024.png")
with cols[1]:
    st.image("images/depth map visual_screenshot_22.04.2024.png")







st.markdown('## Evaluation Metrics')
st.markdown('### Visual Inspection')
st.markdown('Disparity Map Visualization: Evaluate the smoothness and consistency of the disparity map.')

st.markdown('### Matching Accuracy: Percentage of correctly matched pixels or keypoints.')
st.latex(r'''
A = \frac{N_c}{N_t} \times 100\%
''')