#Обработчик запроса
def make_response(text):
    return{
        'response':{
            'text': text,
        },
        'version': '1.0',
    }

def welcome_message (event):
    text = ('Здравствуй!\
 У тебя плохое настроение? Что-то случилось в жизни? А, может, наоборот ничего не случилось, но что-то не то?\
 Без паники, я здесь, чтобы помочь!\
 Обращаю внимание на то, что этот навык не заменит вам психолога. Я смогу поддержать замотивировать, но не смогу оказать полноценную помощь.\
 Единый Российский номер доверия: 8 (800) 333-44-34\
 Как ты себя сегодня чувствуешь?')
    return make_response(text)


def mood_select (event):
    intent = event['request']['nlu']['intents']['mood_select']
    Mood = intent['slots']['Mood']['value']
    if Mood == 'mood_good':
        return make_response(text = ('Рада это слышать! Именно поэтому я приготовила для тебя один интересный факт. Хочешь послушать?'))
    elif Mood == 'mood_nah':
        return make_response(text = ('Расскажешь, что случилось?'))
    elif Mood == 'mood_bad':
        return make_response(text = ('Мне жаль. Что тебя сегодня так расстроило?'))
    else:
        return fallback(event) 


def bad_select (event):
    intent = event['request']['nlu']['intents']['bad_select']
    Bad = intent['slots']['Bad']['value']
    if Bad == 'studies':
        return make_response(text = ('Ты сейчас учишься в школе или в университете?'))
    elif Bad == 'work':
        return make_response(text=('Ты ищешь работу или уже работаешь?'))
    elif Bad == 'health':
        return make_response (text=('Ты уже обращался к врачу?'))
    else:
        return fallback(event)

#Накладывается с интентами согласия "да/нет" у school_ex, advie и fact
def st_place (event):
    intent = event['request']['nlu']['intents']['st_place']
    Place = intent['slots']['Place']['value']
    if Place == 'school':
        return make_response(text = ('Дай угадаю, ты пишешь ОГЭ/ЕГЭ в этом году, да?'))
    if Place == 'university':
        return make_response(text = ('Расскажешь, что тебя беспокоит?'))

def school_ex (event):
    intent = event['request']['nlu']['intents']['school_ex']
    Exams_School = intent['slots']['Exams_School']['value']
    if Exams_School == 'Yes_Ex':
        return make_response(text = ('Да, выпускные экзамены заставляют сильно волноваться. Давай я помогу тебе различными советами по подготовке?'))
    if Exams_School == 'No_Ex':
        return make_response(text = ('Прости, не угадала. Расскажешь, что тебя беспокоит?'))

def advice (event):
    intent = event['request']['nlu']['intents']['advice']
    Exams = intent['slots']['Exams']['value']
    if Exams == 'Yes_Adv':
        return make_response(text = ('Сейчас тебе приходится нелегко, я понимаю. Ты сейчас сильно перегружен, но себе нужно давать время на отдых. Попробуй заниматься час, а потом давать себе перерыв на 20 минут. Это будет полезно и для тебя, и для твоего мозга, который не может постоянно запоминать информацию. Этого перерыва хватит, чтобы новая информация немного уложилась в голове. Хочешь ещё совет?'))
    if Exams == 'No_Adv':
        return make_response(text = ('Если хочешь завершить разговор, просто скажи "Хватит"'))

def fact (event):
    intent = event['request']['nlu']['intents']['fact']
    Good_Fact = intent['slots']['Good_Fact']['value']
    if Exams == 'Yes_Fact':
        return make_response(text = ('Мы все состоим из атомов, которым уже миллиарды лет, и у каждого из них своя уникальная история. После нас они никуда не денутся, а станут частью кого-то другого и будут существовать до конца времени. Таким образом мы все — часть чего-то невероятного и вечного. Существует даже очень-очень крошечный шанс, что наша ДНК когда-то воспроизведется — и это будем мы, но с новой памятью и историей. Рассказать ещё что-нибудь?'))
    if Exams == 'No_Fact':
        return make_response(text = ('Если хочешь завершить разговор, просто скажи "Хватит"'))

#Чисто концовочка и ошибки
def fallback(event):
        return make_response('Прошу прощения, я не разобрала ваш ответ. Повторите, пожалуйста')

def end(event):
    text = ('Хорошего тебе дня. До скорого!')
    return make_response(text)

#Обработчик интентов    
def handler (event, context):
    intents = event['request'].get('nlu',{}).get('intents')
    if event['session']['new']:
       return welcome_message(event)
    elif 'mood_select' in intents:
        return mood_select(event)
    elif 'bad_select' in intents:
       return bad_select(event)
    elif 'st_place' in intents:
       return st_place(event)
    elif 'school_ex' in intents:
       return school_ex(event)
    elif 'advice' in intents:
        return advice (event)
    elif 'fact' in intents:
        return fact (event)
    else:
        return fallback(event)   
    return {
        'response': {
           'text': text,
        },
        'version': '1.0',
    }
