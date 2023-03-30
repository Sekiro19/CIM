--USE master
--GO
--DROP DATABASE DDA
--GO
--CREATE DATABASE DDA
--GO
USE DDA
GO
------------------------------------
CREATE TABLE Adv (
					CodeAdv TINYINT PRIMARY KEY IDENTITY(1, 1),
					NomComplet NVARCHAR(30) NOT NULL UNIQUE,
					Depot VARCHAR(20) NOT NULL,
					Tel VARCHAR(10),
					Email NVARCHAR(40))
GO
CREATE TABLE Client (
					CodeClient INT PRIMARY KEY,
					CodeAdv TINYINT NOT NULL,
					[Description] NVARCHAR(150),
					DateInscription DATE NOT NULL,
					Tel VARCHAR(10),
					Email NVARCHAR(40),
					NumWilaya TINYINT NOT NULL,
					RollingId TINYINT NOT NULL)
GO
CREATE TABLE Facture (
					CodeFacture VARCHAR(14) PRIMARY KEY,
					DateFacture DATE NOT NULL,
					ModePaiement VARCHAR(20) NOT NULL,
					TauxTVA DECIMAL(4, 2) NOT NULL,
					DateEcheance DATE NOT NULL,
					RollingId TINYINT NOT NULL)
GO
CREATE TABLE Commande (
					CodeCommande VARCHAR(17) PRIMARY KEY,
					CodeClient INT NOT NULL,
					DateCommande DATE NOT NULL,
					ModePaiement VARCHAR(20),
					RollingId TINYINT NOT NULL)
GO
ALTER TABLE Commande
ADD Etat AS dbo.GetPercentage(CodeCommande)
CREATE TABLE Livraison (
					CodeLivraison VARCHAR(14) PRIMARY KEY,
					AddressLivraison NVARCHAR(MAX) NOT NULL,
					DateLivraison DATE NOT NULL,
					RollingId TINYINT NOT NULL)
GO
CREATE TABLE Produit (
					CodeProduit VARCHAR(12) PRIMARY KEY,
					NumMarque TINYINT NOT NULL,
					Nom VARCHAR(30) NOT NULL,
					Type VARCHAR(15) NOT NULL,
					PrixUnitaire DECIMAL(7, 4) NOT NULL,
					PoidsUnitaire DECIMAL(6, 3) NOT NULL,
					UnitePoids VARCHAR(1) NOT NULL,
					CapaciteCarton INT NOT NULL,
					CapacitePalette INT NOT NULL,
					RollingId TINYINT NOT NULL)
GO
CREATE TABLE Marque (
					NumMarque TINYINT PRIMARY KEY IDENTITY(1, 1),
					NomMarque VARCHAR(15) NOT NULL,
					[Description] NVARCHAR(150))
GO
CREATE TABLE ProduitCommande (
					CodeProduit VARCHAR(12),
					CodeCommande VARCHAR(17),
					Quantite INT NOT NULL,
					PRIMARY KEY(CodeProduit, CodeCommande))
GO
CREATE TABLE ProduitFacture (
					CodeProduit VARCHAR(12),
					CodeFacture VARCHAR(14),
					Quantite INT NOT NULL,
					Remise DECIMAL(4, 2) NOT NULL,
					CodeCommande VARCHAR(17) NOT NULL,
					Etat VARCHAR(14) NOT NULL,
					PRIMARY KEY(CodeProduit, CodeFacture))
GO
ALTER TABLE ProduitFacture
ADD CONSTRAINT CheckEtatFacture CHECK (Etat IN ('NonPaye', 'Paye'))
GO
CREATE TABLE ProduitLivraison (
					CodeProduit VARCHAR(12) NOT NULL,
					CodeLivraison VARCHAR(14) NOT NULL,
					CodeEmplacement TINYINT NOT NULL,
					Lot VARCHAR(10) NOT NULL,
					DateFabrication DATE NOT NULL,
					DateExpiration DATE NOT NULL,
					Quantite INT NOT NULL,
					QuantiteRecue INT,
					TotalQuantiteRejetee INT,
					DescriptionProduitsRejetee VARCHAR(MAX),
					CodeCommande VARCHAR(17),
					PRIMARY KEY(CodeProduit, CodeLivraison, DateFabrication, CodeEmplacement))
GO
CREATE TABLE Stock (
					CodeEmplacement TINYINT PRIMARY KEY IDENTITY(1,1),
					[Description] NVARCHAR(150))
