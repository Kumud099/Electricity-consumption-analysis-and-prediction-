import streamlit as st
from streamlit_option_menu import option_menu
from dashboard import dashboard
from dataset import dataset
from prediction import prediction
from about import about
from prediction_by_month import prediction_by_month
from prediction_by_year import prediction_by_year

user_emoji = '⚡'

def main():
    st.title("Electricity Consumption Analysis and Prediction")

    # Sidebar navigation for the dashboard
    with st.sidebar:
        # Use st.markdown to display the emoji
        st.markdown(f"# {user_emoji} Electricity Consumption Analysis and Prediction")

        app = option_menu(
            menu_title='',
            options=['Dashboard', 'Dataset', 'Prediction by day', 'Prediction by month', 'Prediction by year', 'about'],
            icons=['bar-chart', 'folder', 'clock', 'clock', 'clock', 'info-circle-fill'],
            default_index=0,
            styles={
                "container": {"padding": "5!important", "background-color": 'black'},
                "icon": {"color": "white", "font-size": "23px"},
                "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "blue"},
                "nav-link-selected": {"background-color": "#02ab21"},
            }
        )

    if app == "Dashboard":
        dashboard()
    elif app == "Dataset":
        dataset()
    elif app == "Prediction by day":
        prediction()
    elif app == "Prediction by month":
        prediction_by_month()
    elif app == "Prediction by year":
        prediction_by_year()
    elif app == "about":
        about()

if __name__ == "__main__":
    main()
