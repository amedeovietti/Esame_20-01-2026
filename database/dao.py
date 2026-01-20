from database.DB_connect import DBConnect
from model.artist import Artist

class DAO:

    @staticmethod
    def get_all_artists():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT *
                FROM artist a
                """
        cursor.execute(query)
        for row in cursor:
            artist = Artist(id=row['id'], name=row['name'])
            result.append(artist)
        cursor.close()
        conn.close()
        return result


    @staticmethod
    def leggiNumeroAlbum(id_artista):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ SELECT COUNT(*)
                    FROM album a
                    WHERE a.artist_id = %s """      # numero di album fatti da un determinato artista con id (nell'esempio id_artista = 90)
        cursor.execute(query, (id_artista,))
        for row in cursor:
            result.append(row['COUNT(*)'])
        cursor.close()
        conn.close()
        n_album = result[0]
        return n_album


    @staticmethod
    def leggiAlbum(id_artista):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ SELECT id 
                    FROM album a 
                    WHERE a.artist_id = %s """
        cursor.execute(query, (id_artista,))
        for row in cursor:
            result.append(row['id'])
        cursor.close()
        conn.close()
        return result


    @staticmethod
    def leggiCanzoni(id_album):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ SELECT DISTINCT genre_id 
                    FROM track t 
                    WHERE t.album_id = %s """
        cursor.execute(query, (id_album,))
        for row in cursor:
            result.append(row['genre_id'])
        cursor.close()
        conn.close()
        return result


    @staticmethod
    def leggiGeneri(a_name):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ SELECT DISTINCT genre_id
                    FROM track t
                    WHERE t.composer = %s """
        cursor.execute(query, (a_name,))
        for row in cursor:
            result.append(row['genre_id'])
        cursor.close()
        conn.close()
        return result

