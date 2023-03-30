USE DDA
GO
-------------------------------------FUNCTIONS-----------------------------------------
ALTER FUNCTION ToQuantiteUnite (@CodeProduit VARCHAR(12), @Quantite INT, @QuantiteCarton INT, @QuantitePalette INT)
RETURNS INT
AS
BEGIN
	IF @Quantite IS NULL
		SET @Quantite=0
	IF @QuantiteCarton IS NULL
		SET @QuantiteCarton=0
	IF @QuantitePalette IS NULL
		SET @QuantitePalette=0

	SET @Quantite = @Quantite + (@QuantiteCarton * (SELECT CapaciteCarton from Produit WHERE CodeProduit=@CodeProduit))
	SET @Quantite = @Quantite + (@QuantitePalette * (SELECT CapacitePalette * CapaciteCarton from Produit WHERE CodeProduit=@CodeProduit))
	RETURN @Quantite
END
GO
ALTER FUNCTION CalcQuantite (@Quantite INT,
							 @CapacitePalette INT,
							 @CapaciteCarton INT)
RETURNS @T TABLE(Palette INT, Carton INT, Unite INT)
AS
BEGIN
	SET @CapacitePalette = @CapacitePalette  * @CapaciteCarton
	DECLARE @Palette INT
	DECLARE @Carton INT
	DECLARE @Unite INT
	SET @Unite = @Quantite
	SET @Palette = @Unite / @CapacitePalette
	SET @Unite = @Unite - (@CapacitePalette * @Palette)
	SET @Carton = (@Unite / @CapaciteCarton)
	SET @Unite = @Unite - (@CapaciteCarton * @Carton)

	INSERT INTO @T VALUES (@Palette, @Carton, @Unite)
	RETURN
END
GO
ALTER FUNCTION GetPercentage (@CodeCommande VARCHAR(17))
RETURNS VARCHAR(100)
AS
BEGIN
	DECLARE @PL FLOAT;
	DECLARE @PF FLOAT;
	DECLARE @count INT;
	DECLARE @Result VARCHAR(50)

	SET @count = (SELECT COUNT(CodeProduit) FROM ProduitLivraison WHERE ProduitLivraison.CodeCommande = @CodeCommande);
	SET @PL = ISNULL((SELECT CAST(ROUND(SUM(Percentage), 2) AS FLOAT) AS TotalPercentage 
						FROM (SELECT CASE 
										WHEN (QuantiteRecue + TotalQuantiteRejetee) = Quantite THEN  (50.0 / @count)
										ELSE 0
									 END AS Percentage
							FROM ProduitLivraison WHERE ProduitLivraison.CodeCommande = @CodeCommande)
							AS temp), 0)
	SET @Result = CASE WHEN @PL < 50 THEN 'Livraison inachevée |' ELSE '' END

	SET @count = (SELECT COUNT(CodeProduit) FROM ProduitFacture WHERE ProduitFacture.CodeCommande = @CodeCommande);
	SET @PF = ISNULL((SELECT CAST(ROUND(SUM(Percentage), 2) AS FLOAT) AS TotalPercentage
						FROM (SELECT CASE 
										WHEN Etat = 'Paye' THEN  50.0 / @count
										ELSE 0
									 END AS Percentage
							FROM ProduitFacture WHERE ProduitFacture.CodeCommande = @CodeCommande) AS temp), 0)
	SET @Result += CASE WHEN @PF < 50 THEN ' Facture non Payée' ELSE '' END

	RETURN CONCAT((@PL+@PF), '% ', TRIM('|' FROM @Result))
END
GO
ALTER FUNCTION CheckFactureEtat (@CodeFacture VARCHAR(14))
RETURNS VARCHAR(30)
AS
BEGIN
	IF (SELECT COUNT(*) FROM ProduitFacture WHERE CodeFacture = @CodeFacture AND Etat <> 'Paye') > 0
		BEGIN
			DECLARE @DaysLeft VARCHAR(3)
			SET @DaysLeft = (SELECT CAST(DATEDIFF(DAY, GETDATE(), DateEcheance) AS VARCHAR) FROM Facture WHERE CodeFacture = @CodeFacture)
			IF  @DaysLeft > 0
				RETURN 'NonPaye | Jours restants: ' + @DaysLeft
			RETURN 'NonPaye | Jours restants: 0j'
		END

	RETURN 'Paye'
END
GO
-------------------------------------PROCEDURES-----------------------------------------
--------CATCH_ERROR
ALTER PROCEDURE CatchError
AS
BEGIN
	SET NOCOUNT ON 
	SET XACT_ABORT ON
	SELECT ERROR_MESSAGE() AS ErrorMessage;
END
GO
--------Produit
ALTER PROCEDURE InsertProduit(@NomMarque VARCHAR(15),
							   @Nom VARCHAR(30),
							   @Type VARCHAR(15),
							   @PrixUnitaire DECIMAL(7, 4),
							   @PoidsUnitaire DECIMAL(6, 3),
							   @UnitePoids VARCHAR(1),
							   @CapaciteCarton INT,
							   @CapacitePalette INT)
AS
SET NOCOUNT ON 
SET XACT_ABORT ON
DECLARE @CodeProduit VARCHAR(12)
DECLARE @RollingId TINYINT
DECLARE @NumMarque TINYINT
SET @NumMarque = (SELECT TOP 1 NumMarque FROM Marque WHERE NomMarque = @NomMarque)
BEGIN
	BEGIN TRY
		SET @RollingId = (SELECT ISNULL(MAX(RollingId), 0) + 1 FROM Produit WHERE NumMarque = @NumMarque AND PoidsUnitaire = @PoidsUnitaire AND UnitePoids = @UnitePoids)
		SET @CodeProduit = (SELECT CONCAT(@NumMarque, '-', CAST(@PoidsUnitaire AS FLOAT), @UnitePoids, '-', @RollingId) AS CodeProduit)
		INSERT INTO Produit (CodeProduit, NumMarque, Nom, Type, PrixUnitaire, PoidsUnitaire, UnitePoids, CapaciteCarton, CapacitePalette, RollingId)
						VALUES (@CodeProduit, @NumMarque, @Nom, @Type, @PrixUnitaire, @PoidsUnitaire, @UnitePoids, @CapaciteCarton, @CapacitePalette, @RollingId)
		SELECT 'succes' AS Result
	END TRY
	BEGIN CATCH
		EXEC CatchError;
	END CATCH
END
GO
ALTER PROCEDURE UpdateProduit(@CodeProduit VARCHAR(12),
							   @NomMarque VARCHAR(15),
							   @Nom VARCHAR(30),
							   @Type VARCHAR(15),
							   @PrixUnitaire DECIMAL(7, 4),
							   @PoidsUnitaire DECIMAL(6, 3),
							   @UnitePoids VARCHAR(1),
							   @CapaciteCarton INT,
							   @CapacitePalette INT)
