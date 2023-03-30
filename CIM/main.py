import os
import re
import sys
import webbrowser
from datetime import datetime
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSql import *
from bin import *
from jinja2 import Template
from num2words import num2words

PAGES = {
    'StockManager': ['Stock', 'MouvementStock', 'Livraison', 'Commande', 'report', 'analyse'],
    "InventorySupervisor": ['Produit', 'Inventaire'],
    "ServiceClient": ['Client', 'Stock', 'Commande', 'Livraison', 'Facture', 'report', 'analyse'],
    "SU": ['Produit', 'Stock', 'Inventaire', 'Client', 'Commande', 'Facture', 'Livraison', 'MouvementStock', 'report', 'analyse']
    }
USERS = {
    'Gestionnaire de stock': 'StockManager',
    "Superviseur de l'inventaire": 'InventorySupervisor',
    "Coordonnateur du service clientèle": 'ServiceClient',
    "dbo": 'SU',
}

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.loginForm = None
        self.authorizedPages = list()
        
        self.functions = Functions()
        self.threadPool = QThreadPool()

        self.pk = None
        self.ui.btnConnect.clicked.connect(self.checkConnection)
        self.functions.signals.error.connect(lambda msg: self.showMsg(msg, STYLE_ERROR_MSG))
        self.functions.signals.info.connect(lambda msg: self.showMsg(msg, STYLE_NOTICE_MSG))
        
        for btn in [self.ui.btnPageProduit, self.ui.btnPageStock, 
                    self.ui.btnPageInv, self.ui.btnPageMS, 
                    self.ui.btnPageClient, self.ui.btnPageCmd, 
                    self.ui.btnPageInsertCmd, self.ui.btnPageFacture,
                    self.ui.btnPageInsertFacture, self.ui.btnPageLiv,
                    self.ui.btnPageInsertLiv, self.ui.btnPageCharts, self.ui.btnPageReport]:
            btn.setVisible(False)
        
        for i in range(self.ui.toolBox.count()):
            self.ui.toolBox.setItemEnabled(i, False)
            
        self.info = {}
        self.setLoginWindow()
        ################
        ################

    def setLoginWindow(self):
        self.loginForm = LoginForm()
        self.loginForm.ui.btnClose.clicked.connect(self.closeAll)
        self.loginForm.ui.btnConnect.clicked.connect(self.login)
        self.loginForm.show()
    
    def login(self):
        QApplication.setOverrideCursor(Qt.WaitCursor)
        server = self.loginForm.ui.cBoxServerName.currentText().strip()
        user = USERS.get(self.loginForm.ui.cBoxPost.currentText())
        password = self.loginForm.ui.editPassword.text()
        if self.functions.setConnectionString(server, user, password):
            self.authorizedPages = PAGES.get(user)
            self.setAuthorizedPages()
            self.loadData()
            if self.loginForm.close():
                QApplication.restoreOverrideCursor()
                self.show()
        else:
            QApplication.restoreOverrideCursor()
            self.showMsg("La connexion a échoué. Veuillez vérifier vos identifiants de connexion et vous assurer que l'instance du serveur SQL est en cours d'exécution.", STYLE_ERROR_MSG)
        
    def closeAll(self):
        self.close()
        self.loginForm.close()
    
    def setAuthorizedPages(self):
        for page in self.authorizedPages:
            if page == 'Produit':
                self.info[page] = {
                'viewObj': self.ui.tableViewProduit, 
                'filterWidgets': (self.ui.cboxFilterProduit, self.ui.editFilterProduit, None), 
                'rangeFilterWidgets': {},
                'pkCols':('CodeProduit',),
                'widgets': (self.ui.cboxMarqueProduitInsert, 
                            self.ui.editNomProduitInsert, 
                            self.ui.cBoxTypeProduitInsert, 
                            self.ui.spinBoxPrixUProduitInsert, 
                            self.ui.spinBoxPoidsUProduitInsert,
                            self.ui.cBoxUPoidsProduitInsert,
                            self.ui.spinBoxCCProduitInsert,
                            self.ui.spinBoxCPProduitInsert),
                'mustCols': (('nom de produit', 1),),  # cols that must be inserted format: (colName, widget index)
                'extraWidgets': (self.ui.btnInsertProduit, self.ui.btnUpdateProduit, self.ui.labelInsertProduit, self.ui.pageInsertProduit),
                'sBoxFetchRows': (self.ui.sboxProduitFetchRows, '(SELECT NULL)')
                            }
                self.ui.btnPageProduit.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pageProduit))
                self.ui.refreshProduit.clicked.connect(lambda: self.loadView('Produit'))
                self.ui.btnPageProduitInsert.clicked.connect(lambda: self.setPageInsert('Produit'))
                self.ui.btnInsertProduit.clicked.connect(lambda: self.insertRecord('Produit'))
                self.ui.btnUpdateProduit.clicked.connect(lambda: self.updateRecord('Produit'))
                self.ui.btnRechProduit.clicked.connect(lambda: self.filterView('Produit'))
                self.ui.toolBox.setItemEnabled(0, True)   
                self.ui.btnPageProduit.setVisible(True)
                      
            elif page == 'Stock':
                self.info[page] = {
                'viewObj': self.ui.tableViewStock, 
                'filterWidgets': (self.ui.cboxFilterStock, self.ui.editFilterStock, self.ui.vBoxShowColsStock),
                'rangeFilterWidgets': {'DateFabrication': (self.ui.checkBoxDFfilterStock, self.ui.dateDFStockFilterT1, self.ui.dateDFStockFilterT2),
                                       'DateExpiration': (self.ui.checkBoxDEfilterStock, self.ui.dateDEStockFilterT1, self.ui.dateDEStockFilterT2),
                                        'Quantite': (self.ui.checkBoxQfilterStock, self.ui.sboxQStockFilterMin, self.ui.sboxQStockFilterMax, self.ui.cboxUQStockFilter)},
                'pkCols':('CodeProduit', 'CodeEmplacement', 'DateFabrication'),
                'widgets': (self.ui.cBoxCodeProduitStockInsert,
                            self.ui.cboxCodeEmpStockInsert,
                            self.ui.dateDFStockInsert,
                            self.ui.dateDEStockInsert,
                            self.ui.spinBoxQuantiteUStockInsert,
                            self.ui.spinBoxQuantiteCStockInsert,
                            self.ui.spinBoxQuantitePStockInsert,
                            self.ui.edtiLotStockInsert),
                'mustCols': (('CodeProduit', 0),),  # cols that must be inserted format: (colName, widget index)
                'extraWidgets': (self.ui.btnInsertStock, self.ui.btnUpdateStock, self.ui.labelInsertStock, self.ui.pageInsertStock),
                'sBoxFetchRows': (self.ui.sboxStockFetchRows, '(SELECT NULL)')
                            }
                self.ui.btnPageStock.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pageStock))
                self.ui.refreshStock.clicked.connect(lambda: self.loadView('Stock'))
                self.ui.btnPageStockInsert.clicked.connect(lambda: self.setPageInsert('Stock'))
                self.ui.btnInsertStock.clicked.connect(lambda: self.insertRecord('Stock'))
                self.ui.btnUpdateStock.clicked.connect(lambda: self.updateRecord('Stock'))
                self.ui.btnRechStock.clicked.connect(lambda: self.filterView('Stock'))
                self.ui.toolBox.setItemEnabled(0, True)
                self.ui.btnPageStock.setVisible(True)
                self.ui.stackedWidget.setCurrentWidget(self.ui.pageStock)
                
            elif page == 'Inventaire':
                self.info[page] = {
                'viewObj': self.ui.tableViewInv, 
                'filterWidgets': (self.ui.cboxFilterInv, self.ui.editFilterInv, self.ui.vBoxShowColsInv),
                'rangeFilterWidgets': {'DateFabrication': (self.ui.checkBoxDFfilterInv, self.ui.dateDFInvFilterT1, self.ui.dateDFInvFilterT2),
                                       'DateExpiration': (self.ui.checkBoxDEfilterInv, self.ui.dateDEInvFilterT1, self.ui.dateDEInvFilterT2),
                                        'Quantite': (self.ui.checkBoxQfilterInv, self.ui.sboxQInvFilterMin, self.ui.sboxQInvFilterMax, self.ui.cboxUQInvFilter)},
                'pkCols':('DateInventaire', 'CodeEmplacement', 'CodeProduit', 'DateFabrication'),
                'widgets': (None, 
                            self.ui.cboxCodeEmpInvInsert,
                            self.ui.cBoxCodeProduitInvInsert,
                            self.ui.dateDFInvInsert,
                            self.ui.dateDEInvInsert,
                            self.ui.spinBoxQuantiteUInvInsert,
                            self.ui.spinBoxQuantiteCInvInsert,
                            self.ui.spinBoxQuantitePInvInsert,
                            self.ui.cboxTypeInvInsert, 
                            self.ui.edtiLotInvInsert),
                'mustCols': (('CodeProduit', 0),),  # cols that must be inserted format: (colName, widget index)
                'extraWidgets': (self.ui.btnInsertInv, self.ui.btnUpdateInv, self.ui.labelInsertInv, self.ui.pageInsertInv),  # format (iBtn, uBtn, lbl, ipage)
                'sBoxFetchRows': (self.ui.sboxInvFetchRows, 'DateInventaire')
                }
                self.ui.btnPageInv.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pageInv))
                self.ui.refreshInv.clicked.connect(lambda: self.loadView('Inventaire'))
                self.ui.btnPageInvInsert.clicked.connect(lambda: self.setPageInsert('Inventaire'))
                self.ui.btnInsertInv.clicked.connect(lambda: self.insertRecord('Inventaire'))
                self.ui.btnUpdateInv.clicked.connect(lambda: self.updateRecord('Inventaire'))
                self.ui.btnRechInv.clicked.connect(lambda: self.filterView('Inventaire'))
                self.ui.toolBox.setItemEnabled(0, True)
                self.ui.btnPageInv.setVisible(True)
                self.ui.stackedWidget.setCurrentWidget(self.ui.pageInv)
                
            elif page == 'Client':
                self.info[page] = {
                'viewObj': self.ui.tableViewClient, 
                'filterWidgets': (self.ui.cboxFilterClient, self.ui.editFilterClient, None), 
                'rangeFilterWidgets': {},
                'pkCols':('CodeClient',),
                'widgets': (self.ui.cBoxNomAdvClientInsert, 
                            self.ui.pTEditDescClientInsert, 
                            self.ui.editNumTelClientInsert, 
                            self.ui.editEmailClientInsert, 
                            self.ui.spinBoxNumWilayaClientInsert),
                'mustCols': (('Description)', 1), ('Numéro de wilaya', 4),),  # cols that must be inserted format: (colName, widget index)
                'extraWidgets': (self.ui.btnInsertClient, self.ui.btnUpdateClient, self.ui.labelInsertClient, self.ui.pageInsertClient),  # format (iBtn, uBtn, lbl, ipage)
                'sBoxFetchRows': (self.ui.sboxClientFetchRows, '(SELECT NULL)')}
                self.ui.btnPageClient.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pageClient))
                self.ui.refreshClient.clicked.connect(lambda: self.loadView('Client'))
                self.ui.btnPageClientInsert.clicked.connect(lambda: self.setPageInsert('Client'))
                self.ui.btnInsertClient.clicked.connect(lambda: self.insertRecord('Client'))
                self.ui.btnUpdateClient.clicked.connect(lambda: self.updateRecord('Client'))
                self.ui.btnRechClient.clicked.connect(lambda: self.filterView('Client'))
                self.ui.toolBox.setItemEnabled(1, True)
                self.ui.btnPageClient.setVisible(True)
                           
            elif page == 'Commande':
                self.info[page] = {
                'viewObj': self.ui.tableViewCmd,
                'filterWidgets': (self.ui.cboxFilterCmd, self.ui.editFilterCmd, self.ui.vBoxShowColsCmd),
                'rangeFilterWidgets': {
                    'DateCommande': (self.ui.checkBoxDCfilterCmd, self.ui.dateDCCmdFilterT1, self.ui.dateDCCmdFilterT2),
                    'Quantite': (self.ui.checkBoxQfilterCmd, self.ui.sboxQCmdFilterMin, self.ui.sboxQCmdFilterMax, self.ui.cboxUQCmdFilter)},
                'pkCols':('CodeCommande',),
                'widgets': (self.ui.cBoxCodeClientCmdInsert, 
                            self.ui.cBoxModePaiementCmdInsert,
                            self.ui.tableWidgetCmd,
                            None,None,None),
                'mustCols': (),  # cols that must be inserted format: (colName, widget index)
                'extraWidgets': (self.ui.btnInsertCmd, self.ui.btnUpdateCmd, self.ui.labelInsertCmd, self.ui.pageInsertCommande),
                'calcWidgets': (self.ui.cboxCalcCmd,),
                'maskView': self.ui.checkBoxViewTypeCmd,
                'sBoxFetchRows': (self.ui.sboxCmdFetchRows, 'DateCommande'),
                            }
                self.ui.btnPageCmd.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pageCommande))
                self.ui.btnPageInsertCmd.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pageInsertCommande))
                self.ui.refreshCmd.clicked.connect(lambda: self.loadView('Commande'))
                self.ui.btnPageCmdInsert.clicked.connect(lambda: self.setPageInsert('Commande'))
                self.ui.btnInsertCmd.clicked.connect(lambda: self.insertRecord('Commande'))
                self.ui.btnUpdateCmd.clicked.connect(lambda: self.updateRecord('Commande'))
                self.ui.btnRechCmd.clicked.connect(lambda: self.filterView('Commande'))
                self.ui.btnAddRowCmd.clicked.connect(lambda: self.ui.tableWidgetCmd.insertRow(self.ui.tableWidgetCmd.rowCount()))
                self.ui.btnSubRowCmd.clicked.connect(lambda: self.removeSelectedRow(self.ui.tableWidgetCmd))
                self.ui.btnCalcCmd.clicked.connect(lambda: self.showCalcView('Commande'))
                self.ui.checkBoxViewTypeCmd.stateChanged.connect(lambda: self.loadView('Commande'))
                self.ui.tableWidgetCmd.cellDoubleClicked.connect(lambda row, column: self.setWidgetEdit(row, column, self.ui.tableWidgetCmd))
                self.ui.toolBox.setItemEnabled(2, True)
                self.ui.btnPageCmd.setVisible(True)
                self.ui.btnPageInsertCmd.setVisible(True)
                
            elif page == 'Facture':
                self.info[page] = {
                'viewObj': self.ui.tableViewFacture,
                'filterWidgets': (self.ui.cboxFilterFacture, self.ui.editFilterFacture, self.ui.vBoxShowColsFacture),
                'rangeFilterWidgets': {
                    'DateFacture': (self.ui.checkBoxDFfilterFacture, self.ui.dateDFFactureFilterT1, self.ui.dateDFFactureFilterT2),
                    'Quantite': (self.ui.checkBoxQfilterFacture, self.ui.sboxQFactureFilterMin, self.ui.sboxQFactureFilterMax, self.ui.cboxUQFactureFilter)},
                'pkCols':('CodeFacture',),
                'widgets': (self.ui.cBoxModePaiementFactureInsert,
                            self.ui.spinBoxTvaFactureInsert,
                            self.ui.dateEchFactureInsert,
                            self.ui.tableWidgetFacture,
                            None,None,None,None,None,None),
                'mustCols': (),  # cols that must be inserted format: (colName, widget index)
                'extraWidgets': (self.ui.btnInsertFacture, self.ui.btnUpdateFacture, self.ui.labelInsertFacture, self.ui.pageInsertFacture),
                'calcWidgets': (self.ui.cboxCalcFacture,),
                'maskView': self.ui.checkBoxViewTypeFacture,
                'sBoxFetchRows': (self.ui.sboxFactureFetchRows, 'DateFacture'),
                'addRowWidgets': (self.ui.cboxCodeLivFactureAdd, """SELECT CodeCommande, CodeProduit, QuantiteUnite, QuantiteCarton, QuantitePalette FROM FactureLivraisonViewFetch WHERE CodeLivraison=""", 5)}
                self.ui.btnPageFacture.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pageFacture))
                self.ui.btnPageInsertFacture.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pageInsertFacture))
                self.ui.refreshFacture.clicked.connect(lambda: self.loadView('Facture'))
                self.ui.btnPageFactureInsert.clicked.connect(lambda: self.setPageInsert('Facture'))
                self.ui.btnInsertFacture.clicked.connect(lambda: self.insertRecord('Facture'))
                self.ui.btnUpdateFacture.clicked.connect(lambda: self.updateRecord('Facture'))
                self.ui.btnRechFacture.clicked.connect(lambda: self.filterView('Facture'))
                self.ui.btnAddRowFacture.clicked.connect(lambda: self.addRow('Facture'))
                self.ui.btnSubRowFacture.clicked.connect(lambda: self.removeSelectedRow(self.ui.tableWidgetFacture))
                self.ui.btnCalcFacture.clicked.connect(lambda: self.showCalcView('Facture'))
                self.ui.checkBoxViewTypeFacture.stateChanged.connect(lambda: self.loadView('Facture'))
                self.ui.tableWidgetFacture.cellDoubleClicked.connect(lambda row, column: self.setWidgetEdit(row, column, self.ui.tableWidgetFacture))
                self.ui.toolBox.setItemEnabled(3, True)
                self.ui.btnPageFacture.setVisible(True)
                self.ui.btnPageInsertFacture.setVisible(True)
                
            elif page == 'Livraison':
                self.info[page] = {
                'viewObj': self.ui.tableViewLiv,
                'filterWidgets': (self.ui.cboxFilterLiv, self.ui.editFilterLiv, self.ui.vBoxShowColsLiv),
                'rangeFilterWidgets': {
                    'DateLivraison': (self.ui.checkBoxDLfilterLiv, self.ui.dateDLLivFilterT1, self.ui.dateDLLivFilterT2),
                    'QuantiteLivree': (self.ui.checkBoxQfilterLiv, self.ui.sboxQLivFilterMin, self.ui.sboxQLivFilterMax, self.ui.cboxUQLivFilter),
                    'QuantiteRecue': (self.ui.checkBoxQRfilterLiv, self.ui.sboxQRLivFilterMin, self.ui.sboxQRLivFilterMax, self.ui.cboxUQRLivFilter)},
                'pkCols':('CodeLivraison',),
                'widgets': (self.ui.editAddrLivInsert, 
                            self.ui.tableWidgetLiv,
                            None,None,None,None,None,None,None,None,None,None,None,None,None),
                'mustCols': (), 
                'extraWidgets': (self.ui.btnInsertLiv, self.ui.btnUpdateLiv, self.ui.labelInsertLiv, self.ui.pageInsertLiv),
                'calcWidgets': (self.ui.cboxCalcLiv,),
                'maskView': self.ui.checkBoxViewTypeLiv,
                'sBoxFetchRows': (self.ui.sboxLivFetchRows, 'DateLivraison'),
                'addRowWidgets': (self.ui.cboxCodeCmdLivAdd, """SELECT CodeCommandeList, CodeProduit,
                                            CodeEmplacement, Lot, DateFabrication, DateExpiration, 
                                            QuantiteUnite, QuantiteCarton, QuantitePalette
                                            FROM LivraisonCommandeViewFetch WHERE CodeCommande=""", 8)
                            }
                self.ui.btnPageLiv.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pageLiv))
                self.ui.btnPageInsertLiv.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pageInsertLiv))
                self.ui.refreshLiv.clicked.connect(lambda: self.loadView('Livraison'))
                self.ui.btnPageLivInsert.clicked.connect(lambda: self.setPageInsert('Livraison'))
                self.ui.btnInsertLiv.clicked.connect(lambda: self.insertRecord('Livraison'))
                self.ui.btnUpdateLiv.clicked.connect(lambda: self.updateRecord('Livraison'))
                self.ui.btnRechLiv.clicked.connect(lambda: self.filterView('Livraison'))
                self.ui.btnAddRowLiv.clicked.connect(lambda: self.addRow('Livraison'))
                self.ui.btnSubRowLiv.clicked.connect(lambda: self.removeSelectedRow(self.ui.tableWidgetLiv))
                self.ui.btnCalcLiv.clicked.connect(lambda: self.showCalcView('Livraison'))
                self.ui.checkBoxViewTypeLiv.stateChanged.connect(lambda: self.loadView('Livraison'))
                self.ui.tableWidgetLiv.cellDoubleClicked.connect(lambda row, column: self.setWidgetEdit(row, column, self.ui.tableWidgetLiv))
                self.ui.toolBox.setItemEnabled(4, True)
                self.ui.btnPageLiv.setVisible(True)
                self.ui.btnPageInsertLiv.setVisible(True)
                
            elif page == 'MouvementStock':
                self.info[page] = {
                'viewObj': self.ui.tableViewMS, 
                'filterWidgets': (self.ui.cboxFilterMS, self.ui.editFilterMS, None), 
                'rangeFilterWidgets': {'Date': (self.ui.checkBoxDfilterMs, self.ui.dateDMsFilterT1, self.ui.dateDMsFilterT2)},
                'sBoxFetchRows': (self.ui.sboxMsFetchRows, 'Date')
                            }
                self.ui.refreshMs.clicked.connect(lambda: self.loadView('MouvementStock'))
                self.ui.btnRechMs.clicked.connect(lambda: self.filterView('MouvementStock'))
                self.ui.btnPageMS.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pageMS))
                
                self.ui.toolBox.setItemEnabled(0, True)
                self.ui.btnPageMS.setVisible(True)
                
            elif page == 'report':
                self.ui.btnPageReport.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pageReport))
                self.ui.btnPageRepPrev.clicked.connect(self.generateReport)
                self.ui.btnPageRepNav.clicked.connect(lambda: self.generateReport(True))
                self.ui.toolBox.setItemEnabled(5, True)
                self.ui.btnPageReport.setVisible(True)
                
            elif page == 'analyse':
                self.canvas = Canvas(parent=self, layout=self.ui.chartArea)
                
                self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                
                self.ui.btnPageCharts.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pageAnalyseChart))
                self.ui.btnAnaLoadDf.clicked.connect(self.setupDfBtn)
                self.ui.cboxAnaCount.currentIndexChanged.connect(self.setCountPlotWidgets)
                self.ui.btnLoad.clicked.connect(self.threadLoadData)
                self.ui.btnAnaCountDisplay.clicked.connect(self.setCountPlot)
                self.ui.btnAnaTSDisplay.clicked.connect(self.setTsPlot)
                self.ui.toolBox.setItemEnabled(5, True)
                self.ui.btnPageCharts.setVisible(True)
            
            else:
                pass
    
    def generateReport(self, openInBrowser: bool=False):
        report = self.ui.cboxRep.currentText()
        code = self.ui.editRep.text().strip()
        if report == 'Facture':
            queryObj = self.functions.select(f"SELECT * FROM FactureReport WHERE CodeFacture = '{code}'")
            variables, table = self.functions.queryObjToJinja(queryObj, ['CodeProduit', 'DescriptionProduit', 'Quantite', 'PrixUnitaire', 'Remise', 'PrixNet', 'MontantHT'], ['CodeCommande'])
            if table:
                with open(os.getcwd()+'\\templates\\Facture.html', 'r') as template:
                    factureTemplate = Template(template.read())
                    
                variables['TTC_TXT'] = num2words(float(variables['TTC'].replace('\xa0', '').replace(',', '.').replace(' ', '')), lang='fr')
                html = factureTemplate.render(variables=variables, table=table)
                self.ui.reportView.setHtml('')
                self.ui.reportView.setHtml(html)
                
                if openInBrowser:
                    with open("templates\FactureReport.html", 'w') as report:
                        report.write(html)
                    webbrowser.open('file://' + os.path.realpath("templates\FactureReport.html"))
            else:
                self.showMsg("Code Facture est incorrect!", STYLE_NOTICE_MSG)
                
    def setTsPlot(self):
        plotName = self.ui.cboxAnaTS.currentText()
        series, title = self.functions.ts(plotName)
        if series is not None:
            if 'Saisonnalité' in plotName:
                self.canvas.seasonalPlot(seasons=series, yLabel='montantHT', figTitle=title)
            elif 'Tendance' in plotName:
                self.canvas.trendPlot(series, figTitle=title)
            
    def setCountPlot(self):
        plotName, datePartition, kind = self.ui.cboxAnaCount.currentText(), self.ui.cboxAnaCountPerDate.currentText(), self.ui.cboxAnaCountChartType.currentText()
        argStr, func = self.ui.editAnaCountValue.text().strip(), self.ui.cboxAnaCountFunc.currentText()

        argList = [s.strip() for s in argStr.split(',')]
        grp, title = self.functions.countGrp(plotName=plotName, datePartition=datePartition, extraArg=argList, func=func)
        if grp is not None:
            self.canvas.countPlot(df=grp, kind=kind, title=title)

    def setCountPlotWidgets(self):
        countPlotName = self.ui.cboxAnaCount.currentText()
        if 'client' in countPlotName:
            self.ui.editAnaCountValue.setPlaceholderText("List de CodeClient ex: 161, 61, 162")
            self.ui.editAnaCountValue.setEnabled(True)
            if 'dépensé' in countPlotName:
                self.ui.cboxAnaCountFunc.setEnabled(True)
                self.ui.cboxAnaCountFunc.setCurrentIndex(0)
            else:
                self.ui.cboxAnaCountFunc.setEnabled(False)
                self.ui.cboxAnaCountFunc.setCurrentIndex(-1)
        elif 'produit' in countPlotName:
            self.ui.editAnaCountValue.setPlaceholderText("List de CodeProduit ex: 1-100G-1, 1-100G-2")
            self.ui.editAnaCountValue.setEnabled(True)
            self.ui.cboxAnaCountFunc.setEnabled(True)
            self.ui.cboxAnaCountFunc.setCurrentIndex(1)
        elif 'mode de paiement' in countPlotName:
            self.ui.editAnaCountValue.setPlaceholderText("")
            self.ui.cboxAnaCountFunc.setEnabled(True)
            self.ui.cboxAnaCountFunc.setCurrentIndex(0)
        else:
            self.ui.editAnaCountValue.setPlaceholderText("")
            self.ui.editAnaCountValue.setEnabled(False)
            self.ui.cboxAnaCountFunc.setEnabled(False)
            self.ui.cboxAnaCountFunc.setCurrentIndex(-1)

    def threadLoadData(self):
        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.loadData()
        QApplication.restoreOverrideCursor()

    def setupDfBtn(self):
        btn = self.sender()
        d1 = self.ui.dateAnaLoadD1.date().toString('yyyy-MM-dd')
        d2 = self.ui.dateAnaLoadD2.date().toString('yyyy-MM-dd')
        
        worker = Worker(self.functions.setDataFrame, 0, d1, d2)
        worker.signals.started.connect(lambda: QApplication.setOverrideCursor(Qt.BusyCursor))
        worker.signals.finished.connect(QApplication.restoreOverrideCursor)
        worker.signals.results.connect(lambda r: 
            (btn.setStyleSheet(btn.styleSheet().replace("data-manipulation-language-100.png", "checkpoint-100.png")), 
             self.showMsg('Données chargées avec succès', STYLE_SUCCESS_MSG)) if r else 
            (btn.setStyleSheet(btn.styleSheet().replace("checkpoint-100.png", "data-manipulation-language-100.png")), 
             self.showMsg("Les données n'ont pas été chargées correctement", STYLE_NOTICE_MSG)))
        self.threadPool.start(worker)
        self.showMsg("Cette opération peut prendre un certain temps\nnous vous informerons lorsqu'elle sera effectuée", STYLE_NOTICE_MSG)
        
    def addRow(self, tableName: str):
        tableWidget = next(filter(lambda x: x is not None, reversed(self.info[tableName]['widgets'])))
        addCbox, queryStr, colCount = self.info[tableName]['addRowWidgets']
        if addCbox.currentText() == 'Ligne vide':
            tableWidget.insertRow(tableWidget.rowCount())
        else:
            value = addCbox.currentText()
            queryObj = self.functions.select(f"{queryStr}'{value}'")
            while queryObj.next():
                values = [queryObj.value(iCol) for iCol in range(queryObj.record().count())]
                self.loadTableWidget(tableWidget, values, colCount)

    def showCalcView(self, tableName: str):
        calcView = self.info[tableName]['calcWidgets'][0].currentText()
        sBox, _ = self.info[tableName]['sBoxFetchRows']
        fetchRows =  f"ORDER BY (SELECT NULL) DESC OFFSET 0 ROWS FETCH NEXT {sBox.value()} ROWS ONLY;"
        model = self.functions.loadQuery(f"SELECT '','', * FROM {tableName}{calcView} {fetchRows}")
        self.info[tableName]['viewObj'].setModel(model)
        for i in range(model.columnCount()):
            self.info[tableName]['viewObj'].resizeColumnToContents(i)
        self.setCbox(tableName)
        
        if tableName == 'Facture':
            self.FactureEtat()
            
    def FactureEtat(self):
        factureView = self.info['Facture']['viewObj']
        factureViewModel = factureView.model()
        EtatIndex = -1
        for iCol in range(factureViewModel.columnCount()):
            if factureViewModel.headerData(iCol, Qt.Orientation.Horizontal) == 'Etat':
                EtatIndex= iCol
        factureView.setItemDelegate(FactureColorPalette(EtatIndex))
        
    def removeSelectedRow(self, tableWidget):
        rows = tableWidget.selectionModel().selectedRows()
        if rows:
            tableWidget.removeRow(rows[0].row())
            
    def multiFilters(self, tableName: str):
        widgetDict = self.info[tableName]['rangeFilterWidgets']
        where = ""
        for col, wlist in widgetDict.items():
            if wlist[0].isChecked():
                values = self.collectValues(wlist[1:])
                if 'Quantite' in col:
                    where += f"({col+values[2]} BETWEEN '{values[0]}' AND '{values[1]}')AND"
                else:
                    where += f"({col} BETWEEN '{values[0]}' AND '{values[1]}')AND"
        if where:
            where = where.strip('AND')
            mask = self.info[tableName].get('maskView')
            if mask and mask.isChecked():
                mask = ''
            else:
                mask = 'View'
            sBox, orderCol = self.info[tableName]['sBoxFetchRows']
            fetchRows =  f"ORDER BY {orderCol} DESC OFFSET 0 ROWS FETCH NEXT {sBox.value()} ROWS ONLY;"
            model = self.functions.loadQuery(f"SELECT '', '', * FROM {tableName}{mask} WHERE {where} {fetchRows}")

            self.info[tableName]['viewObj'].setModel(model)
            self.resizeCols(tableName, model.columnCount())
            
    def filterView(self, tableName: str):
        self.multiFilters(tableName)
        cBoxFilter, editFilter, _ = self.info[tableName]['filterWidgets']
        iCol = cBoxFilter.currentIndex()
        if iCol == -1:
            cBoxFilter.setStyleSheet(cBoxFilter.styleSheet().replace('rgb(200, 200, 200)', 'rgb(255, 44, 83)'))
        else:
            cBoxFilter.setStyleSheet(cBoxFilter.styleSheet().replace('rgb(255, 44, 83)', 'rgb(200, 200, 200)'))
            model = self.info[tableName]['viewObj'].model()
            model.setFilterKeyColumn(iCol + 1 if tableName == 'MouvementStock' else iCol + 2)
            model.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
            col = cBoxFilter.currentText()
            if col.startswith("Prix") or col.startswith("Quantite") or col.startswith("Capacite"):
                model.setFilterRegularExpression(f"^{editFilter.text()}")
            else:
                pattern = "".join([f'(?=.*{w})' for w in editFilter.text().split(' ')])
                model.setFilterRegularExpression(pattern)

    def updateRecord(self, tableName: str):
        values = list()
        values.extend(self.pk)
        cValues = self.collectValues(self.info[tableName]['widgets'])
        values.extend(cValues)
        for i in range(len(cValues)):
            if not cValues[i]:
                for col, iCol in self.info[tableName]['mustCols']:
                    if i == iCol:
                        self.showMsg(f'Insérer le champ ({col})', STYLE_ERROR_MSG)
                        return
        result = self.functions.execProcedure(f'Update{tableName}', values)
        if result == 'succes':
            self.showMsg(f'{tableName} modifier avec succès', STYLE_SUCCESS_MSG)
            self.loadView(tableName)
        elif 'conflicted with the REFERENCE constraint' in result:
            tableRef = re.findall('"FK_([^"]*)"', result)[0].split('_')[0]
            self.showMsg(f'Il y a une référence de cet enregistrement sur la table {tableRef}', STYLE_NOTICE_MSG)
        elif 'Violation of PRIMARY KEY constraint' in result:
            self.showMsg(f'{tableName} existe déjà', STYLE_NOTICE_MSG)
        elif 'conflicted with the FOREIGN KEY constraint' in result:
            pkCol = re.findall("column '(\w+)'", result)[0]
            self.showMsg(f'{pkCol} existe pas', STYLE_NOTICE_MSG)
        elif 'Cannot insert the value NULL' in result:
            col = re.findall("column '(\w+)'", result)[0]
            self.showMsg(f'insérer la column "{col}"', STYLE_NOTICE_MSG)
        elif 'CheckEtatFacture' in result:
            self.showMsg(f"Insérer l'état de facture", STYLE_NOTICE_MSG)
        else:
            self.showMsg(result, STYLE_ERROR_MSG)

    def setPageInsert(self, tableName: str, jumpToPage: bool=True):
        self.resetWidgets(tableName)
        iBtn, uBtn, lbl, iPage = self.info[tableName]['extraWidgets']
        iBtn.setHidden(False)
        uBtn.setHidden(True)
        lbl.setText(lbl.text().replace('Modifier', 'Insérer'))
        if jumpToPage:
            self.ui.stackedWidget.setCurrentWidget(iPage)
        
    def loadData(self):
        for key in self.info.keys():
            self.loadView(key)
            rangeFilterWidgets = self.info[key]['rangeFilterWidgets']
            for col in rangeFilterWidgets.keys():
                rangeFilterWidgets[col][0].setChecked(False)
            if key == 'MouvementStock':
                pass
            else:
                self.setPageInsert(key, False)
                
        self.fillCbox()
        
        if 'Stock' in self.authorizedPages:
            stockView = self.info['Stock']['viewObj']
            stockViewModel = stockView.model()
            DerniereInventaireIndex, QuantitePaletteIndex = -1, -1
            for iCol in range(2, stockViewModel.columnCount()):
                if stockViewModel.headerData(iCol, Qt.Orientation.Horizontal) == 'DerniereInventaire':
                    DerniereInventaireIndex = iCol
                if stockViewModel.headerData(iCol, Qt.Orientation.Horizontal) == 'QuantitePalette':
                    QuantitePaletteIndex = iCol
            
            stockView.setItemDelegate(StockColorPalette(DerniereInventaireIndex, QuantitePaletteIndex))
        
        queryObj = self.functions.select('SELECT * FROM TsLength')
        queryObj.next()
        minDate = datetime.strptime(queryObj.value(0), '%Y-%m-%d').date()
        maxDate = datetime.strptime(queryObj.value(1), '%Y-%m-%d').date()
        self.ui.dateAnaLoadD1.setMinimumDate(minDate)
        self.ui.dateAnaLoadD1.setMaximumDate(maxDate)
        self.ui.dateAnaLoadD1.setDate(minDate)
        
        self.ui.dateAnaLoadD2.setMinimumDate(minDate)
        self.ui.dateAnaLoadD2.setMaximumDate(maxDate)
        self.ui.dateAnaLoadD2.setDate(maxDate)
        
        self.ui.editAnaCountValue.setEnabled(False)
        self.ui.cboxAnaCountFunc.setEnabled(False)
        self.ui.cboxAnaCountFunc.setCurrentIndex(-1)
        self.ui.checkBoxAnaGroupe.setChecked(False)
        self.ui.checkBoxAnaTS.setChecked(False)
        
    def setWidgetEdit(self, row, column, tableWidget):
        colItem = tableWidget.horizontalHeaderItem(column)
        if colItem is not None:
            colName = colItem.text()
            if 'Date' in colName:
                dateEdit = QDateEdit()
                dateEdit.setDisplayFormat("yyyy-M-d")
                item = tableWidget.item(row, column)
                if item:
                    date = datetime.strptime(item.text(), '%Y-%m-%d').date()
                else:
                    date = datetime.now().date()
                dateEdit.setDate(date)
                tableWidget.setCellWidget(row, column, dateEdit)
                dateEdit.setFocus()
                dateEdit.editingFinished.connect(lambda: self.removeWidgetEdit(row, column, dateEdit, tableWidget))
            elif ('Quantite' in colName) or ('Unite' in colName):
                spinBox = QSpinBox()
                spinBox.setMinimum(0)
                spinBox.setMaximum(999999999)
                item = tableWidget.item(row, column)
                if item:
                    value = int(item.text())
                else:
                    value = 0
                spinBox.setValue(value)
                tableWidget.setCellWidget(row, column, spinBox)
                spinBox.setFocus()
                spinBox.editingFinished.connect(lambda: self.removeWidgetEdit(row, column, spinBox, tableWidget))
                
            elif 'Remise' in colName:
                doubleSpinBox = QDoubleSpinBox()
                doubleSpinBox.setMinimum(0)
                doubleSpinBox.setMaximum(100)
                item = tableWidget.item(row, column)
                if item:
                    value = float(item.text())
                else:
                    value = 0
                doubleSpinBox.setValue(value)
                tableWidget.setCellWidget(row, column, doubleSpinBox)
                doubleSpinBox.setFocus()
                doubleSpinBox.editingFinished.connect(lambda: self.removeWidgetEdit(row, column, doubleSpinBox, tableWidget))
            elif 'Etat' in colName:
                cBox = QComboBox()
                cBox.insertItem(0, 'NonPaye')
                cBox.insertItem(1, 'Paye')
                item = tableWidget.item(row, column)
                if item:
                    cBox.setCurrentText(item.text())
                else:   
                    cBox.setCurrentIndex(0)
                tableWidget.setCellWidget(row, column, cBox)
                tableWidget.setItem(row, column, QTableWidgetItem(cBox.currentText()))
                cBox.setFocus()
                cBox.currentIndexChanged.connect(lambda: self.removeWidgetEdit(row, column, cBox, tableWidget))

    def removeWidgetEdit(self, row, column, widget, tableWidget):
        if widget.metaObject().className() == 'QDateEdit':
            item = QTableWidgetItem(widget.text())
            tableWidget.setItem(row, column, item)
            tableWidget.removeCellWidget(row, column)
        elif widget.metaObject().className() in ('QSpinBox', 'QDoubleSpinBox'):
            item = QTableWidgetItem(str(widget.value()))
            tableWidget.setItem(row, column, item)
            tableWidget.removeCellWidget(row, column)
        elif widget.metaObject().className() == 'QComboBox':
            item = QTableWidgetItem(widget.currentText())
            tableWidget.setItem(row, column, item)
            tableWidget.removeCellWidget(row, column)
            
    def collectValues(self, widgets):
        values = list()
        for widget in widgets:
            if widget == None:
                continue
            if widget.metaObject().className() == 'QLineEdit':
                values.append(widget.text().strip())
            if widget.metaObject().className() == 'QPlainTextEdit':
                values.append(widget.toPlainText().strip())
            elif widget.metaObject().className() == 'QComboBox':
                values.append(widget.currentText())
            elif widget.metaObject().className() == 'QDoubleSpinBox':
                values.append(widget.value())
            elif widget.metaObject().className() == 'QSpinBox':
                values.append(widget.value())
            elif widget.metaObject().className() == 'QDateEdit':
                values.append(widget.text())
            elif widget.metaObject().className() == 'QDateTimeEdit':
                values.append(widget.text())
            elif widget.metaObject().className() == 'QTableWidget':
                for col in range(widget.columnCount()):
                    v = ''
                    for row in range(widget.rowCount()):
                        v += '|'
                        if widget.item(row, col):
                            v += widget.item(row, col).text().strip()   
                    values.append(v[1:])
        return values
    
    def insertRecord(self, tableName: str):
        values = self.collectValues(self.info[tableName]['widgets'])
        for i in range(len(values)):
            if not values[i]:
                for col, iCol in self.info[tableName]['mustCols']:
                    if i == iCol:
                        self.showMsg(f'Insérer le {col}', STYLE_ERROR_MSG)
                        return

        result = self.functions.execProcedure(f'Insert{tableName}', values)
        if result == 'succes':
            self.showMsg(f'{tableName} inséré avec succès', STYLE_SUCCESS_MSG)
            self.loadView(tableName)
        elif 'Violation of PRIMARY KEY constraint' in result:
            self.showMsg(f'{tableName} existe déjà', STYLE_NOTICE_MSG)
        elif 'conflicted with the FOREIGN KEY constraint' in result:
            pkCol = re.findall("column '(\w+)'", result)[0]
            self.showMsg(f'{pkCol} existe pas', STYLE_NOTICE_MSG)
        elif 'CheckEtatFacture' in result:
            self.showMsg(f"Insérer l'état de facture", STYLE_NOTICE_MSG)
        else:
            self.showMsg(result, STYLE_ERROR_MSG)

    def fillCbox(self):
        if 'Produit' in self.authorizedPages:
            queryObj = self.functions.select("SELECT NomMarque Type FROM Marque")
            self.ui.cboxMarqueProduitInsert.clear()
            while queryObj.next():
                self.ui.cboxMarqueProduitInsert.addItem(queryObj.value(0))
            self.ui.cboxMarqueProduitInsert.setCurrentIndex(0)
            
        if 'Client' in self.authorizedPages:
            queryObj = self.functions.select("SELECT CONCAT(Depot, ': ', NomComplet) Type FROM Adv")
            self.ui.cBoxNomAdvClientInsert.clear()
            while queryObj.next():
                self.ui.cBoxNomAdvClientInsert.addItem(queryObj.value(0))
            self.ui.cBoxNomAdvClientInsert.setCurrentIndex(0)
            
        if 'Commande' in self.authorizedPages:
            queryObj = self.functions.select("SELECT CodeClient FROM Client")
            self.ui.cBoxCodeClientCmdInsert.clear()
            while queryObj.next():
                self.ui.cBoxCodeClientCmdInsert.addItem(str(queryObj.value(0)))
            self.ui.cBoxCodeClientCmdInsert.setCurrentIndex(0)
            
        if 'Stock' in self.authorizedPages:
            queryObj = self.functions.select("SELECT CodeProduit FROM Produit")
            self.ui.cBoxCodeProduitStockInsert.clear()
            while queryObj.next():
                value = queryObj.value(0)
                self.ui.cBoxCodeProduitStockInsert.addItem(value)
            self.ui.cBoxCodeProduitStockInsert.setCurrentIndex(0)

            queryObj = self.functions.select("SELECT CodeEmplacement FROM Stock")
            self.ui.cboxCodeEmpStockInsert.clear()
            while queryObj.next():
                value = str(queryObj.value(0))
                self.ui.cboxCodeEmpStockInsert.addItem(value)
            self.ui.cboxCodeEmpStockInsert.setCurrentIndex(0)
            
        if 'Inventaire' in self.authorizedPages:
            queryObj = self.functions.select("SELECT CodeEmplacement FROM Stock")
            self.ui.cboxCodeEmpInvInsert.clear()
            while queryObj.next():
                value = str(queryObj.value(0))
                self.ui.cboxCodeEmpInvInsert.addItem(value)
            self.ui.cboxCodeEmpInvInsert.setCurrentIndex(0)
    
            queryObj = self.functions.select("SELECT CodeProduit FROM Produit")
            self.ui.cBoxCodeProduitInvInsert.clear()
            while queryObj.next():
                value = queryObj.value(0)
                self.ui.cBoxCodeProduitInvInsert.addItem(value)
            self.ui.cBoxCodeProduitInvInsert.setCurrentIndex(0)
            
    def resetWidgets(self, tableName: str):
        for widget in self.info[tableName]['widgets']:
            if widget == None:
                continue
            if widget.metaObject().className() in ('QLineEdit', 'QPlainTextEdit'):
                widget.clear()
            elif widget.metaObject().className() == 'QComboBox':
                widget.setCurrentIndex(0)
            elif widget.metaObject().className() == 'QDoubleSpinBox':
                widget.setValue(0)
            elif widget.metaObject().className() == 'QSpinBox':
                widget.setValue(0)
            elif widget.metaObject().className() == 'QDateEdit':
                widget.dateTimeFromText(datetime.today().strftime('%m-%d-%Y'))
            elif widget.metaObject().className() == 'QDateTimeEdit':
                widget.dateTimeFromText(datetime.today().strftime('%m-%d-%Y %H:%M'))
            elif widget.metaObject().className() == 'QTableWidget':
                widget.clearContents()
                widget.setRowCount(0)

    @staticmethod
    def clearLayout(layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
    
    def setCbox(self, tableName: str):
        cBoxFilter, _, vBoxShow = self.info[tableName]['filterWidgets']
        cBoxFilter.clear()
        if vBoxShow:
            self.clearLayout(vBoxShow)
            self.cBoxShow = CheckableComboBox()
            vBoxShow.addWidget(self.cBoxShow)
            self.cBoxShow.view().pressed.connect(lambda: self.setHiddenCols(tableName))
            
        model = self.info[tableName]['viewObj'].model()
        for i in range(model.columnCount()):
            col = model.headerData(i, Qt.Orientation.Horizontal)
            if col:
                cBoxFilter.addItem(model.headerData(i, Qt.Orientation.Horizontal))
                if vBoxShow:
                    self.cBoxShow.addItem(model.headerData(i, Qt.Orientation.Horizontal))
                    self.cBoxShow.setItemChecked(i-2, True)
                
    def setHiddenCols(self, tableName: str):
        cbox = self.info[tableName]['filterWidgets'][2].itemAt(0).widget()
        viewObj = self.info[tableName]['viewObj']
        model = viewObj.model()
        for i in range(2, model.columnCount()):
            if cbox.itemChecked(i-2):
                viewObj.setColumnHidden(i, False)
                viewObj.resizeColumnToContents(i)
            else:
                viewObj.setColumnHidden(i, True)
        
    def loadView(self, tableName: str):
        mask = self.info[tableName].get('maskView')
        sBox, orderCol = self.info[tableName]['sBoxFetchRows']
        fetchRows =  f"ORDER BY {orderCol} DESC OFFSET 0 ROWS FETCH NEXT {sBox.value()} ROWS ONLY;"
        if mask and mask.isChecked():
            model = self.functions.loadQuery(query=f"SELECT '', '', * FROM {tableName} {fetchRows}")
            model.removeColumn(model.columnCount()-1)
        else:
            model = self.functions.loadQuery(query=f"SELECT '', '', * FROM {tableName}View {fetchRows}")
        
        self.info[tableName]['viewObj'].setModel(model)
        self.resizeCols(tableName, model.columnCount())
        self.setCbox(tableName)
    
        if tableName == 'Facture':
            self.FactureEtat()
        
    def resizeCols(self, tableName, colCount: int):
        tavleView = self.info[tableName]['viewObj']
        for i in range(colCount):
            tavleView.resizeColumnToContents(i)
            
        if tableName == 'MouvementStock':
            self.addMsFlowBtns()
        else:
            self.info[tableName]['viewObj'].selectionModel().selectionChanged.connect(lambda: self.addTableBtns(tableName))

    def addMsFlowBtns(self):
        tableViewObj = self.info['MouvementStock']['viewObj']
        model = tableViewObj.model()
        model.removeColumn(0)
        for i in range(model.rowCount()):            
            data = model.data(model.index(i, 1))
            if data == 'Sortie':
                style = STYLE_BTN_FLOW_OUT
                toolTip = 'Retirer du stock'
            else:
                style = STYLE_BTN_FLOW_IN
                toolTip = 'Ajouter au stock'

            self.ui.btnFlow = viewBtn(style, toolTip)
            self.ui.containerFlow = QWidget()
            self.ui.vBoxFlow = QVBoxLayout()
            self.ui.vBoxFlow.setContentsMargins(0, 0, 0, 0)
            self.ui.containerFlow.setLayout(self.ui.vBoxFlow)
            self.ui.vBoxFlow.addWidget(self.ui.btnFlow)
            tableViewObj.setIndexWidget(model.index(i, 0), self.ui.containerFlow)
            
            self.ui.btnFlow.id.append(tableViewObj.model().index(i, 3).data())
            self.ui.btnFlow.id.append(tableViewObj.model().index(i, 4).data())
            self.ui.btnFlow.clicked.connect(self.msBulk)

    def msBulk(self):
        pk = self.sender().id
        msg = self.showMsg(f"Confirmer la mis à jour du stock\nPour ({', '.join(pk)})", STYLE_NOTICE_MSG, [QMessageBox.Yes, QMessageBox.No])
        if msg == QMessageBox.Yes:
            result = self.functions.execProcedure(f'StockFlowUpdater', pk)
            if result == 'succes':
                self.showMsg(f'Succès', STYLE_SUCCESS_MSG)
            else:
                self.showMsg(result, STYLE_ERROR_MSG)
    
    def addTableBtns(self, tableName: str):
        tableViewObj = self.info[tableName]['viewObj']
        for i in range(tableViewObj.model().rowCount()):
            if tableViewObj.indexWidget(tableViewObj.model().index(i, 0)):
                tableViewObj.setIndexWidget(tableViewObj.model().index(i, 0), None)
                tableViewObj.setIndexWidget(tableViewObj.model().index(i, 1), None)
        
        selectedRows = tableViewObj.selectionModel().selectedRows()
        if len(selectedRows) == 0:  # pyside6 bug
            return
        iRow = selectedRows[0].row()
        
        self.ui.btnDel = viewBtn(STYLE_BTN_DEL, "Supprimer")
        self.ui.containerDel = QWidget()
        self.ui.vBoxDel = QVBoxLayout()
        self.ui.vBoxDel.setContentsMargins(0, 0, 0, 0)
        self.ui.containerDel.setLayout(self.ui.vBoxDel)
        self.ui.vBoxDel.addWidget(self.ui.btnDel)
        tableViewObj.setIndexWidget(tableViewObj.model().index(iRow, 0), self.ui.containerDel)
        
        self.ui.btnEdit = viewBtn(STYLE_BTN_EDIT, "Modifier")        
        self.ui.containerEdit = QWidget()
        self.ui.vBoxEdit = QVBoxLayout()
        self.ui.vBoxEdit.setContentsMargins(0, 0, 0, 0)
        self.ui.containerEdit.setLayout(self.ui.vBoxEdit)
        self.ui.vBoxEdit.addWidget(self.ui.btnEdit)
        tableViewObj.setIndexWidget(tableViewObj.model().index(iRow, 1), self.ui.containerEdit)
        
        pk = [str(tableViewObj.model().index(iRow, iCol).data().toString(r'M/d/yyyy'))
            if isinstance(tableViewObj.model().index(iRow, iCol).data(), QDate)
            else str(tableViewObj.model().index(iRow, iCol).data())
            for iCol in range(2, tableViewObj.model().columnCount())
            if tableViewObj.model().headerData(iCol, Qt.Orientation.Horizontal) in self.info[tableName]['pkCols']]

        self.ui.btnDel.clicked.connect(lambda: self.deleteRecord(tableName, pk))
        self.ui.btnEdit.clicked.connect(lambda: self.editRecord(tableName, pk))

    def editRecord(self, tableName: str, pk: list):
        query = f"SELECT * FROM {tableName}ViewFetch WHERE "+' AND '.join([f"{col} = '{k}'" for col, k in dict(zip(self.info[tableName]['pkCols'], pk)).items()])
        queryObj = self.functions.select(query)
        values = list()
        while queryObj.next():
            for i in range(queryObj.record().count()):
                if len(values) == len(self.info[tableName]['widgets']):
                    break
                data = queryObj.value(i)
                if isinstance(data, QDate):
                    values.append(data.toString(r'M-d-yyyy'))
                else:
                    values.append(data)
        
        self.loadWidgets(tableName, values)
        self.pk = pk
        
    def loadWidgets(self, tableName: str, values: list):
        widgets = self.info[tableName]['widgets']
        for i in range(len(widgets)):
            if widgets[i] == None:
                continue
            if widgets[i].metaObject().className() == 'QLineEdit':
                widgets[i].setText(values[i])
            if widgets[i].metaObject().className() == 'QPlainTextEdit':
                widgets[i].setPlainText(values[i])
            elif widgets[i].metaObject().className() == 'QComboBox':
                widgets[i].setCurrentText(str(values[i]))
            elif widgets[i].metaObject().className() == 'QDoubleSpinBox':
                widgets[i].setValue(values[i])
            elif widgets[i].metaObject().className() == 'QSpinBox':
                widgets[i].setValue(values[i])
            elif widgets[i].metaObject().className() == 'QDateEdit':
                widgets[i].setDate(datetime.strptime(values[i], '%m-%d-%Y').date())
            elif widgets[i].metaObject().className() == 'QDateTimeEdit':
                widgets[i].setDate(datetime.strptime(values[i], '%m-%d-%Y %H:%M'))
            elif widgets[i].metaObject().className() == 'QTableWidget':
                widgets[i].setRowCount(0)
                self.loadTableWidget(widgets[i], values[i:], widgets[i].columnCount())

        iBtn, uBtn, lbl, iPage = self.info[tableName]['extraWidgets']
        iBtn.setHidden(True)
        uBtn.setHidden(False)
        lbl.setText(lbl.text().replace('Insérer', 'Modifier'))
        self.ui.stackedWidget.setCurrentWidget(iPage)

    @staticmethod
    def loadTableWidget(tableWidget, grid, colCount: int):
        prevRowCount = tableWidget.rowCount()
        tableWidget.setRowCount(prevRowCount+len(grid[0].split('|')))
        for col in range(colCount):
            vals = grid[col].split('|')
            for row in range(prevRowCount, tableWidget.rowCount()):
                tableWidget.setItem(row, col, QTableWidgetItem(str(vals[row-prevRowCount])))

    def deleteRecord(self, tableName: str, pk: list):
        msg = self.showMsg(f"Confirmer la suppression de l'enregistrement ({', '.join(pk)})", STYLE_NOTICE_MSG, [QMessageBox.Yes, QMessageBox.No])
        if msg == QMessageBox.Yes:
            result = self.functions.execProcedure(f'Delete{tableName}', pk)
            if result == 'succes':
                self.showMsg('Enregistrement supprimé avec succès', STYLE_SUCCESS_MSG)
                self.loadView(tableName)
            elif 'conflicted with the REFERENCE constraint' in result:
                tableRef = re.findall('"FK_([^"]*)"', result)[0].split('_')[0]
                msg = self.showMsg(f'Il y a une référence de cet enregistrement sur la table {tableRef}\n\nVoulez-vous supprimer toutes les références de cet enregistrement?', STYLE_NOTICE_MSG, [QMessageBox.Yes, QMessageBox.No])
                if msg == QMessageBox.Yes:
                    pk.append('1')
                    self.deleteRecord(tableName, pk)
            else:
                self.showMsg(result, STYLE_ERROR_MSG)

    def showMsg(self, text: str, msgStyle, buttons: list=list()):
        msg = QMessageBox()
        for btn in buttons:
            msg.addButton(btn)
        msg.setWindowFlag(Qt.FramelessWindowHint)
        msg.setStyleSheet(msgStyle)
        msg.setText(text)
        return msg.exec()

    def checkConnection(self):
        queryObj = self.functions.select("SELECT @@SERVERNAME, CURRENT_USER")
        if queryObj:
            while queryObj.next():
                self.showMsg(f"Vous êtes connecté aux:\n\nServer: {queryObj.value(0)}\nUser: {queryObj.value(1)}", STYLE_SUCCESS_MSG)

    def closeEvent(self, event: QCloseEvent) -> None:  # handle close window
        msg = QMessageBox.question(self,
                                   "Window close",
                                   "Fermer la fenêtre ?",
                                   QMessageBox.Yes, QMessageBox.No)
        if msg == QMessageBox.Yes:
            if self.functions.db.isOpen():
                self.functions.db.close()
            event.accept()
        else:
            event.ignore()
            
class LoginForm(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_loginForm()
        self.ui.setupUi(self)
        self.clickPosition = 0
        
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        self.ui.leftFrame.mouseMoveEvent = self.moveWindow
        self.ui.checkBoxShowPassword.stateChanged.connect(self.changeEchoMode)

    def changeEchoMode(self, state):
        if Qt.CheckState(state) == Qt.CheckState.Checked:
            self.ui.editPassword.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.editPassword.setEchoMode(QLineEdit.Password)

    def moveWindow(self, event):
        if not self.isMaximized() and event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPosition().toPoint() - self.clickPosition)
            self.clickPosition = event.globalPosition().toPoint()
            event.accept()        
    
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPosition().toPoint()

    def triggerloadingAnimation(self, animation: QMovie, start: bool):
        animation.frameChanged.connect(lambda: self.ui.btnConnect.setIcon(animation.currentPixmap()))
        if start:
            self.ui.btnConnect.setEnabled(False)
            animation.start()
        else:
            self.ui.btnConnect.setEnabled(True)
            animation.stop()
            self.ui.btnConnect.setIcon(QIcon())
            del animation

if __name__ == "__main__":
    app = QApplication()
    app.setApplicationName('CEM')
    app.setApplicationVersion('v1.0.0 (64-bit)')
    app.setWindowIcon(QIcon(r':/icons/bin/ui/icons/logo.svg'))
    mainWindows = MainWindow()
    mainWindows.setWindowTitle('Compact Inventory Monitor (CEM)')
    sys.exit(app.exec())