GO
CREATE TABLE ProduitStock (
					CodeProduit VARCHAR(12),
					CodeEmplacement TINYINT,
					DateFabrication DATE NOT NULL,
					DateExpiration DATE NOT NULL,
					Quantite INT NOT NULL,
					Lot VARCHAR(10),
					PRIMARY KEY(CodeProduit, CodeEmplacement, DateFabrication))
GO
CREATE TABLE Inventaire (
					DateInventaire DATETIME,
					CodeEmplacement TINYINT NOT NULL,
					CodeProduit VARCHAR(12) NOT NULL,
					DateFabrication DATE NOT NULL,
					DateExpiration DATE NOT NULL,
					Quantite INT NOT NULL,
					TypeInventaire VARCHAR(15) NOT NULL,
					Lot VARCHAR(10),
					PRIMARY KEY(DateInventaire, CodeProduit, CodeEmplacement, DateFabrication))
GO
------------------------------RELATIONS--------------------------------
-- FK_Client_Adv
ALTER TABLE Client
ADD CONSTRAINT FK_Client_Adv FOREIGN KEY (CodeAdv)
REFERENCES Adv (CodeAdv)
GO
-- FK_ProduitFacture_Commande
ALTER TABLE ProduitFacture
ADD CONSTRAINT FK_ProduitFacture_Commande FOREIGN KEY (CodeCommande)
REFERENCES Commande (CodeCommande)
GO
-- FK_Commande_Client
ALTER TABLE Commande
ADD CONSTRAINT FK_Commande_Client FOREIGN KEY (CodeClient)
REFERENCES Client (CodeClient)
GO
-- FK_ProduitCommande_Commande
ALTER TABLE ProduitCommande
ADD CONSTRAINT FK_ProduitCommande_Commande FOREIGN KEY (CodeCommande)
REFERENCES Commande (CodeCommande)
GO
-- FK_ProduitCommande_Produit
ALTER TABLE ProduitCommande
ADD CONSTRAINT FK_ProduitCommande_Produit FOREIGN KEY (CodeProduit)
REFERENCES Produit (CodeProduit)
GO
-- FK_ProduitFacture_Facture
ALTER TABLE ProduitFacture
ADD CONSTRAINT FK_ProduitFacture_Facture FOREIGN KEY (CodeFacture)
REFERENCES Facture (CodeFacture)
GO
-- FK_ProduitFacture_Produit
ALTER TABLE ProduitFacture
ADD CONSTRAINT FK_ProduitFacture_Produit FOREIGN KEY (CodeProduit)
REFERENCES Produit (CodeProduit)
GO
-- FK_ProduitLivraison_Livraison
ALTER TABLE ProduitLivraison
ADD CONSTRAINT FK_ProduitLivraison_Livraison FOREIGN KEY (CodeLivraison)
REFERENCES Livraison (CodeLivraison)
GO
-- FK_ProduitLivraison_Produit
ALTER TABLE ProduitLivraison
ADD CONSTRAINT FK_ProduitLivraison_Produit FOREIGN KEY (CodeProduit)
REFERENCES Produit (CodeProduit)
GO
-- FK_ProduitLivraison_Stock
ALTER TABLE ProduitLivraison
ADD CONSTRAINT FK_ProduitLivraison_Stock FOREIGN KEY (CodeEmplacement)
REFERENCES Stock (CodeEmplacement)
GO
-- FK_ProduitLivraison_Commande
ALTER TABLE ProduitLivraison
ADD CONSTRAINT FK_ProduitLivraison_Commande FOREIGN KEY (CodeCommande)
REFERENCES Commande (CodeCommande)
GO
-- FK_Produit_Marque
ALTER TABLE Produit
ADD CONSTRAINT FK_Produit_Marque FOREIGN KEY (NumMarque)
REFERENCES Marque (NumMarque)
GO
-- FK_ProduitStock_Stock
ALTER TABLE ProduitStock
ADD CONSTRAINT FK_ProduitStock_Stock FOREIGN KEY (CodeEmplacement)
REFERENCES Stock (CodeEmplacement)
GO
-- FK_ProduitStock_Produit
ALTER TABLE ProduitStock
ADD CONSTRAINT FK_ProduitStock_Produit FOREIGN KEY (CodeProduit)
REFERENCES Produit (CodeProduit)
GO
-- FK_Inventaire_Produit
ALTER TABLE Inventaire
ADD CONSTRAINT FK_Inventaire_Produit FOREIGN KEY (CodeProduit)
REFERENCES Produit (CodeProduit)
GO
-- FK_Inventaire_Stock
ALTER TABLE Inventaire
ADD CONSTRAINT FK_Inventaire_Stock FOREIGN KEY (CodeEmplacement)
REFERENCES Stock (CodeEmplacement)
GO
-------------------------------------Default Inserts-----------------------------------------
--INSERT INTO Adv VALUES ('Badji Mohamed', 'Akbou', '0770919370', 'badji.mohamed@danone.com'),
--					   ('Mokrani Hichem', 'Oran', '0770823153', 'mokrani.hichem@danone.com'),
--					   ('Dali yahya', 'AinBeniane', '0770122145', 'dali.Yahya@danone.com'),
--					   ('Madi Hichem', 'Constantin', '0770995326', 'madi.Hichem@danone.com')
--GO
--INSERT INTO Marque VALUES ('ACTIMEL', ''),
--					        ('ACTIVIA', ''),
--					        ('DANAO', ''),
--					        ('DANETTE', ''),
--					        ('DANINO', ''),
--					        ('DANONE', ''),
--					        ('TREFLE', '')
--GO
--INSERT INTO Stock VALUES ('Une capacité de 10 000 caisses'), ('Une capacité de 5 000'), ('Une capacité de 6 000 caisses'), ('Une capacité de 2 000 caisses')
--GO
-------------------------------------Views-----------------------------------------
-- tableView
ALTER VIEW ProduitView AS 
SELECT Produit.CodeProduit, 
	   CONCAT(Marque.NomMarque, ' ', Produit.Nom, ' ', CAST(Produit.PoidsUnitaire AS FLOAT), Produit.UnitePoids, ' ', Produit.Type) AS DescriptionProduit,
	   PrixUnitaire,
	   CapaciteCarton,
	   CapacitePalette
