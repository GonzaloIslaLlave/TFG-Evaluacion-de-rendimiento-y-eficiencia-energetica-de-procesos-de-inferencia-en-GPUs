import pandas as pd
import os
import matplotlib.pyplot as plt
import re

dtype = {
    'Set_id': str,
    'Time': float,
    'Line 8': float,
    'Line 9': float,
    'Line 10': float,
    'Sum': float
}

folder_path = '/home/gonzalo/Escritorio/tfg/energia/AGX15W/bert/'
save_path = '/home/gonzalo/Escritorio/tfg/graficasAGX15W/bert/'



#name_mapping = {
#    'test_Orin_bert_Offline1_200.csv': 'Batch=1 QPS=200',
#    'test_Orin_bert_Offline2_300.csv': 'Batch=2 QPS=300',
#    'test_Orin_bert_Offline10_450.csv': 'Batch=10 QPS=450',
#    'test_Orin_bert_Offline20_500.csv': 'Batch=20 QPS=500',
#    'test_Orin_bert_Offline70_500.csv': 'Batch=70 QPS=500',
#}

name_mapping = {
    'test_Orin_bert_Offline1_39.csv': 'Batch=1 QPS=39',
    'test_Orin_bert_Offline20_67.csv': 'Batch=20 QPS=67',
    'test_Orin_bert_Offline70_67.csv': 'Batch=70 QPS=67',
}


files_data = {}
file_order = []  # Lista para mantener el orden de los archivos
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        print("Analizando archivo: {}".format(filename))
        filepath = os.path.join(folder_path, filename)
        df = pd.read_csv(filepath, delimiter=';', dtype=dtype)
        files_data[filename] = df
        file_order.append(filename)  # Agregar el nombre del archivo al orden de archivos


file_order.sort(key=lambda x: int(re.search(r'\d+', x).group()))

fig_line8, ax_line8 = plt.subplots(figsize=(4, 3.5), frameon=True)  # Set the figure size here
legend_labels = []  # Lista para las leyendas en el orden correcto
for filename in file_order:
    df = files_data[filename]
    time = df['Time']
    line_data = df['Line 8']

    label = name_mapping.get(filename, filename)
    ax_line8.plot(time, line_data, label=label)  # Usar el nombre modificado como etiqueta
    legend_labels.append(label)  # Agregar el nombre modificado a las leyendas

ax_line8.set_xlabel('Time (s)')
ax_line8.set_ylabel('Gasto de GPU (W)')

ax_line8.legend(legend_labels)

#plt.title('Consumo de potencia con Bert en la Jetson Orin AGX 15W')
output_filename_line8 = 'line8_bert_AGX_15W.png'
ax_line8.set_xlim(0, 700)
ax_line8.set_ylim(0, 15)
#ax_line8.set_xlim(0.0, 800)
#ax_line8.set_ylim(0, 60)

ax_line8.grid(True)
fig_line8.subplots_adjust(left=0.1)
plt.savefig(os.path.join(save_path, output_filename_line8), bbox_inches='tight')
plt.close(fig_line8)


#save_plot(fig_line8, ax_line8, 'Potencia medida en Rnnt con Jetson Orin AGX', 'line8_rnntAGX.png', legend_labels=['Batch=1 QPS=20', 'Batch=2 QPS=26', 'Batch=100 QPS=178', 'Batch=500 QPS=1150'])
#save_plot(fig_line8, ax_line8, 'Potencia medida en Rnnt con Jetson Orin AGX 15W', 'line8_rnntAGX15W.png', legend_labels=['Batch=1 QPS=6', 'Batch=500 QPS=165'])
#save_plot(fig_line8, ax_line8, 'Potencia medida en Resnet50 con Jetson Orin AGX', 'line8_resnet50AGX.png', legend_labels=['Batch=1 QPS=1600', 'Batch=7 QPS= 1750','Batch=70 QPS=1800' ,'Batch=200 QPS=1800'])




# Plot para Line 9
#fig_line9, ax_line9 = plt.subplots()
#for filename, df in sorted(files_data.items(), key=lambda x: x[0]):
#    time = df['Time']
#    line_data = df['Line 9']
#    ax_line9.plot(time, line_data, label=filename)

#save_plot(fig_line9, ax_line9, 'Line 9 Rnnt Offline AGX 15w', 'line9_rnnt.png')

# Plot para Line 10
#fig_line10, ax_line10 = plt.subplots()
#for filename, df in sorted(files_data.items(), key=lambda x: x[0]):
#    time = df['Time']
#    line_data = df['Line 10']
#    ax_line10.plot(time, line_data, label=filename)

#save_plot(fig_line10, ax_line10, 'Line 10 Rnnt Offline AGX 15w', 'line10_rnnt.png')