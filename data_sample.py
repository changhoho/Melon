"""
data:
    genre_gn_all.json:
        - 총 254개의 장르코드가 존재하며 30개의 대분류 장르코드와 224개의 상세 장르코드
        - 대분류 장르코드:
            - 대분류 장르는 총 30개
            - 장르코드(gnr_code)에서 숫자 네 자리 중 뒷자리 두 자리가 00인 코드로 분류
        - 상세 장르코드
            - 상세 장르는 총 224개
            - 숫자 네 자리 중 뒷자리 두 자리가 00이 아닌 나머지 코드로 분류
        - 대부분의 곡들은 한 개의 대분류 장르와 매핑되어 있습니다.
        - 전체 곡의 약 13%는 2개 이상의 대분류 장르


    song_meta.json:
        - 총 707,989곡의 메타 정보
        - song_gn_dtl_gnr_basket : 상세 장르 코드
        - issue_date : 곡 발매 일자 (yyyymmdd)
        - album_name : 앨범 명
        - album_id : 앨범 아이디
        - artist_id_basket : 아티스트 아이디 (복수일 경우 띄어쓰기로 구분)
        - song_name : 곡 명
        - song_gn_gnr_basket : 대분류 장르코드
        - artist_name_basket : 아티스트 명 (복수일 경우 띄어쓰기로 구분)
        - id : 곡 아이디

    train.json:
        - 학습 데이터에는 총 115,071개 플레이리스트 정보
        - tags : 플레이리스트에 매핑된 태그
        - id : 플레이리스트 아이디
        - plylst_title : 플레이리스트 명
        - songs : 플레이리스트 내 수록된 곡 아이디
        - like_cnt : 플레이리스트 좋아요 횟수
        - updt_date : 플레이리스트 업데이트 일시






"""