FROM Produit JOIN Marque ON Marque.NumMarque = Produit.NumMarque
GO
ALTER VIEW StockView AS 
SELECT ProduitStock.CodeProduit,
	   ProduitStock.CodeEmplacement,
	   CONCAT(Marque.NomMarque, ' ', Produit.Nom, ' ', CAST(Produit.PoidsUnitaire AS FLOAT), Produit.UnitePoids, ' ', Produit.Type) AS DescriptionProduit,
	   Q.Palette AS QuantitePalette,
	   Q.Carton  AS QuantiteCarton,
	   Q.Unite AS QuantiteUnite,
	   ProduitStock.Quantite AS TotalQuantiteUnite,
	   ProduitStock.DateFabrication,
	   ProduitStock.DateExpiration,
	   STR((Produit.PrixUnitaire * ProduitStock.Quantite), 11, 4) AS PrixTotal,
	   ProduitStock.Lot,
	   DerniereInventaire = CASE WHEN (Inv.TotalQuantiteUnite - ProduitStock.Quantite) = 0 THEN CONCAT(Inv.DerniereInventaire, ' | Quantite identique: True |') ELSE CONCAT(ISNULL(Inv.DerniereInventaire, 'Inventaire introuvable'), ' | Quantite identique: False |') END
FROM Produit JOIN ProduitStock ON ProduitStock.CodeProduit = Produit.CodeProduit 
			 JOIN Marque ON Marque.NumMarque = Produit.NumMarque
			 LEFT JOIN (SELECT *, CONCAT('| Quantite: P:', LastInv.QuantitePalette, ', C:', LastInv.QuantiteCarton, ', ', 'U:', LastInv.QuantiteUnite, ' | Date: ', CAST(LastInv.DateInventaire AS VARCHAR)) AS DerniereInventaire FROM 
(SELECT *, RANK() OVER (PARTITION BY InventaireView.CodeEmplacement, InventaireView.CodeProduit, InventaireView.DateFabrication ORDER BY InventaireView.DateInventaire DESC) AS RankInventaire 
FROM InventaireView) AS LastInv WHERE LastInv.RankInventaire = 1 AND LastInv.TypeInventaire = 'Verification') AS Inv
			 ON Inv.CodeProduit = Produit.CodeProduit AND Inv.CodeEmplacement = ProduitStock.CodeEmplacement AND Inv.DateFabrication = ProduitStock.DateFabrication 
