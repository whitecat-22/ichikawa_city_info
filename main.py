from datetime import datetime
import pandas as pd
import folium
from folium.plugins import MarkerCluster

# 地図生成（千葉県市川市八幡1丁目1-1：市川市役所第一庁舎　中心）
folium_map = folium.Map(location=[35.72179702, 139.9310206], zoom_start=14)


def AEDMap():
    # csvからのデータ読み込み(必要なカラムだけを抽出)
    df = pd.read_csv(
        './open_data/201_福祉・健康・医療/108_AED設置箇所一覧/122033_108_aed.csv',
        encoding='cp932',
        )

    # 地図生成（千葉県市川市八幡1丁目1-1：市川市役所第一庁舎　中心）
    folium_map_108 = folium.Map(location=[35.72179702, 139.9310206], zoom_start=14)
    marker_cluster = MarkerCluster().add_to(folium_map_108)

    # マーカープロット
    for i, row in df.iterrows():
        if pd.isna(row['電話番号']):
            row['電話番号'] = 'ー'
        if pd.isna(row['建物名等(方書)']):
            text = f"【設置場所】{row['名称']} {row['設置位置']}  【住所】{row['所在地_連結表記']}  【電話番号】{row['電話番号']}"
        else:
            text = f"【設置場所】{row['名称']} {row['設置位置']}  【住所】{row['所在地_連結表記']}{row['建物名等(方書)']}  【電話番号】{row['電話番号']}"
        folium.Marker(
            location=[row['緯度'], row['経度']],
            popup=text,
            icon=folium.Icon(color='red')
        ).add_to(marker_cluster)

    # 地図表示
    folium_map_108.save('./data/108_aed_map.html')


def PublicFacility():
    # csvからのデータ読み込み(必要なカラムだけを抽出)
    df = pd.read_csv(
        './open_data/101_公共施設一覧/122033_101_public_facility.csv',
        encoding='cp932',
        )

    # 地図生成（千葉県市川市八幡1丁目1-1：市川市役所第一庁舎　中心）
    folium_map_101 = folium.Map(location=[35.72179702, 139.9310206], zoom_start=14)
    marker_cluster = MarkerCluster().add_to(folium_map_101)

    # マーカープロット
    for i, row in df.iterrows():
        if pd.isna(row['電話番号']):
            row['電話番号'] = 'ー'
        if pd.isna(row['建物名等(方書)']):
            text = f"【施設名】{row['名称']}  【住所】{row['所在地_連結表記']}  【電話番号】{row['電話番号']}"
        else:
            text = f"【施設名】{row['名称']}  【住所】{row['所在地_連結表記']}{row['建物名等(方書)']}  【電話番号】{row['電話番号']}"
        folium.Marker(
            location=[row['緯度'], row['経度']],
            popup=text,
            icon=folium.Icon(color='red')
        ).add_to(marker_cluster)

    # 地図表示
    folium_map_101.save('./data/101_public-facility_map.html')


def CulturalProperty():
    # csvからのデータ読み込み(必要なカラムだけを抽出)
    df = pd.read_csv(
        './open_data/102_文化財一覧/122033_102_cultural_property.csv',
        encoding='cp932',
        )

    # excelデータをdatetime型に変換する
    df['文化財指定日'] = pd.TimedeltaIndex(df['文化財指定日'].astype(int), unit='d') + datetime(1900, 1, 1)

    # 地図生成（千葉県市川市八幡1丁目1-1：市川市役所第一庁舎　中心）
    folium_map_102 = folium.Map(location=[35.72179702, 139.9310206], zoom_start=14)
    marker_cluster = MarkerCluster().add_to(folium_map_102)

    # マーカープロット
    for i, row in df.iterrows():
        if pd.isna(row['緯度']) or pd.isna(row['経度']):
            row['緯度'], row['経度'] = 35.72179702, 139.9310206
        if pd.isna(row['所有者等']):
            row['所有者等'] = 'ー'
        row['文化財指定日'] = row['文化財指定日'].strftime('%Y/%m/%d')
        if pd.isna(row['建物名等(方書)']):
            text = f"【名称】{row['名称']}  【文化財分類】{row['文化財分類']}  【種類】{row['種類']}  【文化財指定日】{row['文化財指定日']}  【住所】{row['所在地_連結表記']}  【所有者等】{row['所有者等']}"
        else:
            text = f"【名称】{row['名称']}  【文化財分類】{row['文化財分類']}  【種類】{row['種類']}  【文化財指定日】{row['文化財指定日']}  【住所】{row['所在地_連結表記']}{row['建物名等(方書)']}  【所有者等】{row['所有者等']}"
        folium.Marker(
            location=[row['緯度'], row['経度']],
            popup=text,
            icon=folium.Icon(color='red')
        ).add_to(marker_cluster)

    # 地図表示
    folium_map_102.save('./data/102_cultural-property_map.html')


