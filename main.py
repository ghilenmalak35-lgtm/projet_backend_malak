from fastapi import FastAPI
from user.user_controller import router
<<<<<<< HEAD
from client.client_controller import router
=======
from client.client_controller import routerclient
from catégorie.categorie_controller import router
from produit.produit_controller import router
from fournisseur.fournisseur_controller import router
from vent.vent_controller import router
from achat.achat_controller import router
>>>>>>> 4d65fae4acc8cc295b743cce98ac8e009772f744
app = FastAPI()
app.include_router(router)
app.include_router(routerclient)