OUTER APPLY dbo.CalcQuantite(ProduitStock.Quantite, Produit.CapacitePalette, Produit.CapaciteCarton) Q
GO
ALTER VIEW InventaireView AS 
SELECT CONVERT(CHAR(16), DateInventaire , 20) AS DateInventaire, CodeEmplacement, Inventaire.CodeProduit,
	   CONCAT(Marque.NomMarque, ' ', Produit.Nom, ' ', CAST(Produit.PoidsUnitaire AS FLOAT), Produit.UnitePoids, ' ', Produit.Type) AS DescriptionProduit,
	   Q.Palette AS QuantitePalette,
	   Q.Carton  AS QuantiteCarton,
	   Q.Unite AS QuantiteUnite,
	   Quantite AS TotalQuantiteUnite, DateFabrication, DateExpiration, TypeInventaire, Lot
FROM Inventaire JOIN Produit ON Inventaire.CodeProduit = Produit.CodeProduit  JOIN 
	 Marque ON Marque.NumMarque = Produit.NumMarque
OUTER APPLY dbo.CalcQuantite(Inventaire.Quantite, Produit.CapacitePalette, Produit.CapaciteCarton) Q
GO
ALTER VIEW ClientView AS 
SELECT Client.CodeClient, Client.[Description], Client.DateInscription, Client.Tel, Client.Email, Client.NumWilaya, 
CONCAT(Adv.NomComplet, ' | ', Adv.Depot, ' | ', Adv.Tel, ' | ', Adv.Email) AS ADV
FROM Client JOIN Adv ON Client.CodeAdv = Adv.CodeAdv
GO
ALTER VIEW CommandeView AS
SELECT Commande.DateCommande,
	   ProduitCommande.CodeCommande,
	   Commande.CodeClient,
	   ProduitCommande.CodeProduit,
	   ProduitView.DescriptionProduit,
	   Q.Palette AS QuantitePalette,
	   Q.Carton  AS QuantiteCarton,
	   Q.Unite AS QuantiteUnite,
	   ProduitCommande.Quantite AS TotalQuantiteUnite,
	   ProduitView.PrixUnitaire,
	   STR((ProduitView.PrixUnitaire * ProduitCommande.Quantite), 11, 4) AS MontantHT,
	   Commande.ModePaiement
FROM Commande JOIN ProduitCommande ON Commande.CodeCommande = ProduitCommande.CodeCommande JOIN ProduitView ON ProduitView.CodeProduit = ProduitCommande.CodeProduit
OUTER APPLY dbo.CalcQuantite(ProduitCommande.Quantite, ProduitView.CapacitePalette, ProduitView.CapaciteCarton) Q
GO
ALTER VIEW FactureView AS  
SELECT *, STR((FV.PrixNet * FV.TotalQuantiteUnite), 11, 4) AS MontantHT FROM 
(SELECT Facture.DateFacture, 
	   ProduitFacture.CodeFacture,
	   ProduitFacture.CodeCommande,
	   ProduitFacture.CodeProduit,
	   ProduitView.DescriptionProduit,
	   Q.Palette AS QuantitePalette,
	   Q.Carton  AS QuantiteCarton,
	   Q.Unite AS QuantiteUnite,
	   ProduitFacture.Quantite AS TotalQuantiteUnite,
	   ProduitView.PrixUnitaire,
	   CONCAT(ProduitFacture.Remise, ' %') AS Remise,
	   CAST(ROUND(ProduitView.PrixUnitaire * (1 - ProduitFacture.Remise/100), 4) AS DECIMAL(7, 4)) AS PrixNet,
	   Facture.TauxTVA,
	   Facture.ModePaiement,
	   Facture.DateEcheance,
	   ProduitFacture.Etat
FROM Facture JOIN 
	 ProduitFacture ON Facture.CodeFacture = ProduitFacture.CodeFacture JOIN 
	 ProduitView ON ProduitFacture.CodeProduit = ProduitView.CodeProduit
	 OUTER APPLY dbo.CalcQuantite(ProduitFacture.Quantite, ProduitView.CapacitePalette, ProduitView.CapaciteCarton) Q) AS FV
