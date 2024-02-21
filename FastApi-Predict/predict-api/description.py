descriptions = """
L'API vous aide à faire des choses géniales. 🚀


## Endpoints

Vous pourrez:

* **Hello world (without params)**: Ce endpoint renvoie un simple message de bienvenue. Il ne nécessite aucun paramètre.

* **Hello world (with params)**: Ce endpoint renvoie un message de bienvenue personnalisé. Cela nécessite un paramètre 'name' dans la requête.

* **Predictions**: Ce endpoint renvoie une prédiction effectuée par le modèle d'apprentissage automatique « model_1.pkl ». Il nécessite un objet « Crédit » en entrée.

* **Predictions 2**: Ce endpoint renvoie une prédiction effectuée par le modèle d'apprentissage automatique « model_2.pkl ». Il nécessite un objet 'Credit2' en entrée.

## Models

Vous pouvez utiliser les modèles suivants pour effectuer des prédictions:

* **Model 1**: Ce modèle est utilisé pour effectuer des prédictions dans le point de terminaison « Prédictions ». Il attend un objet « Crédit » en entrée et renvoie une prédiction en sortie.

* **Model 2**: Ce modèle est utilisé pour effectuer des prédictions dans le point de terminaison « Prédictions 2 ». Il attend un objet 'Credit2' en entrée et renvoie une prédiction en sortie.

Chargement des modèles : 

Deux modèles de machine learning, 'model_1.pkl' et 'model_2.pkl', sont chargés à l'aide de la bibliothèque pickle.

## Data Types

* **Credit**: Il s'agit d'un modèle Pydantic utilisé comme entrée pour le endpoint « Prédictions ».

* **Credit2**: Il s'agit d'un modèle Pydantic utilisé comme entrée pour le endpoint « Predictions 2 ». 
"""