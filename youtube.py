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

def Finance_YT():
    global ages_yt,male_viewer_yt,female_viewer_yt,country_name,country_viewer_per,country_lat,country_lon,viewes,avg_duration,year_month,option
    ages_yt = ['18-24', '25-34', '35-44', '45-54', '55+']
    male_viewer_yt = [41.0, 45.4, 4.9, 0.1, 0]
    female_viewer_yt = [3.6, 4.9, 0.0, 0.1, 0]
    country_name = ['United Arab Emirates', 'Australia', 'Germany', 'United Kingdom', 'India', 'Japan', 'Korea, Republic of', 'Nepal', 'Singapore', 'United States']
    country_viewer_per = [0.06142425866147392, 0.4090594247030072, 0.12023471908203405, 0.043127670975077435, 0.04574146921599122, 0.060117359541017025, 0.17251068390030974, 98.77151482677053, 0.013068991204568918, 0.3032005959459989]
    country_lat = [24.0002488, -24.7761086, 51.0834196, 54.7023545, 22.3511148, 36.5748441, 36.638392, 28.1083929, 1.357107, 39.7837304]
    country_lon = [53.9994829, 134.755, 10.4234469, -3.2765753, 78.6677428, 139.2394179, 127.6961188, 84.0917139, 103.8194992, -100.445882]
    viewes = [9898, 8720, 6107, 5905, 5814, 3904, 3326, 3754, 2186, 1909, 2425, 2605, 2444, 2293, 4854, 2454, 1650, 1501, 1738, 1637, 1643, 1689, 6589, 8233]
    avg_duration = [8.452666666666667, 8.53225806451613, 8.982222222222221, 8.25, 9.948333333333332, 10.433870967741935, 9.741397849462366, 10.030357142857143, 9.118279569892474, 9.431666666666667, 9.812903225806451, 8.37888888888889, 8.823655913978493, 8.34731182795699, 6.330555555555555, 6.902688172043011, 5.308333333333334, 7.782258064516129, 7.004301075268817, 7.354166666666667, 7.663978494623655, 7.415555555555556, 6.4, 7.148717948717948]
    year_month = ['2020/7', '2020/8', '2020/9', '2020/10', '2020/11', '2020/12', '2021/1', '2021/2', '2021/3', '2021/4', '2021/5', '2021/6', '2021/7', '2021/8', '2021/9', '2021/10', '2021/11', '2021/12', '2022/1', '2022/2', '2022/3', '2022/4', '2022/5', '2022/6']
    option = "Finance Factory"

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
    
ages_fb=male_viewer_fb=female_viewer_fb=ages_insta=male_viewer_insta=female_viewer_insta=country_name_fb_insta=country_viewer_per_insta=country_lat_insta=country_lon_insta=country_name_fb=country_viewer_per_fb=country_lat_fb=country_lon_fb=year_month_fb_insta=like_fb=follower_insta=option=facebook_reach=insta_reach = None    

