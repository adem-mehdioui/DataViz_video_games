import sys
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt Interface")
        self.setGeometry(0, 0, 1000, 600)

        self.button = QPushButton("Load Dataset", self)
        self.button.setFixedWidth(200)  # Set the width of the button
        self.button.setFixedHeight(30)  # Set the height of the button
        self.button.clicked.connect(self.load_and_display_data)
        self.label = QLabel("...", self)

        hbox = QHBoxLayout()
        hbox.addWidget(self.button)
        hbox.addWidget(self.label)

        # Create layouts for the plots
        self.plot_layout_1 = QHBoxLayout()
        self.plot_layout_2 = QHBoxLayout()

        # Create a layout for the entire window
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)  # Add the button and label layout to the window layout
        vbox.addLayout(self.plot_layout_1)
        vbox.addLayout(self.plot_layout_2)
        vbox.addStretch(1)    # Add a stretchable space to push the button and label to the top

        self.setLayout(vbox)

    def load_and_display_data(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv)", options=options)
        if fileName:
            print("Selected file:", fileName)
            self.label.setText("Dataset has been successfully loaded")

            # Read CSV file
            df = pd.read_csv(fileName)


            # Plotting pie chart
            self.plot_pie_chart(df)

            # Plotting bar chart
            self.plot_bar_chart(df)

            

    def plot_pie_chart(self, data):
        figure = Figure()
        ax = figure.add_subplot(111)
        data['Platform'].value_counts().head(10).plot.pie(ax=ax, autopct='%1.1f%%')
        ax.set_title('First 10 Platforms')
        canvas = FigureCanvas(figure)
        self.plot_layout_1.addWidget(canvas)


    def plot_bar_chart(self, data):
        figure = Figure()
        ax = figure.add_subplot(111)
        data['Publisher'].value_counts().head(10).plot(kind='bar', ax=ax)
        ax.set_title('Top 10 Publisher')
        ax.set_xlabel('Publisher')
        ax.set_ylabel('Count')
        canvas = FigureCanvas(figure)
        self.plot_layout_1.addWidget(canvas)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit_code = app.exec_()
    sys.exit(sys.exit_code)


