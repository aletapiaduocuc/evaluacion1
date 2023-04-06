#Grupo 8: Tapia Toledo Lopez

#Se importan las librerias
import json
import yaml
#Se establece instrucción de apertura para myfilejson
with open('myfile.json','r') as json_file:
    ourjson = json.load(json_file)
#Posterior a llamar la variable ourjson con metodo json.load
#Se imprime la variable con el metodo cargado
print(ourjson)

#Impresión valor token y tiempo de expiración
print("The access token is: {}".format(ourjson['access_token']))
print("The token expires in {} seconds.".format(ourjson['expires_in']))

#Se imprime output JSON en formato YAML
print("\n\n---")
print(yaml.dump(ourjson))