def EvacuationSpace():
    # csvからのデータ読み込み(必要なカラムだけを抽出)
    df = pd.read_csv(
        './open_data/103_防災/103_指定緊急避難場所一覧/122033_103_evacuation_space.csv',
        encoding='cp932',
        )

    # 地図生成（千葉県市川市八幡1丁目1-1：市川市役所第一庁舎　中心）
    folium_map_103 = folium.Map(location=[35.72179702, 139.9310206], zoom_start=14)
    marker_cluster = MarkerCluster().add_to(folium_map_103)

    # マーカープロット
    for i, row in df.iterrows():
        if pd.isna(row['電話番号']):
            row['電話番号'] = 'ー'
        if pd.isna(row['建物名等(方書)']):
            text = f"【名称】{row['名称']}  【住所】{row['所在地_連結表記']}  【電話番号】{row['電話番号']}"
        else:
            text = f"【名称】{row['名称']}  【住所】{row['所在地_連結表記']}{row['建物名等(方書)']}  【電話番号】{row['電話番号']}"
        folium.Marker(
            location=[row['緯度'], row['経度']],
            popup=text,
            icon=folium.Icon(color='red')
        ).add_to(marker_cluster)

    # 地図表示
    folium_map_103.save('./data/103_evacuation-space_map.html')


def KitakuKonnan():
    # csvからのデータ読み込み(必要なカラムだけを抽出)
    df = pd.read_csv(
        './open_data/103_防災/206_帰宅困難者支援ステーション/122033_206_kitaku_konnan.csv',
        encoding='cp932',
        )

    # 地図生成（千葉県市川市八幡1丁目1-1：市川市役所第一庁舎　中心）
    folium_map_206 = folium.Map(location=[35.72179702, 139.9310206], zoom_start=14)
    marker_cluster = MarkerCluster().add_to(folium_map_206)

    # マーカープロット
    for i, row in df.iterrows():
        if pd.isna(row['店舗名称（ブランド名）']):
            text = f"【店舗名称】{row['店名']}  【住所】{row['所在地']}"
        else:
            text = f"【店舗名称】{row['店舗名称（ブランド名）']}{row['店名']}  【住所】{row['所在地']}"
        folium.Marker(
            location=[row['緯度'], row['経度']],
            popup=text,
            icon=folium.Icon(color='red')
        ).add_to(marker_cluster)

    # 地図表示
    folium_map_206.save('./data/206_kitaku-konnan_map.html')


def WellForDisaster():
    # csvからのデータ読み込み(必要なカラムだけを抽出)
    df = pd.read_csv(
        './open_data/103_防災/207_防災用井戸/122033_207_well_for_disaster.csv',
        encoding='cp932',
        )

    # 地図生成（千葉県市川市八幡1丁目1-1：市川市役所第一庁舎　中心）
    folium_map_207 = folium.Map(location=[35.72179702, 139.9310206], zoom_start=14)
    marker_cluster = MarkerCluster().add_to(folium_map_207)

    # マーカープロット
    for i, row in df.iterrows():
        text = f"【設置場所】{row['名称']}  【住所】{row['所在地_連結表記']}"
        folium.Marker(
            location=[row['緯度'], row['経度']],
            popup=text,
            icon=folium.Icon(color='red')
        ).add_to(marker_cluster)

    # 地図表示
    folium_map_207.save('./data/207_well-for-disaster_map.html')


def MedicalAidStation():
    # csvからのデータ読み込み(必要なカラムだけを抽出)
    df = pd.read_csv(
        './open_data/103_防災/208_医療救護所/122033_208_medical_aid_station.csv',
        encoding='cp932',
        )

    # 地図生成（千葉県市川市八幡1丁目1-1：市川市役所第一庁舎　中心）
    folium_map_208 = folium.Map(location=[35.72179702, 139.9310206], zoom_start=14)
    marker_cluster = MarkerCluster().add_to(folium_map_208)

    # マーカープロット
    for i, row in df.iterrows():
        text = f"【設置場所】{row['名称']}  【住所】{row['所在地_連結表記']}"
        folium.Marker(
            location=[row['緯度'], row['経度']],
            popup=text,
            icon=folium.Icon(color='red')
        ).add_to(marker_cluster)

    # 地図表示
    folium_map_208.save('./data/208_medical-aid-station_map.html')


def main():
    AEDMap()
    PublicFacility()
    CulturalProperty()
    EvacuationSpace()
    KitakuKonnan()
    WellForDisaster()
    MedicalAidStation()


if __name__ == '__main__':
    main()
