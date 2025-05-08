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


import os
os.environ["ALLOWED_HOSTS"] = "feedback-systeme.onrender.com,www.feedback-systeme.onrender.com,127.0.0.1,localhost"
print([host.strip() for host in os.environ.get("ALLOWED_HOSTS", "").split(",") if host.strip()])