GO
ALTER VIEW LivraisonView AS
SELECT Livraison.DateLivraison, ProduitLivraison.CodeLivraison, 
	   ProduitLivraison.CodeCommande, 
	   Livraison.AddressLivraison, ProduitLivraison.CodeProduit, 
	   CONCAT(Marque.NomMarque, ' ', Produit.Nom, ' ', CAST(Produit.PoidsUnitaire AS FLOAT), Produit.UnitePoids, ' ', Produit.Type) AS DescriptionProduit,
	   ProduitLivraison.CodeEmplacement,
	   ProduitLivraison.Lot,
	   ProduitLivraison.DateFabrication,
	   ProduitLivraison.DateExpiration,
	   CONCAT('Palette: ', QL.Palette, ' | Carton: ', QL.Carton, ' | Unite: ', QL.Unite) AS QuantiteLivree,
	   ProduitLivraison.Quantite AS TotalQuantiteUniteLivree,
	   CONCAT(CAST(ProduitLivraison.Quantite * Produit.PoidsUnitaire AS DECIMAL), Produit.UnitePoids) AS TotalPoidsNetLivree,

	   CONCAT('Palette: ', QR.Palette, ' | Carton: ', QR.Carton, ' | Unite: ', QR.Unite) AS QuantiteRecue,
	   ProduitLivraison.QuantiteRecue AS TotalQuantiteUniteRecue,

	   ISNULL(ProduitLivraison.TotalQuantiteRejetee, 0) AS TotalQuantiteRejetee,
	   ISNULL(ProduitLivraison.DescriptionProduitsRejetee, '') AS DescriptionProduitsRejetee
FROM Livraison FULL JOIN 
	 ProduitLivraison ON Livraison.CodeLivraison = ProduitLivraison.CodeLivraison JOIN 
	 Produit ON Produit.CodeProduit = ProduitLivraison.CodeProduit JOIN  
	 Marque ON Marque.NumMarque = Produit.NumMarque
	 OUTER APPLY dbo.CalcQuantite(ProduitLivraison.Quantite, Produit.CapacitePalette, Produit.CapaciteCarton) QL
	 OUTER APPLY dbo.CalcQuantite(ProduitLivraison.QuantiteRecue, Produit.CapacitePalette, Produit.CapaciteCarton) QR
GO
ALTER VIEW MouvementStockView AS
SELECT 'Entrée' AS FluxDuStock, CAST(Inventaire.DateInventaire AS DATE) AS [Date], CONVERT(CHAR(16), Inventaire.DateInventaire, 20) AS id, Inventaire.CodeProduit, DateFabrication, DateExpiration, Q.Palette, Q.Carton, Q.Unite, 0 AS TotalQuantiteRejetee, '' AS DescriptionProduitsRejetee
	FROM Inventaire JOIN Produit ON Inventaire.CodeProduit = Produit.CodeProduit
	OUTER APPLY dbo.CalcQuantite(Inventaire.Quantite, Produit.CapacitePalette, Produit.CapaciteCarton) AS Q
	WHERE (TypeInventaire = 'Production') AND (Palette > 0 OR Carton > 0 OR Unite > 0)
UNION ALL
	SELECT 'Sortie' AS FluxDuStock, Livraison.DateLivraison AS [Date], ProduitLivraison.CodeLivraison AS id, ProduitLivraison.CodeProduit, DateFabrication, DateExpiration, QR.Palette, QR.Carton, QR.Unite, TotalQuantiteRejetee, DescriptionProduitsRejetee
	FROM ProduitLivraison JOIN Produit ON ProduitLivraison.CodeProduit = Produit.CodeProduit JOIN Livraison ON Livraison.CodeLivraison = ProduitLivraison.CodeLivraison
	OUTER APPLY dbo.CalcQuantite(ProduitLivraison.QuantiteRecue, Produit.CapacitePalette, Produit.CapaciteCarton) AS QR
	WHERE Palette > 0 OR Carton > 0 OR Unite > 0
ORDER BY [Date] DESC OFFSET 0 ROWS
GO
-- tableViewFetch
ALTER VIEW ProduitViewFetch AS 
SELECT Marque.NomMarque, Produit.Nom, Produit.Type, Produit.PrixUnitaire, Produit.PoidsUnitaire, Produit.UnitePoids, Produit.CapaciteCarton, Produit.CapacitePalette, Produit.CodeProduit
FROM Produit JOIN Marque ON Produit.NumMarque = Marque.NumMarque
GO
ALTER VIEW StockViewFetch AS 
SELECT CodeProduit, CodeEmplacement, DateFabrication, DateExpiration, QuantiteUnite, QuantiteCarton, QuantitePalette, Lot FROM StockView
GO
ALTER VIEW InventaireViewFetch AS 
SELECT DateInventaire, CodeEmplacement, CodeProduit, DateFabrication, DateExpiration, QuantiteUnite, QuantiteCarton, QuantitePalette, TypeInventaire, Lot FROM InventaireView
GO
ALTER VIEW ClientViewFetch AS 
SELECT CONCAT(Adv.Depot, ': ', Adv.NomComplet) AS ADV, Client.[Description], Client.Tel, Client.Email, Client.NumWilaya, Client.CodeClient FROM Client JOIN Adv ON Client.CodeAdv = Adv.CodeAdv
GO
ALTER VIEW CommandeViewFetch AS 
SELECT CodeClient, ModePaiement, 
	   STRING_AGG(CodeProduit, '|') AS CodeProduit, 
	   STRING_AGG(QuantiteUnite, '|') AS QuantiteUnite, 
	   STRING_AGG(QuantiteCarton, '|') AS QuantiteCarton, 
	   STRING_AGG(QuantitePalette, '|') AS QuantitePalette, 
	   CodeCommande 
