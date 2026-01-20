import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_create_graph(self, e):
        try:
            n_album = int(self._view.txtNumAlbumMin.value)
            print(n_album)
            if n_album > 0:
                self._model.build_graph(n_album)
                self._view.txt_result.controls.clear()
                self._view.txt_result.controls.append(ft.Text(f"Grafo creato: {self._model._graph.number_of_nodes()} nodi (artisti), {self._model._graph.number_of_edges()} archi"))
                self._view.ddArtist.disabled = False
                self._view.btnArtistsConnected.disabled = False
                self._view._page.update()
                self._view.ddArtist.options.clear()
                for n in self._model._graph.nodes():
                    self._view.ddArtist.options.append(ft.dropdown.Option(key = n.id, text = n.name))
                self._view.ddArtist.update()
        except ValueError:
            self._view.show_alert("Non è stato inserito un numero intero")


    def handle_connected_artists(self, e):
        id_artista = self._view.ddArtist.value
        connessi = self._model.get_connessi(int(id_artista))
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Artisti direttamente collegati all'artista {id_artista}:"))
        for c in connessi:
            self._view.txt_result.controls.append(ft.Text(f"{c} - Numero di generi in comune:"))
        self._view._page.update()


        """
        dati i nodi c (iterando su connessi) e il nodo il cui id è id_arista
        dal grafo prendo [c][node]["weight"] (il peso) e lo stampo"""
