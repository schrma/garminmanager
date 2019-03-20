import garminmanager.ui.PlotC

def test_plot():
    my_plot = garminmanager.ui.PlotC.PlotC()
    my_plot.add_plot_data([1,2,3],[4,5,7],"first")
    my_plot.add_plot_data([1,2,3],[10,22,23],"seccond")
    my_plot.show()
