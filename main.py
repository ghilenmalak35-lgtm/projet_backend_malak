from fastapi import FastAPI
from user.user_controller import router
<<<<<<< HEAD

from client.client_controller import router

=======
from client.client_controller import router
>>>>>>> 940f4b47a49956917d60823dd0752fff28b2bcb4
from client.client_controller import routerclient
from catégorie.categorie_controller import router
from produit.produit_controller import router
from fournisseur.fournisseur_controller import router
from vent.vent_controller import router
from achat.achat_controller import router
<<<<<<< HEAD

=======
>>>>>>> 940f4b47a49956917d60823dd0752fff28b2bcb4
app = FastAPI()
app.include_router(router)
app.include_router(routerclient)