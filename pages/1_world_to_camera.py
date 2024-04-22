import streamlit as st


st.markdown('# World to Camera')

st.markdown("""
There are 4 coordinates involved while converting a 3D point into an 2D pixel image.
1. World coordinates
1. Camera coordinates
1. Image plane coordinates
1. Sensor coordinates
""")

st.image('images/1.jpg')

st.markdown("""
The object goes through these transformation, and is eventually converted from 3D to 2D image.
            
            """)
st.markdown("""
The transformations are governed by certain parameters depending on the orientation of the camera and camera properties (like focal length).
            \n We classify these parameters into 2 types : \n
- Extrinsics
- Intrinsics
""")


st.image('images/2.jpg')



st.markdown('## Extrinsics')
st.markdown('''
Describes the pose of the camera in the world
            \nTotal - 6 parameters
            \n
- 3 translations
- 3 rotations
            
`If we move the camera, the Extrinsics changes!`
''')
st.markdown('Extrinsic transformation matrix')
st.latex(r''' \text{translation} \;\;\;\;\; X_o =
         \begin{bmatrix}
         X_o & Y_o & Z_o
         
         \end{bmatrix}
''')
st.latex(r'''\text{rotation} \;\;\;\;\; R =
        \begin{bmatrix}
         R & 0 \\
         0^T & 1
         \end{bmatrix}
         ''')
st.markdown('We write them combined as -')
st.latex(r'''
         \text{Extrinsics}  \;\;\; = \;\;\;
        R \begin{bmatrix}
            I_3 | & -X_0
         \end{bmatrix}
''')



st.markdown('## Intrinsics')
st.markdown('''
Mapping of scene in front of the camera to pixels
            \nTotal - 5+ parameters
            \n

`Intrinsics are constant for a camera!`
''')
st.markdown('Intrinsic transformation')
st.latex(r'''K = 
\begin{bmatrix}
        c & cs & x_H \\
         0 & c(1+m) & y_H \\
         0 & 0 & 1
         \end{bmatrix}
''')
st.markdown('''
- Camera constant - c
- Principal point - (x_h, y_h)
- Scale difference - m
- Shear - s (approximately 0)
            \n ---
''')


st.markdown('## Combined transformation')
st.latex(r'''\boxed{
P = KR \begin{bmatrix}
            I_3 | & -X_0
         \end{bmatrix}
}
         
''')


st.markdown('''
`Our task is to estimate these parameters, so that we can reconstruct the 3D image!` 
\n 
`In total - 11+ parameters => 6 extrinsics, 5 intrinsics`
            
We use Direct Linear Transform (DLT) to estimate these parameters for a given camera.
''')

st.markdown('''**Note** - We use Homogeneous coordinates to represent these transformations.''')


st.markdown('''
---
## Homogeneous Coordinates
We use special coordinates to represent all the matrix tranformations.
- Represent infinity in these coordinates.
- Tell which lines are parallel
- Check where is the horizon line (i.e where all parallel lines meet)
- Most importantly - All Matrix transformations are essentially matrix multiplications. Thus we can chain them!
''')


st.markdown('''
---
## Non linear errors
1. Lens Distortion (wide angle - barrel distortion)
2. Imperfect lens
3. Planarity of sensor
            
`To correct them, we introduce more parameters to estimate!`
''')