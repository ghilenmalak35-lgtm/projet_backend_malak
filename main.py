from fastapi import FastAPI
from user.user_controller import router
from client.client_controller import router
from catégorie.categorie_controller import router
from fournisseur.fournisseur_controller import router
from vent.vent_controller import router
app = FastAPI()
app.include_router(router)