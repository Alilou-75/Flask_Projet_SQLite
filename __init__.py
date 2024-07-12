from flask import Flask, render_template_string, render_template, jsonify, request, redirect, url_for, session, flash
from flask import render_template
from flask import json
from urllib.request import urlopen
from werkzeug.utils import secure_filename
import sqlite3
from datetime import datetime

app = Flask(__name__)                                                                                                                  
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # Clé secrète pour les sessions

# Fonction pour créer une clé "authentifie" dans la session utilisateur
def est_authentifie():
    return session.get('authentifie')
    
# Ajout d'une route pour acceder à la page d'accueil serveur:
# ===========================================================
@app.route('/')
def hello_world():
    return render_template('hello.html')
    
# Route pour afficher la tempirature à Paris:
# ==========================================
@app.route('/graphique')
def températures():
    return render_template('graphique.html')
    
# Route pour acceder à la base de données avec authentification:
# ==============================================================
@app.route('/lecture')
def lecture():
    if not est_authentifie():
        # Rediriger vers la page d'authentification si l'utilisateur n'est pas authentifié
        return redirect(url_for('authentification'))

  # Si l'utilisateur est authentifié
    return "<h2>Bravo, vous êtes authentifié</h2>"

@app.route('/authentification', methods=['GET', 'POST'])
def authentification():
    if request.method == 'POST':
        # Vérifier les identifiants
        if request.form['username'] == 'Ali' and request.form['password'] == '12345': # password à cacher par la suite
            session['authentifie'] = True
            # Rediriger vers la route lecture après une authentification réussie
            return redirect(url_for('lecture'))
        else:
            # Afficher un message d'erreur si les identifiants sont incorrects
            return render_template('formulaire_authentification.html', error=True)

    return render_template('formulaire_authentification.html', error=False)
    
#================================================( Base de données Clients )============================================================

# Ajout d'une route pour consulter la liste des Clients
# =====================================================
@app.route('/consultation/')
def ReadBDD():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients;')
    clients = cursor.fetchall()
    conn.close()
    return render_template('read_data.html', clients=clients)

