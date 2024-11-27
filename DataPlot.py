import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def Compressor_ReadTime_plot():
    data = pd.read_excel("/Users/sagnik/Documents/Research_Project/Data/Settings.xlsx", sheet_name='Compressor')
    data = data.iloc[71:75, 0:]
    #color = ['red', 'yellow', 'black', 'blue', 'orange']
    plt.bar(data['Shuffle'], data['Read_Time'], width=0.3)
    plt.title("Compressor Read Time Stats")
    plt.xlabel("shuffle")
    plt.ylabel("Read Time(seconds)")
    plt.show()

def Compressor_ReadTimeblosclz_plot():
    data = pd.read_excel("/Users/sagnik/Documents/Research_Project/Data/Settings.xlsx", sheet_name='Compressor')
    data = data.iloc[71:75, 0:]

    #color = ['red', 'yellow', 'black', 'blue', 'orange']
    plt.bar(data['Shuffle'], data['Read_Time'], width=0.3)
    plt.title("Compressor Read Time Stats")
    plt.xlabel("shuffle")
    plt.ylabel("Read Time(seconds)")
    plt.show()

def Compressor_CPU_plot():
    data = pd.read_excel("/Users/sagnik/Documents/Research_Project/Data/Settings.xlsx", sheet_name='Compressor')
    data = data.iloc[0:5, 0:]
    color = ['red', 'yellow', 'black', 'blue', 'orange']
    plt.bar(data['Name'], data['CPU_Usage'], color=color)
    plt.title("Compressor CPU Usage Stats")
    plt.xlabel("Compressor")
    plt.ylabel("Average CPU Usage(%)")
    plt.show()

def Compressor_DiskRead_plot():
    data = pd.read_excel("/Users/sagnik/Documents/Research_Project/Data/Settings.xlsx", sheet_name='Compressor')
    data = data.iloc[0:5, 0:]
    #color = ['red', 'yellow', 'black', 'blue', 'orange']
    plt.bar(data['Shuffle'], data['Disk_Read_IO'], width=0.3)
    plt.title("Compressor Disk Read IO Stats")
    plt.xlabel("shuffle")
    plt.ylabel("Disk Read Count")
    plt.show()

def Query_ReadTime_plot():
    data = pd.read_excel("/Users/sagnik/Documents/Research_Project/Data/Settings.xlsx", sheet_name='Query')
    data = data.iloc[30:35, 0:]
    #color = ['red', 'yellow', 'black', 'blue', 'orange']
    plt.bar(data['Chunking'].astype(str), data['Read_Time'].astype(float), width=0.3)
    plt.title("Query Read Time Stats")
    plt.xlabel("Chunking")
    plt.ylabel("Read Time(seconds)")
    plt.show()

def Query_CPU_plot():
    data = pd.read_excel("/Users/sagnik/Documents/Research_Project/Data/Settings.xlsx", sheet_name='Query')
    data = data.iloc[30:35, 0:]
    #color = ['red', 'yellow', 'black', 'blue', 'orange']
    plt.plot(data['Chunking'].astype(str), data['Average_CPU_Usage'].astype(float))
    plt.title("Query CPU Usage Stats")
    plt.xlabel("Chunking")
    plt.ylabel("CPU Usage(%)")
    plt.show()

def Query_IO_plot():
    data = pd.read_excel("/Users/sagnik/Documents/Research_Project/Data/Settings.xlsx", sheet_name='Query')
    data = data.iloc[30:35, 0:]
    #color = ['red', 'yellow', 'black', 'blue', 'orange']
    plt.bar(data['Chunking'].astype(str), data['Average_IO'].astype(float), width=0.3)
    plt.title("Query Disk Read Stats")
    plt.xlabel("Chunking")
    plt.ylabel("Disk Reads")
    plt.show()


def Compressor_RAM_plot():
    data = pd.read_excel("/Users/sagnik/Documents/Research_Project/Data/Settings.xlsx", sheet_name='Compressor')
    data = data.iloc[0:5, 0:]
    color = ['red', 'yellow', 'black', 'blue', 'orange']
    plt.bar(data['Name'], data['RAM Usage'], color=color)
    plt.title("Compressor RAM Usage Stats")
    plt.xlabel("Compressor")
    plt.ylabel("RAM Usage(%)")
    plt.show()


def Query_RAM_plot():
    data = pd.read_excel("/Users/sagnik/Documents/Research_Project/Data/Settings.xlsx", sheet_name='Query')
    data = data.iloc[30:35, 0:]
    #color = ['red', 'yellow', 'black', 'blue', 'orange']
    plt.bar(data['Chunking'].astype(str), data['RAM_Usage'].astype(float), width=0.3)
    plt.title("Query RAM Usage Stats")
    plt.xlabel("Chunnking")
    plt.ylabel("RAM_Usage(%)")
    plt.show()


#Calling the plot functions respectively
#Compressor_ReadTime_plot()
#Compressor_CPU_plot()
#Compressor_DiskRead_plot()
#Compressor_ReadTimeblosclz_plot()
#Query_ReadTime_plot()
#Query_CPU_plot()
Query_IO_plot()
#Compressor_RAM_plot()
#Query_RAM_plot()