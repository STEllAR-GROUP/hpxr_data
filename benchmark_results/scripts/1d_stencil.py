import matplotlib.pyplot as plt
import math

# dataflow Replay parameters
cores = ['32']
runs = []

variations = {
    '128': '16000',
    '256': '8000'
}

for i in range(1, 11):
    runs.append(str(i))


# Graph generation
for tile, subdomain_width in variations.iteritems():
    # Graph parameters
    font_size = 12
    figure_size = [18, 12]
    color = ['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9']
    font = {'family':'serif', 'serif': ['Palatino'],
            'weight' : 'bold',
            'size'   : 40}
    markers = ["o", "^", "*", "P", "s"]

    # Initializing x params
    error_rate = []
    label = ['0.005', '0.01', '0.03', '0.1', '0.25', '0.67', '1.8', '5.0']
    for i in range(11, 3, -1):
        error_rate.append(i)

    color_counter = 0
    markers_counter = 0
    plt.figure(figsize=(figure_size[0], figure_size[1]))
    plt.rc('font', **font)
    plt.rc('text', usetex=True)

    # Initializing dataflow plot values
    time_dataflow = 0.0
    # Initializing dataflow replay plot values
    time_dataflow_replay = [0] * 8
    # Initializing dataflow replay validate plot values
    time_dataflow_replay_validate = [0] * 8

    for run in runs:
        file = '../benchmarks/stencil/1d_stencil_32' + '_' + subdomain_width + '_' + run + '.txt'
        with open(file) as f:
            counter_dataflow_replay = 0
            counter_dataflow_replay_validate = 0

            counter = 0
            contents = f.read().splitlines()

            for content in contents:
                if 'Time' in content:
                    line = content.split(' ')
                    if counter % 2 == 0:
                        time_dataflow_replay[counter_dataflow_replay] += (float(line[-1]))
                        counter_dataflow_replay += 1
                    elif counter % 2 == 1:
                        time_dataflow_replay_validate[counter_dataflow_replay_validate] += (float(line[-1]))
                        counter_dataflow_replay_validate += 1
                    counter += 1

        file = '../benchmarks/stencil/1d_pure_stencil_32' + '_' + subdomain_width + '_' + run + '.txt'
        with open(file) as f:
            contents = f.read().splitlines()
            for content in contents:
                if 'Time' in content:
                    line = content.split(' ')
                    time_dataflow += (float(line[-1]))
                    break
        
    # Average times amongst 10 runs
    for i in range(8):
        time_dataflow_replay[i] = ((time_dataflow_replay[i] - time_dataflow) / time_dataflow) * 100
        time_dataflow_replay_validate[i] = ((time_dataflow_replay_validate[i] - time_dataflow) / time_dataflow) * 100

    print time_dataflow
    print time_dataflow_replay
    print time_dataflow_replay_validate

    if subdomain_width == '16000':
        plt.plot(error_rate, time_dataflow_replay, color[color_counter], linewidth=3.0, marker=markers[markers_counter], markersize=15.0, label='Replay')
        plt.plot(error_rate, time_dataflow_replay_validate, color[color_counter+1], linewidth=3.0, marker=markers[markers_counter+1], markersize=15.0, label='Replay with checksums')
        plt.xticks(error_rate, label[::-1], rotation=45, horizontalalignment='right')
        plt.ylim(ymin=0)
        plt.grid()
        plt.legend()
        plt.ylabel('Percentage extra execution time (in \%)', fontsize=40)
        plt.xlabel('Probability of error occurrence per task (in \%)', fontsize=40)

        fig_name = '1d_stencil_exec_case_A.png'
        plt.savefig('../graphs/1d_stencil/' + fig_name, bbox_inches='tight')
        plt.close()
    else:
        plt.plot(error_rate, time_dataflow_replay, color[color_counter], linewidth=3.0, marker=markers[markers_counter], markersize=15.0, label='Replay')
        plt.plot(error_rate, time_dataflow_replay_validate, color[color_counter+1], linewidth=3.0, marker=markers[markers_counter+1], markersize=15.0, label='Replay with checksums')
        # title = 'dataflow Replay and Replay Validate:\nExtra task execution time vs Probability of error occurrence, with task size of us'
        # plt.title(title, fontsize=22, fontweight='bold')
        plt.xticks(error_rate, label[::-1], rotation=45, horizontalalignment='right')
        plt.ylim(ymin=0)
        # plt.yscale('log')
        plt.grid()
        plt.legend()
        plt.ylabel('Percentage extra execution time (in \%)', fontsize=40)
        plt.xlabel('Probability of error occurrence per task (in \%)', fontsize=40)

        fig_name = '1d_stencil_exec_case_B.png'
        plt.savefig('../graphs/1d_stencil/' + fig_name, bbox_inches='tight')
        plt.close()
        plt.plot(error_rate, time_dataflow_replay, color[color_counter], linewidth=3.0, marker=markers[markers_counter], markersize=15.0, label='Replay')
        plt.plot(error_rate, time_dataflow_replay_validate, color[color_counter+1], linewidth=3.0, marker=markers[markers_counter+1], markersize=15.0, label='Replay with checksums')

    color_counter += 2
    markers_counter += 2