# Selectionner un client par son Numero:
# =====================================
@app.route('/fiche_client/<int:client_id>')
def Readfiche(client_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients WHERE id = ?', (client_id,))
    clients = cursor.fetchall()
    conn.close()
    # Rendre le template HTML et transmettre les données
    return render_template('read_data.html', clients=clients)
    
 # Selectionner un client par son Nom:
 # ==================================

@app.route('/fiche_nom_client/<string:nom>')
def Readfiche1(nom):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients WHERE nom = ?', (nom,))
    clients = cursor.fetchall()
    conn.close()
    # Rendre le template HTML et transmettre les données
    return render_template('read_data.html', clients=clients)

 # Formulaire d'enregistrement d'un client:
 # =======================================
@app.route('/enregistrer_client', methods=['GET'])
def formulaire_client():
    return render_template('formulaire.html')  # afficher le formulaire

@app.route('/enregistrer_client', methods=['POST'])
def enregistrer_client():
    nom = request.form['nom']
    prenom = request.form['prenom']
    adresse = request.form['adresse']
    # Connexion à la base de données
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Exécution de la requête SQL pour insérer un nouveau client
    cursor.execute('INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)', (nom, prenom, adresse))
    conn.commit()
    conn.close()
    return redirect('/consultation/')  # Rediriger vers la page d'accueil après l'enregistrement
                                                                                                                                       
if __name__ == "__main__":
  app.run(debug=True)
    
# Route pour suppression d'un client par son Numero:
#==================================================
@app.route('/delete_client/<int:client_id>', methods=['POST'])
def delete_client(client_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM clients WHERE id = ?', (client_id,))
    conn.commit()
    conn.close()
    flash('Client supprimé avec succès')
    return redirect('/consultation/')

if __name__ == "__main__":
    app.run(debug=True)

# Route pour chercher un Client:
 # =============================
@app.route('/search_clients', methods=['GET'])
def search_clients():
    query = request.args.get('query')
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
         SELECT * FROM clients 
        WHERE (nom LIKE ? OR prenom LIKE ?)
    ''', ('%' + query + '%', '%' + query + '%'))
    clients = cursor.fetchall()
    conn.close()
    return render_template('read_data.html', clients=clients)
    
#================================================( Projet de Bibliothèque )============================================================

# Connexion à la base de données
def get_db_connection():
    conn = sqlite3.connect('database2.db')
    conn.row_factory = sqlite3.Row
    return conn

 # Consulter la liste des Livres:
 # ==============================
@app.route('/livres/')
def ReadBDD2():
    conn = sqlite3.connect('database2.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Livres;')
    data = cursor.fetchall()
    conn.close()
    return render_template('read_data2.html', data=data)

# Selectionner un livre par son Numero:
# =====================================
@app.route('/fiche_livre/<int:ID_livre>')
def Readfiche2(post_ID_livre):
    conn = sqlite3.connect('database2.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livres WHERE ID_livre = ?', (ID_livre,))
    data = cursor.fetchall()
    conn.close()
    # Rendre le template HTML et transmettre les données
    return render_template('read_data2.html', data=data)
    
 # Selectionner un livre par son Nom:
 # ==================================

@app.route('/fiche_Titre_livre/<string:titre>')
def Readfiche3(titre):
    conn = sqlite3.connect('database2.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livres WHERE titre = ?', (titre,))
    data = cursor.fetchall()
    conn.close()
    # Rendre le template HTML et transmettre les données
    return render_template('read_data2.html', data=data)


 # Formulaire d'enregistrement d'un livre:
 # =======================================

@app.route('/enregistrer_livre', methods=['GET', 'POST'])
def enregistrer_livre():
    if request.method == 'POST':
        titre = request.form['titre']
        auteur = request.form['auteur']
        annee_publication = request.form['annee_publication']
        quantite = request.form['quantite']
        
        # Connexion à la base de données
        conn = sqlite3.connect('database2.db')
        cursor = conn.cursor()

        # Exécution de la requête SQL pour insérer un nouveau livre
        cursor.execute("INSERT INTO livres (titre, auteur, annee_publication, quantite) VALUES (?, ?, ?, ?)", (titre, auteur, annee_publication, quantite))
        conn.commit()
        conn.close()
        flash('Livre enregistré avec succès')
        return redirect('/livres/') # Rediriger vers la page d'accueil après l'enregistrement
    return render_template('formulaire2.html')                                                                                                          
    
# Route pour suppression d'un livre par son Numero:
#=================================================

@app.route('/delete_livre/<int:ID_livre>', methods=['POST'])
def delete_livre(ID_livre):
    conn = sqlite3.connect('database2.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM livres WHERE ID_livre = ?', (ID_livre,))
    conn.commit()
    conn.close()
    flash('Livre supprimé avec succès')
    return redirect('/livres/')

 # Route pour chercher un Livre:
 # =============================
@app.route('/search_livres', methods=['GET'])
def search_livres():
    query = request.args.get('query')
    conn = sqlite3.connect('database2.db')
    cursor = conn.cursor()
    cursor.execute('''
         SELECT * FROM livres 
        WHERE (titre LIKE ? OR auteur LIKE ?) AND quantite > 0
    ''', ('%' + query + '%', '%' + query + '%'))
    data = cursor.fetchall()
    conn.close()
    return render_template('read_data2.html', data=data)
    
# Route pour afficher les livres disponibles:
#============================================

@app.route('/livres_disponibles/')
def livres_disponibles():
    conn = sqlite3.connect('database2.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livres WHERE quantite > 0')
    livres = cursor.fetchall()
    conn.close()
    return render_template('livres_disponibles.html', livres=livres)

#Route pour emprunter un livre:
#==============================
@app.route('/emprunter_livre/<int:ID_livre>', methods=['POST'])
def emprunter_livre(ID_livre):
    ID_user = request.form['ID_user']
    date_emprunt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    Date_retour_prevue = request.form['Date_retour_prevue']
    conn = sqlite3.connect('database2.db')
    cursor = conn.cursor()

    # Vérifier la quantité disponible
    cursor.execute('SELECT quantite FROM livres WHERE ID_livre = ?', (ID_livre,))
    quantite = cursor.fetchone()[0]

    if quantite > 0:
        # Insérer l'emprunt
        cursor.execute('''
            INSERT INTO emprunts (ID_user, ID_livre, date_emprunt, Date_retour_prevue) 
            VALUES (?, ?, ?, ?)
        ''', (ID_user, ID_livre, date_emprunt, Date_retour_prevue))

        # Mettre à jour la quantité du livre
        cursor.execute('UPDATE livres SET quantite = quantite - 1 WHERE ID_livre = ?', (ID_livre,))
        conn.commit()
    conn.close()
    return "Livre emprunté avec succès"
    return redirect('/livres_disponibles')
    
# Route pour consulter la liste des livres empruntés:
# ==================================================
@app.route('/livres_empruntés/')
def ReadBDDEm():
    conn = sqlite3.connect('database2.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Emprunts;')
    data = cursor.fetchall()
    conn.close()
    return render_template('livres_empruntés.html', data=data)


# Route pour Checher les Livres à emprunter:
# ==========================================
@app.route('/search_emprunts', methods=['GET'])
def search_emprunts():
    query = request.args.get('query')
    conn = sqlite3.connect('database2.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM livres 
        WHERE (titre LIKE ? OR auteur LIKE ?) AND quantite > 0
    ''', ('%' + query + '%', '%' + query + '%'))
    livres = cursor.fetchall()
    conn.close()
    return render_template('livres_disponibles.html', livres=livres)

# Route pour afficher le formulaire de retour:
#============================================
@app.route('/retourner_livre/')
def retourner_livre():
    conn = sqlite3.connect('database2.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Emprunts;')
    data = cursor.fetchall()
    conn.close()
    return render_template('retourner_livre.html', data=data)

# Route pour gérer le processus de retour:
#=========================================
@app.route('/confirmer_retour/<int:ID_livre>', methods=['POST'])
def confirmer_retour(ID_livre):
    ID_user = request.form['ID_user']
    Date_retour_effective = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    conn = sqlite3.connect('database2.db')
    cursor = conn.cursor()

    cursor.execute('UPDATE emprunts SET Date_retour_effective = ? WHERE ID_livre = ? AND ID_user = ? AND Date_retour_effective IS NULL', (Date_retour_effective, ID_livre, ID_user))
    cursor.execute('UPDATE livres SET quantite = quantite + 1 WHERE ID_livre = ?', (ID_livre,))
    conn.commit()
    conn.close()
    flash('Livre retourné avec succès')
    return redirect('/livres_disponibles')




#==============================( La gestion des utilisateurs )===============================

 # Formulaire d'enregistrement d'un utilisateur:
 # =============================================

@app.route('/enregistrer_user', methods=['GET', 'POST'])
def enregistrer_user():
    if request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        adresse = request.form['adresse']
        
        conn = sqlite3.connect('database2.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO utilisateurs (nom, prenom, adresse) VALUES (?, ?, ?)", (nom, prenom, adresse))
        conn.commit()
        conn.close()
        flash('Utilisateur enregistré avec succès')
        return redirect('/utilisateurs/')
    return render_template('formulaire_user.html')
                                                                                                                                          
# Route pour consulter la liste des utilisateurs:
# ===============================================
@app.route('/utilisateurs/')
def ReadBDDu():
    conn = sqlite3.connect('database2.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM utilisateurs;')
    data = cursor.fetchall()
    conn.close()
    return render_template('read_data_user.html', data=data)

# Route pour suppression un utilisateur:
#=======================================
# Formulaire de suppression d'un utilisateur avec mot de passe
@app.route('/delete_user/<int:ID_user>', methods=['GET', 'POST'])
def delete_user(ID_user):
    return render_template('delete_user.html', ID_user=ID_user)

@app.route('/confirm_delete_user/<int:ID_user>', methods=['POST'])
def confirm_delete_user(ID_user):
    password = request.form['password']
    admin_password = "admin_secret_password"  # You should store this securely, not in plain text

    if password == admin_password:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM utilisateurs WHERE ID_user = ?', (ID_user,))
        conn.commit()
        conn.close()
        flash('Utilisateur supprimé avec succès')
    else:
        flash('Mot de passe incorrect')
    
    return redirect('/utilisateurs/')

if __name__ == "__main__":
    app.run(debug=True)

 # Route pour chercher un utilisateur:
 # ===================================
@app.route('/search_users', methods=['GET'])
def search_users():
    query = request.args.get('query')
    conn = sqlite3.connect('database2.db')
    cursor = conn.cursor()
    cursor.execute('''
         SELECT * FROM utilisateurs 
        WHERE (Nom LIKE ? OR Prenom LIKE ?) 
    ''', ('%' + query + '%', '%' + query + '%'))
    data = cursor.fetchall()
    conn.close()
    return render_template('read_data_user.html', data=data)
    









