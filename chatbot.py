from chatterbot import ChatBot #importamos la libreria de chatterbot

chatbot = ChatBot(
    "UNIVERSIDAD DEL CAUCA"),
    

    storage_adapter='chatterbot.storage.MongoDatabaseAdapter', #utilizamos la base de datos de mongodb
    database_uri='mongodb://localhost:27017/', #damos la configuración para el acceso al storage
    database='chatterbot_unicauca',
    
    input_adapter="chatterbot.input.TerminalAdapter", #entrada y salida 
    
    output_adapter="chatterbot.output.OutputAdapter", #generamos  configuraciónes para saber que información  hay en el imput y que respuesta dar
    output_format="text",

    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch", #lo que se encuentre mas razonable
            "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
            "response_selection_method": "chatterbot.response_selection.get_most_frequent_response"
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.51, # si lo encontrado no es mayor a este porcentaje  se dará una respuesta evasiba.
            'default_response': 'Disculpa, no te he entendido bien, solo te puedo ayudar en temas de la universidad ¿Puedes ser más específico?.'
        },
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter', # pregunta concreta.
            'input_text': 'Quiero realizar una inscripción',
            'output_text': 'Puedes realizarla ahora en: https://www.unicauca.edu.co/matriculas/'
        },
    ],
    
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace' # limpia los resultados anteriores --
    ],
    
    read_only=False, # dejar  que aprenda a medida que hacen pregutnas
)
DEFAULT_SESSION_ID = chatbot.default_session.id


from chatterbot.trainers import ChatterBotCorpusTrainer # base de datos con preugntas y respuestas frecuentes para entreno

chatbot.set_trainer(ChatterBotCorpusTrainer)
chatbot.train("./estudiante.txt")

while True: # muestre un campo de texto  para hacer alguna pregunta para que el bot de una respuesta
    input_statement = chatbot.input.process_input_statement()
    statement, response = chatbot.generate_response(input_statement, DEFAULT_SESSION_ID)
    print("\n%s\n\n" % response)