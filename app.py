import streamlit as st
import os
import pandas as pd
import numpy as np
st.set_page_config(layout="wide") 
st.title('Cape Town Urban Simulation Model')

st.image('pictures/logo.png')

st.write('The urban simulation model presented in this dashboard is intended for ease of analysis and comparison of policy and behaviourial assumptions. The model is based on existing Urban Economic theoretical assumptions adapted to the unique conditions of the City of Cape Town.')
# st.write('The tabs below outline some of the key assumptions, background research and approach used.')

@st.cache
def load_parameters():
    parameters = pd.read_csv('metadata/options_and_param.csv').set_index('parameters')
    return parameters

parameters = load_parameters()



# st.dataframe(parameters.astype('str'))
helpTab,dataTab, paramTab,outputTab=st.tabs(['Help','Data','Inputs','Outputs'])


with helpTab:
    with st.expander('Introduction to Urban Economics'):
    
        st.write('### The Fundamental Trade-off in Urban Economics')
        # st.write(os.listdir())
        st.image('pictures/urbanEcon.png')
        st.write("* Urban Economic models measure some of the trade-offs present in urban labour and real estate markets. ")
        st.write("* Households proximity to employment centers is associated with **higher rents** and **lower transport costs**.") 
        st.write("* **Developers respond** to these forces by using land more intensively where rents are high. ")
        st.write("* These factors, along with idiosyncratic factors like proximity to amenities directly impact the spatial structure of urban development.")
        st.write("### References")
        st.write("Alonso, W. 1964. [*Location and Land Use.*](https://www.amazon.com/Location-Publications-Joint-Center-Studies/dp/0674729560)")
        st.write("Mills, E. S. 1967. [*Transportation and Patterns of Urban Development.*](https://www.jstor.org/stable/1821621)")
        st.write("Muth, R. F. 1969. [*Cities and Housing: the Spatial Pattern of Urban Residential Land Use.*](https://www.amazon.com/Cities-Housing-Spatial-Pattern-Residential/dp/B002DX9922)")

    with st.expander('The Nedum Model'):
        st.write('### Framework of the Nedum model')
        st.write('The Nedum model takes exogenous factors including the geographic, legal and infrastructure constrains of the city and models the responses of agents including Households, Firms and Developers.')
        st.image('pictures/modelChoices.png')

    # with st.expander('Inputs and Choices'):
    #     st.write('### Inputs and Choices in the Nedum Model')
    #     st.write("The Nedum model includes several parameters related to the ability of agents to respond to external forces, such as flood risk.")
    #     # st.image('pictures/settlements.png')




    # with st.expander('Outputs and Insights'):

    #     st.write('### Output Dashboards')
    #     st.write("Output dashboards have been created to focus on some of the key insights gained from the model. These can broadly be categorised in 3 groups:")
    #     st.write("* **Welfare** measurements focus on the impact of developments on households in various income strata.")
    #     st.write("* **Climate** measures focus on climatic risks to households.")
    #     st.write("* **Development** measures focus on economic measures including construction density and rental values.")
    #     col1, col2, col3 = st.columns(3)

    #     with col1:
    #         st.write("#### Welfare")
    #         st.write('⛽ Fuel')
        
    #     with col2:
    #         st.write("#### Climate")
    #         st.write('🌊 Floods')
        
    #     with col3:
    #         st.write("#### Development")
    #         st.write("🏘️ Housing")

    # with st.expander('User Guide'):
    #     st.write('user guide here')

with dataTab:
        st.write("### Source Data")
        st.dataframe(pd.read_csv('modelOutputs/data_list.csv'))

with paramTab:

    st.write("### Parameters and Options ")
    st.write("The parameters and options have been classified by type and category can be explored below. ")
    "Categories are aranged thematically: "
    "* ***User*** variables are factors external to the model which can be changed by the user"
    "* ***Options*** can be changed based on user preferences and changing economic conditions."
    "* ***Calibration*** variables technical inputs and cannot be set by the user"
    

# [   "User Defined","Parameters","Calibration"]

    categoryChoice =st.radio(label='CATEGORY',options=['Housing','Policy','Transport','Macroeconomic','Theoretical',"Incomes"], horizontal=True)
    varType = st.radio(label="TYPE", options=['all','user','options','calibration'],horizontal=True)
    if varType == 'all':
        varType =['user','options','calibration']
    else: varType = [varType]

    st.dataframe(parameters[np.logical_and(parameters.category==categoryChoice,[x in varType for x in parameters.type])].astype('str'))
    

with outputTab:
    st.write('### Outputs')
    col1, col2 = st.columns(2)
    # with col1:
    #     filterSelection=st.multiselect("FILTER SELECTION", ['sim','validation','formal','informal','subsidized','backyard','damages','flood','coastal','pluvial','fluvial'])

    # with col2:
        
    #     filterType = st.radio("FILTER TYPE",['and','or'],horizontal=True)

    #     figList  = os.listdir(scenPath)

    #     outputList = []
    #     # for fig in figList:
            
    #     #     if filterType=='or':




    


    col3, col4 = st.columns(2)

    with col3:
        scenario = st.selectbox("SCENARIO",['142','212'])
        scenPath = "modelOutputs/outputs/floods10_P11_C11_scenario"+scenario+"/plots/"
        outputList= os.listdir(scenPath)

    with col4:
        Figure = st.selectbox('output',outputList)

    st.image(scenPath+Figure)



st.write('*For any queries regarding this dashboard email kristoff.potgieter@capetown.gov.za*')
