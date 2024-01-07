import pandas as pd
import folium
from folium.plugins import MarkerCluster


# csvからのデータ読み込み(必要なカラムだけを抽出)
df1 = pd.read_csv(
    './open_data/201_福祉・健康・医療/108_AED設置箇所一覧/122033_108_aed.csv',
    encoding='cp932',
    )


# 地図生成（千葉県市川市八幡1丁目1-1：市川市役所第一庁舎　中心）
folium_map = folium.Map(location=[35.72179702, 139.9310206], zoom_start=14)
marker_cluster = MarkerCluster().add_to(folium_map)

# マーカープロット
for i, row in df1.iterrows():
    if str(row['建物名等(方書)']) == "nan":
        text = f"【設置場所】{row['名称']} {row['設置位置']}  【住所】{row['所在地_連結表記']}  【電話番号】{row['電話番号']}"
    else:
        text = f"【設置場所】{row['名称']} {row['設置位置']}  【住所】{row['所在地_連結表記']}{row['建物名等(方書)']}  【電話番号】{row['電話番号']}"
    folium.Marker(
        location=[row['緯度'], row['経度']],
        popup=text,
        icon=folium.Icon(color='red')
    ).add_to(marker_cluster)

# 地図表示
folium_map.save('./data/aed-map.html')
