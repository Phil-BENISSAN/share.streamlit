import pandas as pd
import seaborn as sns
import streamlit as st


# Charger le dataset "taxis"
df_taxis = sns.load_dataset('taxis')

st.title('Welcome to WCS Taxi driver')


list_pickup_borough = sorted(list(df_taxis[df_taxis['pickup_borough'].notna()]['pickup_borough'].unique()))


choice_pickup_borough = st.selectbox(  "Enter your pickup area :", 
                                       list_pickup_borough
                                    )

st.write(f'You are choosen : {choice_pickup_borough}')

# AFFICHAGE DE L'IMAGE
st.image(f'https://github.com/Phil-BENISSAN/share.streamlit/blob/main/img/{choice_pickup_borough}.png',
         use_column_width=True,
         )



