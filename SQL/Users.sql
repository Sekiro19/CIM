USE DDA
GO
-------- SERVER LEVEL SECURITY
CREATE LOGIN StockManager WITH PASSWORD = '147895623Gs';
GO
CREATE LOGIN ServiceClient WITH PASSWORD = '147895623Sc';
GO
CREATE LOGIN InventorySupervisor WITH PASSWORD = '147895623Si';
GO
CREATE LOGIN SU WITH PASSWORD = '147895623Sekiro';
GO
-------- DATABASE LEVEL SECURITY
USE DDA
CREATE USER SU FOR LOGIN SU;
CREATE USER StockManager FOR LOGIN StockManager;
CREATE USER ServiceClient FOR LOGIN ServiceClient;
CREATE USER InventorySupervisor FOR LOGIN InventorySupervisor;
GO
-- ROLES
CREATE ROLE CommonMethods;
GRANT EXECUTE ON dbo.CatchError TO CommonMethods;
GRANT EXECUTE ON dbo.ToQuantiteUnite TO CommonMethods;
GRANT EXECUTE ON dbo.GetPercentage TO CommonMethods;
GRANT EXECUTE ON dbo.CheckFactureEtat TO CommonMethods;
GO
EXEC sp_addrolemember 'CommonMethods', 'StockManager';
EXEC sp_addrolemember 'CommonMethods', 'ServiceClient';
EXEC sp_addrolemember 'CommonMethods', 'InventorySupervisor';
GO
CREATE ROLE Analysis;
GRANT SELECT ON AllCommande TO CommonMethods;
GRANT SELECT ON AllLivraison TO CommonMethods;
GRANT SELECT ON AllFacture TO CommonMethods;
GRANT SELECT ON TsLength TO CommonMethods;
GO
EXEC sp_addrolemember 'Analysis', 'StockManager';
GO
-------- Permissions
EXEC sp_depends 'dbo.DeleteLivraison';
-- root
EXEC sp_addsrvrolemember 'SU', 'sysadmin';
EXEC sp_addrolemember 'db_owner', 'SU';
-- StockManager
GRANT SELECT, INSERT, UPDATE, DELETE ON ProduitStock TO StockManager;
GRANT SELECT ON TsLength TO StockManager;
GRANT SELECT ON StockView TO StockManager;
GRANT SELECT ON MouvementStockView TO StockManager;
GRANT SELECT ON Stock TO StockManager;
GRANT SELECT ON StockViewFetch TO StockManager;
GRANT EXECUTE ON InsertStock TO StockManager;
GRANT EXECUTE ON UpdateStock TO StockManager;
GRANT EXECUTE ON DeleteStock TO StockManager;
GRANT EXECUTE ON InsertLivraison TO StockManager;
GRANT EXECUTE ON UpdateLivraison TO StockManager;
GRANT EXECUTE ON DeleteLivraison TO StockManager;
GRANT EXECUTE ON StockFlowUpdater TO StockManager;
GRANT SELECT ON CommandeView TO StockManager;
GRANT SELECT ON CommandeViewFetch TO StockManager;
GRANT SELECT ON LivraisonViewFetch TO StockManager;
GRANT SELECT ON CommandeTotalMontantHT TO StockManager;
GRANT SELECT ON CommandeTotalQuantite TO StockManager;
GRANT SELECT ON Commande TO StockManager;
GRANT SELECT ON Client TO StockManager;
GRANT SELECT, INSERT, UPDATE, DELETE ON Livraison TO StockManager;
GRANT SELECT, INSERT, UPDATE, DELETE ON ProduitLivraison TO StockManager;
GRANT SELECT ON LivraisonView TO StockManager;
GRANT SELECT ON Produit TO StockManager;
GRANT SELECT ON LivraisonTotalQuantite TO StockManager;
GO
