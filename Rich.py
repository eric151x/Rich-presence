from discordrp import Presence
import time
import os
import requests

def connect(Client_id):
    presence = Presence(Client_id)

    class Wrapper:
        def update(self, pid=None, state=None, details=None, start=None, end=None, large_image=None, large_text=None, small_image=None, small_text=None, party_id=None, party_size=None, join=None, spectate=None, match=None, buttons=None, type=None):
            if start is None:
                start = int(time.time())
            if pid is None:
                pid = os.getpid()

            timestamps = {"start": start}
            if isinstance(end, (int, float)):
                timestamps["end"] = int(end)

            assets = {}
            if large_image: assets["large_image"] = large_image
            if large_text: assets["large_text"] = large_text
            if small_image: assets["small_image"] = small_image
            if small_text: assets["small_text"] = small_text

            party = {}
            if party_id: party["id"] = party_id
            if party_size: party["size"] = party_size

            secrets = {}
            if join: secrets["join"] = join
            if spectate: secrets["spectate"] = spectate
            if match: secrets["match"] = match

            dic = {
            "state": state,
            "details": details,
            "timestamps": timestamps,
            "assets": assets,
            "party": party,
            "pid": pid
        }
            #Onde coloca coisas no dicionario caso tenha colocado
            if join or spectate or match: dic["secrets"] = secrets
            if buttons: dic["buttons"] = buttons
            if type is not None: dic["type"] = type

            #Onde analisa se tem algum erro
            if dic["secrets"] and buttons:
                print("Error: existe botões e secrets")
                return
            if type in (1, 4):
                print("Error: não pode usar 1 ou 4, somente 0, 2, 3 ou 5")
                return

            presence.set(dic)
            
        def clear(self):
            presence.clear()

        def close(self):
            presence.close()
    return Wrapper()