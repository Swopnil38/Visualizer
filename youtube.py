import base64
import math
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
from Value_Processing import read_audio_files, read_fb_insta, read_overall_particular, read_yt_csv, read_yt_csv_dately, tiktok_data
from Visualizations import animatedline_chart, horizontal_bar, pie
from PIL import Image
from pydeck.types import String
import moviepy.editor as mp




ages_yt=male_viewer_yt=female_viewer_yt=country_name=country_viewer_per=country_lat=country_lon=viewes=avg_duration=year_month=option = None

def read_yt(options):
    global ages_yt,male_viewer_yt,female_viewer_yt,country_name,country_viewer_per,country_lat,country_lon,viewes,avg_duration,year_month,option
    ages_yt,male_viewer_yt,female_viewer_yt,country_name,country_viewer_per,country_lat,country_lon,viewes,avg_duration,year_month = read_yt_csv(options)
    option = options
    





def YT_age_gender():
    col1,col2,col3 = st.columns([1,2,1])
    with col2:
        try:
            print(ages_yt)
            st.markdown("<h1 style='text-align: center;'>Age Gender Chart of Youtube</h1><br><br>", unsafe_allow_html=True)
            figure = horizontal_bar(ages_yt,male_viewer_yt,female_viewer_yt,option)
            st.pyplot(figure)
        except:
            st.text("Error Retreiving Age Gender Chart of Youtube")

def YT_country(): 
    try:
        st.markdown("<h1 style='text-align: center;'>Country wise Viewer Percent Data of Youtube</h1><br><br>", unsafe_allow_html=True)
        col,col2 = st.columns([4,2])
        with col:
            df = pd.DataFrame(list(zip(country_name,country_viewer_per,country_lat,country_lon)),columns = ['name','view','lat','lng'])
            df['views'] = df['view'].apply(lambda viewed: math.pow(viewed,5))
            
            layer = pdk.Layer(
                "ScatterplotLayer",
                df,
                pickable=True,
                opacity=0.8,
                stroked=True,
                filled=True,
                radius_min_pixels=10,
                radius_max_pixels=1000,
                get_position=['lng','lat'],
                get_radius="view",
                get_fill_color=[255, 140, 0],
                get_line_color=[0, 0, 0],
            )

            # Set the viewport location
            view_state = pdk.ViewState(
                longitude=84, latitude=28, zoom=6
            )

            # Combined all of it and render a viewport
            r = pdk.Deck(
                layers=[layer],
                initial_view_state=view_state,
                tooltip={"text": "{view}\n{name}"}
            )
            
            st.pydeck_chart(r)
        with col2:
            df = pd.DataFrame(list(zip(country_name,country_viewer_per)),columns = ['Country Name','Country Viewer Percentage'])
            df.sort_values(by='Country Viewer Percentage')
            st.dataframe(df)
    except:
        st.write("Error Retreiving Geographical Map of Youtube")
    
def YT_overall_view():
    st.markdown("<h1 style='text-align: center;'>Month Wise Viewer Graph of Youtube</h1><br><br>", unsafe_allow_html=True)   
    try:
        figure2 = animatedline_chart(year_month,viewes,option)

        clip = mp.VideoFileClip(figure2)
        clip.write_videofile("{}.mp4".format(option))

        video_file = open('{}.mp4'.format(option), 'rb')
        video_bytes = video_file.read()

        st.video(video_bytes)
    except:
        st.title("Error Retreiving Views Data of Youtube")

def YT_particular_view(year_select,month_select):

    data,labels = read_yt_csv_dately(option,int(year_select),int(month_select))
    month_data = pd.DataFrame(data,index=labels)
    if data == []:
        st.write("No Data Found of Selected Date")
    else:
        st.markdown("<h1 style='text-align: center;'>{}/{} Viewer Chart of Youtube</h1><br><br>".format(year_select,month_select), unsafe_allow_html=True)
        st.area_chart(month_data)
    
