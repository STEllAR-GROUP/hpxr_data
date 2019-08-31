import matplotlib.pyplot as plt
import math

# Async Replay parameters
cores = ['1', '4', '8', '16', '32']
exectimes = ['200']
runs = []

for i in range(1, 11):
    runs.append(str(i))

# Graph parameters
font_size = 12
figure_size = [18, 12]
color = ['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9']
font = {'family' : 'serif', 'serif': ['Palatino'],
        'weight' : 'normal',
        'size'   : 40}
markers = ["o", "^", "*", "P", "s"]

# Initializing x params
error_rate = []
label = ['0.005', '0.01', '0.03', '0.1', '0.25', '0.67', '1.8', '5.0']

for i in range(11, 3, -1):
    error_rate.append(i)
    # error_rate.append(float(format((math.exp(-i))*100, '.4f')))

print error_rate

time_async = [2013.316995, 504.431704, 252.521205, 126.45367, 63.809629]
async_counter = 0

# Graph generation
for exectime in exectimes:
    color_counter = 0
    markers_counter = 0
    plt.figure(figsize=(figure_size[0], figure_size[1]))
    plt.rc('font', **font)
    plt.rc('text', usetex=True)

    for core in cores:
        # Initializing async replay plot values
        time_async_replay = [0] * 8
        # Initializing async replay validate plot values
        time_async_replay_validate = [0] * 8

        for run in runs:
            file = '../benchmarks/async_replay/async_replay_' + core + '_' + exectime + '_' + run + '.txt'
            with open(file) as f:
                counter_async_replay = 0
                counter_async_replay_validate = 0

                counter = 0
                contents = f.read().splitlines()

                for content in contents:
                    if 'time' in content:
                        line = content.split(' ')
                        if counter % 2 == 0:
                            time_async_replay[counter_async_replay] += (float(line[-1]))
                            counter_async_replay += 1
                        else:
                            time_async_replay_validate[counter_async_replay_validate] += (float(line[-1]))
                            counter_async_replay_validate += 1
                        counter += 1

        # Average times amongst 10 runs
        for i in range(8):
            time_async_replay[i] = ((time_async_replay[i] - time_async[async_counter]) / 10.0)
            time_async_replay_validate[i] = ((time_async_replay_validate[i] - time_async[async_counter]) / 10.0)

        async_counter += 1

        print time_async_replay
        print time_async_replay_validate
        plt.plot(error_rate, time_async_replay, color[color_counter], linewidth=3.0, marker=markers[markers_counter], markersize=15.0, label=core + ' cores (Async Replay and variations)')
        color_counter += 1
        markers_counter += 1

    plt.xticks(error_rate, label[::-1], rotation=45, horizontalalignment='right', fontsize=40)
    plt.yticks(fontsize=40)
    plt.grid()
    plt.ylim(ymin=0)
    plt.legend()
    plt.ylabel('Extra execution time per task in us', fontsize=40)
    plt.xlabel('Probability of error occurrence per task (in percentage)', fontsize=40)

    fig_name = 'asyc_replay_exec_time_' + exectime + '.png'
    plt.savefig('../graphs/async_replay/' + fig_name, bbox_inches='tight')
    plt.close()