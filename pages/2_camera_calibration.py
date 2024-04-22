import streamlit as st

st.markdown('# Camera Calibration')

st.markdown('''
The process of estimating the camera paremeters (both extrinsics and intrinsics) is known as camera calibration.       
We perfrom camera calibration by method known as Direct Linear Transform (DLT).

**Note** - In order to use DLT algorithm, we need to know several points in the world!
            For that we use a known pattern image, like a chessboard with known corner points (e.g.- (9,6)).
''')


cols = st.columns(2)

with cols[0]:
    st.image("images/3.png")

with cols[1]:
    st.image("images/4.png")


cols = st.columns(2)

with cols[0]:
    st.image("images/5.png")

with cols[1]:
    st.image("images/6.png")

st.markdown('''
`Usually we give 25-30 such images in order to calibrate the camera well!`

`We do this for both cameras!`
''')


st.markdown('## Evaluation Metrics')
st.markdown('### Reprojection Error')
st.markdown('Average distance between the projected points and the actual points in the calibration pattern.')
st.markdown('The reprojection error e_i for each point i is given by')
st.latex(r'''
    e_i = \sqrt{ (x_i - \hat{x}_i)^2 + (y_i - \hat{y}_i)^2 }
''')
st.markdown('The total reprojection Error E is calculated as the root mean square (RMS) of all individual reprojection errors')
st.latex(r''' \boxed {
    E = \sqrt{\frac{1}{N} \sum_{i=1}^{N} e_i^2}
    }
''')