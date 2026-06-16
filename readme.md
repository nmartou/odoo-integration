# Real estate manager - Odoo integration

## Context

Exemples de projet:
Application de sondages, application de gestionnaire de salaire, magasin vend des vinyles (gestion de stock), facturation, dépot, CRM, fiche de paie.

Prérequis : Avoir une validation métier de l'appli, éviter un simple CRUD

## Explication technique

Le programme doit être réalisé au minium en console et avec Python et une base de donnée PosgreSQL. SQL alchemy comme ORM. Utilisation de Git (main, dev, branche feat).
Streamlit pour front python si on veut. Sinon autre framework, peut utiliser odoo comme base (le meilleur évidemment)

## Projet

### Gestion parc immobilier

#### Fonctionnalités

Rôles Personnes:

- Locataire
- Acheteur
- Propriétaire
- Gérant

Sous-traitants :

- Num TVA

Sous-traitants titre :

- Maçon
- Electicien
- Généraliste
- Charpentier
- Bâtisseur
- Jardinier

Adresse personnes

Type de biens:

- Appartement
- Maison
- Field

Type d'appartement & appartement & terrain :

- Duplex
- Simple
- 2 façades
- 3 façades
- Villa
- emtpy

Gestion des travaux :

- Réparations
- Constructions
- Rénovations
- Améliorations

Statut des travaux :

- Requête (initialisation d'une demande)
- Démarré (Au minimum 1 sous-traitant demandé)
- En cours (travaux démarrés)
- Finalisation (travaux principaux terminés)
- Fini (travaux tout confondu fini)

Statut des sous-traitant par projet :

- A demander (ST sélectionné, il faut demander)
- Validé (ST validé pour le chantier)
- En cours (ST sur projet)
- Fini (ST fini de travailler)
- Payé (ST payé)

adresses

Dans la gestion immobilière on va retrouver différents aspects du métier :

- L'achat de propriété
- La vente de propriété
- La location de propriété

L'achat est lié à un acheteur
Trouver une vente ou une location est lié à un acheteur
La vente est lié à un vendeur
La vente d'un bien représente 2% à 5% HTVA de la valeur du bien (200.000 < => 4% - 5%, sinon 2% - 3%)
La location est lié à un vendeur
La location peut être partielle (gestionnaire administrative et financière ou courante)
Gestion administrative et financière 4,5% à 6% HTVA (encaissement, indexation des loyers, rappels, garanties locatives)
Gestion courante 7% à 8% HTVA (décompte des charges des copropriétés et petits travaux du quotidien)
Gestion totale 10% HTVA (assurance loyé impayé et couverture juridique)
Gestion propriétaire, 100% du revenu reviens à l'entreprise
La location si elle est partielle (donc le bien n'appartient pas à l'entreprise), un revenu mensuel est perçu pour la gestion
La location avec revenu nécessite une gestion mensuelle de la perception
automatisation des indexations sans 

Payment type :

- location_month
- purchase

transaction_type   ENUM(
                     RENT_COLLECTION,      -- loyer perçu
                     OWNER_DISBURSEMENT,   -- reversement au proprio
                     AGENCY_FEE,           -- commission agence
                     MANAGEMENT_FEE        -- frais de gestion
                   )

OWNER
TENANT
GUARANTOR
AGENCY
MANAGED_OWNER

CAS 1 — Agence mandate (gestion locative)
Locataire → paie loyer → Agence → reverse (loyer - commission) → Propriétaire
                                → garde commission

CAS 2 — Agence facture ses frais de gestion
Propriétaire → paie frais de gestion → Agence

CAS 3 — Agence est propriétaire
Locataire → paie loyer → Agence (en tant que propriétaire)

### 

Gestion de domaine pour les tables de types afin de modifier le domaine une seule fois et donc créer des checks vis-à-vis de ces domaines (proche de l'enum)

gestion des mini tables via un enum python ou des types pré définis python pour éviter la surcharge de la db