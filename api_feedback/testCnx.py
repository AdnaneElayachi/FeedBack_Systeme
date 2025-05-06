# import psycopg2

# try:
#     conn = psycopg2.connect(
#         dbname="postgres",
#         user="postgres",
#         password="post123456",
#         host="prod-ca-2021.crt",
#         port="5432",
#         sslmode="require",
#         sslrootcert="supabase-ca.pem"  # Assurez-vous que le fichier est dans le projet
#     )
#     print("✅ Connexion réussie !")
# except Exception as e:
#     print(f"❌ Erreur : {e}")