ages_fb=male_viewer_fb=female_viewer_fb=ages_insta=male_viewer_insta=female_viewer_insta=country_name_fb_insta=country_viewer_per_insta=country_lat_insta=country_lon_insta=country_name_fb=country_viewer_per_fb=country_lat_fb=country_lon_fb=year_month_fb_insta=like_fb=follower_insta=option = None    
def read_fb_insta_values(optionss):
    try:
        global ages_fb,male_viewer_fb,female_viewer_fb,ages_insta,male_viewer_insta,female_viewer_insta,country_name_fb_insta,country_viewer_per_insta,country_lat_insta,country_lon_insta,country_name_fb,country_viewer_per_fb,country_lat_fb,country_lon_fb,year_month_fb_insta,like_fb,follower_insta,option
        ages_fb,male_viewer_fb,female_viewer_fb,ages_insta,male_viewer_insta,female_viewer_insta,country_name_fb_insta,country_viewer_per_insta,country_lat_insta,country_lon_insta,country_name_fb,country_viewer_per_fb,country_lat_fb,country_lon_fb,year_month_fb_insta,like_fb,follower_insta = read_fb_insta(optionss) 
        print(country_name_fb_insta)
        print(country_viewer_per_insta) 
        option = optionss
        print("2")
    except Exception as e:
        print(e)    
    print("3")
        
def Fb_age_gender():
    try:
        st.markdown("<h1 style='text-align: center;'>Age Gender Chart of Facebook</h1><br><br>", unsafe_allow_html=True)
        figure = horizontal_bar(ages_fb,male_viewer_fb,female_viewer_fb,option)
        st.pyplot(figure)
    except:
        st.write("Error while Retreiving Gender Age Data of Facebook")
def Insta_age_gender():
    
    st.markdown("<h1 style='text-align: center;'>Age Gender Chart of Instagram</h1><br><br>", unsafe_allow_html=True)
    figure = horizontal_bar(ages_insta,male_viewer_insta,female_viewer_insta,option)
    st.pyplot(figure)

def Insta_country():
    try:
        st.markdown("<h1 style='text-align: center;'>Country wise Follower of Instagram</h1><br><br>", unsafe_allow_html=True)
        col,col2 = st.columns([3,2])
        with col:
            df = pd.DataFrame(list(zip(country_name_fb_insta,country_viewer_per_insta,country_lat_insta,country_lon_insta)),columns = ['name','view','lat','lng'])
            df['views'] = df['view'].apply(lambda viewed: math.pow(viewed,5))
            
            layer = pdk.Layer(
                "ScatterplotLayer",
                df,
                pickable=True,
                opacity=0.8,
                stroked=True,
                filled=True,
                radius_min_pixels=10,
                radius_max_pixels=1000,
                get_position=['lng','lat'],
                get_radius="view",
                get_fill_color=[255, 140, 0],
                get_line_color=[0, 0, 0],
            )

            # Set the viewport location
            view_state = pdk.ViewState(
                longitude=84, latitude=28, zoom=6
            )

            # Combined all of it and render a viewport
            r = pdk.Deck(
                layers=[layer],
                initial_view_state=view_state,
                tooltip={"text": "{view}\n{name}"}
            )
            
            st.pydeck_chart(r)
        with col2:
            df = pd.DataFrame(list(zip(country_name,country_viewer_per)),columns = ['Country Name','Country Viewer Percentage'])
            df.sort_values(by='Country Viewer Percentage')
            st.dataframe(df)
    except:
        st.write("Error while retreiving Country Follower Data of Instagram")
