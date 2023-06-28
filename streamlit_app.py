import streamlit as st
import pandas as pd

## CREATE USER INPUT SIDEBAR

with st.sidebar.form('User Input HDB Features'):
    flat_address = st.text_input("Flat Address or Postal Code", '988B BUANGKOK GREEN') # flat address
    
    town = st.selectbox('Town', list(['ANG MO KIO', 'BEDOK', 'BISHAN', 'BUKIT BATOK', 'BUKIT MERAH',
                                            'BUKIT TIMAH', 'CENTRAL AREA', 'CHOA CHU KANG', 'CLEMENTI',
                                            'GEYLANG', 'HOUGANG', 'JURONG EAST', 'JURONG WEST',
                                            'KALLANG/WHAMPOA', 'MARINE PARADE', 'QUEENSTOWN', 'SENGKANG',
                                            'SERANGOON', 'TAMPINES', 'TOA PAYOH', 'WOODLANDS', 'YISHUN',
                                            'LIM CHU KANG', 'SEMBAWANG', 'BUKIT PANJANG', 'PASIR RIS','PUNGGOL']),
                                index=10)
    flat_model = st.selectbox('Flat Model', list(['Model A', 'Improved', 'Premium Apartment', 'Standard',
                                                            'New Generation', 'Maisonette', 'Apartment', 'Simplified',
                                                            'Model A2', 'DBSS', 'Terrace', 'Adjoined flat', 'Multi Generation',
                                                            '2-room', 'Executive Maisonette', 'Type S1S2']), index=0)
    flat_type = st.selectbox('Flat Type', list(['2 ROOM', '3 ROOM', '4 ROOM', '5 ROOM', 'EXECUTIVE']),
                                    index=2)
    floor_area = st.slider("Floor Area (sqm)", 34,280,93) # floor area
    storey = st.selectbox('Storey', list(['01 TO 03','04 TO 06','07 TO 09','10 TO 12','13 TO 15',
                                                '16 TO 18','19 TO 21','22 TO 24','25 TO 27','28 TO 30',
                                                '31 TO 33','34 TO 36','37 TO 39','40 TO 42','43 TO 45',
                                                '46 TO 48','49 TO 51']), index=3)
    #lease_commence_date = st.selectbox('Lease Commencement Date', list(reversed(range(1966, 2017))), index=1)
    submitted1 = st.form_submit_button(label = 'Submit HDB 🔎')