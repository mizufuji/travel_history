# 2番目に作成
# 8番目に作成
# 10番目に作成
# 11番目に作成 pandasでデータをUIに表形式で表示

import streamlit as st
import json
import requests
import random
import pandas as pd

page = st.sidebar.selectbox(
    "Select",
    ["locations", "travels"]
)

if page == "locations":
    st.title("旅行先登録画面")
    with st.form(key="loc"):
        #location_id: int = random.randint(1,10)
        location_name: str = st.text_input("旅行先", max_chars=30)
        data = {
            # "location_id": location_id,
            "location_name": location_name
        }

        submitted = st.form_submit_button(label="送信")
        if submitted:
            #st.write("## 送信データ")
            #st.json(data)
            st.write("## レスポンス結果")
            url = "http://127.0.0.1:8000/locations"

            res = requests.post(
                url,
                data=json.dumps(data)
            )
            if res.status_code == 200:
                st.success("旅行先登録完了")
            st.write(res.status_code)
            #st.json(res.json())

elif page == "travels":
    st.title("旅行履歴一覧")

    # UI上に旅行先一覧を表示したいので、
    url_locations = "http://127.0.0.1:8000/locations"
    res = requests.get(url_locations)
    res_locations = res.json()

    # res_locationsは複数のデータが入っていて、リストの中に辞書型で入っているので、
    # location_nameをKey,location_idをvalueとする辞書型に変更する。
    locations_dict = {}
    for res_location in res_locations:
        locations_dict[res_location["location_name"]] = res_location["location_id"]
        #st.write(loactions_dict)

    # pandasでUI上に旅行先一覧を表示する。
    # vidual studion code上でpandasを使うのはなんだか違和感がある。

    st.write("### 旅行先一覧")
    df_location = pd.DataFrame(res_locations) 
    df_location.columns = ['旅行先', '旅行先ID']
    # 静的なtableを表示。　動的ならdataframe
    st.table(df_location)

    url_travels = "http://127.0.0.1:8000/travels"
    res = requests.get(url_travels)
    res_travels = res.json()
    df_travel = pd.DataFrame(res_travels)

    locations_id = {}
    for res_location in res_locations:
        locations_id[res_location['location_id']] = res_location['location_name']

    # UI上でlocation_idを表示しても分からない。札幌・石垣島といった名前で表示したい。
    to_location_name = lambda x: locations_id[x]
    
    # 特定の列に適用
    df_travel['location_id'] = df_travel['location_id'].map(to_location_name)

    df_travel = df_travel.rename(columns={
        'location_id': '旅行先',
        'departure_month': '旅行月',
        'days': '日数',
        'travel_id': '旅行ID'
    })

    st.write("旅行履歴一覧")
    st.table(df_travel)


    with st.form(key="ryokou"):
        location_name: str = st.selectbox("旅行先名", locations_dict.keys())
        #travel_id: int = random.randint(1,10)
        departure_month: int = st.number_input("旅行月", step=1, min_value=1)
        days: int = st.number_input("旅行日数", step=1, min_value=1)

        submitted = st.form_submit_button(label="送信")

        if submitted:
            location_id: int = locations_dict[location_name]

            data = {
            #"travel_id": travel_id,
            "location_id": location_id,
            "departure_month": departure_month,
            "days": days
        }


            st.write("## 送信データ")
            st.json(data)
            st.write("## レスポンス結果")
            url = "http://127.0.0.1:8000/travels"

            res = requests.post(
                url,
                data = json.dumps(data)
            )
            if res.status_code == 200:
                st.success("入力完了しました")
            st.write(res.status_code)
            #st.json(res.json())