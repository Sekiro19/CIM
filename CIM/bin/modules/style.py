STYLE_ERROR_MSG = """QMessageBox {
									font: 700 10pt "Arial";
									color:  rgb(255, 255, 255);
									background-color: rgb(6, 35, 100);
									border: 2px solid rgb(255, 44, 83);
									background-position: center;
									}
				QMessageBox QLabel {color: rgb(255, 255, 255); padding-left: 10px; padding-right: 10px;}			
				QPushButton {
								font: 700 10pt "Arial";
								color:  rgb(182, 212, 255);
								border: none;	
								}
				QPushButton:hover {color: rgb(255, 255, 255);}
				QPushButton:pressed {color: rgb(255, 255, 255);}
				 """

STYLE_SUCCESS_MSG = """QMessageBox {
									font: 700 10pt "Arial";
									color:  rgb(255, 255, 255);
									background-color: rgb(6, 35, 100);
									border: 2px solid rgb(189, 255, 0);
									background-position: center;
									}
				QMessageBox QLabel {color: rgb(220,220,220); padding-left: 10px; padding-right: 10px;}			
				QPushButton {
								font: 700 10pt "Arial";
								color:  rgb(182, 212, 255);
								border: none;	
								}
				QPushButton:hover {color: rgb(255, 255, 255);}
				QPushButton:pressed {color: rgb(255, 255, 255);}
				 """
STYLE_NOTICE_MSG = """QMessageBox {
									font: 700 10pt "Arial";
									color:  rgb(255, 255, 255);
									background-color: rgb(6, 35, 100);
									border: 2px solid rgb(255, 164, 0);
									background-position: center;
									}
				QMessageBox QLabel {color: rgb(220,220,220); padding-left: 10px; padding-right: 10px;}			
				QPushButton {
								font: 700 10pt "Arial";
								color:  rgb(182, 212, 255);
								border: none;	
								}
				QPushButton:hover {color: rgb(255, 255, 255);}
				QPushButton:pressed {color: rgb(255, 255, 255);}
				 """

STYLE_BTN_EDIT = """QPushButton {
	background-color:  transparent;
	image: url(:/icons/bin/ui/icons/icons8-pencil-30.png);
}
QPushButton:hover {
	border: 2px solid transparent;
}"""
STYLE_BTN_DEL = """QPushButton {
	background-color:  transparent;
	image: url(:/icons/bin/ui/icons/icons8-close-30.png);
}
QPushButton:hover {
	border: 2px solid transparent;
}"""
STYLE_BTN_FLOW_IN = """QPushButton {
	background-color:  transparent;
 	image: url(:/icons/bin/ui/icons/icons8-forward-arrow-30.png); 
}
QPushButton:hover {
	border: 2px solid transparent;
}"""
STYLE_BTN_FLOW_OUT = """QPushButton {
	background-color:  transparent;
	image: url(:/icons/bin/ui/icons/icons8-reply-arrow-30.png);
}
QPushButton:hover {
	border: 2px solid transparent;
}"""