def Finance_Fb_Insta():
    global ages_fb,male_viewer_fb,female_viewer_fb,ages_insta,male_viewer_insta,female_viewer_insta,country_name_fb_insta,country_viewer_per_insta,country_lat_insta,country_lon_insta,country_name_fb,country_viewer_per_fb,country_lat_fb,country_lon_fb,year_month_fb_insta,like_fb,follower_insta,option,facebook_reach,insta_reach  
    ages_fb = ['18-24', '25-34', '35-44', '45-54', '55+']
    male_viewer_fb = [22.9, 40.7, 13.5, 1.5, 0.5]
    female_viewer_fb = [7.9, 11.3, 1.5, 0.0, 0.2]
    ages_insta = ['18-24', '25-34', '35-44', '45-54', '55+']
    male_viewer_insta = [332.0, 40.2, 6.8, 0.8, 0.6]
    female_viewer_insta = [7.6, 9.7, 0.8, 0.2, 0.1]
    country_name_fb_insta = ['Kathmandu, Nepal', 'Pokhara, Nepal', 'Butwal, Nepal', 'Sydney, NSW, Australia', 'Jhapa District, Nepal']
    country_viewer_per_insta = [88.02153432032303, 4.441453566621804, 3.095558546433378, 2.4226110363391657, 2.018842530282638]
    country_lat_insta=[27.708317, 28.209538, 27.6827731, -33.8698439, 26.583735400000002]
    country_lon_insta=[85.3205817, 83.991402, 83.44386204928969, 151.2082848, 87.88570103314731]
    country_name_fb=['Kathmandu, Nepal', 'Pokhara, Nepal', 'Lalitpur, Nepal', 'Butwal, Nepal', 'Bhaktapur, Nepal', 'Bharatpur, Nepal', 'Jhapa District, Nepal', 'Biratnagar, Nepal', 'Itahari, Nepal', 'Hetauda, Nepal']
    country_viewer_per_fb = [82.98122065727698, 3.4037558685446, 3.0516431924882625, 2.8169014084507036, 2.4647887323943656, 1.1737089201877933, 1.1737089201877933, 1.0563380281690138, 1.0563380281690138, 0.8215962441314552]
    country_lat_fb = [27.708317, 28.209538, 27.6676649, 27.6827731, 27.6718111, 27.6879274, 26.583735400000002, 26.4623007, 26.673931449999998, 27.4187156]
    country_lon_fb=[85.3205817, 83.991402, 85.3183888179628, 83.44386204928969, 85.4264284, 84.4360695372875, 87.88570103314731, 87.281617, 87.25838795294675, 85.01009335459317]
    year_month_fb_insta = ['2019/1', '2019/2', '2019/3', '2019/4', '2019/5', '2019/6', '2019/7', '2019/8', '2019/9', '2019/10', '2019/11', '2019/12', '2020/1', '2020/2', '2020/3', '2020/4', '2020/5', '2020/6', '2020/7', '2020/8', '2020/9', '2020/10', '2020/11', '2020/12', '2021/1', '2021/2', '2021/3', '2021/4', '2021/5', '2021/6', '2021/7', '2021/8', '2021/9', '2021/10', '2021/11', '2021/12', '2022/1', '2022/2', '2022/3', '2022/4', '2022/5', '2022/6', '2022/7', '2022/8', '2022/9', '2022/10', '2022/11', '2022/12']
    like_fb = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 147, 16, 6, 8, 5, 7, 5, 6, 13, 13, 14, 10, 172, 67, 24, 6, 10, 15, 4, 2, 6, 7, 15, 1, 0, 0, 0, 0, 0]
    follower_insta = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 43.0, 48.0, 70.0, 87.0, 64.0, 86.0, 132.0, 0, 0, 0, 0, 0, 0, 0, 0]
    facebook_reach = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 339, 5207, 596, 1288, 103, 62, 53, 42, 37, 31, 39, 544, 564, 7110, 4867, 1017, 1020, 283, 335, 188, 158, 121, 109, 141, 0, 0, 0, 0, 0, 0]
    insta_reach = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3581, 6351, 3133, 4903, 918, 153, 3799, 7360, 5589, 2176, 362, 7854, 4573, 4301, 3486, 1505, 1902, 617, 214, 38, 633, 339, 288, 57, 0, 0, 0, 0, 0, 0]
    option = "Finance Factory"

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
        print(ages_fb,male_viewer_fb,female_viewer_fb,option)
        figure = horizontal_bar(ages_fb,male_viewer_fb,female_viewer_fb,option)
        st.pyplot(figure)
    except:
        st.write("Error while Retreiving Gender Age Data of Facebook")
def Insta_age_gender():
    
    st.markdown("<h1 style='text-align: center;'>Age Gender Chart of Instagram</h1><br><br>", unsafe_allow_html=True)
    (ages_insta,male_viewer_insta,female_viewer_insta,option)
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
            df = pd.DataFrame(list(zip(country_name_fb_insta,country_viewer_per_insta)),columns = ['Country Name','Country Viewer Percentage'])
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