FROM CommandeView
GROUP BY CodeCommande, CodeClient, ModePaiement
GO
ALTER VIEW FactureViewFetch AS 
SELECT ModePaiement, TauxTVA, DateEcheance,
	   STRING_AGG(CodeCommande, '|') AS CodeCommande, 
	   STRING_AGG(CodeProduit, '|') AS CodeProduit, 
	   STRING_AGG(QuantiteUnite, '|') AS QuantiteUnite, 
	   STRING_AGG(QuantiteCarton, '|') AS QuantiteCarton, 
	   STRING_AGG(QuantitePalette, '|') AS QuantitePalette, 
	   STRING_AGG(CAST(REPLACE(Remise, '%', '') AS FLOAT), '|') AS Remise,
	   STRING_AGG(Etat, '|') AS Etat,
	   CodeFacture
FROM FactureView
GROUP BY CodeFacture, ModePaiement, TauxTVA, DateEcheance
GO
ALTER VIEW LivraisonViewFetch AS 
SELECT Livraison.AddressLivraison, 
	   STRING_AGG(CodeCommande, '|') AS CodeCommande, 
	   STRING_AGG(ProduitLivraison.CodeProduit, '|') AS CodeProduit, 
	   STRING_AGG(CodeEmplacement, '|') AS CodeEmplacement, 
	   STRING_AGG(Lot, '|') AS Lot, 
	   STRING_AGG(DateFabrication, '|') AS DateFabrication, 
	   STRING_AGG(DateExpiration, '|') AS DateExpiration, 

	   STRING_AGG(QL.Unite, '|') AS QuantiteLivreeUnite, 
	   STRING_AGG(QL.Carton, '|') AS QuantiteLivreeCarton, 
	   STRING_AGG(QL.Palette, '|') AS QuantiteLivreePalette, 

	   STRING_AGG(QR.Unite, '|') AS QuantiteRecueUnite, 
	   STRING_AGG(QR.Carton, '|') AS QuantiteRecueCarton, 
	   STRING_AGG(QR.Palette, '|') AS QuantiteRecuePalette, 

	   STRING_AGG(TotalQuantiteRejetee, '|') AS TotalProduitCassesUnite, 
	   STRING_AGG(DescriptionProduitsRejetee, '|') AS DescriptionProduitsRejetee, 
	   Livraison.CodeLivraison
FROM Livraison FULL JOIN 
	 ProduitLivraison ON Livraison.CodeLivraison = ProduitLivraison.CodeLivraison JOIN
	 Produit ON Produit.CodeProduit = ProduitLivraison.CodeProduit
	 OUTER APPLY dbo.CalcQuantite(ProduitLivraison.Quantite, Produit.CapacitePalette, Produit.CapaciteCarton) QL
	 OUTER APPLY dbo.CalcQuantite(ProduitLivraison.QuantiteRecue, Produit.CapacitePalette, Produit.CapaciteCarton) QR
GROUP BY Livraison.CodeLivraison, Livraison.AddressLivraison
GO
---
ALTER VIEW LivraisonCommandeViewFetch AS
SELECT STRING_AGG(CommandeView.CodeCommande, '|') AS CodeCommandeList,
	   STRING_AGG(CommandeView.CodeProduit, '|') AS CodeProduit,
	   STRING_AGG(ProduitStock.CodeEmplacement, '|') AS CodeEmplacement, 
	   STRING_AGG(ProduitStock.Lot, '|') AS Lot,
	   STRING_AGG(ProduitStock.DateFabrication, '|') AS DateFabrication, 
	   STRING_AGG(ProduitStock.DateExpiration, '|') AS DateExpiration, 
	   STRING_AGG(CommandeView.QuantiteUnite, '|') AS QuantiteUnite, 
	   STRING_AGG(CommandeView.QuantiteCarton, '|') AS QuantiteCarton, 
	   STRING_AGG(CommandeView.QuantitePalette, '|') AS QuantitePalette,
	   CodeCommande AS CodeCommande
