from pyrogram import Client, filters,utils, enums
api_id=21155047
api_hash="52bf758193e332633cdec7be92949dee"
app = Client("my_account",api_id=api_id,api_hash=api_hash)

def get_peer_type_new(peer_id: int) -> str:
    peer_id_str = str(peer_id)
    if not peer_id_str.startswith("-"):
        return "user"
    elif peer_id_str.startswith("-100"):
        return "channel"
    else:
        return "chat"

utils.get_peer_type = get_peer_type_new

#Ответ на личные сообщения

# @app.on_message(filters.private)
# async def hello(client, message):
#     await message.reply("sorry")
# app.run()


#Отправить сообщение

# async def main():
#     async with app:
#         await app.send_message(-1001806154571, "Hi!") // беседа оверласт
# app.run(main())


# Отправка сообщений 

#https://docs.google.com/spreadsheets/d/1C0H9RSnGnepJp8FrMoZfVt013I0G1m2Ah8IlrhkM06A/edit?gid=0#gid=0 #old
#https://docs.google.com/spreadsheets/d/1hs5JDcjtI3KaMJYaUKM22ztIXBNpfzfl-YsX67iM4lg/edit?gid=0#gid=0 #new
@app.on_message()
async def my_handler(client, message):
    # if message.chat.id==468415265:#личка
    if message.chat.id==-1001186867179: # Беседа алевкурпа
        if "https://docs.google.com/spreadsheets/d/" in message.text:
            link = message.text.strip("edit?gid=0#gid=0")
            link +="edit?gid=1571222038#gid=1571222038"
            
            # await app.send_message("me",            link                    ,disable_notification = True,disable_web_page_preview = True) # беседа ОСП
            # await app.send_message("me","Вторник\n"+link+"&range=A77:A141"  ,disable_notification = True,disable_web_page_preview = True)  #Вторник
            # await app.send_message("me","Среда  \n"+link+"&range=A150:A213" ,disable_notification = True,disable_web_page_preview = True) #Среда
            # await app.send_message("me","Четверг\n"+link+"&range=A223:A289" ,disable_notification = True,disable_web_page_preview = True) #Четверг
            # await app.send_message("me","Пятница\n"+link+"&range=A296:A357" ,disable_notification = True,disable_web_page_preview = True) #Пятница
            await app.send_message(-4210146983,            link                    ,disable_notification = True,disable_web_page_preview = True) # беседа ОСП
            await app.send_message(-4210146983,"Вторник\n"+link+"&range=A77:A141"  ,disable_notification = True,disable_web_page_preview = True)  #Вторник
            await app.send_message(-4210146983,"Среда\n"+  link+"&range=A150:A213" ,disable_notification = True,disable_web_page_preview = True) #Среда
            await app.send_message(-4210146983,"Четверг\n"+link+"&range=A223:A289" ,disable_notification = True,disable_web_page_preview = True) #Четверг
            await app.send_message(-4210146983,"Пятница\n"+link+"&range=A296:A357" ,disable_notification = True,disable_web_page_preview = True) #Пятница
    if message.chat.id==881098702: # Вася
        print(message)
        if "тест" in message.text.lower() :
                await app.send_message(message.chat.id,"ТЫСТЕ")
        if message.from_user.id==881098702: # Вася
            
            if message.media == enums.MessageMediaType.PHOTO:
                await app.send_reaction(message.chat.id, message.id, "🤣")
            if message.media == enums.MessageMediaType.VIDEO:
                await app.send_reaction(message.chat.id, message.id, "🔥")
            if message.media == enums.MessageMediaType.STICKER:
                await app.send_reaction(message.chat.id, message.id, "🥱")
            if message.media == enums.MessageMediaType.VOICE:
                await app.send_reaction(message.chat.id, message.id, "🙉")
            if message.media == enums.MessageMediaType.VIDEO_NOTE:
                await app.send_reaction(message.chat.id, message.id, "🙈")
            if "ты" in message.text.lower() :
                await app.send_message(message.chat.id,"нет, ты")
            if "чмо" in message.text.lower() :
                await app.send_message(message.chat.id,"сам чмо")
            if "тварь" in message.text.lower() :
                await app.send_message(message.chat.id,"сам тварь БЕБЕБЕБЕБЕБЕ")
            if "кек" in message.text.lower() :
                await app.send_message(message.chat.id,"типа выпал? или просто кек?")
            if "го" in message.text.lower() :
                await app.send_message(message.chat.id,"ну го")
            if "дебил" in message.text.lower() :
                await app.send_sticker(message.chat.id,"CAACAgIAAxkBAAEE75ZnXDeIH55_Biu5ghrfekft6qY4TQAC2TsAApO0uEsAAYvgidtGdX0eBA")


app.run()

