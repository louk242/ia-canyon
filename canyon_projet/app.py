from flask import Flask, request, render_template
import json
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def accueil():
    with open("projets.json", "r", encoding="utf-8") as f:
        projets = json.load(f)

    idees_filtrees = []
    conseils = ""
    competences = []

    if request.method == "POST":
        competences = request.form.getlist("competences")

        idees_filtrees = [
            p for p in projets if any(comp in p["competences"] for comp in competences)
        ]

        if competences:
            conseil_base = {
                "python": "Profite de ton expertise Python pour créer des outils automatisés ou des scripts SaaS.",
                "flask": "Flask est léger : idéal pour lancer des MVP rapides à vendre.",
                "html": "Un bon design responsive peut faire la différence sur CodeCanyon.",
                "css": "Tu pourrais viser des templates visuellement percutants.",
                "javascript": "Les dashboards interactifs sont très demandés.",
                "api": "Crée des intégrations API utiles, les développeurs les adorent.",
                "finance": "Les outils financiers bien présentés se vendent très bien."
            }
            conseils = " ".join([conseil_base[c] for c in competences if c in conseil_base])

    return render_template("accueil.html", idees=idees_filtrees, conseils=conseils)

if __name__ == "__main__":
    app.run(debug=True)
