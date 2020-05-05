import json
import itertools
import pickle

"""
    곡: idx
    장르: idx
    태그: idx
"""
if __name__=="__main__":

    with open('./dataset/song_meta.json', encoding='UTF-8') as json_file:
        songs = json.load(json_file)

    with open('./dataset/train.json', encoding='UTF-8') as json_file:
        train = json.load(json_file)

    with open('./dataset/genre_gn_all.json', encoding='UTF-8') as json_file:
        genre = json.load(json_file)

    idx_song = {x["id"]: x['song_name'] for x in songs}

    gndtl = [x for x in genre if x[-2:] != "00"]
    gndtl_idx = {gen: idx for idx, gen in enumerate(gndtl)}
    idx_gndtl = {values: key for key, values in gndtl_idx.items()}

    song_gndtl_idx = dict()

    for x in songs:
        song_id = x["id"]
        gns = x["song_gn_dtl_gnr_basket"]

        song_gndtl_idx[song_id] = [gndtl_idx[gn] for gn in gns]

    tags = [x["tags"] for x in train]
    tags = list(set(itertools.chain(*tags)))

    tags_idx = {tags: idx for idx, tags in enumerate(tags)}
    idx_tags = {values: key for key, values in tags_idx.items()}


    meta = dict()
    meta["idx_song"] = idx_song
    meta["gndtl_idx"] = gndtl_idx
    meta["idx_gndtl"] = idx_gndtl
    meta["song_gndtl_idx"] = song_gndtl_idx
    meta["tags_idx"] = tags_idx
    meta["idx_tags"] = idx_tags


    with open('./dataset/meta.pkl', 'wb') as f:
        pickle.dump(meta, f)



















