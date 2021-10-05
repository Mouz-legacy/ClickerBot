from flask_restful import Resource
from flask import request
from app.back_menu import *
from multiprocessing import Process
import json
import logging
import configparser


config = configparser.ConfigParser()
config.read('/home/src/app_back/app/cnf.ini')
logging.basicConfig(level=config['LOGGING']['level'], filename=config['LOGGING']['filename'])
logger = logging.getLogger(__name__)


class DatabaseOperations(Resource):

    def get(self, id):
        p = Process(target=logger.info(f'Get method initialized'))
        if "ArmyMenu" in id:
            p = Process(target=logger.info("ArmyMenu was returned"))
            chat_data = army_menu()
            chat_data = json.dumps(chat_data)
            return chat_data, 200
        elif "BackMenu" in id:
            p = Process(target=logger.info("BackMenu was returned"))
            chat_data = main_menu()
            chat_data = json.dumps(chat_data)
            return chat_data, 200
        elif "Menu" in id:
            p = Process(target=logger.info("Bad request"))
            return "Bad request. You must send Menu type", 400
        else:
            p = Process(target=logger.info("Bad request"))
            return "Menu not found or message was invalid", 404

    def post(self, id=0):
        from app.models  import Users, Army, db, Infantry, Fleet, Airplanes, AchievementManager, Tanks, Medals, ArmyInfo
        p = Process(target=logger.info("Post request initiated"))
        chat_data = "Chat info"
        if "callback_query" in request.json:
            user_id = request.json["callback_query"]["from"]["id"]
            rdata = request.json["callback_query"]["data"]
            try:
                user = Users.query.get(int(user_id))
                if rdata == "BalanceMenu":
                    p = Process(target=logger.info("Balance was returned"))
                    balance = user.balance
                    chat_data = json.dumps(f"User balance: {balance}$")
                    return chat_data, 200
                elif rdata == "AdminMenu" and user.is_admin == 1:
                    p = Process(target=logger.info("AdminMenu was returned"))
                    chat_data = json.dumps(admin_menu())
                    return chat_data, 200
                elif rdata == "BuyFleet":
                    p = Process(target=logger.info(f"User: {user_id} is trying to buy fleet"))
                    army_id = user.army_id
                    army = Army.query.get(int(army_id))
                    fleet = Fleet.query.get(int(army.fleet_id))
                    if fleet.price <= user.balance:
                        p = Process(target=logger.info(f"User: {user_id} bought fleet"))
                        user.balance -= fleet.price
                        fleet.count += 1
                        chat_data = json.dumps("Fleet was bought!")
                    else:
                        chat_data = json.dumps("Not enough money for fleet(")
                    db.session.commit()
                    return chat_data, 200
                elif rdata == "BuyTank":
                    p = Process(target=logger.info(f"User: {user_id} is trying to buy tank"))
                    army_id = user.army_id
                    army = Army.query.get(int(army_id))
                    tank = Tanks.query.get(int(army.tanks_id))
                    if tank.price <= user.balance:
                        p = Process(target=logger.info(f"User: {user_id} bought tank"))
                        user.balance -= tank.price
                        tank.count += 1
                        chat_data = json.dumps("Tank was bought!")
                    else:
                        chat_data = json.dumps("Not enough money for tank(")
                    db.session.commit()
                    return chat_data, 200
                elif rdata == "BuyAirplane":
                    p = Process(target=logger.info(f"User: {user_id} is trying to buy airplane"))
                    army_id = user.army_id
                    army = Army.query.get(int(army_id))
                    airplane = Airplanes.query.get(int(army.airplanes_id))
                    if airplane.price <= user.balance:
                        p = Process(target=logger.info(f"User: {user_id} bought airplane"))
                        user.balance -= airplane.price
                        airplane.count += 1
                        chat_data = json.dumps("Airplane was bought!")
                    else:
                        chat_data = json.dumps("Not enough money for airplane(")
                    db.session.commit()
                    return chat_data, 200
                elif rdata == "BuyInfantry":
                    p = Process(target=logger.info(f"User: {user_id} is trying to buy infantry"))
                    army_id = user.army_id
                    army = Army.query.get(int(army_id))
                    infantry = Infantry.query.get(int(army.infantry_id))
                    if infantry.price <= user.balance:
                        p = Process(target=logger.info(f"User: {user_id} bought infantry"))
                        user.balance -= infantry.price
                        infantry.count += 1
                        chat_data = json.dumps("Infantry was bought!")
                    else:
                        chat_data = json.dumps("Not enough money for infantry(")
                    db.session.commit()
                    return chat_data, 200
                elif rdata == "AdminInfo":
                    p = Process(target=logger.info(f"Admin info was returned"))
                    users = Users.query.all()
                    medals = Medals.query.all()
                    achievements = AchievementManager.query.all()
                    text = ""
                    for user in users:
                        for medal in medals:
                            for achievement in achievements:
                                if achievement.user_id == user.id and achievement.medal_id == medal.id:
                                    text += f"User: {user.username} has {medal.medal_type} achievement!"
                    chat_data = json.dumps(text)
                    return chat_data, 200
                elif rdata == "ChangeBalance":
                    p = Process(target=logger.info(f"User: {user_id} get 100 dollars from admin panel"))
                    user.balance += 100
                    chat_data = json.dumps("This action will recharge your balance with 100$")
                    db.session.commit()
                    return chat_data, 200
                elif rdata == "InfoMenu":
                    p = Process(target=logger.info(f"Info menu was returned"))
                    text = ""
                    army_id = user.army_id
                    army = Army.query.get(int(army_id))
                    fleet = Fleet.query.get(int(army.fleet_id))
                    text += f"Amount of fleet: {fleet.count}. Price per item:{int(fleet.price)}$"
                    text += '\n'
                    infantry = Infantry.query.get(int(army.infantry_id))
                    text += f"Amount of infantry: {infantry.count}. Price per item:{int(infantry.price)}$"
                    text += '\n'
                    tank = Tanks.query.get(int(army.tanks_id))
                    text += f"Amount of tanks: {tank.count}. Price per item: {int(tank.price)}$"
                    text += '\n'
                    airplane = Airplanes.query.get(int(army.airplanes_id))
                    text += f"Amount of airplanes: {airplane.count}. Price per item: {int(airplane.price)}$"
                    chat_data = json.dumps(text)
                    return chat_data, 200
                db.session.commit()
            except (RuntimeError, TypeError, NameError, AttributeError):
                chat_data = json.dumps("Error occurred while processing menu operations or buy operations")
                return chat_data, 200
        elif "message" in request.json and "text" in request.json["message"]:
            user_id = request.json["message"]["from"]["id"]
            username = request.json["message"]["from"]["username"]
            user = Users.query.get(int(user_id))
            if user is None and request.json["message"]["text"] == "/start":
                p = Process(target=logger.info(f"User: {user_id} is starting application"))
                medal = Medals.query.get(int(1))
                if medal is None:
                    medal = Medals(medal_type="New player", id=1)
                    db.session.add(medal)
                    db.session.commit()
                    new_medal = Medals(medal_type="1000 backs!", id=2)
                    db.session.add(new_medal)
                    db.session.commit()
                    another_medal = Medals(medal_type="10000 backs! Great player!", id=3)
                    db.session.add(another_medal)
                    db.session.commit()
                fleet = Fleet(price=2500, income=200, count=0)
                tanks = Tanks(price=100, income=5, count=0)
                airplanes = Airplanes(price=1000, income=75, count=0)
                infantry = Infantry(price=25, income=1, count=0)
                db.session.add(fleet)
                db.session.add(tanks)
                db.session.add(airplanes)
                db.session.add(infantry)
                db.session.commit()
                army = Army(infantry_id=infantry.id, tanks_id=tanks.id, airplanes_id=airplanes.id, fleet_id=fleet.id)
                db.session.add(army)
                db.session.commit()
                army_info = ArmyInfo(army_id=army.id, info="Normal")
                db.session.add(army_info)
                db.session.commit()
                user = Users(id=int(user_id), balance=50, username=username, is_admin=1, army_id=army.id)
                db.session.add(user)
                db.session.commit()
                achive_manager = AchievementManager(medal_id=1, user_id=int(user_id))
                db.session.add(achive_manager)
                db.session.commit()
                chat_data = main_menu()
                chat_data = json.dumps(chat_data)
                return chat_data, 200
            else:
                chat_data = main_menu()
                chat_data = json.dumps(chat_data)
                return chat_data, 200
        chat_data = "Error request!"
        chat_data = json.dumps(chat_data)
        return chat_data, 200

    def put(self, id=0):
        from app.models import Users, Army, db, Infantry, Fleet, Airplanes, Tanks
        users = Users.query.all()
        p = Process(target=logger.info(f"Users are getting income from their army's"))
        for user in users:
            army = Army.query.get(int(user.army_id))
            fleet = Fleet.query.get(int(army.fleet_id))
            tank = Tanks.query.get(int(army.tanks_id))
            infantry = Infantry.query.get(int(army.infantry_id))
            airplanes = Airplanes.query.get(int(army.airplanes_id))
            user.balance += infantry.count * infantry.income
            user.balance += fleet.count * fleet.income
            user.balance += tank.count * tank.income
            user.balance += airplanes.count * airplanes.income
            db.session.commit()
        return 200

    def delete(self, id):
        from app.models import Users, Army, db, Infantry, Fleet, Airplanes, Tanks, AchievementManager, ArmyInfo
        user = Users.query.get(id)
        army = Army.query.get(user.army_id)
        ArmyInfo.query.filter_by(army_id=army.id).delete()
        AchievementManager.query.filter_by(user_id=id).delete()
        Users.query.filter_by(id=id).delete()
        Army.query.filter_by(id=user.army_id).delete()
        Infantry.query.filter_by(id=army.infantry_id)
        Fleet.query.filter_by(id=army.fleet_id)
        Airplanes.query.filter_by(id=army.airplanes_id)
        Tanks.query.filter_by(id=army.tanks_id)
        db.session.commit()
        p = Process(target=logger.info(f"User: {user.id} has deleted his account!"))
        return "User was deleted, if he exist", 200
