
drama1 = {
    "제목": "아이리스",           
    "장르": "드라마",    
    "주제": "첩보",        
    "방영기간": "2009-10-14 ~ 2009-12-17",      
    "배우": ["이병헌","김태희","정준호"],           
    "명대사": "\"나한테 왜 그랬어요?\""           
}

drama2 = {
    "제목": "동백꽃 필 무렵",      
    "장르": "드라마",           
    "주제": "가족, 로맨틱 코미디",          
    "방영기간": "2019.09.18 - 2019.11.21",     
    "배우": ["공효진","강하늘"],         
    "명대사": "\"사는 것도 피곤한테 무슨 작전이야?\"" 
}

new_title = input("새 드라마 제목: ")  

new_genre = input("새 드라마 장르: ")                       
new_theme = input("새 드라마 주제: ")                  
new_period = input("새 드라마 방영기간(예: 2024-01-01 ~ 2024-02-01): ")                       
new_actors_input = input("새 드라마 배우들(쉼표로 구분): ")                
new_quote_raw = input("인상 깊었던 대사(따옴표 없이 입력): ")                  

new_actors = new_actors_input.split(",")
new_quote = f"\"{new_quote_raw}\""

drama3 = {
    "제목": new_title,
    "장르": new_genre,
    "주제": new_theme,
    "방영기간": new_period,
    "배우": new_actors,
    "명대사": new_quote
}


upd_title = input("수정(덮어쓰기)할 제목(대상: drama2): ")  
upd_genre = input("수정할 장르: ")                       
upd_theme = input("수정할 주제: ")                        
upd_period = input("tnwjdgkf qkddudrlrks: ")                     
upd_actors_input = input("수정할 배우들(쉼표로 구분): ")                 
upd_quote_raw = input("수정할 명대사(따옴표 없이 입력): ")           

upd_actors = upd_actors_input.split(",")
upd_quote = f"\"{upd_quote_raw}\""

drama2["제목"] = upd_title
drama2["장르"] = upd_genre
drama2["주제"] = upd_theme
drama2["방영기간"] = upd_period
drama2["배우"] = upd_actors
drama2["명대사"] = upd_quote

print("\n[드라마 1]")
print(f"제목: {drama1['제목']}")
print(f"장르: {drama1['장르']}")
print(f"주제: {drama1['주제']}")
print(f"방영기간: {drama1['방영기간']}")
print(f"배우: {drama1['배우']}")
print(f"명대사: {drama1['명대사']}")

print("\n[드라마 2]  # 수정 후")
print(f"제목: {drama2['제목']}")
print(f"장르: {drama2['장르']}")
print(f"주제: {drama2['주제']}")
print(f"방영기간: {drama2['방영기간']}")
print(f"배우: {drama2['배우']}")
print(f"명대사: {drama2['명대사']}")

print("\n[드라마 3]  # 새로 추가")
print(f"제목: {drama3['제목']}")
print(f"장르: {drama3['장르']}")
print(f"주제: {drama3['주제']}")
print(f"방영기간: {drama3['방영기간']}")
print(f"배우: {drama3['배우']}")
print(f"명대사: {drama3['명대사']}")