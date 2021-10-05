from app.config import URL_WEB, TELEGRAM_URL, BOT_TOKEN
import requests
import json
import ast


def validate_request(data):
    if data is None:
        return "No data", 200
    headers = {"Content-type": "application/json"}
    message_url = f"{TELEGRAM_URL}/bot{BOT_TOKEN}/sendMessage"
    if "callback_query" in data:
        user_id = data["callback_query"]["from"]["id"]
        rdata = data["callback_query"]["data"]
        url = URL_WEB + "/rest-users/"
        chat_data = {"chat_id": user_id, "text": "Menu"}
        if "ArmyMenu" in rdata:
            url += "ArmyMenu"
            chat_data["text"] = "ArmyMenu"
            request_data = requests.get(url).content
            json_response = json.loads(request_data)
            dictionary_response = dict(ast.literal_eval(json_response))
            chat_data.update(dictionary_response)
            chat_data = json.dumps(chat_data)
            requests.post(message_url, headers=headers, data=chat_data)
        elif "BackMenu" in rdata:
            url += "BackMenu"
            chat_data["text"] = "MainMenu"
            request_data = requests.get(url).content
            json_response = json.loads(request_data)
            dictionary_response = dict(ast.literal_eval(json_response))
            chat_data.update(dictionary_response)
            chat_data = json.dumps(chat_data)
            requests.post(message_url, headers=headers, data=chat_data)
        elif "AdminMenu" in rdata:
            url += "AdminMenu"
            chat_data["text"] = "AdminMenu"
            send_data = json.dumps(data)
            request_data = requests.post(url, headers=headers, data=send_data).content
            json_response = json.loads(request_data)
            dictionary_response = dict(ast.literal_eval(json_response))
            chat_data.update(dictionary_response)
            chat_data = json.dumps(chat_data)
            requests.post(message_url, headers=headers, data=chat_data)
        elif "DeleteUser" in rdata:
            url += f"{user_id}"
            requests.delete(url)
            chat_data["text"] = "User was deleted! If you want to start new game, just write /start"
            requests.post(message_url, headers=headers, data=chat_data)
        elif "BalanceMenu" in rdata or "InfoMenu" in rdata or "BuyInfantry" in rdata or "BuyTank" in rdata or \
             "BuyAirplane" in rdata or "BuyFleet" in rdata or "ChangeBalance" in rdata or "AdminInfo" in rdata:
            url = URL_WEB + "/rest-users/" + rdata
            send_data = json.dumps(data)
            request_data = requests.post(url, headers=headers, data=send_data).content
            string_response = json.loads(request_data)
            chat_data["text"] = string_response
            requests.post(message_url, data=chat_data)
    elif data["message"]["text"] == "/start":
        url = URL_WEB + "/rest-users/"
        send_data = json.dumps(data)
        request_data = requests.post(url, headers=headers, data=send_data).content
        json_response = json.loads(request_data)
        dictionary_response = dict(ast.literal_eval(json_response))
        user_id = data["message"]["from"]["id"]
        chat_data = {"chat_id": user_id, "text": "Bot initialized!"}
        chat_data.update(dictionary_response)
        chat_data = json.dumps(chat_data)
        requests.post(message_url, headers=headers, data=chat_data)
    else:
        return "Use buttons to communicate with bot!", 200