AS
SET NOCOUNT ON 
SET XACT_ABORT ON
DECLARE @newCodeProduit VARCHAR(12)
DECLARE @NumMarque TINYINT
SET @NumMarque = (SELECT TOP 1 NumMarque FROM Marque WHERE NomMarque = @NomMarque)
SET @newCodeProduit = (SELECT CONCAT(@NumMarque, '-', CAST(@PoidsUnitaire AS FLOAT), @UnitePoids, '-', (SELECT RollingId FROM Produit WHERE CodeProduit=@CodeProduit)) AS CodeProduit)
BEGIN
	BEGIN TRY
		UPDATE Produit
		SET CodeProduit=@newCodeProduit, NumMarque=@NumMarque, Nom=@Nom, Type=@Type, PrixUnitaire=@PrixUnitaire, PoidsUnitaire=@PoidsUnitaire, UnitePoids=@UnitePoids, CapaciteCarton=@CapaciteCarton, CapacitePalette=@CapacitePalette
		WHERE CodeProduit=@CodeProduit
		SELECT 'succes' AS Result
	END TRY
	BEGIN CATCH
		EXEC CatchError;
	END CATCH
END
GO
ALTER PROCEDURE DeleteProduit(@CodeProduit VARCHAR(12), @BruteForce BIT=0)
AS
BEGIN
	SET NOCOUNT ON 
	SET XACT_ABORT ON
	DECLARE @trancount INT = @@trancount

	if @trancount = 0
		BEGIN tran
	BEGIN TRY
		IF @BruteForce = 1
			BEGIN
				DELETE Inventaire WHERE CodeProduit=@CodeProduit
				DELETE ProduitStock WHERE CodeProduit=@CodeProduit
				DELETE ProduitLivraison WHERE CodeProduit=@CodeProduit
				DELETE ProduitCommande WHERE CodeProduit=@CodeProduit
				DELETE ProduitFacture WHERE CodeProduit=@CodeProduit
			END
		DELETE Produit WHERE CodeProduit=@CodeProduit

		SELECT 'succes' AS Result
		if XACT_STATE() = 1 and @trancount = 0
			commit;
	END TRY
	BEGIN CATCH
		EXEC CatchError;
		if XACT_STATE() <> 0 and @trancount = 0
			rollback;
		else
			throw;
	END CATCH
END
GO
--------ProduitStock
ALTER PROCEDURE InsertStock(@CodeProduit VARCHAR(12),
							@CodeEmplacement TINYINT,
							@DateFabrication DATE,
							@DateExpiration DATE,
							@Quantite INT,
							@QuantiteCarton INT,
							@QuantitePalette INT,
							@Lot VARCHAR(10))
AS
SET NOCOUNT ON 
SET XACT_ABORT ON
BEGIN
	SET @Quantite = ISNULL(dbo.ToQuantiteUnite(@CodeProduit, @Quantite, @QuantiteCarton, @QuantitePalette), 0)
	BEGIN TRY
		IF (SELECT COUNT(*) FROM ProduitStock WHERE CodeProduit=@CodeProduit AND CodeEmplacement=@CodeEmplacement AND DateFabrication=@DateFabrication) > 0
			BEGIN
				UPDATE ProduitStock SET Quantite += @Quantite
				WHERE CodeProduit=@CodeProduit AND CodeEmplacement=@CodeEmplacement AND DateFabrication=@DateFabrication
			END
		ELSE
			BEGIN
				INSERT INTO ProduitStock (CodeProduit, CodeEmplacement, DateFabrication, DateExpiration, Quantite, Lot)
								  VALUES (@CodeProduit, @CodeEmplacement, @DateFabrication, @DateExpiration, @Quantite, @Lot)
			END
		SELECT 'succes' AS Result
	END TRY
	BEGIN CATCH
		EXEC CatchError;
	END CATCH
END
GO
ALTER PROCEDURE UpdateStock(@CodeProduit VARCHAR(12),
									@CodeEmplacement TINYINT,
									@DateFabrication DATE,
									@NewCodeProduit VARCHAR(12),
									@NewCodeEmplacement TINYINT,
									@NewDateFabrication DATE,
									@DateExpiration DATE,
									@Quantite INT,
									@QuantiteCarton INT,
									@QuantitePalette INT,
									@Lot VARCHAR(10))
AS
SET NOCOUNT ON 
SET XACT_ABORT ON
BEGIN
	SET @Quantite = ISNULL(dbo.ToQuantiteUnite(@CodeProduit, @Quantite, @QuantiteCarton, @QuantitePalette), 0)
	BEGIN TRY
		UPDATE ProduitStock
		SET CodeProduit=@NewCodeProduit, CodeEmplacement=@NewCodeEmplacement, DateFabrication=@NewDateFabrication, DateExpiration=@DateExpiration, Quantite=@Quantite, Lot=@Lot
		WHERE CodeProduit=@CodeProduit AND CodeEmplacement=@CodeEmplacement AND DateFabrication=@DateFabrication
		SELECT 'succes' AS Result
	END TRY
	BEGIN CATCH
		EXEC CatchError;
	END CATCH
END
GO
ALTER PROCEDURE DeleteStock(@CodeProduit VARCHAR(12), @CodeEmplacement TINYINT, @DateFabrication DATE, @BruteForce BIT=0)
AS
BEGIN
	SET NOCOUNT ON 
	SET XACT_ABORT ON
	DECLARE @trancount INT = @@trancount

	if @trancount = 0
		BEGIN tran
	BEGIN TRY
		DELETE ProduitStock WHERE CodeProduit=@CodeProduit AND CodeEmplacement=@CodeEmplacement AND DateFabrication=@DateFabrication
		SELECT 'succes' AS Result
		if XACT_STATE() = 1 and @trancount = 0
			commit;
	END TRY
	BEGIN CATCH
		EXEC CatchError;
		if XACT_STATE() <> 0 and @trancount = 0
			rollback;
		else
			throw;
	END CATCH
END
GO
--------Inventaire
ALTER PROCEDURE InsertInventaire(@CodeEmplacement TINYINT,
								 @CodeProduit VARCHAR(12),
								 @DateFabrication DATE,
								 @DateExpiration DATE,
								 @Quantite INT,
								 @QuantiteCarton INT,
								 @QuantitePalette INT,
								 @TypeInventaire VARCHAR(15),
								 @Lot VARCHAR(10))
AS
SET NOCOUNT ON 
SET XACT_ABORT ON
BEGIN
	BEGIN TRY
		SET @Quantite = dbo.ToQuantiteUnite(@CodeProduit, @Quantite, @QuantiteCarton, @QuantitePalette)
		INSERT INTO Inventaire (DateInventaire, CodeProduit, CodeEmplacement, DateFabrication, DateExpiration, Quantite, TypeInventaire, Lot)
						VALUES (CONVERT(CHAR(16), GETDATE(), 20), @CodeProduit, @CodeEmplacement, @DateFabrication, @DateExpiration, @Quantite, @TypeInventaire, @Lot)
		SELECT 'succes' AS Result
	END TRY
	BEGIN CATCH
		EXEC CatchError;
	END CATCH
END
GO
ALTER PROCEDURE UpdateInventaire(@DateInventaire DATETIME,
								 @CodeEmplacement TINYINT,
								 @CodeProduit VARCHAR(12),
								 @DateFabrication DATE,
								 @NewCodeEmplacement TINYINT,
								 @NewCodeProduit VARCHAR(12),
								 @NewDateFabrication DATE,
								 @DateExpiration DATE,
							 	 @Quantite INT,
								 @QuantiteCarton INT,
								 @QuantitePalette INT,
								 @TypeInventaire VARCHAR(15),
								 @Lot VARCHAR(10))
