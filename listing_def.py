import tkinter as tk
import json
import random
choices = []

#list_text = "1. おはようございます！\n2. おはようございました！\n3. おはようおげんきですか？"  

def get_choices_from_text(list_text):
    choices = list_text.split("\n")
    choices = [choice.strip() for choice in choices if choice.strip()]  # 空の選択肢を取り除く
    return choices


def list_response(choices,var="質問"):
    
    response_list = {
        "question": var,
        "list1": choices[0],
        "list2": choices[1],     
        "list3": choices[2],
        
        
        #"list4": choices[3],
        #"list5": choices[4],
        #"list6": choices[5],
        #"list7": choices[6],
        #"list8": choices[7],       
        #"list9": choices[8],  
        #"list10": choices[9],   
    }   

    with open("responses_list1.json", "w", encoding="utf-8") as json_file:
        json.dump(response_list, json_file, ensure_ascii=False, indent=4)

#choices = get_choices_from_text(list_text) #選択肢を改行させる
#list_response(choices,var="質問") #リスポンスリストとしてJsonに保存する

