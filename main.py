import tweepy
import json
import os
from dotenv import load_dotenv
from datetime import datetime

# Cargar variables de entorno
load_dotenv()

class TwitterBasicStats:
    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.api_secret = os.getenv("API_SECRET")
        self.access_token = os.getenv("ACCESS_TOKEN")
        self.access_secret = os.getenv("ACCESS_SECRET")
        self.api = self._authenticate()

    def _authenticate(self):
        """Configurar autenticación de Twitter API"""
        try:
            auth = tweepy.OAuthHandler(self.api_key, self.api_secret)
            auth.set_access_token(self.access_token, self.access_secret)
            api = tweepy.API(auth)
            
            # Verificar credenciales
            me = api.verify_credentials()
            print("✅ Autenticación exitosa!")
            print(f"📱 Conectado como: @{me.screen_name}")
            print(f"👥 Followers count: {me.followers_count}")
            print(f"👤 Following count: {me.friends_count}")
            return api
        except tweepy.errors.Unauthorized:
            print("❌ Error: Credenciales inválidas")
            raise
        except Exception as e:
            print(f"❌ Error durante la autenticación: {str(e)}")
            raise

    def get_non_followers(self):
        """Encontrar usuarios que no te siguen de vuelta"""
        try:
            print("\n🔍 Analizando tu cuenta...")
            
            # Obtener IDs de las personas que sigues
            following_ids = set(self.api.get_friend_ids())
            print(f"👤 Sigues a {len(following_ids)} usuarios")
            
            # Obtener IDs de tus seguidores
            followers_ids = set(self.api.get_follower_ids())
            print(f"👥 Te siguen {len(followers_ids)} usuarios")
            
            # Encontrar los que no te siguen de vuelta
            non_followers_ids = following_ids - followers_ids
            
            # Convertir IDs a información de usuario
            non_followers = []
            for id_chunk in self._chunk_list(list(non_followers_ids), 100):
                users = self.api.lookup_users(user_id=id_chunk)
                for user in users:
                    non_followers.append({
                        'screen_name': user.screen_name,
                        'name': user.name,
                        'followers_count': user.followers_count,
                        'verified': user.verified
                    })
            
            # Guardar resultados
            self.save_results(non_followers)
            
            return non_followers
            
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return []

    def _chunk_list(self, lst, n):
        """Dividir lista en chunks de tamaño n"""
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

    def save_results(self, non_followers):
        """Guardar resultados en archivo JSON"""
        data = {
            "non_followers": non_followers,
            "last_updated": datetime.now().isoformat()
        }
        with open("non_followers.json", "w") as file:
            json.dump(data, file, indent=2)
        print("\n✅ Resultados guardados en non_followers.json")



    def get_user_stats(self):
        """Obtener estadísticas básicas del usuario"""
        try:
            me = self.api.verify_credentials()
            stats = {
                "username": me.screen_name,
                "name": me.name,
                "followers_count": me.followers_count,
                "following_count": me.friends_count,
                "tweets_count": me.statuses_count,
                "account_created": me.created_at.isoformat(),
                "verified": me.verified,
                "location": me.location,
                "description": me.description
            }
            
            # Guardar estadísticas
            self.save_stats(stats)
            
            return stats
            
        except Exception as e:
            print(f"❌ Error obteniendo estadísticas: {str(e)}")
            return None

    def save_stats(self, stats):
        """Guardar estadísticas con marca de tiempo"""
        data = {
            "stats": stats,
            "last_updated": datetime.now().isoformat()
        }
        with open("twitter_stats.json", "w") as file:
            json.dump(data, file, indent=2)
        print("\n✅ Estadísticas guardadas en twitter_stats.json")

def main():
    try:
        stats = TwitterBasicStats()
        user_stats = stats.get_user_stats()
        non_followers = stats.get_non_followers()

        print("\n📊 Resultados:")
        print("-" * 30)
        print(f"😢 {len(non_followers)} usuarios no te siguen de vuelta:")
        
        # Ordenar por número de seguidores
        non_followers.sort(key=lambda x: x['followers_count'], reverse=True)
        
        for user in non_followers:
            verified = "✓" if user['verified'] else " "
            print(f"@{user['screen_name']} {verified}")
            print(f"   Nombre: {user['name']}")
            print(f"   Seguidores: {user['followers_count']}")
            print("-" * 30)
            
    except Exception as e:
        print(f"❌ Error fatal: {str(e)}")

        if user_stats:
            print("\n📊 Estadísticas detalladas:")
            print("-" * 30)
            print(f"📝 Nombre: {user_stats['name']}")
            print(f"📱 Username: @{user_stats['username']}")
            print(f"👥 Seguidores: {user_stats['followers_count']}")
            print(f"👤 Siguiendo: {user_stats['following_count']}")
            print(f"🐦 Tweets totales: {user_stats['tweets_count']}")
            print(f"📍 Ubicación: {user_stats['location'] or 'No especificada'}")
            print(f"ℹ️ Bio: {user_stats['description'] or 'No especificada'}")
            
    except Exception as e:
        print(f"❌ Error fatal: {str(e)}")

if __name__ == "__main__":
    main()