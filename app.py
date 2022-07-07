import streamlit as st
from Value_Processing import read_yt_csv_dately

from youtube import Finance_Fb_Insta, Finance_Tiktok, Finance_YT, YT_age_gender,YT_country,YT_overall_view,Fb_age_gender,Fb_Country, YT_particular_view, audio_apps, audio_plays, country_audio,fb_like,Insta_age_gender,Insta_country,insta_like, overall, read_audio, read_audio_datas, read_fb_insta_values,tiktok_age,tiktok_country,tiktok_follower,read_yt,read_fb_insta_values,read_tiktok_data
st.set_page_config(page_title = "Data Visualization",layout="wide")


val = st.empty()
with val.container():
    col1,col2,col3 = st.columns([3,2,3])
    with col2:
        st.title('Login Form')

        with st.form("my_form"):
            username = st.text_input("Username")
            password = st.text_input("Password")

            # Every form must have a submit button.
            submitted = st.form_submit_button("Submit")
  

if "submit_state" not in st.session_state:
        st.session_state.submit_state = False
  
if submitted or st.session_state.submit_state:
    
    
    if username == "viewfinders" and password == "viewfinders123":
        st.session_state.submit_state = True
        val.empty()

        st.title('Social Media Data Visualization')


        col1,col2,col3,col4,col5 = st.columns([3,1,4,1,3])

        with col1:
            counter = 1
            count = 1000
            optioned = st.multiselect(
                'Which Channel Data you want to view?',
                ('Finance Factory','Agrifo','Generation of Nepal','Khulla Manch','The Doers','The Good Health','ViewFinders Production','Wedding Dreams'),['Agrifo'],key=count)
            count += 1
            channeels = ['Finance Factory','The Doers','The Good Health']
            
            for k in optioned:
                if k in channeels:
                    with col3:
                        option2 = st.multiselect('Which Social Media Data You want to view?',['Youtube','Facebook','Instagram','Tiktok','Audio Sites','Overall'],key = "option2")
                        special_for  = ['Audio Sites']
                        
                    for k in option2:
                        if k in special_for and len(option2)>1:
                            
                            with col5:
                                option3 = st.multiselect('Which Data You want to view?',['Age/Gender','Country Follower/viewer','Views/Follower/Plays','Apps'],key = counter)
                                counter = counter + 1
                                break
                        elif k in special_for and len(option2) == 1:
                            with col5:
                                option3 = st.multiselect('Which Data You want to view?',['Country Follower/viewer','Views/Follower/Plays','Apps'],key = counter)
                                counter = counter + 1
                                break
                    else:
                        with col5:
                            option3 = st.multiselect('Which Data You want to view?',['Age/Gender','Country Follower/viewer','Views/Follower/Plays'],key = counter)
                            counter = counter +1
                
                    break
            else:
                with col3:
                    option2 = st.multiselect('Which Social Media Data You want to view?',['Youtube'],key = "option2")
                with col5:
                    option3 = st.multiselect('Which Data You want to view?',['Age/Gender','Country Follower/viewer','Views/Follower/Plays'],key = counter)
                    counter = counter + 1

            

        for k in optioned:
            if (k == "Finance Factory"):
                st.title('Data Visualization of :{}'.format(k))
                for i in option2:
                    print(i)
                    if i == "Audio Sites":
                        read_audio()
                        for j in option3:
                            if j == "Country Follower/viewer":
                                country_audio()
                            if j == "Views/Follower/Plays":
                                audio_plays()
                            if j == "Apps":
                                audio_apps()
                    if i =="Overall":
                        overall(k)
                    if i == "Youtube":
                        Finance_YT()
                        for j in option3:
                            if j == "Age/Gender":
                                YT_age_gender()
                            if j == "Country Follower/viewer":
                                YT_country()
                            if j == "Views/Follower/Plays":
                                YT_overall_view()
                                col1,col2,col3,col4,col5 = st.columns([4,1,2,1,4])
                                
                                with col2:
                                    year_select   = st.selectbox(
                                        'Select Year',
                                        ('2020','2021','2022'),key = "year_select"
                                    )
                                if year_select == "2020":   
                                    with col4:
                                        month_select = st.selectbox(
                                        'Select Month',
                                        ('7','8','9','10','11','12'),key = "month_select")
                                elif year_select == "2021":
                                    with col4:
                                        month_select = st.selectbox(
                                        'Select Month',
                                        ('1', '2', '3','4','5','6','7','8','9','10','11','12'),key = "month_select")
                                else:
                                    with col4:
                                        month_select = st.selectbox(
                                        'Select Month',
                                        ('1', '2', '3','4','5','6'),key = "month_select")
                                YT_particular_view(year_select,month_select)
                    try:
                        if i == "Facebook":
                            Finance_Fb_Insta()
                            try:
                                read_fb_insta_values(k)
                            except:
                                print("Error")
                            print(i)
                            for j in option3:
                                print(j)
                                if j == "Age/Gender":
                                    Fb_age_gender()
                                if j == "Country Follower/viewer":
                                    Fb_Country()
                                if j == "Views/Follower/Plays":
                                    fb_like()
                    except Exception as e:
                        print(e)
                    if i == "Instagram":
                        Finance_Fb_Insta()
                        for j in option3:
                            if j == "Age/Gender":
                                Insta_age_gender()
                            if j == "Country Follower/viewer":
                                Insta_country()
                            if j == "Views/Follower/Plays":
                                insta_like()
                    if i == "Tiktok":
                        Finance_Tiktok()
                        for j in option3:
                            if j == "Age/Gender":
                                tiktok_age()
                            if j == "Country Follower/viewer":
                                tiktok_country()
                            if j == "Views/Follower/Plays":
                                tiktok_follower()
            else:
                st.title('Data Visualization of :{}'.format(k))
                for i in option2:
                    print(i)
                    if i == "Audio Sites":
                        read_audio_datas(k)
                        for j in option3:
                            if j == "Country Follower/viewer":
                                country_audio()
                            if j == "Views/Follower/Plays":
                                audio_plays()
                            if j == "Apps":
                                audio_apps()
                    if i =="Overall":
                        overall(k)
                    if i == "Youtube":
                        read_yt(k)
                        for j in option3:
                            if j == "Age/Gender":
                                YT_age_gender()
                            if j == "Country Follower/viewer":
                                YT_country()
                            if j == "Views/Follower/Plays":
                                YT_overall_view()
                                col1,col2,col3,col4,col5 = st.columns([4,1,2,1,4])
                                
                                with col2:
                                    year_select   = st.selectbox(
                                        'Select Year',
                                        ('2020','2021','2022'),key = "year_select"
                                    )
                                if year_select == "2020":   
                                    with col4:
                                        month_select = st.selectbox(
                                        'Select Month',
                                        ('7','8','9','10','11','12'),key = "month_select")
                                elif year_select == "2021":
                                    with col4:
                                        month_select = st.selectbox(
                                        'Select Month',
                                        ('1', '2', '3','4','5','6','7','8','9','10','11','12'),key = "month_select")
                                else:
                                    with col4:
                                        month_select = st.selectbox(
                                        'Select Month',
                                        ('1', '2', '3','4','5','6'),key = "month_select")
                                YT_particular_view(year_select,month_select)
                    try:
                        if i == "Facebook":
                            
                            try:
                                read_fb_insta_values(k)
                            except:
                                print("Error")
                            print(i)
                            for j in option3:
                                print(j)
                                if j == "Age/Gender":
                                    Fb_age_gender()
                                if j == "Country Follower/viewer":
                                    Fb_Country()
                                if j == "Views/Follower/Plays":
                                    fb_like()
                    except Exception as e:
                        print(e)
                    if i == "Instagram":
                        read_fb_insta_values(k)
                        for j in option3:
                            if j == "Age/Gender":
                                Insta_age_gender()
                            if j == "Country Follower/viewer":
                                Insta_country()
                            if j == "Views/Follower/Plays":
                                insta_like()
                    if i == "Tiktok":
                        read_tiktok_data(k)
                        for j in option3:
                            if j == "Age/Gender":
                                tiktok_age()
                            if j == "Country Follower/viewer":
                                tiktok_country()
                            if j == "Views/Follower/Plays":
                                tiktok_follower()
        
        
            
    
    
    