def Finance_Tiktok():
    global tik_age,tik_age_label,tik_geo_label,tik_geo_value,follower_tiktok,year_month_tiktok,country_lat_fb,country_lon_fb,option
    tik_age = [83, 17]
    tik_age_label = ['Male', 'Female']
    tik_geo_label = ['United Arab Emirates', 'Australia', 'South Korea', 'Japan', 'Nepal']
    tik_geo_value = [1.5, 0.5, 0.25, 0.75, 97.0]
    
    follower_tiktok = [3212, 3210, 3211, 3208, 3206, 3207, 3203, 3202, 3200, 3207, 3215, 3283, 3615, 3709, 3749, 3775, 3989, 3989, 4214, 4247, 4264, 4264, 4306, 4323, 10564, 14865, 14865, 15773, 15757, 15733, 15711, 15683, 15652, 15628, 15619, 15590, 15567, 15542, 15526, 15503, 15483, 15464, 15446, 15442, 15428, 15412, 15391, 15372, 15348, 15334, 15316, 15305, 15290, 15270, 15257, 15239, 15225, 15205, 15189, 15177]
    year_month_tiktok = ['2022-05-03', '2022-05-04', '2022-05-05', '2022-05-06', '2022-05-07', '2022-05-08', '2022-05-09', '2022-05-10', '2022-05-11', '2022-05-12', '2022-05-13', '2022-05-14', '2022-05-15', '2022-05-16', '2022-05-17', '2022-05-18', '2022-05-19', '2022-05-20', '2022-05-21', '2022-05-22', '2022-05-23', '2022-05-24', '2022-05-25', '2022-05-26', '2022-05-27', '2022-05-28', '2022-05-29', '2022-05-30', '2022-05-31', '2022-06-01', '2022-06-02', '2022-06-03', '2022-06-04', '2022-06-05', '2022-06-06', '2022-06-07', '2022-06-08', '2022-06-09', '2022-06-10', '2022-06-11', '2022-06-12', '2022-06-13', '2022-06-14', '2022-06-15', '2022-06-16', '2022-06-17', '2022-06-18', '2022-06-19', '2022-06-20', '2022-06-21', '2022-06-22', '2022-06-23', '2022-06-24', '2022-06-25', '2022-06-26', '2022-06-27', '2022-06-28', '2022-06-29', '2022-06-30', '2022-07-01']
    country_lat_fb = [24.0002488, -24.7761086, 36.638392, 36.5748441, 28.1083929]
    country_lon_fb = [53.9994829, 134.755, 127.6961188, 139.2394179, 84.0917139]
    option = "Finance Factory"

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
        print(follower_tiktok)
        print(year_month_tiktok)
        follower_data = pd.DataFrame(follower_tiktok,index=year_month_tiktok)
        print("Here")
        if follower_tiktok == []:
            st.title("No Data Found")
        else:
            print("New")
            st.area_chart(follower_data)
    except:
        st.write("Error while Retreving Data of Follower from Tiktok")
 
plays_date=plays_time=apps=percent_apps=country=country_lat_audio=country_lon_audio=percent_country=option=None

