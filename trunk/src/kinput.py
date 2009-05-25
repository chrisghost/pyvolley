# coding=UTF-8
from PySFML import sf

class kInput:
    """
    Gère l'ajout/supression/traitement des évenements 
    d'entrées utilisateur/système.
 
    Stockage de la forme
    event[type][key] = (fonction, argument)
    """
    def __init__(self, display):
        self.input = display.GetInput() #Lien à une instance window
        self.get_events = display.GetEvent #Référence pour réduire le parcours du code.
        self.event = sf.Event() #Création de l'instance chargées de gérer les évènements
 
        self.fonctions = {}
        '''
        self.fonctions[sf.Event.KeyReleased] = {}
        self.fonctions[sf.Event.KeyPressed] = {}
        self.fonctions[sf.Event.MouseButtonPressed] = {}
        self.fonctions[sf.Event.MouseButtonReleased] = {}
        self.fonctions[sf.Event.JoyButtonPressed] = {}
        self.fonctions[sf.Event.JoyButtonReleased] = {}
        self.fonctions[sf.Event.JoyMoved] = {}
        '''
 
    def AddEvent(self, type, key, fonction, argument):
        """
        AddEvent(self, type, key, fonction, argument)
        prépare le moteur à exécuter la [fonction]([argument]) pour l'évènement
        de type [type] et de touche [key].
        """
        if not self.fonctions.has_key(type):
            self.fonctions[type] = {}
        self.fonctions[type][key] = (fonction, argument)
 
    def DelEvent(self, type, key):
        """
        DelEvent(self, type, key)
        Supprime l'écoute de l'évènement [type][key]
        """
        self.fonctions[type].pop(key)


    def Scan(self):
        """
        Inspecte les entrées pour exécuter les évènements mémorisés. 
        A appeler à chaque tour de boucle.
        """
        event = self.event      #Allège le parcours
        fonc = self.fonctions
 
        while self.get_events(event):
 
            if fonc.has_key(event.Type):
                code = None
                #=== Récuperation du code ===
                if event.Type == sf.Event.KeyReleased or event.Type == sf.Event.KeyPressed:
                    code = event.Key.Code
                elif event.Type == sf.Event.MouseButtonPressed or event.Type == sf.Event.MouseButtonReleased:
                    code = event.MouseButton.Button
                elif event.Type == sf.Event.JoyButtonPressed or event.Type == sf.Event.JoyButtonReleased:
                    code = sf.Event.JoyButton.Button
                elif event.Type == sf.Event.JoyMoved:
                    code = event.JoyMove.Axis
 
                #=== Execution de la bonne fonction ===
                if fonc[event.Type].has_key(code):
			arguments = []
			for sub in fonc[event.Type][code][1]:
				if sub == "_Mouse_X":
					arguments.append(event.MouseButton.X)
				elif sub == "_Mouse_Y":
					arguments.append(event.MouseButton.Y)
				else:
					arguments.append(sub)

			arguments[-1] = " "
			fonc[event.Type][code][0](arguments)

"""
 
    def Scan(self):
        event = self.event
        fonc = self.fonctions
        code = None
 
        while self.get_events(event):
            code = None
 
            if event.Type == sf.Event.KeyReleased or event.Type == sf.Event.KeyPressed:
                code = event.Key.Code
            elif event.Type == sf.Event.MouseButtonPressed or event.Type == sf.Event.MouseButtonReleased:
                code = event.MouseButton.Button
            elif event.Type == sf.Event.JoyButtonPressed or event.Type == sf.Event.JoyButtonReleased:
                code = event.JoyButton.Button
            elif event.Type == sf.Event.JoyMoved:
                code = event.JoyMove.Axis
	if code != None :
		print "code!=none"
		if len(self.fonctions.get(event.Type)) :
			print "len"
			if code in self.fonctions.get(event.Type):
				print "code in"
				print self.fonctions[event.Type][code][0], self.fonctions[event.Type][code][1]
    	    	       		self.fonctions[event.Type][code][0](event, self.fonctions[event.Type][code][1])

"""