def Fb_Country(): 
    try:
        st.markdown("<h1 style='text-align: center;'>Country wise Follower of Facebook</h1><br><br>", unsafe_allow_html=True)
        col,col2 = st.columns([3,2])
        with col:
            df = pd.DataFrame(list(zip(country_name_fb,country_viewer_per_fb,country_lat_fb,country_lon_fb)),columns = ['name','view','lat','lng'])
            df['views'] = df['view'].apply(lambda viewed: math.pow(viewed,5))
            
            layer = pdk.Layer(
                "ScatterplotLayer",
                df,
                pickable=True,
                opacity=0.8,
                stroked=True,
                filled=True,
                radius_min_pixels=10,
                radius_max_pixels=1000,
                get_position=['lng','lat'],
                get_radius="view",
                get_fill_color=[255, 140, 0],
                get_line_color=[0, 0, 0],
            )

            # Set the viewport location
            view_state = pdk.ViewState(
                longitude=84, latitude=28, zoom=6
            )

            # Combined all of it and render a viewport
            r = pdk.Deck(
                layers=[layer],
                initial_view_state=view_state,
                tooltip={"text": "{view}\n{name}"}
            )
            
            st.pydeck_chart(r)
        with col2:
            df = pd.DataFrame(list(zip(country_name_fb,country_viewer_per_fb)),columns = ['Country Name','Country Viewer Percentage'])
            df.sort_values(by='Country Viewer Percentage')
            st.dataframe(df)
    except:
        st.write("Error while Retreving Country Follower Data of Facebook")
def fb_like():
    try:
        st.markdown("<h1 style='text-align: center;'>Like by Month Graph of Facebook</h1><br><br>", unsafe_allow_html=True)    
        like_data = pd.DataFrame(like_fb,index=year_month_fb_insta)
        if like_fb == []:
            st.title("No Data Found")
        else:
            st.area_chart(like_data)
    except:
        st.write("Error while Retreiving Likes Data of Facebook")
def insta_like():
    st.markdown("<h1 style='text-align: center;'>Like by Month Graph of Instagram</h1><br><br>", unsafe_allow_html=True)    
    follower_data = pd.DataFrame(follower_insta,index=year_month_fb_insta)
    if follower_insta == []:
        st.title("No Data Found")
    else:
        st.area_chart(follower_data)
    

    
tik_age=tik_age_label=tik_geo_label=tik_geo_value=follower_tiktok=year_month_tiktok=country_lat_fb=country_lon_fb=option = None
def read_tiktok_data(optionsss):
    global tik_age,tik_age_label,tik_geo_label,tik_geo_value,follower_tiktok,year_month_tiktok,country_lat_fb,country_lon_fb,option
    tik_age,tik_age_label,tik_geo_label,tik_geo_value,follower_tiktok,year_month_tiktok,country_lat_fb,country_lon_fb = tiktok_data(optionsss)
    option = optionsss
def tiktok_age():

    col1,col2,col3 = st.columns([1,2,1])
    with col2:
        try:
            st.markdown("<h1 style='text-align: center;'>Age Pie Chart of Tiktok</h1><br><br>", unsafe_allow_html=True)    
            figure = pie(tik_age_label,tik_age,option)
            st.pyplot(figure)
        except:
            st.write("Error while retreving Age Data of Tiktok")
def tiktok_country():
    try:
        col,col2 = st.columns([3,2])
        with col:
            df = pd.DataFrame(list(zip(tik_geo_label,tik_geo_value,country_lat_fb,country_lon_fb)),columns = ['name','view','lat','lng'])
            df['views'] = df['view'].apply(lambda viewed: math.pow(viewed,5))
            
            layer = pdk.Layer(
                "ScatterplotLayer",
                df,
                pickable=True,
                opacity=0.8,
                stroked=True,
                filled=True,
                radius_min_pixels=10,
                radius_max_pixels=1000,
                get_position=['lng','lat'],
                get_radius="view",
                get_fill_color=[255, 140, 0],
                get_line_color=[0, 0, 0],
            )

            # Set the viewport location
            view_state = pdk.ViewState(
                longitude=84, latitude=28, zoom=6
            )

            # Combined all of it and render a viewport
            r = pdk.Deck(
                layers=[layer],
                initial_view_state=view_state,
                tooltip={"text": "{view}\n{name}"}
            )
            
            st.pydeck_chart(r)
        with col2:
            df = pd.DataFrame(list(zip(tik_geo_label,tik_geo_value)),columns = ['Country Name','Country Viewer Percentage'])
            df.sort_values(by='Country Viewer Percentage')
            st.dataframe(df)
    except:
        st.write("Error While Retreving Country Data of Tiktok")