AS
SET NOCOUNT ON 
SET XACT_ABORT ON
BEGIN
	SET @Quantite = dbo.ToQuantiteUnite(@CodeProduit, @Quantite, @QuantiteCarton, @QuantitePalette)
	BEGIN TRY
		UPDATE Inventaire
		SET CodeProduit=@NewCodeProduit, CodeEmplacement=@NewCodeEmplacement, 
			DateFabrication=@NewDateFabrication, DateExpiration=@DateExpiration, 
			Quantite=@Quantite, TypeInventaire=@TypeInventaire, Lot=@Lot
		WHERE DateInventaire = @DateInventaire AND CodeProduit=@CodeProduit AND CodeEmplacement=@CodeEmplacement AND DateFabrication=@DateFabrication
		SELECT 'succes' AS Result
	END TRY
	BEGIN CATCH
		EXEC CatchError;
	END CATCH
END
GO
ALTER PROCEDURE DeleteInventaire(@DateInventaire DATETIME, @CodeEmplacement TINYINT, @CodeProduit VARCHAR(12), @DateFabrication DATE, @BruteForce BIT=0)
AS
BEGIN
	SET NOCOUNT ON 
	SET XACT_ABORT ON
	DECLARE @trancount INT = @@trancount

	if @trancount = 0
		BEGIN tran
	BEGIN TRY
		DELETE Inventaire WHERE DateInventaire=@DateInventaire AND CodeEmplacement=@CodeEmplacement AND CodeProduit=@CodeProduit AND DateFabrication=@DateFabrication

		SELECT 'succes' AS Result
		if XACT_STATE() = 1 and @trancount = 0
			commit;
	END TRY
	BEGIN CATCH
		EXEC CatchError;
		if XACT_STATE() <> 0 and @trancount = 0
			rollback;
		else
			throw;
	END CATCH
END
GO
--------Client
ALTER PROCEDURE InsertClient(@NomComplet NVARCHAR(70),
							   @Description NVARCHAR(150),
							   @Tel VARCHAR(10),
							   @Email NVARCHAR(40),
							   @NumWilaya TINYINT)
AS
SET NOCOUNT ON 
SET XACT_ABORT ON
DECLARE @CodeClient INT
DECLARE @RollingId TINYINT
DECLARE @CodeAdv TINYINT
SET @NomComplet = (SELECT LTRIM(PARSENAME(REPLACE('Akbou: Badji Mohamed',':','.'),1)))
SET @CodeAdv = (SELECT CodeAdv FROM Adv WHERE NomComplet = @NomComplet)
BEGIN
	BEGIN TRY
		SET @RollingId = (SELECT ISNULL(MAX(RollingId), 0) + 1 FROM Client WHERE NumWilaya = @NumWilaya)
		SET @CodeClient = (SELECT CONCAT(@NumWilaya, @RollingId) AS CodeClient)
		INSERT INTO Client (CodeClient, CodeAdv, Description, DateInscription, Tel, Email, NumWilaya, RollingId)
						VALUES (@CodeClient, @CodeAdv, @Description, GETDATE(), @Tel, @Email, @NumWilaya, @RollingId)
		SELECT 'succes' AS Result
	END TRY
	BEGIN CATCH
		EXEC CatchError;
	END CATCH
END
GO
ALTER PROCEDURE UpdateClient(@CodeClient INT,
							  @NomComplet NVARCHAR(70),
							  @Description NVARCHAR(150),
							  @Tel VARCHAR(10),
							  @Email NVARCHAR(40),
							  @NumWilaya TINYINT)
AS
SET NOCOUNT ON 
SET XACT_ABORT ON
DECLARE @NewCodeClient INT
DECLARE @CodeAdv TINYINT
SET @NomComplet = (SELECT TOP 1 LTRIM(PARSENAME(REPLACE(@NomComplet,':','.'), 1)))
SET @CodeAdv = (SELECT CodeAdv FROM Adv WHERE NomComplet = @NomComplet)
BEGIN
	BEGIN TRY
		SET @NewCodeClient = (SELECT CONCAT(@NumWilaya, (SELECT RollingId FROM Client WHERE CodeClient = @CodeClient)) AS CodeClient)
		UPDATE Client
		SET CodeClient=@NewCodeClient, CodeAdv=@CodeAdv, [Description]=@Description, Tel=@Tel, Email=@Email, NumWilaya=@NumWilaya
		WHERE CodeClient=@CodeClient
		SELECT 'succes' AS Result
	END TRY
	BEGIN CATCH
		EXEC CatchError;
	END CATCH
END
GO
ALTER PROCEDURE DeleteClient(@CodeClient INT, @BruteForce BIT=0)
AS
BEGIN
	SET NOCOUNT ON 
	SET XACT_ABORT ON
	DECLARE @trancount INT = @@trancount

	if @trancount = 0
		BEGIN tran
	BEGIN TRY
		IF @BruteForce = 1
			BEGIN
				DELETE FROM ProduitCommande FROM ProduitCommande INNER JOIN Commande ON ProduitCommande.CodeCommande = Commande.CodeCommande WHERE Commande.CodeClient=@CodeClient;
				DELETE ProduitLivraison FROM ProduitLivraison INNER JOIN Commande ON ProduitLivraison.CodeCommande = Commande.CodeCommande WHERE Commande.CodeClient=@CodeClient;
				DELETE Commande WHERE CodeClient=@CodeClient;

				DELETE ProduitFacture FROM ProduitFacture INNER JOIN Commande ON ProduitFacture.CodeCommande = Commande.CodeCommande WHERE Commande.CodeClient=@CodeClient;
				DELETE Facture FROM Facture JOIN ProduitFacture ON Facture.CodeFacture = ProduitFacture.CodeFacture INNER JOIN Commande ON ProduitFacture.CodeCommande = Commande.CodeCommande WHERE Commande.CodeClient=@CodeClient;
			END
		DELETE Client WHERE CodeClient=@CodeClient

		SELECT 'succes' AS Result
		if XACT_STATE() = 1 and @trancount = 0
			commit;
	END TRY
	BEGIN CATCH
		EXEC CatchError;
		if XACT_STATE() <> 0 and @trancount = 0
			rollback;
		else
			throw;
	END CATCH
END
GO
--------Commande
ALTER PROCEDURE InsertCommande (@CodeClient INT,
								@ModePaiement VARCHAR(20),
							    @CodeProduitList VARCHAR(MAX),
							    @QuantiteList VARCHAR(MAX),
							    @QuantiteCartonList VARCHAR(MAX),
							    @QuantitePaletteList VARCHAR(MAX))
