from app import create_app, db
from app.models import User

# Création de l'application Flask
app = create_app()

with app.app_context():
    # Création des tables dans la base de données
    db.create_all()
    print("✅ Base de données initialisée.")

    # Création de l'utilisateur admin s'il n'existe pas
    if not User.query.filter_by(username='admin').first():
        admin = User(
            nom_complet='Admin Principal',
            username='admin',
            email='admin@example.com',
            role='chef'
        )
        admin.set_password('admin123')
        db.session.add(admin)
        print("👤 Utilisateur admin créé.")

    else:
        print("ℹ️ L'utilisateur admin existe déjà.")

    # Création d'un responsable s'il n'existe pas
    if not User.query.filter_by(username='responsable1').first():
        responsable = User(
            nom_complet="Responsable Alpha",
            username="responsable1",
            email="responsable1@example.com",
            role="responsable"
        )
        responsable.set_password("motdepasse123")
        db.session.add(responsable)
        print("👤 Responsable ajouté.")
    else:
        print("ℹ️ Le responsable existe déjà.")

    # Enregistrement des modifications
    db.session.commit()
    print("✅ Données sauvegardées.")
