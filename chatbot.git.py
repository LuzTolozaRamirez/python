from chatterbot import chatterbot
chatbot = chatbot (
	"Universidad del Cauca",
	trainer ="chatterbot.trainers.chatterbotCorpustrainer"
	)
	chatbot.train(
		"chatterbot.Corpus.spanish")
	while True:
		usuario = input (">>>")
		respuesta = chatbot.get_response(usuario)
		print ("BOT:"+str(respuesta))