AS
DECLARE @CodeCommande VARCHAR(17)
DECLARE @RollingId TINYINT
DECLARE @DateCommande DATE
DECLARE @SplitsTable TABLE(CodeProduit VARCHAR(12), CodeCommande VARCHAR(17), Quantite INT)
BEGIN
	SET NOCOUNT ON 
	SET XACT_ABORT ON
	DECLARE @trancount INT = @@trancount

	if @trancount = 0
		BEGIN tran
		BEGIN TRY
			SET @DateCommande = GETDATE()
			SET @RollingId = (SELECT ISNULL(MAX(RollingId), 0) + 1 FROM Commande WHERE DateCommande = @DateCommande AND CodeClient = @CodeClient)
			SET @CodeCommande = (SELECT CONCAT('C-', FORMAT(@DateCommande, 'yyMMdd'), '-', @CodeClient, '-', @RollingId))

			INSERT INTO @SplitsTable
			SELECT CodeProduit, @CodeCommande AS CodeCommande, dbo.ToQuantiteUnite(CodeProduit, Quantite, QuantiteCarton, QuantitePalette) AS Quantite FROM
			(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS CodeProduit FROM STRING_SPLIT(@CodeProduitList, '|')) AS CP FULL JOIN
			(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS Quantite FROM STRING_SPLIT(@QuantiteList, '|')) AS QU ON QU.i = CP.i FULL JOIN
			(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS QuantiteCarton FROM STRING_SPLIT(@QuantiteCartonList, '|')) AS QC ON QC.i = CP.i FULL JOIN
			(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS QuantitePalette FROM STRING_SPLIT(@QuantitePaletteList, '|')) AS QP ON QP.i = CP.i

			INSERT INTO Commande(CodeCommande, CodeClient, DateCommande, ModePaiement, RollingId)
							VALUES (@CodeCommande, @CodeClient, @DateCommande, @ModePaiement, @RollingId)
		
			Declare @p VARCHAR(12)
			Declare @q VARCHAR(12)
			SET NOCOUNT ON
			Select CodeProduit, Quantite Into #Temp FROM @SplitsTable
			WHILE EXISTS(SELECT * FROM #Temp)
				BEGIN
					SELECT TOP 1 @p = CodeProduit, @q = Quantite From #Temp
					IF (SELECT COUNT(ProduitStock.CodeProduit) FROM ProduitStock WHERE ProduitStock.CodeProduit = @P) = 0
						BEGIN
							RAISERROR('Produit "%s" exist pas dont stock.', 11, 1, @p)
							BREAK
						END
					ELSE
						IF (SELECT COUNT(ProduitStock.CodeProduit) FROM ProduitStock WHERE ProduitStock.CodeProduit = @P AND ProduitStock.Quantite >= @q) = 0
							BEGIN
								RAISERROR('Quantite insuffisant dans stock.
{CodeProduit: %s, Quantite: %s}', 11, 1, @p, @q)
								BREAK
							END
					Delete #Temp Where #Temp.CodeProduit = @p
				END
			DROP TABLE #Temp

			INSERT INTO ProduitCommande SELECT * FROM @SplitsTable
			
			SELECT 'succes' AS Result

			if XACT_STATE() = 1 and @trancount = 0
				commit;
		END TRY
		BEGIN CATCH
			EXEC CatchError;
			if XACT_STATE() <> 0 and @trancount = 0
				rollback;
			else
				throw;
		END CATCH
END
GO
ALTER PROCEDURE UpdateCommande (@CodeCommande VARCHAR(17),
								@CodeClient INT,
								@ModePaiement VARCHAR(20),
							    @CodeProduitList VARCHAR(MAX),
							    @QuantiteList VARCHAR(MAX),
							    @QuantiteCartonList VARCHAR(MAX),
							    @QuantitePaletteList VARCHAR(MAX))
AS								 
DECLARE @NewCodeCommande VARCHAR(17)
DECLARE @SplitsTable TABLE(CodeProduit VARCHAR(12), CodeCommande VARCHAR(17), Quantite INT)
BEGIN
	SET NOCOUNT ON 
	SET XACT_ABORT ON
	DECLARE @trancount INT = @@trancount

	if @trancount = 0
		BEGIN tran
	BEGIN TRY
		SET @NewCodeCommande = (SELECT CONCAT('C-', FORMAT((SELECT DateCommande FROM Commande WHERE CodeCommande = @CodeCommande), 'yyMMdd'), '-', @CodeClient, '-', (SELECT RollingId FROM Commande WHERE CodeCommande = @CodeCommande)))

		INSERT INTO @SplitsTable
		SELECT CodeProduit, @NewCodeCommande AS CodeCommande, dbo.ToQuantiteUnite(CodeProduit, Quantite, QuantiteCarton, QuantitePalette) AS Quantite FROM
		(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS CodeProduit FROM STRING_SPLIT(@CodeProduitList, '|')) AS CP FULL JOIN
		(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS Quantite FROM STRING_SPLIT(@QuantiteList, '|')) AS QU ON QU.i = CP.i FULL JOIN
		(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS QuantiteCarton FROM STRING_SPLIT(@QuantiteCartonList, '|')) AS QC ON QC.i = CP.i FULL JOIN
		(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS QuantitePalette FROM STRING_SPLIT(@QuantitePaletteList, '|')) AS QP ON QP.i = CP.i
		
		Declare @p VARCHAR(12)
		Declare @q VARCHAR(12)
		SET NOCOUNT ON
		Select CodeProduit, Quantite Into #Temp FROM @SplitsTable
		WHILE EXISTS(SELECT * FROM #Temp)
			BEGIN
				SELECT TOP 1 @p = CodeProduit, @q = Quantite From #Temp
				IF (SELECT COUNT(Produit.CodeProduit) FROM Produit WHERE Produit.CodeProduit = @P) = 0
					BEGIN
						RAISERROR('Produit "%s" exist pas.', 11, 1, @p)
						BREAK
					END
				Delete #Temp Where #Temp.CodeProduit = @p
			END
		DROP TABLE #Temp
		DELETE ProduitCommande WHERE CodeCommande=@CodeCommande
		UPDATE Commande SET CodeCommande=@NewCodeCommande, CodeClient=@CodeClient, ModePaiement=@ModePaiement WHERE CodeCommande=@CodeCommande

		INSERT INTO ProduitCommande SELECT * FROM @SplitsTable
		SELECT 'succes' AS Result

		if XACT_STATE() = 1 and @trancount = 0
			commit;
	END TRY
	BEGIN CATCH
		EXEC CatchError;
		if XACT_STATE() <> 0 and @trancount = 0
			rollback;
		else
			throw;
	END CATCH
END
GO
ALTER PROCEDURE DeleteCommande (@CodeCommande VARCHAR(17), @BruteForce BIT=0)
AS
BEGIN
	SET NOCOUNT ON 
	SET XACT_ABORT ON
	DECLARE @trancount INT = @@trancount

	if @trancount = 0
		BEGIN tran
	BEGIN TRY
		IF @BruteForce = 1
			BEGIN
				DELETE ProduitCommande WHERE ProduitCommande.CodeCommande=@CodeCommande;

				DECLARE @CL VARCHAR(14);
				DECLARE @i INT;
				SET @i = 1;
				WHILE @i <= (SELECT COUNT(CodeLivraison) FROM ProduitLivraison WHERE ProduitLivraison.CodeCommande=@CodeCommande)
				BEGIN
					SET @CL = (SELECT TOP 1 CodeLivraison FROM ProduitLivraison WHERE ProduitLivraison.CodeCommande=@CodeCommande);
					EXEC DeleteLivraison @CL, 1;
					SET @i = @i + 1;
				END;

			END
		DELETE Commande WHERE CodeCommande=@CodeCommande;

		SELECT 'succes' AS Result
		if XACT_STATE() = 1 and @trancount = 0
			commit;
	END TRY
	BEGIN CATCH
		EXEC CatchError;
		if XACT_STATE() <> 0 and @trancount = 0
			rollback;
		else
			throw;
	END CATCH
END
GO
--------Facture
ALTER PROCEDURE InsertFacture (@ModePaiement VARCHAR(20),
							   @TauxTVA DECIMAL(4, 2),
							   @DateEcheance DATE,
							   @CodeCommandeList VARCHAR(MAX),
							   @CodeProduitList VARCHAR(MAX),
							   @QuantiteList VARCHAR(MAX),
							   @QuantiteCartonList VARCHAR(MAX),
							   @QuantitePaletteList VARCHAR(MAX),
							   @RemiseList VARCHAR(MAX),
							   @EtatList VARCHAR(MAX))
AS
DECLARE @CodeFacture VARCHAR(14)
DECLARE @CodeClient INT
DECLARE @RollingId TINYINT
DECLARE @NumWilaya TINYINT
DECLARE @DateFacture DATE
DECLARE @SplitsTable TABLE(CodeProduit VARCHAR(12), Quantite INT, Remise DECIMAL(4, 2), CodeCommande VARCHAR(17), Etat VARCHAR(17))
BEGIN
	SET NOCOUNT ON 
	SET XACT_ABORT ON
	DECLARE @trancount INT = @@trancount

	if @trancount = 0
		BEGIN tran
		BEGIN TRY
			INSERT INTO @SplitsTable
			SELECT CodeProduit, dbo.ToQuantiteUnite(CodeProduit, Quantite, QuantiteCarton, QuantitePalette) AS Quantite, ISNULL(CAST(Remise AS DECIMAL(4, 2)), 0) AS Remise, CodeCommande, Etat FROM
			(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS CodeProduit FROM STRING_SPLIT(@CodeProduitList, '|')) AS CP FULL JOIN
			(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS Quantite FROM STRING_SPLIT(@QuantiteList, '|')) AS QU ON QU.i = CP.i FULL JOIN
			(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS QuantiteCarton FROM STRING_SPLIT(@QuantiteCartonList, '|')) AS QC ON QC.i = CP.i FULL JOIN
			(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS QuantitePalette FROM STRING_SPLIT(@QuantitePaletteList, '|')) AS QP ON QP.i = CP.i FULL JOIN
			(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, CASE WHEN value='' THEN NULL ELSE value END AS Remise FROM STRING_SPLIT(@RemiseList, '|')) AS R ON R.i = CP.i FULL JOIN
			(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS CodeCommande FROM STRING_SPLIT(@CodeCommandeList, '|')) AS CC ON CC.i = CP.i FULL JOIN
			(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS Etat FROM STRING_SPLIT(@EtatList, '|')) AS EF ON EF.i = CP.i

			IF (SELECT COUNT(DISTINCT Commande.CodeClient) FROM Commande JOIN Client ON Commande.CodeClient = Client.CodeClient WHERE CodeCommande IN (SELECT CodeCommande FROM @SplitsTable)) > 1
				BEGIN 
					RAISERROR('Les CodeCommande revient a plusieurs clients.', 11, 1)
				END
			ELSE
				BEGIN
					SELECT @CodeClient=CodeClient, @NumWilaya=NumWilaya FROM
					(SELECT DISTINCT Commande.CodeClient, Client.NumWilaya 
					 FROM Commande JOIN Client ON Commande.CodeClient = Client.CodeClient 
					 WHERE CodeCommande IN (SELECT CodeCommande FROM @SplitsTable)) AS ClNw
				END

			Declare @p VARCHAR(12)
			SET NOCOUNT ON
			Select CodeProduit Into #Temp FROM @SplitsTable
			WHILE EXISTS(SELECT * FROM #Temp)
			BEGIN
				SELECT TOP 1 @p = CodeProduit From #Temp
				IF (SELECT COUNT(Produit.CodeProduit) FROM Produit WHERE Produit.CodeProduit=@p) = 0
					BEGIN
						RAISERROR('CodeProduit "%s" exist pas.', 11, 1, @p)
						BREAK
					END
				ELSE
					Delete #Temp Where #Temp.CodeProduit = @p
			END
			DROP TABLE #Temp

			SET @DateFacture = GETDATE()
			SET @RollingId = (SELECT ISNULL(MAX(Facture.RollingId), 0) + 1 FROM Facture FULL JOIN Client ON Client.CodeClient = @CodeClient WHERE DateFacture = @DateFacture AND NumWilaya = @NumWilaya)
			SET @CodeFacture = (SELECT CONCAT('F-', FORMAT(@DateFacture, 'yyMMdd'), '-', @NumWilaya, '-', @RollingId))

			INSERT INTO Facture(CodeFacture, DateFacture, ModePaiement, TauxTVA, DateEcheance, RollingId)
				VALUES (@CodeFacture, @DateFacture, @ModePaiement, @TauxTVA, @DateEcheance, @RollingId)
			INSERT INTO ProduitFacture SELECT CodeProduit, @CodeFacture AS CodeFacture, Quantite, Remise, CodeCommande, Etat FROM @SplitsTable
			SELECT 'succes' AS Result

			if XACT_STATE() = 1 and @trancount = 0
				commit;
		END TRY
		BEGIN CATCH
			EXEC CatchError;
			if XACT_STATE() <> 0 and @trancount = 0
				rollback;
			else
				throw;
		END CATCH
END
GO
ALTER PROCEDURE UpdateFacture (@CodeFacture VARCHAR(14),
							   @ModePaiement VARCHAR(20),
							   @TauxTVA DECIMAL(4, 2),
							   @DateEcheance DATE,
							   @CodeCommandeList VARCHAR(MAX),
							   @CodeProduitList VARCHAR(MAX),
							   @QuantiteList VARCHAR(MAX),
							   @QuantiteCartonList VARCHAR(MAX),
							   @QuantitePaletteList VARCHAR(MAX),
							   @RemiseList VARCHAR(MAX),
							   @EtatList VARCHAR(MAX))
AS								 
DECLARE @NewCodeFacture VARCHAR(14)
DECLARE @NumWilaya TINYINT
DECLARE @SplitsTable TABLE(CodeProduit VARCHAR(12), Quantite INT, Remise DECIMAL(4, 2), CodeCommande VARCHAR(17), Etat VARCHAR(17))
BEGIN
	SET NOCOUNT ON 
	SET XACT_ABORT ON
	DECLARE @trancount INT = @@trancount
	if @trancount = 0
		BEGIN tran
			BEGIN TRY
				INSERT INTO @SplitsTable
				SELECT CodeProduit, dbo.ToQuantiteUnite(CodeProduit, Quantite, QuantiteCarton, QuantitePalette) AS Quantite, ISNULL(CAST(Remise AS DECIMAL(4, 2)), 0) AS Remise, CodeCommande, Etat FROM
				(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS CodeProduit FROM STRING_SPLIT(@CodeProduitList, '|')) AS CP FULL JOIN
				(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS Quantite FROM STRING_SPLIT(@QuantiteList, '|')) AS QU ON QU.i = CP.i FULL JOIN
				(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS QuantiteCarton FROM STRING_SPLIT(@QuantiteCartonList, '|')) AS QC ON QC.i = CP.i FULL JOIN
				(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS QuantitePalette FROM STRING_SPLIT(@QuantitePaletteList, '|')) AS QP ON QP.i = CP.i FULL JOIN
				(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, CASE WHEN value='' THEN NULL ELSE value END AS Remise FROM STRING_SPLIT(@RemiseList, '|')) AS R ON R.i = CP.i FULL JOIN
				(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS CodeCommande FROM STRING_SPLIT(@CodeCommandeList, '|')) AS CC ON CC.i = CP.i FULL JOIN
				(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS Etat FROM STRING_SPLIT(@EtatList, '|')) AS EF ON EF.i = CP.i

				IF (SELECT COUNT(DISTINCT Commande.CodeClient) FROM Commande JOIN Client ON Commande.CodeClient = Client.CodeClient WHERE CodeCommande IN (SELECT CodeCommande FROM @SplitsTable)) > 1
					BEGIN 
						RAISERROR('Les CodeCommande revient a plusieurs clients.', 11, 1)
					END
				ELSE
					BEGIN
						SELECT @NumWilaya=NumWilaya FROM
						(SELECT DISTINCT Client.NumWilaya 
						 FROM Commande JOIN Client ON Commande.CodeClient = Client.CodeClient 
						 WHERE CodeCommande IN (SELECT CodeCommande FROM @SplitsTable)) AS ClNw
					END
				SET @NewCodeFacture = (SELECT CONCAT('F-', FORMAT((SELECT DateFacture FROM Facture WHERE CodeFacture = @CodeFacture), 'yyMMdd'), '-', @NumWilaya, '-', (SELECT RollingId FROM Facture WHERE CodeFacture = @CodeFacture)))
				Declare @p VARCHAR(12)
				SET NOCOUNT ON
				Select CodeProduit Into #Temp FROM @SplitsTable
				WHILE EXISTS(SELECT * FROM #Temp)
				BEGIN
					SELECT TOP 1 @p = CodeProduit From #Temp
					IF (SELECT COUNT(Produit.CodeProduit) FROM Produit WHERE Produit.CodeProduit=@p) = 0
						BEGIN
							RAISERROR('Produit "%s" exist pas.', 11, 1, @p)
							BREAK
						END
					ELSE
						Delete #Temp Where #Temp.CodeProduit = @p
				END
				DROP TABLE #Temp

				DELETE ProduitFacture WHERE CodeFacture=@CodeFacture

				UPDATE Facture SET CodeFacture=@NewCodeFacture, ModePaiement=@ModePaiement, TauxTVA=@TauxTVA, DateEcheance=@DateEcheance WHERE CodeFacture=@CodeFacture
				INSERT INTO ProduitFacture SELECT CodeProduit, @NewCodeFacture AS CodeFacture, Quantite, Remise, CodeCommande, Etat FROM @SplitsTable
				SELECT 'succes' AS Result

				if XACT_STATE() = 1 and @trancount = 0
					commit;
			END TRY
			BEGIN CATCH
				EXEC CatchError;
				if XACT_STATE() <> 0 and @trancount = 0
					rollback;
				else
					throw;
			END CATCH
END
GO
ALTER PROCEDURE DeleteFacture (@CodeFacture VARCHAR(14), @BruteForce BIT=0)
AS
BEGIN
	SET NOCOUNT ON 
	SET XACT_ABORT ON
	DECLARE @trancount INT = @@trancount

	if @trancount = 0
		BEGIN tran
	BEGIN TRY
		IF @BruteForce = 1
			BEGIN
				DELETE ProduitFacture WHERE ProduitFacture.CodeFacture=@CodeFacture;
			END
		DELETE Facture WHERE CodeFacture=@CodeFacture;

		SELECT 'succes' AS Result
		if XACT_STATE() = 1 and @trancount = 0
			commit;
	END TRY
	BEGIN CATCH
		EXEC CatchError;
		if XACT_STATE() <> 0 and @trancount = 0
			rollback;
		else
			throw;
	END CATCH
END
GO
--------Livraison
ALTER PROCEDURE InsertLivraison (@AddressLivraison NVARCHAR(MAX),
								 @CodeCommandeList VARCHAR(MAX),
							     @CodeProduitList VARCHAR(MAX),
								 @CodeEmplacementList VARCHAR(MAX),
								 @LotList VARCHAR(MAX),
							     @DateFabricationList VARCHAR(MAX),
							     @DateExpirationList VARCHAR(MAX),
								 
							     @QuantiteList VARCHAR(MAX),
							     @QuantiteCartonList VARCHAR(MAX),
							     @QuantitePaletteList VARCHAR(MAX),
								 
								 @QuantiteRecueList VARCHAR(MAX),
							     @QuantiteCartonRecueList VARCHAR(MAX),
							     @QuantitePaletteRecueList VARCHAR(MAX),
							     @TotalQuantiteRejeteeList VARCHAR(MAX),
								 @DescriptionProduitsRejeteeList VARCHAR(MAX))
AS
DECLARE @CodeLivraison VARCHAR(14)
DECLARE @RollingId TINYINT
DECLARE @NumWilaya TINYINT
DECLARE @DateLivraison DATE
DECLARE @SplitsTable TABLE(CodeProduit VARCHAR(12),
						   CodeEmplacement TINYINT,
						   Lot VARCHAR(10),
						   DateFabrication DATE, 
						   DateExpiration DATE, 
						   Quantite INT, 
						   QuantiteRecue INT,
						   TotalQuantiteRejetee INT,
						   DescriptionProduitsRejetee VARCHAR(MAX), 
						   CodeCommande VARCHAR(17))
BEGIN
	SET NOCOUNT ON
	SET XACT_ABORT ON
	DECLARE @trancount INT = @@trancount

	if @trancount = 0
		BEGIN tran
		BEGIN TRY
			
			SET @DateLivraison = GETDATE()

			INSERT INTO @SplitsTable SELECT CodeProduit, CodeEmplacement, NULLIF(Lot, ''), DateFabrication, DateExpiration,
											dbo.ToQuantiteUnite(CodeProduit, Quantite, QuantiteCarton, QuantitePalette) AS Qantite, 
											dbo.ToQuantiteUnite(CodeProduit, QuantiteRecue, QuantiteCartonRecue, QuantitePaletteRecue) AS QuantiteRecue,
											TotalQuantiteRejetee, DescriptionProduitsRejetee, CodeCommande FROM (
			(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS CodeProduit FROM STRING_SPLIT(@CodeProduitList, '|')) AS P FULL JOIN
			(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS CodeEmplacement FROM STRING_SPLIT(@CodeEmplacementList, '|')) AS CE ON CE.i = P.i FULL JOIN
			(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS Lot FROM STRING_SPLIT(@LotList, '|')) AS L ON L.i = P.i FULL JOIN
			(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS DateFabrication FROM STRING_SPLIT(@DateFabricationList, '|')) AS F ON F.i = P.i FULL JOIN
			(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS DateExpiration FROM STRING_SPLIT(@DateExpirationList, '|')) AS E ON E.i = P.i FULL JOIN
			(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS Quantite FROM STRING_SPLIT(@QuantiteList, '|')) AS QU ON QU.i = P.i FULL JOIN
			(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS QuantiteCarton FROM STRING_SPLIT(@QuantiteCartonList, '|')) AS QC ON QC.i = P.i FULL JOIN
			(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS QuantitePalette FROM STRING_SPLIT(@QuantitePaletteList, '|')) AS QP ON QP.i = P.i FULL JOIN
			(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS QuantiteRecue FROM STRING_SPLIT(@QuantiteRecueList, '|')) AS QUR ON QUR.i = P.i FULL JOIN
			(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS QuantiteCartonRecue FROM STRING_SPLIT(@QuantiteCartonRecueList, '|')) AS QCR ON QCR.i = P.i FULL JOIN
			(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS QuantitePaletteRecue FROM STRING_SPLIT(@QuantitePaletteRecueList, '|')) AS QPR ON QPR.i = P.i FULL JOIN
			(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS TotalQuantiteRejetee FROM STRING_SPLIT(@TotalQuantiteRejeteeList, '|')) AS TPC ON TPC.i = P.i FULL JOIN
			(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS DescriptionProduitsRejetee FROM STRING_SPLIT(@DescriptionProduitsRejeteeList, '|')) AS D ON D.i = P.i FULL JOIN
			(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS CodeCommande FROM STRING_SPLIT(@CodeCommandeList, '|')) AS CC ON CC.i = P.i)

			SET @NumWilaya = (SELECT TOP 1 NumWilaya FROM Commande LEFT JOIN Client ON Commande.CodeClient=Client.CodeClient WHERE Commande.CodeCommande IN (SELECT CodeCommande FROM @SplitsTable))

			SET @RollingId = (SELECT ISNULL(MAX(Livraison.RollingId), 0) + 1 FROM Livraison FULL JOIN ProduitLivraison ON Livraison.CodeLivraison = ProduitLivraison.CodeLivraison 
																								 JOIN Commande ON ProduitLivraison.CodeCommande=Commande.CodeCommande
																								 JOIN Client ON Client.CodeClient=Client.CodeClient 
							  WHERE Livraison.DateLivraison=@DateLivraison AND Client.NumWilaya=@NumWilaya)
			SET @CodeLivraison = (SELECT CONCAT('L-', FORMAT(@DateLivraison, 'yyMMdd'), '-', @NumWilaya, '-', @RollingId))

			Declare @p VARCHAR(12)
			Declare @d VARCHAR(10)
			Declare @q INT
			Declare @qr INT
			Declare @qc INT
			SET NOCOUNT ON
			SELECT CodeProduit, Quantite, DateFabrication, QuantiteRecue, TotalQuantiteRejetee INTO #Temp FROM @SplitsTable
			WHILE EXISTS(SELECT * FROM #Temp)
				BEGIN
					SELECT TOP 1 @p=CodeProduit, @q=Quantite, @d=DateFabrication, @qr=QuantiteRecue, @qc=TotalQuantiteRejetee FROM #Temp
					IF (SELECT COUNT(ProduitStock.CodeProduit) FROM ProduitStock WHERE ProduitStock.CodeProduit = @p AND ProduitStock.DateFabrication = @d) = 0
						BEGIN
							RAISERROR('Produit exist pas dont stock.
{CodeProduit: %s, DateFabrication: %s}', 11, 1, @p, @d)
						END
					ELSE
						IF (SELECT COUNT(ProduitStock.CodeProduit) FROM ProduitStock WHERE ProduitStock.CodeProduit = @p AND ProduitStock.Quantite >= @q) = 0
							BEGIN
								RAISERROR('Quantite insuffisant dans stock.
{CodeProduit: %s, DateFabrication: %s}', 11, 1, @p, @d)
							END
					IF (@qr + @qc) > @q
						BEGIN
								RAISERROR('QuantiteRecue > QuantiteLivree ?!
QuantiteLivree < (QuantiteRecue + TotalQuantiteRejetee)
{CodeProduit: %s, DateFabrication: %s}', 11, 1, @p, @d)
						END
					Delete #Temp Where #Temp.CodeProduit = @p AND DateFabrication = @d
				END
			DROP TABLE #Temp

			INSERT INTO Livraison(CodeLivraison, AddressLivraison, DateLivraison, RollingId) VALUES (@CodeLivraison, @AddressLivraison, @DateLivraison, @RollingId)

			INSERT INTO ProduitLivraison SELECT @CodeLivraison AS CodeLivraison, ST.CodeProduit, ST.CodeEmplacement, ST.Lot,
												ST.DateFabrication, ST.DateExpiration, ST.Quantite, ST.QuantiteRecue, 
												ST.TotalQuantiteRejetee, ST.DescriptionProduitsRejetee, ST.CodeCommande 
			FROM @SplitsTable AS ST
			SELECT 'succes' AS Result

			if XACT_STATE() = 1 and @trancount = 0
				commit;
		END TRY
		BEGIN CATCH
			EXEC CatchError;
			if XACT_STATE() <> 0 and @trancount = 0
				rollback;
			else
				throw;
		END CATCH
END
GO
ALTER PROCEDURE UpdateLivraison (@CodeLivraison VARCHAR(14),
								 @AddressLivraison NVARCHAR(MAX),
								 
								 @CodeCommandeList VARCHAR(MAX),
							     @CodeProduitList VARCHAR(MAX),
								 @CodeEmplacementList VARCHAR(MAX),
								 @LotList VARCHAR(MAX),
							     @DateFabricationList VARCHAR(MAX),
							     @DateExpirationList VARCHAR(MAX),
								 
							     @QuantiteList VARCHAR(MAX),
							     @QuantiteCartonList VARCHAR(MAX),
							     @QuantitePaletteList VARCHAR(MAX),
								 
								 @QuantiteRecueList VARCHAR(MAX),
							     @QuantiteCartonRecueList VARCHAR(MAX),
							     @QuantitePaletteRecueList VARCHAR(MAX),
							     @TotalQuantiteRejeteeList VARCHAR(MAX),
								 @DescriptionProduitsRejeteeList VARCHAR(MAX))
AS
DECLARE @NewCodeLivraison VARCHAR(14)
DECLARE @NumWilaya TINYINT
DECLARE @SplitsTable TABLE(CodeProduit VARCHAR(12),
						   CodeEmplacement TINYINT,
						   Lot VARCHAR(10),
						   DateFabrication DATE, 
						   DateExpiration DATE, 
						   Quantite INT, 
						   QuantiteRecue INT,
						   TotalQuantiteRejetee INT,
						   DescriptionProduitsRejetee VARCHAR(MAX), 
						   CodeCommande VARCHAR(17))
BEGIN
	SET NOCOUNT ON 
	SET XACT_ABORT ON
	DECLARE @trancount INT = @@trancount

	if @trancount = 0
		BEGIN tran
		BEGIN TRY
			
			INSERT INTO @SplitsTable SELECT CodeProduit, CodeEmplacement, NULLIF(Lot, ''), DateFabrication, DateExpiration,
											dbo.ToQuantiteUnite(CodeProduit, Quantite, QuantiteCarton, QuantitePalette) AS Qantite, 
											dbo.ToQuantiteUnite(CodeProduit, QuantiteRecue, QuantiteCartonRecue, QuantitePaletteRecue) AS QuantiteRecue,
											TotalQuantiteRejetee, DescriptionProduitsRejetee, CodeCommande FROM (
			(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS CodeProduit FROM STRING_SPLIT(@CodeProduitList, '|')) AS P FULL JOIN
			(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS CodeEmplacement FROM STRING_SPLIT(@CodeEmplacementList, '|')) AS CE ON CE.i = P.i FULL JOIN
			(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS Lot FROM STRING_SPLIT(@LotList, '|')) AS L ON L.i = P.i FULL JOIN
			(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS DateFabrication FROM STRING_SPLIT(@DateFabricationList, '|')) AS F ON F.i = P.i FULL JOIN
			(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS DateExpiration FROM STRING_SPLIT(@DateExpirationList, '|')) AS E ON E.i = P.i FULL JOIN
			(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS Quantite FROM STRING_SPLIT(@QuantiteList, '|')) AS QU ON QU.i = P.i FULL JOIN
			(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS QuantiteCarton FROM STRING_SPLIT(@QuantiteCartonList, '|')) AS QC ON QC.i = P.i FULL JOIN
			(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS QuantitePalette FROM STRING_SPLIT(@QuantitePaletteList, '|')) AS QP ON QP.i = P.i FULL JOIN
			(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS QuantiteRecue FROM STRING_SPLIT(@QuantiteRecueList, '|')) AS QUR ON QUR.i = P.i FULL JOIN
			(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS QuantiteCartonRecue FROM STRING_SPLIT(@QuantiteCartonRecueList, '|')) AS QCR ON QCR.i = P.i FULL JOIN
			(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS QuantitePaletteRecue FROM STRING_SPLIT(@QuantitePaletteRecueList, '|')) AS QPR ON QPR.i = P.i FULL JOIN
			(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS TotalQuantiteRejetee FROM STRING_SPLIT(@TotalQuantiteRejeteeList, '|')) AS TPC ON TPC.i = P.i FULL JOIN
			(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS DescriptionProduitsRejetee FROM STRING_SPLIT(@DescriptionProduitsRejeteeList, '|')) AS D ON D.i = P.i FULL JOIN
			(SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS i, Value AS CodeCommande FROM STRING_SPLIT(@CodeCommandeList, '|')) AS CC ON CC.i = P.i)

			SET @NumWilaya = (SELECT TOP 1 NumWilaya FROM Commande LEFT JOIN Client ON Commande.CodeClient=Client.CodeClient WHERE Commande.CodeCommande IN (SELECT CodeCommande FROM @SplitsTable))
			SET @NewCodeLivraison = (SELECT CONCAT('L-', FORMAT((SELECT DateLivraison FROM Livraison WHERE CodeLivraison = @CodeLivraison), 'yyMMdd'), '-', @NumWilaya, '-', (SELECT RollingId FROM Livraison WHERE CodeLivraison=@CodeLivraison)))

			Declare @p VARCHAR(12)
			Declare @d VARCHAR(10)
			Declare @q INT
			Declare @qr INT
			Declare @qc INT
			SET NOCOUNT ON
			SELECT CodeProduit, Quantite, DateFabrication, QuantiteRecue, TotalQuantiteRejetee INTO #Temp FROM @SplitsTable
			WHILE EXISTS(SELECT * FROM #Temp)
				BEGIN
					SELECT TOP 1 @p=CodeProduit, @q=Quantite, @d=DateFabrication, @qr=QuantiteRecue, @qc=TotalQuantiteRejetee FROM #Temp
					IF (SELECT COUNT(ProduitStock.CodeProduit) FROM ProduitStock WHERE ProduitStock.CodeProduit = @p AND ProduitStock.DateFabrication = @d) = 0
						BEGIN
							RAISERROR('Produit exist pas dont stock.
{CodeProduit: %s, DateFabrication: %s}', 11, 1, @p, @d)
						END
					ELSE
						IF (SELECT COUNT(ProduitStock.CodeProduit) FROM ProduitStock WHERE ProduitStock.CodeProduit = @p AND ProduitStock.Quantite >= @q) = 0
							BEGIN
								RAISERROR('Quantite insuffisant dans stock.
{CodeProduit: %s, DateFabrication: %s}', 11, 1, @p, @d)
							END
					IF (@qr + @qc) > @q
						BEGIN
								RAISERROR('QuantiteRecue > QuantiteLivree ?!
{CodeProduit: %s, DateFabrication: %s}', 11, 1, @p, @d)
						END
					Delete #Temp Where #Temp.CodeProduit = @p AND DateFabrication = @d
				END
			DROP TABLE #Temp

			DELETE ProduitLivraison WHERE CodeLivraison = @CodeLivraison

			UPDATE Livraison SET CodeLivraison=@NewCodeLivraison, AddressLivraison=@AddressLivraison WHERE CodeLivraison = @CodeLivraison
			INSERT INTO ProduitLivraison SELECT @CodeLivraison AS CodeLivraison, ST.CodeProduit, ST.CodeEmplacement, ST.Lot,
												ST.DateFabrication, ST.DateExpiration, ST.Quantite, ST.QuantiteRecue, 
												ST.TotalQuantiteRejetee, ST.DescriptionProduitsRejetee, ST.CodeCommande 
			FROM @SplitsTable AS ST
			SELECT 'succes' AS Result

			if XACT_STATE() = 1 and @trancount = 0
				commit;
		END TRY
		BEGIN CATCH
			EXEC CatchError;
			if XACT_STATE() <> 0 and @trancount = 0
				rollback;
			else
				throw;
		END CATCH
END
GO
ALTER PROCEDURE DeleteLivraison (@CodeLivraison VARCHAR(14), @BruteForce BIT=0)
AS
BEGIN
	SET NOCOUNT ON 
	SET XACT_ABORT ON
	DECLARE @trancount INT = @@trancount

	if @trancount = 0
		BEGIN tran
	BEGIN TRY
		IF @BruteForce = 1
			BEGIN
				DELETE ProduitLivraison WHERE ProduitLivraison.CodeLivraison=@CodeLivraison;
			END
		DELETE Livraison WHERE CodeLivraison=@CodeLivraison;

		SELECT 'succes' AS Result
		if XACT_STATE() = 1 and @trancount = 0
			commit;
	END TRY
	BEGIN CATCH
		EXEC CatchError;
		if XACT_STATE() <> 0 and @trancount = 0
			rollback;
		else
			throw;
	END CATCH
END
GO
--------
ALTER PROCEDURE StockFlowUpdater (@id VARCHAR(20), @CodeProduit VARCHAR(12))
AS
SET NOCOUNT ON 
SET XACT_ABORT ON
DECLARE @QuantiteRecue INT
DECLARE @QuantiteCasse INT
DECLARE @DateFabrication DATE
DECLARE @CodeEmplacement TINYINT
BEGIN
	DECLARE @trancount INT = @@trancount

	if @trancount = 0
		BEGIN tran
			BEGIN TRY
				IF LEFT(@id, 1) = 'L'
					BEGIN
						SELECT @CodeEmplacement=CodeEmplacement, @QuantiteRecue=QuantiteRecue, @QuantiteCasse=TotalQuantiteRejetee, @DateFabrication=DateFabrication FROM ProduitLivraison WHERE CodeLivraison = @id AND CodeProduit = @CodeProduit
						UPDATE ProduitStock SET Quantite -= (@QuantiteRecue + @QuantiteCasse)
						WHERE CodeEmplacement = @CodeEmplacement AND CodeProduit = @CodeProduit AND DateFabrication = @DateFabrication
					END
				ELSE
					BEGIN
						DECLARE @DateExpiration DATE
						DECLARE @Quantite INT
						DECLARE @QuantiteCarton INT 
						DECLARE @QuantitePalette INT 
						DECLARE @Lot VARCHAR(10)

						SELECT @CodeEmplacement=CodeEmplacement, @DateFabrication=DateFabrication, @DateExpiration=DateExpiration, @Quantite=QuantiteUnite, @QuantiteCarton=QuantiteCarton, @QuantitePalette=QuantitePalette, @Lot=Lot FROM InventaireView WHERE DateInventaire = @id
				
						EXEC InsertStock @CodeProduit, @CodeEmplacement, @DateFabrication, @DateExpiration, @Quantite, @QuantiteCarton, @QuantitePalette, @Lot
					END
				SELECT 'succes' AS Result
				IF XACT_STATE() = 1 and @trancount = 0
					commit;
			END TRY
			BEGIN CATCH
				EXEC CatchError;
				if XACT_STATE() <> 0 and @trancount = 0
					rollback;
				else
					throw;
			END CATCH
END
GO
-------------------------------------TESTING-----------------------------------------