FROM CommandeView
OUTER APPLY (SELECT TOP 1 * FROM ProduitStock WHERE CommandeView.CodeProduit = ProduitStock.CodeProduit ORDER BY DateFabrication) AS ProduitStock
GROUP BY CodeCommande
GO
ALTER VIEW FactureLivraisonViewFetch AS
SELECT STRING_AGG(CodeCommande, '|') AS CodeCommande, 
	   STRING_AGG(ProduitLivraison.CodeProduit, '|') AS CodeProduit, 
	   STRING_AGG(QR.Unite, '|') AS QuantiteUnite, 
	   STRING_AGG(QR.Carton, '|') AS QuantiteCarton, 
	   STRING_AGG(QR.Palette, '|') AS QuantitePalette,
	   Livraison.CodeLivraison
FROM Livraison FULL JOIN 
	 ProduitLivraison ON Livraison.CodeLivraison = ProduitLivraison.CodeLivraison JOIN 
	 Produit ON Produit.CodeProduit = ProduitLivraison.CodeProduit  
	 OUTER APPLY dbo.CalcQuantite(ProduitLivraison.Quantite, Produit.CapacitePalette, Produit.CapaciteCarton) QL
	 OUTER APPLY dbo.CalcQuantite(ProduitLivraison.QuantiteRecue, Produit.CapacitePalette, Produit.CapaciteCarton) QR
GROUP BY Livraison.CodeLivraison
GO
-- CALCs
ALTER VIEW CommandeTotalMontantHT
AS
SELECT CodeCommande, STR(SUM((Produit.PrixUnitaire * ProduitCommande.Quantite)), 11, 4) AS TotalMontantHT FROM ProduitCommande JOIN Produit ON ProduitCommande.CodeProduit = Produit.CodeProduit GROUP BY CodeCommande ORDER BY CodeCommande DESC OFFSET 0 rows
GO
ALTER VIEW CommandeTotalQuantite
AS
SELECT CodeCommande, SUM(CommandeView.QuantiteUnite) AS TotalQuantiteUnite, 
					 SUM(CommandeView.QuantiteCarton) AS TotalQuantiteCarton, 
					 SUM(CommandeView.QuantitePalette) AS TotalQuantitePalette,
					 SUM(CommandeView.TotalQuantiteUnite) AS TotalQuantiteParUnite
FROM CommandeView GROUP BY CodeCommande
GO
ALTER VIEW FactureTotalQuantite_TotalHT_TVA_TTC AS
SELECT T.CodeFacture, 
	   T.TotalQuantite, 
	   FORMAT(T.TotalHT, 'N2', 'fr-FR') AS TotalHT, 
	   CAST((TauxTVA*100) AS DECIMAL(4, 2)) AS TauxTVA, 
	   FORMAT((T.TotalHT * TauxTVA), 'N2', 'fr-FR') AS TVA,
	   FORMAT(ROUND(T.TotalHT + T.TotalHT * TauxTVA, 2), 'N2', 'fr-FR') AS TTC,
	   Etat
FROM 
(SELECT CodeFacture, 
	    SUM(CAST(MontantHT AS FLOAT)) AS TotalHT, 
		MIN(TauxTVA)/100 AS TauxTVA,
		CONCAT('Palette: ', SUM(FactureView.QuantitePalette), ' Carton: ', SUM(FactureView.QuantiteCarton), ' Unite:', SUM(FactureView.QuantiteUnite)) AS TotalQuantite, 
		dbo.CheckFactureEtat(CodeFacture) AS Etat
FROM FactureView GROUP BY CodeFacture ORDER BY MIN(DateFacture) DESC OFFSET 0 ROWS) AS T
GO
ALTER VIEW LivraisonTotalQuantite AS
SELECT Livraison.CodeLivraison,
	   CONCAT(N'Livrée:', SUM(QL.Palette), N' | Recue:', SUM(QR.Palette)) AS TotalPalette,
	   CONCAT(N'Livrée:', SUM(QL.Carton), N' | Recue:', SUM(QR.Carton)) AS TotalCarton,
	   CONCAT(N'Livrée:', SUM(QL.Unite), N' | Recue:', SUM(QR.Unite)) AS TotalUnite,
	   CONCAT(N'Livrée:', SUM(ProduitLivraison.Quantite), N' | Recue:', SUM(ProduitLivraison.QuantiteRecue)) AS QuantiteTotalParUnite,
	   SUM(TotalQuantiteRejetee) AS TotalQuantiteRejetee
