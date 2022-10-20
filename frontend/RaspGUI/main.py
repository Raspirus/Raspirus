# This Python file uses the following encoding: utf-8
import sys
import urllib.request
import json
from pathlib import Path

from PySide6.QtQuick import QQuickView
from PySide6.QtCore import QStringListModel, QUrl
from PySide6.QtGui import QGuiApplication

if __name__ == '__main__':

    # get our data
    url = "http://country.io/names.json"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode('utf-8'))

    # Format and sort the data
    data_list = list(data.values())
    data_list.sort()

    # Set up the application window
    app = QGuiApplication(sys.argv)
    view = QQuickView()
    view.setResizeMode(QQuickView.SizeRootObjectToView)

    # Expose the list to the Qml code
    my_model = QStringListModel()
    my_model.setStringList(data_list)
    view.setInitialProperties({"myModel": my_model})

    # Load the QML file
    qml_file = Path(__file__).parent.parent / "qml/view.qml"
    view.setSource(QUrl.fromLocalFile(qml_file.resolve()))

    # Show the window
    if view.status() == QQuickView.Error:
        sys.exit(-1)
    view.show()

    # execute and cleanup
    app.exec()
    del view
