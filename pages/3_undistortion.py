import streamlit as st


st.markdown('# Undistortion')

st.markdown('''
After performing calibration, we need to undistort the images. Most cameras mainly contain barrel noise. 
In such noise, the straight lines closer to the image edge looks curvy.
''')



cols = st.columns(2)

with cols[0]:
    st.markdown('## Before undistortion')
    st.image("images/3.png")
    st.image("images/4.png")


with cols[1]:
    st.markdown('## After undistortion')
    st.image("images/7.png")
    st.image("images/8.png")


st.markdown('## Evaluation Metrics')
st.markdown('### Visual Inspection')
st.markdown('Check whether straight lines appear straight!')

st.markdown('### Mean Square Error (MSE)')
st.latex(r'''
\text{MSE} = \frac{1}{MN} \sum_{i=1}^{M} \sum_{j=1}^{N} (I(i, j) - \hat{I}(i, j))^2

''')


st.markdown('### Structural Similarity Index (SSI)')
st.latex(r'''
\text{SSI}(I, \hat{I}) = \frac{{2 \mu_I \mu_{\hat{I}} + c_1}}{{\mu_I^2 + \mu_{\hat{I}}^2 + c_1}} \cdot \frac{{2 \sigma_{I\hat{I}} + c_2}}{{\sigma_I^2 + \sigma_{\hat{I}}^2 + c_2}}

''')