FROM Livraison FULL JOIN
	 ProduitLivraison ON Livraison.CodeLivraison = ProduitLivraison.CodeLivraison JOIN 
	 Produit ON Produit.CodeProduit = ProduitLivraison.CodeProduit  
	 OUTER APPLY dbo.CalcQuantite(ProduitLivraison.Quantite, Produit.CapacitePalette, Produit.CapaciteCarton) QL
	 OUTER APPLY dbo.CalcQuantite(ProduitLivraison.QuantiteRecue, Produit.CapacitePalette, Produit.CapaciteCarton) QR
GROUP BY Livraison.CodeLivraison
GO
-- Analyse
ALTER VIEW AllCommande AS
SELECT CAST(DateCommande AS VARCHAR) AS DateCommande, 
	   CodeCommande, CodeClient, CodeProduit, TotalQuantiteUnite,
	   MontantHT, ModePaiement FROM CommandeView
GO 
ALTER VIEW AllLivraison AS
SELECT CAST(DateLivraison AS VARCHAR) AS DateLivraison,
	   CodeLivraison, CodeCommande, CodeProduit, CodeEmplacement,
	   TotalQuantiteUniteLivree, TotalQuantiteUniteRecue, TotalQuantiteRejetee, DescriptionProduitsRejetee FROM LivraisonView
GO 
ALTER VIEW AllFacture AS
SELECT CAST(DateFacture AS VARCHAR) AS DateFacture,
	   CodeFacture, Commande.CodeClient, FactureView.CodeCommande, CodeProduit,
	   TotalQuantiteUnite, MontantHT, FactureView.Etat, FactureView.ModePaiement
FROM FactureView 
JOIN Commande ON FactureView.CodeCommande = Commande.CodeCommande
GO 
ALTER VIEW TsLength AS
SELECT MIN(T.minDate) AS minDate, MAX(T.maxDate) AS maxDate FROM
(SELECT MIN(DateCommande) AS minDate, MAX(DateCommande) AS maxDate FROM AllCommande
UNION ALL
SELECT MIN(DateLivraison) AS minDate, MAX(DateLivraison) AS maxDate FROM AllLivraison
UNION ALL
SELECT MIN(DateFacture) AS minDate, MAX(DateFacture) AS maxDate FROM AllFacture) AS T
GO
-- Report
ALTER VIEW FactureReport AS
SELECT DISTINCT FactureView.CodeFacture,
	   CAST(FactureView.DateFacture AS VARCHAR) AS DateFacture,
	   FactureView.CodeCommande,
	   Commande.CodeClient,
	   ClientView.Description AS DescriptionClient,
	   ClientView.Tel AS TelClient,
	   ClientView.Email AS EmailClient,
	   Livraison.AddressLivraison,
	   ClientView.ADV,

	   FactureView.CodeProduit,
	   FactureView.DescriptionProduit, 
	   CONCAT('Palette: ', FactureView.QuantitePalette, ' Carton: ', FactureView.QuantiteCarton, ' Unite:', FactureView.QuantiteUnite) AS Quantite,
	   FactureView.PrixUnitaire, 
	   FactureView.Remise,
	   FactureView.PrixNet, 
	   FactureView.MontantHT,

	   FactureTotalQuantite_TotalHT_TVA_TTC.TotalQuantite,
	   FactureTotalQuantite_TotalHT_TVA_TTC.TotalHT,
	   FactureTotalQuantite_TotalHT_TVA_TTC.TauxTVA,
	   FactureTotalQuantite_TotalHT_TVA_TTC.TVA,
	   FactureTotalQuantite_TotalHT_TVA_TTC.TTC,

	   FactureView.ModePaiement, 
	   CAST(FactureView.DateEcheance AS VARCHAR) AS DateEcheance
FROM FactureView JOIN FactureTotalQuantite_TotalHT_TVA_TTC ON FactureView.CodeFacture = FactureTotalQuantite_TotalHT_TVA_TTC.CodeFacture
JOIN ProduitLivraison ON FactureView.CodeCommande = ProduitLivraison.CodeCommande 
JOIN Livraison ON ProduitLivraison.CodeLivraison = Livraison.CodeLivraison
JOIN Commande ON FactureView.CodeCommande = Commande.CodeCommande
JOIN ClientView ON Commande.CodeClient = ClientView.CodeClient
GO

SELECT @@SERVERNAME