def read_audio():
    global plays_date,plays_time,apps,percent_apps,country,country_lat_audio,country_lon_audio,percent_country,option
    plays_date = ['6/19/2020, 12:00:00', '7/19/2020, 22:00:00', '8/19/2020, 08:00:00', '9/18/2020, 18:00:00', '10/19/2020, 04:00:00', '11/18/2020, 14:00:00', '12/19/2020, 24:00:00', '1/18/2021, 10:00:00', '2/17/2021, 20:00:00', '3/20/2021, 06:00:00', '4/19/2021, 16:00:00', '5/20/2021, 02:00:00', '6/19/2021, 12:00:00', '7/19/2021, 22:00:00', '8/19/2021, 08:00:00', '9/18/2021, 18:00:00', '10/19/2021, 04:00:00', '11/18/2021, 14:00:00', '12/19/2021, 24:00:00', '1/18/2022, 10:00:00', '2/17/2022, 20:00:00', '3/20/2022, 06:00:00', '4/19/2022, 16:00:00', '5/20/2022, 02:00:00', '6/19/2022, 12:00:00', '6/19/2020, 12:00:00', '7/19/2020, 22:00:00', '8/19/2020, 08:00:00', '9/18/2020, 18:00:00', '10/19/2020, 04:00:00', '11/18/2020, 14:00:00', '12/19/2020, 24:00:00', '1/18/2021, 10:00:00', '2/17/2021, 20:00:00', '3/20/2021, 06:00:00', '4/19/2021, 16:00:00', '5/20/2021, 02:00:00', '6/19/2021, 12:00:00', '7/19/2021, 22:00:00', '8/19/2021, 08:00:00', '9/18/2021, 18:00:00', '10/19/2021, 04:00:00', '11/18/2021, 14:00:00', '12/19/2021, 24:00:00', '1/18/2022, 10:00:00', '2/17/2022, 20:00:00', '3/20/2022, 06:00:00', '4/19/2022, 16:00:00', '5/20/2022, 02:00:00', '6/19/2022, 12:00:00']
    plays_time = [10, 147, 180, 150, 61, 272, 201, 102, 164, 107, 144, 48, 34, 88, 90, 47, 135, 186, 113, 114, 93, 104, 37, 83, 44, 10, 147, 180, 150, 61, 272, 201, 102, 164, 107, 144, 48, 34, 88, 90, 47, 135, 186, 113, 114, 93, 104, 37, 83, 44]
    apps = ['Apple Podcasts', 'Google Podcasts', 'Spotify', 'CastBox', 'Web Browser', 'Other']
    percent_apps = [0.286855482933914, 0.265432098765432, 0.225853304284676, 0.0591866376180101, 0.027596223674655, 0.135076252723311]
    country = ['Nepal', 'United States', 'Australia', 'United Kingdom', 'India', 'South Korea', 'United Arab Emirates', 'Germany', 'New Zealand', 'Norway', 'Qatar', 'Hong Kong', 'Mongolia', 'Japan', 'Singapore', 'Canada', 'Iraq', 'Finland', 'Netherlands', 'Thailand', 'Israel', 'Russia', 'Myanmar', 'Brazil', 'France', 'Switzerland', 'Nigeria', 'Spain', 'Ireland', 'Portugal', 'Colombia', 'Pakistan', 'Oman', 'Czech Republic']
    country_lat_audio = [28.1083929, 39.7837304, -24.7761086, 54.7023545, 22.3511148, 36.638392, 24.0002488, 51.0834196, -41.5000831, 60.5000209, 25.3336984, 22.2793278, 46.8250388, 36.5748441, 1.357107, 61.0666922, 33.0955793, 63.2467777, 52.2288689, 14.8971921, 31.5313113, 64.6863136, 17.1750495, -10.3333333, 46.603354, 46.7985624, 9.6000359, 39.3260685, 52.865196, 40.0332629, 4.099917, 30.3308401, 21.0000287, 49.8167003]
    country_lon_audio = [84.0917139, -100.445882, 134.755, -3.2765753, 78.6677428, 127.6961188, 53.9994829, 10.4234469, 172.8344077, 9.0999715, 51.2295295, 114.1628131, 103.8499736, 139.2394179, 103.8194992, -107.991707, 44.1749775, 25.9209164, 5.3214503, 100.83273, 34.8667654, 97.7453061, 95.9999652, -53.2, 1.8883335, 8.2319736, 7.9999721, -4.8379791, -7.9794599, -7.8896263, -72.9088133, 71.247499, 57.0036901, 15.4749544]
    percent_country = [55.00000000000001, 11.0, 8.0, 5.0, 4.0, 4.0, 3.0, 2.0, 2.0, 1.0, 0.844346549192364, 0.624082232011747, 0.550660792951541, 0.440528634361233, 0.367107195301027, 0.293685756240822, 0.22026431718061598, 0.22026431718061598, 0.11013215859030799, 0.11013215859030799, 0.0734214390602055, 0.0734214390602055, 0.0367107195301027, 0.0367107195301027, 0.0367107195301027, 0.0367107195301027, 0.0367107195301027, 0.0367107195301027, 0.0367107195301027, 0.0367107195301027, 0.0367107195301027, 0.0367107195301027, 0.0367107195301027, 0.0367107195301027]
    option = "Finance Factory"

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