def tiktok_follower():
    try:
        follower_data = pd.DataFrame(follower_tiktok,index=year_month_tiktok)
        if follower_tiktok == []:
            st.title("No Data Found")
        else:
            st.area_chart(follower_data)
    except:
        st.write("Error while Retreving Data of Follower from Tiktok")
 
plays_date=plays_time=apps=percent_apps=country=country_lat_audio=country_lon_audio=percent_country=option=None
def read_audio_datas(optionssss):
    global plays_date,plays_time,apps,percent_apps,country,country_lat_audio,country_lon_audio,percent_country,option
    plays_date,plays_time,apps,percent_apps,country,country_lat_audio,country_lon_audio,percent_country = read_audio_files(optionssss)
    option = optionssss
    
def audio_plays():
    st.markdown("<h1 style='text-align: center;'>Month Wise Viewer Graph of Audio Sites</h1><br><br>", unsafe_allow_html=True)   
    try:
        figure2 = animatedline_chart(plays_date,plays_time,option)
        options = 'audio_file'
        clip = mp.VideoFileClip(figure2)
        clip.write_videofile("{}.mp4".format(options))

        video_file = open('{}.mp4'.format(options), 'rb')
        video_bytes = video_file.read()

        st.video(video_bytes)
    except:
        st.title("Error Retreiving Views Data of Audios")

def audio_apps():
    try:
        col1,col2,col3 = st.columns([1,2,1])
        with col2:
            print(apps)
            print(percent_apps)
            st.markdown("<h1 style='text-align: center;'>APps Pie Chart of Audio</h1><br><br>", unsafe_allow_html=True)    
            figure = pie(apps,percent_apps,option)
            st.pyplot(figure)
    except:
        st.write("Error while retreving App Data of Audio")

def country_audio():
    try:
        col,col2 = st.columns([3,2])
        with col:
            df = pd.DataFrame(list(zip(country,percent_country,country_lat_audio,country_lon_audio)),columns = ['name','view','lat','lng'])
            df['views'] = df['view'].apply(lambda viewed: math.pow(viewed,5))
            
            layer = pdk.Layer(
                "ScatterplotLayer",
                df,
                pickable=True,
                opacity=0.8,
                stroked=True,
                filled=True,
                radius_min_pixels=10,
                radius_max_pixels=1000,
                get_position=['lng','lat'],
                get_radius="view",
                get_fill_color=[255, 140, 0],
                get_line_color=[0, 0, 0],
            )

            # Set the viewport location
            view_state = pdk.ViewState(
                longitude=84, latitude=28, zoom=6
            )

            # Combined all of it and render a viewport
            r = pdk.Deck(
                layers=[layer],
                initial_view_state=view_state,
                tooltip={"text": "{view}\n{name}"}
            )
            
            st.pydeck_chart(r)
        with col2:
            df = pd.DataFrame(list(zip(country,country_viewer_per)),columns = ['Country Name','Country Viewer Percentage'])
            df.sort_values(by='Country Viewer Percentage')
            st.dataframe(df)
    except:
        st.write("Error While Retreving Country Data of Audio")
    
    
def overall(option):
    ages,male_viewer_average,female_viewer_average = read_overall_particular(option)
    print(male_viewer_average)
    print(female_viewer_average)
    print(ages)
    try:
        col1,col2,col3 = st.columns([1,2,1])
        with col2:
            st.markdown("<h1 style='text-align: center;'>Age Gender Chart of Overall</h1><br><br>", unsafe_allow_html=True)
            age = ['18-24','25-34','35-44','45-54','55+']
            
            figures = horizontal_bar(age,male_viewer_average,female_viewer_average,option)
            st.pyplot(figures)
    except:
        st.write("Error while Retreiving Age Gender Data of Instagram")
