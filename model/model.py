import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._artists_list = []
        self.load_all_artists()
        self.dict_generi = {}  # creo un dizionario in cui a ogni artista DEL GRAFO sono associati i suoi generi

    def load_all_artists(self):
        self._artists_list = DAO.get_all_artists()
        print(f"Artisti: {self._artists_list}")





    def build_graph(self, min_albums):
        if self._artists_list is not None:
            for a in self._artists_list:
                a_album = DAO.leggiNumeroAlbum(a.id)
                if a_album >= min_albums:
                    self._graph.add_node(a)

        for a in self._graph.nodes:
            album_di_a = DAO.leggiAlbum(a.id)
            generi_di_a = []
            for album in album_di_a:
                genere_album = DAO.leggiCanzoni(album)
                for g in genere_album:
                    generi_di_a.append(g)
            self.dict_generi[a] = generi_di_a

        for a1 in self._graph.nodes:
            for a2 in self._graph.nodes:
                if a1 != a2:
                    peso = 0
                    for g1 in self.dict_generi[a1]:
                        for g2 in self.dict_generi[a2]:
                            if g1 == g2:
                                peso += 1
                    if peso != 0:
                        self._graph.add_edge(a1, a2, weight=peso)


    def get_connessi(self, id_artista):
        for node in self._graph.nodes:
            if id_artista == node.id:
                return nx.node_connected_component(self._graph, node)            # l'output è un set di nodi connessi {artista1, artista2, ...}

            """
            for c in connessi:
                id = c.id
                name = c.name
                peso = self._graph[artista][id]['weight']                           # peso dell'arco come nodi artista e il nodo connesso

"""