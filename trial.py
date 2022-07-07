from Value_Processing import fb_insta_reach, read_audio_files, read_fb_insta, read_yt_csv, tiktok_data



print(tiktok_data("Finance Factory"))
def Finance_Tiktok():
    tik_age = [83, 17]
    tik_age_label = ['Male', 'Female']
    tik_geo_label = ['United Arab Emirates', 'Australia', 'South Korea', 'Japan', 'Nepal']
    tik_geo_value = [1.5, 0.5, 0.25, 0.75, 97.0]
    
    follower_tiktok = [0, 0, 0, 0, 158832, 463170, 15177, 0, 0, 0, 0, 0]
    year_month_tiktok = ['2022/1', '2022/2', '2022/3', '2022/4', '2022/5', '2022/6']
    country_lat_fb = [24.0002488, -24.7761086, 36.638392, 36.5748441, 28.1083929]
    country_lon_fb = [53.9994829, 134.755, 127.6961188, 139.2394179, 84.0917139]
    
    return tik_age,tik_age_label,tik_geo_label,tik_geo_value,follower_tiktok,year_month_tiktok,country_lat_fb,country_lon_fb

