from flask import Flask, render_template_string, render_template, jsonify, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask import json
from urllib.request import urlopen
from werkzeug.utils import secure_filename
import sqlite3

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

# Ajout d'une route pour consulter la liste des Clients
# =====================================================
@app.route('/consultation/')
def ReadBDD():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients;')
    data = cursor.fetchall()
    conn.close()
    return render_template('read_data.html', data=data)

# Selectionner un client par son Numero:
# =====================================
@app.route('/fiche_client/<int:post_id>')
def Readfiche(post_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients WHERE id = ?', (post_id,))
    data = cursor.fetchall()
    conn.close()
    # Rendre le template HTML et transmettre les données
    return render_template('read_data.html', data=data)
    
 # Selectionner un client par son Nom:
 # ==================================

@app.route('/fiche_nom_client/<string:nom>')
def Readfiche1(nom):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients WHERE nom = ?', (nom,))
    data = cursor.fetchall()
    conn.close()
    # Rendre le template HTML et transmettre les données
    return render_template('read_data.html', data=data)

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
@app.route('/fiche_livre/<int:post_ID_livre>')
def Readfiche2(post_ID_livre):
    conn = sqlite3.connect('database2.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livres WHERE ID_livre = ?', (post_ID_livre,))
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
@app.route('/enregistrer_livre', methods=['GET'])
def formulaire_livre():
    return render_template('formulaire2.html')  # afficher le formulaire

@app.route('/enregistrer_livre', methods=['POST'])
def enregistrer_livre():
    titre = request.form['titre']
    auteur = request.form['auteur']
    annee_publication = request.form['annee_publication']
    quantite = request.form['quantite']

    # Connexion à la base de données
    conn = sqlite3.connect('database2.db')
    cursor = conn.cursor()

    # Exécution de la requête SQL pour insérer un nouveau client
    cursor.execute("INSERT INTO livres (titre, auteur, annee_publication, quantite) VALUES (?, ?, ?, ?)", (titre, auteur, annee_publication, quantite))
    conn.commit()
    conn.close()
    return redirect('/livres/')  # Rediriger vers la page d'accueil après l'enregistrement
                                                                                                                                       
if __name__ == "__main__":
  app.run(debug=True)

@app.route('/delete/<int:id>')
def delete_livre(id):
    livre = livre.query.get_or_404(id)
    try:
        db.session.delete(livre)
        db.session.commit()
        flash('Livre supprimé avec succès!', 'success')
    except Exception as e:
        flash(f'Erreur lors de la suppression du livre: {str(e)}', 'danger')
    return redirect(url_for('livres'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)





















